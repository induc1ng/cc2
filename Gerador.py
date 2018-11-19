from ANTLR.TileMapVisitor import *
from ANTLR.TileMapParser import *
import numpy as np
import random
from Semantico import Tiles



class Gerador(TileMapVisitor):

    size = 0
    quantity = 0
    case = ''
    tile = ''
    tipoArray = []
    #Array que armazena as imagens

    imageCounter = 0
    tileCounter = 0
    tipoCounter = 0
    gameMap = ''

    tileArray = []

    # Geramos um texto ~final~ para que possamos gerar o arquivo HTML #
    # Replaces são feitos conforme a descida #

    final = """<!DOCTYPE html><html>
                <head>

                <script type="text/javascript">
                var ctx = null;
                var tile = new Array();
                var image = new Array();
                var gameMap = new Array();
                
                {tiles}
                {gameMap}

                var tileW = 16, tileH = 16;
                var mapW = {size}, mapH = {size};
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
                                {case}
                            }

                        }
                    }

                    ctx.fillStyle = "#ff0000";a

                    requestAnimationFrame(drawGame);
                }
                </script>

                </head>
                <body>

                {select}

                <canvas id="game" width="{scale}" height="{scale}"></canvas>

                </body>
                </html>
    """

    def getTilesByTipo(self,tile,tipo):
        auxList = []
        for i in range(0,len(tile)):
            if(tile[i].tipo==tipo):
                auxList.append(i)
        
        return auxList

    def visitMap(self, ctx: TileMapParser.MapaContext):
        self.size = int(str(ctx.size()[0].NUM_INT()))
        self.quantity = int(str(ctx.size()[1].NUM_INT()))
        self.final = self.final.replace('{tiles}',str(self.visitTile(ctx.tile())))
        self.select = '<select onchange="drawMap(value)">\n'
        
        self.visitCommands(ctx.commands())      
           


        for i in range(0,len(self.tipoArray)):
            self.select+='<option value="'+str(i)+'">'+self.tipoArray[i]+'</option>\n'

        self.select += '</select>\n'


        for x in range(0,len(self.tipoArray)):
            self.gameMap += "gameMap["+str(x)+"]=["
            for j in range(0,self.size*self.size):
                if(j==0):  
                    self.gameMap += str(random.choice(self.getTilesByTipo(self.tileArray,self.tipoArray[x])))
                else:
                    self.gameMap += ","+str(random.choice(self.getTilesByTipo(self.tileArray,self.tipoArray[x])))
            self.gameMap+= "];\n"

        for x in range(0, self.imageCounter):
            self.case += "case "+ str(x) +":\n ctx.drawImage(image["+str(x)+"],x*tileW,y*tileH);\n break;\n"        

        self.final = self.final.replace('{gameMap}',self.gameMap)
        self.final = self.final.replace('{select}',self.select)
        self.final = self.final.replace('{size}',str(self.size))
        self.final = self.final.replace('{scale}',str(self.size*self.size))
        self.final = self.final.replace('{case}',self.case)

        return 1
    
    def visitTile(self,ctx: TileMapParser.TileContext):
        path = str(ctx.path().CADEIA())
        name = str(ctx.ID())
        tipo = str(ctx.tipoTyle().ID())
        

        if ctx is not None:
            self.tile += "\n\ntile["+str(self.imageCounter)+"] = { \n path:"+path+", name:'"+name+"',tipo:'"+tipo+"'"
            self.tile +='};'
            self.tile+="\nimage["+str(self.imageCounter)+"] = new Image(40,40);" + "\nimage["+str(self.imageCounter)+"].src = tile["+str(self.imageCounter)+"].path;"
            
            self.visitRecur_tiles(ctx.recur_tiles())
            self.tileArray.append((Tiles(path,name,tipo)))

        return self.tile;


    def visitCommands(self,ctx: TileMapParser.CommandsContext):
        if ctx is not None:
            if ctx.add() is not None:
                add_size = int(str(ctx.add().NUM_INT()))
                tipo = str(ctx.add().tipoTyle().ID())
                for i in range(0,add_size):
                    self.tipoArray.append(tipo)
        return self.visitRecur_commands(ctx.recur_commands())

    def visitRecur_tiles(self, ctx: TileMapParser.Recur_tilesContext):
        self.imageCounter+=1
        return self.visitTile(ctx.tile()) if ctx.tile() is not None else ''

    def visitRecur_commands(self, ctx: TileMapParser.Recur_commandsContext):
        return self.visitCommands(ctx.commands()) if ctx.commands() is not None else ''
    
    
    def getCodigo(self):
        return self.final


        
