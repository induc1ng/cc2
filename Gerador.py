from ANTLR.TileMapVisitor import *
from ANTLR.TileMapParser import *
import numpy as np


class Gerador(TileMapVisitor):

    size = 0
    quantity = 0

    #Array que armazena as imagens

    imageArray = []
    imageCounter = 0
    tileCounter = 0



    def visitMap(self, ctx: TileMapParser.MapaContext):
        self.size = int(str(ctx.size()[0].NUM_INT()))
        self.quantity = int(str(ctx.size()[1].NUM_INT()))

        #Checando Tiles#
        self.visitTile(ctx.tile())

        for x in range(0, self.quantity):
            self.imageArray.append(np.random.random_integers(0, self.imageCounter, (self.size, self.size)))

        print(self.imageArray)
        return 1
    
    def visitTile(self,ctx: TileMapParser.TileContext):
        path = str(ctx.path().CADEIA())
        name = str(ctx.ID())

        if ctx is not None:
            self.visitRecur_tiles(ctx.recur_tiles())
        
        return 1


    def visitRecur_tiles(self, ctx: TileMapParser.Recur_tilesContext):
        self.imageCounter+=1
        return self.visitTile(ctx.tile()) if ctx.tile() is not None else ''


        
