import antlr4
import os
import sys
import argparse
import glob
from ANTLR.TileMapLexer import *
from ANTLR.TileMapParser import *
from Sintatico import ErrosSintaticosErrorListener
from Semantico import Semantico


def casos_de_teste_sintatico():
    # - Adicionar arquivos de teste - #
    name = sys.argv[1]
    outfile = open(sys.argv[2], 'w')
    with open(name) as caso_de_teste:
        programa = caso_de_teste.read()
        programa_input = antlr4.InputStream(programa)

        lexer = TileMapLexer(input=programa_input)
        lexer.removeErrorListeners()
        tokens = antlr4.CommonTokenStream(lexer=lexer)

        parser = TileMapParser(tokens)

        parser.removeErrorListeners()
        erros_sintaticos = ErrosSintaticosErrorListener()
        parser.addErrorListener(erros_sintaticos)
        # - Arrumar mensagem igual dos casos de teste - #
        try:
            parser.programa()
            print('Fim da compilacao')
        except Exception as e:
            print(str(e))
            outfile.write(str(e)+'\nFim da compilacao\n')
            pass


def casos_de_teste_semantico():
    with open('oi.txt', 'r') as caso_de_teste:
        programa = caso_de_teste.read()
        programa_input = antlr4.InputStream(programa)

        lexer = TileMapLexer(input=programa_input)
        lexer.removeErrorListeners()
        tokens = antlr4.CommonTokenStream(lexer=lexer)

        parser = TileMapParser(tokens)

        parser.removeErrorListeners()
        erros_sintaticos = ErrosSintaticosErrorListener()
        parser.addErrorListener(erros_sintaticos)
        try:
            programa = parser.programa()
            analisador_semantico = Semantico()
            analisador_semantico.visitPrograma(programa)
            print('[SEMANTICO] Compilação finalizada')
        except Exception as e:
            print('[SEMANTICO] ' +
                  str(e), file=sys.stderr)
            pass


casos_de_teste_sintatico()
