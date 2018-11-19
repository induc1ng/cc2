from ANTLR.TileMapVisitor import *
from ANTLR.TileMapParser import *


class Tiles:
    def __init__(self, path, name, tipo):
        self.path = path
        self.name = name
        self.tipo = tipo



class Semantico(TileMapVisitor):

    #Variaveis Globais
    size = 0
    imageCounter = 0
    tipoCounter = 0
    addCounter = 0
    tile = []

    ## - Mensagens de Erro - ##

    def get_linha_do_erro(self, dados_do_erro):
        return 'Erro semântico na linha ' + str(dados_do_erro).split(',')[3].split(':')[0] + ': '

    def get_regra_do_erro(self, dados_do_erro):
        return ' no comando ' + str(dados_do_erro).split(',')[1].split('=')[1] + '.'

    def get_erro_variavel_ja_declarada(self,dados,variavel):
        erro = self.get_linha_do_erro(dados) + 'a variavel " ' + variavel + ' " ja foi declarada' + \
               self.get_regra_do_erro(dados)
        raise Exception(erro)

    def get_erro_tamanho(self,dados):
        erro = self.get_linha_do_erro(dados) + 'o tamanho exede o numero de mapas ' + \
               self.get_regra_do_erro(dados)
        raise Exception(erro)

    def get_erro_tamanho_zero(self,dados):
        erro = self.get_linha_do_erro(dados) + 'o tamanho tem que ser diferente de zero ' + \
               self.get_regra_do_erro(dados)
        raise Exception(erro)

    def get_erro_tipo_nao_declaro(self,dados,variavel):
        erro = self.get_linha_do_erro(dados) + 'o tipo " ' + variavel + ' " nao foi declarado' + \
               self.get_regra_do_erro(dados)
        raise Exception(erro)



    # Funcao para verficar se variavel esta na tabela #
    def checkTable(self,name,tile,imageCounter):
        for i in range(0, imageCounter):
            if(tile[i].name==name):
                return 0
        return 1
    
    def checkTableTipo(self,name,tile,tipoCounter):
        for i in range(0, tipoCounter):
            if(tile[i].tipo==name):
                return 0
        return 1    



    def visitMap(self, ctx: TileMapParser.MapaContext):
        self.size = int(str(ctx.size()[1].NUM_INT()))
        if ctx.tile() is not None:
            self.visitTile(ctx.tile())
        if ctx.commands() is not None:
            self.visitCommands(ctx.commands())


    def visitTile(self,ctx: TileMapParser.TileContext):
        if ctx is not None:
            path = str(ctx.path().CADEIA())
            name = str(ctx.ID())
            tipo = str(ctx.tipoTyle().ID())
            if(self.checkTable(name,self.tile,self.imageCounter)):
                    self.tile.append((Tiles(path,name,tipo)))
                    self.imageCounter+=1
                    self.tipoCounter+=1
            else:
                self.get_erro_variavel_ja_declarada(ctx.start, name)

        return self.visitRecur_tiles(ctx.recur_tiles())

    def visitCommands(self,ctx: TileMapParser.CommandsContext):

        if ctx is not None:
            if ctx.add() is not None:
                add_size = int(str(ctx.add().NUM_INT()))
                tipo = str(ctx.add().tipoTyle().ID())
                if(self.checkTableTipo(tipo,self.tile,self.tipoCounter) == 1):
                    self.get_erro_tipo_nao_declaro(ctx.start,tipo)                
                self.addCounter+=1
                if add_size==0:
                    self.get_erro_tamanho_zero(ctx.start)
                if add_size>int(self.size) or self.addCounter>int(self.size):
                    self.get_erro_tamanho(ctx.start)
                else:
                    self.addCounter+=1
        
        
        
        return self.visitRecur_commands(ctx.recur_commands())

    def visitRecur_tiles(self, ctx: TileMapParser.Recur_tilesContext):
        return "\n"+self.visitTile(ctx.tile()) if ctx.tile() is not None else ''

    def visitRecur_commands(self, ctx: TileMapParser.Recur_commandsContext):
        return "\n"+self.visitCommands(ctx.commands()) if ctx.commands() is not None else ''