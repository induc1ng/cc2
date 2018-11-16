from ANTLR.TileMapVisitor import *
from ANTLR.TileMapParser import *
import numpy as np
import random


class Gerador(TileMapVisitor):

    size = 0
    quantity = 0

    tile = ''

    #Array que armazena as imagens

    imageArray = []
    imageCounter = 0
    tileCounter = 0
    gameMap = ''

    # Geramos um texto ~final~ para que possamos gerar o arquivo HTML #
    # Replaces são feitos conforme a descida #

    final = """<!DOCTYPE html><html>
                <head>

                <script type="text/javascript">
                var ctx = null;

                var book = new Array();
                var tile = new Array();

                var image = new Array();
                
                {tiles}
                {gameMap}

                var tileW = 40, tileH = 40;
                var mapW = 10, mapH = 10;
                var currentSecond = 0, frameCount = 0, framesLastSecond = 0;

                window.onload = function()
                {
                    drawMap(0);

                };

                function drawMap(map){
                    map = parseInt(map,10);
                    ctx = document.getElementById('game').getContext("2d");
                    ctx.font = "bold 10pt sans-serif";
                    requestAnimationFrame(drawGame(map));
                }

                function drawGame(map)
                {
                    console.log(map);

                    if(ctx==null) { return; }

                    var sec = Math.floor(Date.now()/1000);
                    if(sec!=currentSecond)
                    {
                        currentSecond = sec;
                        framesLastSecond = frameCount;
                        frameCount = 1;
                    }
                    else { frameCount++; }

                    for(var y = 0; y < mapH; ++y)
                    {
                        for(var x = 0; x < mapW; ++x)
                        {
                            switch(gameMap[map][((y*mapW)+x)])
                            {
                                case 0:
                        ctx.drawImage(image[0],x*tileW,y*tileH);
                                    break;
                                default:
                                    ctx.drawImage(image[1],x*tileW,y*tileH);
                            }

                        }
                    }

                    ctx.fillStyle = "#ff0000";
                    ctx.fillText("-: " + framesLastSecond, 10, 20);

                    requestAnimationFrame(drawGame);
                }
                </script>

                </head>
                <body>

                {select}

                <canvas id="game" width="400" height="400"></canvas>

                </body>
                </html>
    """



    def visitMap(self, ctx: TileMapParser.MapaContext):
        self.size = int(str(ctx.size()[0].NUM_INT()))
        self.quantity = int(str(ctx.size()[1].NUM_INT()))
        self.final = self.final.replace('{tiles}',str(self.visitTile(ctx.tile())))
        self.select = '<select onchange="drawMap(value)">\n'
        

        for x in range(0, self.quantity):
            self.gameMap += "gameMap["+str(x)+"]=["
            for j in range(0,self.size*self.size):
                if(j==0):
                    self.gameMap += str(random.randint(0,self.imageCounter))
                else:
                    self.gameMap += ","+str(random.randint(0,self.imageCounter))
            self.gameMap+= "];\n"
            self.select += '<option value="'+str(x)+'">'+str(x)+'</option>\n'
            
        self.select += '</select>\n'
        self.final = self.final.replace('{gameMap}',self.gameMap)
        self.final = self.final.replace('{select}',self.select)
        print(self.final)
        return 1
    
    def visitTile(self,ctx: TileMapParser.TileContext):
        path = str(ctx.path().CADEIA())
        name = str(ctx.ID())

        if ctx is not None:
            self.tile += "\n\ntile["+str(self.imageCounter)+"] = { \n path:"+path+", name:'"+name+"'"
            self.tile +='};'
            self.tile+="\nimage["+str(self.imageCounter)+"] = new Image(40,40);" + "\nimage["+str(self.imageCounter)+"].src = tile["+str(self.imageCounter)+"].path;"
            self.visitRecur_tiles(ctx.recur_tiles())

        return self.tile;


    def visitRecur_tiles(self, ctx: TileMapParser.Recur_tilesContext):
        self.imageCounter+=1
        return self.visitTile(ctx.tile()) if ctx.tile() is not None else ''


        
