import antlr4
import os
import sys
import argparse
import glob
from ANTLR.TileMapLexer import *
from ANTLR.TileMapParser import *
from Sintatico import ErrosSintaticosErrorListener
from Gerador import Gerador


def casos_de_teste_sintatico():
    # - Adicionar arquivos de teste - #
    name = sys.argv[1]
    outfile = open(sys.argv[2], 'w')
    with open(name) as caso_de_teste:
        mapa = caso_de_teste.read()
        mapa_input = antlr4.InputStream(mapa)

        lexer = TileMapLexer(input=mapa_input)
        lexer.removeErrorListeners()
        tokens = antlr4.CommonTokenStream(lexer=lexer)

        parser = TileMapParser(tokens)

        parser.removeErrorListeners()
        erros_sintaticos = ErrosSintaticosErrorListener()
        parser.addErrorListener(erros_sintaticos)
        # - Arrumar mensagem igual dos casos de teste - #
        try:
            parser.mapa()
            print('Fim da compilacao')
        except Exception as e:
            print(str(e))
            outfile.write(str(e)+'\nFim da compilacao\n')
            pass


def casos_gerador():
    with open('oi.txt', 'r') as caso_de_teste:
        mapa = caso_de_teste.read()
        mapa_input = antlr4.InputStream(mapa)

        lexer = TileMapLexer(input=mapa_input)
        lexer.removeErrorListeners()
        tokens = antlr4.CommonTokenStream(lexer=lexer)

        parser = TileMapParser(tokens)

        parser.removeErrorListeners()
        erros_sintaticos = ErrosSintaticosErrorListener()
        parser.addErrorListener(erros_sintaticos)
        try:
            mapa = parser.mapa()
            analisador_semantico = Gerador()
            analisador_semantico.visitMap(mapa)
            print('Compilação finalizada')
        except Exception as e:
            print('Erro?' +
                  str(e), file=sys.stderr)
            pass


casos_gerador()
