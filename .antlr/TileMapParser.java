// Generated from c:\Users\Makoto\Desktop\cc2\cc2\TileMap.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TileMapParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, ID=16, NUM_INT=17, 
		NUM_REAL=18, CADEIA=19, WS=20;
	public static final int
		RULE_mapa = 0, RULE_commands = 1, RULE_recur_commands = 2, RULE_add = 3, 
		RULE_remove = 4, RULE_tile = 5, RULE_recur_tiles = 6, RULE_tipoTyle = 7, 
		RULE_size = 8, RULE_nivel = 9, RULE_path = 10;
	public static final String[] ruleNames = {
		"mapa", "commands", "recur_commands", "add", "remove", "tile", "recur_tiles", 
		"tipoTyle", "size", "nivel", "path"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'map'", "'('", "')'", "'quantity'", "'import'", "'{'", "'}'", "'commands'", 
		"'add'", "'remove'", "'type'", "':'", "'size'", "'nivel'", "'path'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, null, null, "ID", "NUM_INT", "NUM_REAL", "CADEIA", "WS"
	};
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "TileMap.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public TileMapParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}
	public static class MapaContext extends ParserRuleContext {
		public List<SizeContext> size() {
			return getRuleContexts(SizeContext.class);
		}
		public SizeContext size(int i) {
			return getRuleContext(SizeContext.class,i);
		}
		public TerminalNode EOF() { return getToken(TileMapParser.EOF, 0); }
		public TileContext tile() {
			return getRuleContext(TileContext.class,0);
		}
		public CommandsContext commands() {
			return getRuleContext(CommandsContext.class,0);
		}
		public MapaContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mapa; }
	}

	public final MapaContext mapa() throws RecognitionException {
		MapaContext _localctx = new MapaContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_mapa);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(22);
			match(T__0);
			setState(23);
			match(T__1);
			setState(24);
			size();
			setState(25);
			match(T__2);
			setState(26);
			match(T__3);
			setState(27);
			match(T__1);
			setState(28);
			size();
			setState(29);
			match(T__2);
			setState(30);
			match(T__4);
			setState(31);
			match(T__5);
			setState(33);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(32);
				tile();
				}
			}

			setState(35);
			match(T__6);
			setState(36);
			match(T__7);
			setState(37);
			match(T__5);
			setState(39);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__8 || _la==T__9) {
				{
				setState(38);
				commands();
				}
			}

			setState(41);
			match(T__6);
			setState(42);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CommandsContext extends ParserRuleContext {
		public Recur_commandsContext recur_commands() {
			return getRuleContext(Recur_commandsContext.class,0);
		}
		public AddContext add() {
			return getRuleContext(AddContext.class,0);
		}
		public RemoveContext remove() {
			return getRuleContext(RemoveContext.class,0);
		}
		public CommandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commands; }
	}

	public final CommandsContext commands() throws RecognitionException {
		CommandsContext _localctx = new CommandsContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_commands);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				{
				setState(44);
				add();
				}
				break;
			case T__9:
				{
				setState(45);
				remove();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(48);
			recur_commands();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Recur_commandsContext extends ParserRuleContext {
		public CommandsContext commands() {
			return getRuleContext(CommandsContext.class,0);
		}
		public Recur_commandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recur_commands; }
	}

	public final Recur_commandsContext recur_commands() throws RecognitionException {
		Recur_commandsContext _localctx = new Recur_commandsContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_recur_commands);
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
			case T__9:
				enterOuterAlt(_localctx, 1);
				{
				setState(50);
				commands();
				}
				break;
			case T__6:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AddContext extends ParserRuleContext {
		public TipoTyleContext tipoTyle() {
			return getRuleContext(TipoTyleContext.class,0);
		}
		public TerminalNode NUM_INT() { return getToken(TileMapParser.NUM_INT, 0); }
		public AddContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_add; }
	}

	public final AddContext add() throws RecognitionException {
		AddContext _localctx = new AddContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_add);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(T__8);
			setState(55);
			tipoTyle();
			setState(56);
			match(NUM_INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RemoveContext extends ParserRuleContext {
		public TileContext tile() {
			return getRuleContext(TileContext.class,0);
		}
		public TerminalNode NUM_INT() { return getToken(TileMapParser.NUM_INT, 0); }
		public RemoveContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_remove; }
	}

	public final RemoveContext remove() throws RecognitionException {
		RemoveContext _localctx = new RemoveContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_remove);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(T__9);
			setState(59);
			tile();
			setState(60);
			match(NUM_INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TileContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(TileMapParser.ID, 0); }
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public TipoTyleContext tipoTyle() {
			return getRuleContext(TipoTyleContext.class,0);
		}
		public Recur_tilesContext recur_tiles() {
			return getRuleContext(Recur_tilesContext.class,0);
		}
		public TileContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tile; }
	}

	public final TileContext tile() throws RecognitionException {
		TileContext _localctx = new TileContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_tile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(ID);
			setState(63);
			match(T__5);
			setState(64);
			path();
			setState(65);
			match(T__10);
			setState(66);
			match(T__11);
			setState(67);
			tipoTyle();
			setState(68);
			match(T__6);
			setState(69);
			recur_tiles();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Recur_tilesContext extends ParserRuleContext {
		public TileContext tile() {
			return getRuleContext(TileContext.class,0);
		}
		public Recur_tilesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recur_tiles; }
	}

	public final Recur_tilesContext recur_tiles() throws RecognitionException {
		Recur_tilesContext _localctx = new Recur_tilesContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_recur_tiles);
		try {
			setState(73);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(71);
				tile();
				}
				break;
			case T__6:
			case NUM_INT:
				enterOuterAlt(_localctx, 2);
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TipoTyleContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(TileMapParser.ID, 0); }
		public TipoTyleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipoTyle; }
	}

	public final TipoTyleContext tipoTyle() throws RecognitionException {
		TipoTyleContext _localctx = new TipoTyleContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_tipoTyle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SizeContext extends ParserRuleContext {
		public TerminalNode NUM_INT() { return getToken(TileMapParser.NUM_INT, 0); }
		public SizeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_size; }
	}

	public final SizeContext size() throws RecognitionException {
		SizeContext _localctx = new SizeContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_size);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(T__12);
			setState(78);
			match(T__11);
			setState(79);
			match(NUM_INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class NivelContext extends ParserRuleContext {
		public TerminalNode NUM_INT() { return getToken(TileMapParser.NUM_INT, 0); }
		public NivelContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nivel; }
	}

	public final NivelContext nivel() throws RecognitionException {
		NivelContext _localctx = new NivelContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_nivel);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			match(T__13);
			setState(82);
			match(T__11);
			setState(83);
			match(NUM_INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class PathContext extends ParserRuleContext {
		public TerminalNode CADEIA() { return getToken(TileMapParser.CADEIA, 0); }
		public PathContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_path; }
	}

	public final PathContext path() throws RecognitionException {
		PathContext _localctx = new PathContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_path);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(T__14);
			setState(86);
			match(T__11);
			setState(87);
			match(CADEIA);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\26\\\4\2\t\2\4\3"+
		"\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13"+
		"\4\f\t\f\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2$\n\2\3\2\3\2"+
		"\3\2\3\2\5\2*\n\2\3\2\3\2\3\2\3\3\3\3\5\3\61\n\3\3\3\3\3\3\4\3\4\5\4\67"+
		"\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\b\3\b\5\bL\n\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3"+
		"\f\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24\26\2\2\2U\2\30\3\2\2\2\4"+
		"\60\3\2\2\2\6\66\3\2\2\2\b8\3\2\2\2\n<\3\2\2\2\f@\3\2\2\2\16K\3\2\2\2"+
		"\20M\3\2\2\2\22O\3\2\2\2\24S\3\2\2\2\26W\3\2\2\2\30\31\7\3\2\2\31\32\7"+
		"\4\2\2\32\33\5\22\n\2\33\34\7\5\2\2\34\35\7\6\2\2\35\36\7\4\2\2\36\37"+
		"\5\22\n\2\37 \7\5\2\2 !\7\7\2\2!#\7\b\2\2\"$\5\f\7\2#\"\3\2\2\2#$\3\2"+
		"\2\2$%\3\2\2\2%&\7\t\2\2&\'\7\n\2\2\')\7\b\2\2(*\5\4\3\2)(\3\2\2\2)*\3"+
		"\2\2\2*+\3\2\2\2+,\7\t\2\2,-\7\2\2\3-\3\3\2\2\2.\61\5\b\5\2/\61\5\n\6"+
		"\2\60.\3\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\63\5\6\4\2\63\5\3\2\2\2\64"+
		"\67\5\4\3\2\65\67\3\2\2\2\66\64\3\2\2\2\66\65\3\2\2\2\67\7\3\2\2\289\7"+
		"\13\2\29:\5\20\t\2:;\7\23\2\2;\t\3\2\2\2<=\7\f\2\2=>\5\f\7\2>?\7\23\2"+
		"\2?\13\3\2\2\2@A\7\22\2\2AB\7\b\2\2BC\5\26\f\2CD\7\r\2\2DE\7\16\2\2EF"+
		"\5\20\t\2FG\7\t\2\2GH\5\16\b\2H\r\3\2\2\2IL\5\f\7\2JL\3\2\2\2KI\3\2\2"+
		"\2KJ\3\2\2\2L\17\3\2\2\2MN\7\22\2\2N\21\3\2\2\2OP\7\17\2\2PQ\7\16\2\2"+
		"QR\7\23\2\2R\23\3\2\2\2ST\7\20\2\2TU\7\16\2\2UV\7\23\2\2V\25\3\2\2\2W"+
		"X\7\21\2\2XY\7\16\2\2YZ\7\25\2\2Z\27\3\2\2\2\7#)\60\66K";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}