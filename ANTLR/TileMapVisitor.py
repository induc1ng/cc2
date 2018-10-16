# Generated from .\TileMap.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .TileMapParser import TileMapParser
else:
    from TileMapParser import TileMapParser

# This class defines a complete generic visitor for a parse tree produced by TileMapParser.

class TileMapVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TileMapParser#mapa.
    def visitMapa(self, ctx:TileMapParser.MapaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#commands.
    def visitCommands(self, ctx:TileMapParser.CommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#recur_commands.
    def visitRecur_commands(self, ctx:TileMapParser.Recur_commandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#add.
    def visitAdd(self, ctx:TileMapParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#remove.
    def visitRemove(self, ctx:TileMapParser.RemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#tile.
    def visitTile(self, ctx:TileMapParser.TileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#recur_tiles.
    def visitRecur_tiles(self, ctx:TileMapParser.Recur_tilesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#tipoTyle.
    def visitTipoTyle(self, ctx:TileMapParser.TipoTyleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#size.
    def visitSize(self, ctx:TileMapParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#nivel.
    def visitNivel(self, ctx:TileMapParser.NivelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TileMapParser#path.
    def visitPath(self, ctx:TileMapParser.PathContext):
        return self.visitChildren(ctx)



del TileMapParser