import antlr4
import os
import sys
import argparse
import glob
from ANTLR.LALexer import *
from ANTLR.LAParser import *
from Sintatico import ErrosSintaticosErrorListener


def casos_de_teste_sintatico():
    # - Adicionar arquivos de teste - #
    name = sys.argv[1]
    outfile = open(sys.argv[2], 'w')
    with open(name) as caso_de_teste:
        programa = caso_de_teste.read()
        programa_input = antlr4.InputStream(programa)

        lexer = LALexer(input=programa_input)
        lexer.removeErrorListeners()
        tokens = antlr4.CommonTokenStream(lexer=lexer)

        parser = LAParser(tokens)

        parser.removeErrorListeners()
        erros_sintaticos = ErrosSintaticosErrorListener()
        parser.addErrorListener(erros_sintaticos)
        # - Arrumar mensagem igual dos casos de teste - #
        try:
            parser.programa()
            print('Fim da compilacao')
        except Exception as e:
            print(str(e)+'\nFim da compilacao')
            outfile.write(str(e)+'Fim da compilacao')
            pass


casos_de_teste_sintatico()
