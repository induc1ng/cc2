# Generated from .\TileMap.g4 by ANTLR 4.7.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26")
        buf.write("`\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2%\n\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2+\n\2\3\2\5\2.\n\2\3\2\3\2\3\2\3\3\3\3\5\3\65")
        buf.write("\n\3\3\3\3\3\3\4\3\4\5\4;\n\4\3\5\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\5\bN\n\b")
        buf.write("\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2")
        buf.write("\2\2Z\2\30\3\2\2\2\4\64\3\2\2\2\6:\3\2\2\2\b<\3\2\2\2")
        buf.write("\n@\3\2\2\2\fD\3\2\2\2\16M\3\2\2\2\20O\3\2\2\2\22S\3\2")
        buf.write("\2\2\24W\3\2\2\2\26[\3\2\2\2\30\31\7\3\2\2\31\32\7\4\2")
        buf.write("\2\32\33\5\22\n\2\33\34\7\5\2\2\34\35\7\6\2\2\35\36\7")
        buf.write("\4\2\2\36\37\5\22\n\2\37 \7\5\2\2 !\7\7\2\2!\"\7\b\2\2")
        buf.write("\"$\7\7\2\2#%\5\f\7\2$#\3\2\2\2$%\3\2\2\2%&\3\2\2\2&\'")
        buf.write("\7\t\2\2\'-\7\n\2\2(*\7\7\2\2)+\5\4\3\2*)\3\2\2\2*+\3")
        buf.write("\2\2\2+,\3\2\2\2,.\7\t\2\2-(\3\2\2\2-.\3\2\2\2./\3\2\2")
        buf.write("\2/\60\7\t\2\2\60\61\7\2\2\3\61\3\3\2\2\2\62\65\5\b\5")
        buf.write("\2\63\65\5\n\6\2\64\62\3\2\2\2\64\63\3\2\2\2\65\66\3\2")
        buf.write("\2\2\66\67\5\6\4\2\67\5\3\2\2\28;\5\4\3\29;\3\2\2\2:8")
        buf.write("\3\2\2\2:9\3\2\2\2;\7\3\2\2\2<=\7\13\2\2=>\5\20\t\2>?")
        buf.write("\7\23\2\2?\t\3\2\2\2@A\7\f\2\2AB\5\f\7\2BC\7\23\2\2C\13")
        buf.write("\3\2\2\2DE\7\22\2\2EF\7\7\2\2FG\5\26\f\2GH\5\20\t\2HI")
        buf.write("\7\t\2\2IJ\5\16\b\2J\r\3\2\2\2KN\5\f\7\2LN\3\2\2\2MK\3")
        buf.write("\2\2\2ML\3\2\2\2N\17\3\2\2\2OP\7\r\2\2PQ\7\16\2\2QR\7")
        buf.write("\22\2\2R\21\3\2\2\2ST\7\17\2\2TU\7\16\2\2UV\7\23\2\2V")
        buf.write("\23\3\2\2\2WX\7\20\2\2XY\7\16\2\2YZ\7\23\2\2Z\25\3\2\2")
        buf.write("\2[\\\7\21\2\2\\]\7\16\2\2]^\7\25\2\2^\27\3\2\2\2\b$*")
        buf.write("-\64:M")
        return buf.getvalue()


class TileMapParser ( Parser ):

    grammarFileName = "TileMap.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'map'", "'('", "')'", "'quantity'", "'{'", 
                     "'import:'", "'}'", "'commands'", "'add'", "'remove'", 
                     "'type'", "':'", "'size'", "'nivel'", "'path'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "ID", "NUM_INT", "NUM_REAL", "CADEIA", "WS" ]

    RULE_mapa = 0
    RULE_commands = 1
    RULE_recur_commands = 2
    RULE_add = 3
    RULE_remove = 4
    RULE_tile = 5
    RULE_recur_tiles = 6
    RULE_tipoTyle = 7
    RULE_size = 8
    RULE_nivel = 9
    RULE_path = 10

    ruleNames =  [ "mapa", "commands", "recur_commands", "add", "remove", 
                   "tile", "recur_tiles", "tipoTyle", "size", "nivel", "path" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    ID=16
    NUM_INT=17
    NUM_REAL=18
    CADEIA=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MapaContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def size(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TileMapParser.SizeContext)
            else:
                return self.getTypedRuleContext(TileMapParser.SizeContext,i)


        def EOF(self):
            return self.getToken(TileMapParser.EOF, 0)

        def tile(self):
            return self.getTypedRuleContext(TileMapParser.TileContext,0)


        def commands(self):
            return self.getTypedRuleContext(TileMapParser.CommandsContext,0)


        def getRuleIndex(self):
            return TileMapParser.RULE_mapa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapa" ):
                listener.enterMapa(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapa" ):
                listener.exitMapa(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapa" ):
                return visitor.visitMapa(self)
            else:
                return visitor.visitChildren(self)




    def mapa(self):

        localctx = TileMapParser.MapaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_mapa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(TileMapParser.T__0)
            self.state = 23
            self.match(TileMapParser.T__1)
            self.state = 24
            self.size()
            self.state = 25
            self.match(TileMapParser.T__2)
            self.state = 26
            self.match(TileMapParser.T__3)
            self.state = 27
            self.match(TileMapParser.T__1)
            self.state = 28
            self.size()
            self.state = 29
            self.match(TileMapParser.T__2)
            self.state = 30
            self.match(TileMapParser.T__4)
            self.state = 31
            self.match(TileMapParser.T__5)
            self.state = 32
            self.match(TileMapParser.T__4)
            self.state = 34
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TileMapParser.ID:
                self.state = 33
                self.tile()


            self.state = 36
            self.match(TileMapParser.T__6)
            self.state = 37
            self.match(TileMapParser.T__7)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==TileMapParser.T__4:
                self.state = 38
                self.match(TileMapParser.T__4)
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==TileMapParser.T__8 or _la==TileMapParser.T__9:
                    self.state = 39
                    self.commands()


                self.state = 42
                self.match(TileMapParser.T__6)


            self.state = 45
            self.match(TileMapParser.T__6)
            self.state = 46
            self.match(TileMapParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CommandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def recur_commands(self):
            return self.getTypedRuleContext(TileMapParser.Recur_commandsContext,0)


        def add(self):
            return self.getTypedRuleContext(TileMapParser.AddContext,0)


        def remove(self):
            return self.getTypedRuleContext(TileMapParser.RemoveContext,0)


        def getRuleIndex(self):
            return TileMapParser.RULE_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommands" ):
                listener.enterCommands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommands" ):
                listener.exitCommands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCommands" ):
                return visitor.visitCommands(self)
            else:
                return visitor.visitChildren(self)




    def commands(self):

        localctx = TileMapParser.CommandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_commands)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TileMapParser.T__8]:
                self.state = 48
                self.add()
                pass
            elif token in [TileMapParser.T__9]:
                self.state = 49
                self.remove()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 52
            self.recur_commands()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Recur_commandsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def commands(self):
            return self.getTypedRuleContext(TileMapParser.CommandsContext,0)


        def getRuleIndex(self):
            return TileMapParser.RULE_recur_commands

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecur_commands" ):
                listener.enterRecur_commands(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecur_commands" ):
                listener.exitRecur_commands(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecur_commands" ):
                return visitor.visitRecur_commands(self)
            else:
                return visitor.visitChildren(self)




    def recur_commands(self):

        localctx = TileMapParser.Recur_commandsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_recur_commands)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TileMapParser.T__8, TileMapParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.commands()
                pass
            elif token in [TileMapParser.T__6]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AddContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoTyle(self):
            return self.getTypedRuleContext(TileMapParser.TipoTyleContext,0)


        def NUM_INT(self):
            return self.getToken(TileMapParser.NUM_INT, 0)

        def getRuleIndex(self):
            return TileMapParser.RULE_add

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdd" ):
                return visitor.visitAdd(self)
            else:
                return visitor.visitChildren(self)




    def add(self):

        localctx = TileMapParser.AddContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_add)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(TileMapParser.T__8)
            self.state = 59
            self.tipoTyle()
            self.state = 60
            self.match(TileMapParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RemoveContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tile(self):
            return self.getTypedRuleContext(TileMapParser.TileContext,0)


        def NUM_INT(self):
            return self.getToken(TileMapParser.NUM_INT, 0)

        def getRuleIndex(self):
            return TileMapParser.RULE_remove

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRemove" ):
                listener.enterRemove(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRemove" ):
                listener.exitRemove(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRemove" ):
                return visitor.visitRemove(self)
            else:
                return visitor.visitChildren(self)




    def remove(self):

        localctx = TileMapParser.RemoveContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_remove)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(TileMapParser.T__9)
            self.state = 63
            self.tile()
            self.state = 64
            self.match(TileMapParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TileMapParser.ID, 0)

        def path(self):
            return self.getTypedRuleContext(TileMapParser.PathContext,0)


        def tipoTyle(self):
            return self.getTypedRuleContext(TileMapParser.TipoTyleContext,0)


        def recur_tiles(self):
            return self.getTypedRuleContext(TileMapParser.Recur_tilesContext,0)


        def getRuleIndex(self):
            return TileMapParser.RULE_tile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTile" ):
                listener.enterTile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTile" ):
                listener.exitTile(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTile" ):
                return visitor.visitTile(self)
            else:
                return visitor.visitChildren(self)




    def tile(self):

        localctx = TileMapParser.TileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(TileMapParser.ID)
            self.state = 67
            self.match(TileMapParser.T__4)
            self.state = 68
            self.path()
            self.state = 69
            self.tipoTyle()
            self.state = 70
            self.match(TileMapParser.T__6)
            self.state = 71
            self.recur_tiles()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Recur_tilesContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tile(self):
            return self.getTypedRuleContext(TileMapParser.TileContext,0)


        def getRuleIndex(self):
            return TileMapParser.RULE_recur_tiles

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRecur_tiles" ):
                listener.enterRecur_tiles(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRecur_tiles" ):
                listener.exitRecur_tiles(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecur_tiles" ):
                return visitor.visitRecur_tiles(self)
            else:
                return visitor.visitChildren(self)




    def recur_tiles(self):

        localctx = TileMapParser.Recur_tilesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_recur_tiles)
        try:
            self.state = 75
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [TileMapParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.tile()
                pass
            elif token in [TileMapParser.T__6, TileMapParser.NUM_INT]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TipoTyleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(TileMapParser.ID, 0)

        def getRuleIndex(self):
            return TileMapParser.RULE_tipoTyle

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoTyle" ):
                listener.enterTipoTyle(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoTyle" ):
                listener.exitTipoTyle(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoTyle" ):
                return visitor.visitTipoTyle(self)
            else:
                return visitor.visitChildren(self)




    def tipoTyle(self):

        localctx = TileMapParser.TipoTyleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tipoTyle)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(TileMapParser.T__10)
            self.state = 78
            self.match(TileMapParser.T__11)
            self.state = 79
            self.match(TileMapParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SizeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(TileMapParser.NUM_INT, 0)

        def getRuleIndex(self):
            return TileMapParser.RULE_size

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSize" ):
                listener.enterSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSize" ):
                listener.exitSize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSize" ):
                return visitor.visitSize(self)
            else:
                return visitor.visitChildren(self)




    def size(self):

        localctx = TileMapParser.SizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_size)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(TileMapParser.T__12)
            self.state = 82
            self.match(TileMapParser.T__11)
            self.state = 83
            self.match(TileMapParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NivelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM_INT(self):
            return self.getToken(TileMapParser.NUM_INT, 0)

        def getRuleIndex(self):
            return TileMapParser.RULE_nivel

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNivel" ):
                listener.enterNivel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNivel" ):
                listener.exitNivel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNivel" ):
                return visitor.visitNivel(self)
            else:
                return visitor.visitChildren(self)




    def nivel(self):

        localctx = TileMapParser.NivelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_nivel)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(TileMapParser.T__13)
            self.state = 86
            self.match(TileMapParser.T__11)
            self.state = 87
            self.match(TileMapParser.NUM_INT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PathContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADEIA(self):
            return self.getToken(TileMapParser.CADEIA, 0)

        def getRuleIndex(self):
            return TileMapParser.RULE_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPath" ):
                listener.enterPath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPath" ):
                listener.exitPath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPath" ):
                return visitor.visitPath(self)
            else:
                return visitor.visitChildren(self)




    def path(self):

        localctx = TileMapParser.PathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(TileMapParser.T__14)
            self.state = 90
            self.match(TileMapParser.T__11)
            self.state = 91
            self.match(TileMapParser.CADEIA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





