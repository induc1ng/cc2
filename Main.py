import antlr4
import os
import sys
import argparse
from ANTLR.LALexer import *
from ANTLR.LAParser import *
from Sintatico import ErrosSintaticosErrorListener


def casos_de_teste_sintatico():
    for i in range(1, 2):
        # - Adicionar arquivos de teste - #
        with open('caso_de_teste.txt', encoding='utf-8') as caso_de_teste:
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
                print(str(i) + '] compilação finalizada.')
            except Exception as e:
                print(str(e), file=sys.stderr)
                pass


casos_de_teste_sintatico()
