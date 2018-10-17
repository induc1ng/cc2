from ANTLR.TileMapVisitor import *
from ANTLR.TileMapParser import *


class Semantico(TileMapVisitor):

    def visitPrograma(self, ctx: TileMapParser.MapaContext):
        print(ctx.getText())
