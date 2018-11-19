import antlr4
import os
import sys
import argparse
import glob
from ANTLR.TileMapLexer import *
from ANTLR.TileMapParser import *
from Sintatico import ErrosSintaticosErrorListener
from Gerador import Gerador
from Semantico import Semantico


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
            gerador = Gerador()
            gerador.visitMap(mapa)
            print('Compilação finalizada')

            codigo_gerado = gerador.getCodigo()

            arquivo = "Teste.html"
            arquivo_saida = open(arquivo, 'w', encoding='utf-8')
            arquivo_saida.write(codigo_gerado)
            arquivo_saida.close()            
        except Exception as e:
            print(str(e), file=sys.stderr)
            pass


def casos_de_teste_semantico():
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
            analisador_semantico = Semantico()
            analisador_semantico.visitMap(mapa)
            print('Compilação finalizada')
        except Exception as e:
            print(str(e), file=sys.stderr)
            pass


entrada = input("Deseja gerar o mapa?Y/N")
if entrada == "Y":
    casos_gerador()
else:
    casos_de_teste_semantico()
    

