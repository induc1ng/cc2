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
		T__9=10, T__10=11, T__11=12, T__12=13, ID=14, NUM_INT=15, NUM_REAL=16, 
		CADEIA=17, WS=18;
	public static final int
		RULE_mapa = 0, RULE_commands = 1, RULE_recur_commands = 2, RULE_add = 3, 
		RULE_tile = 4, RULE_recur_tiles = 5, RULE_tipoTyle = 6, RULE_size = 7, 
		RULE_path = 8;
	public static final String[] ruleNames = {
		"mapa", "commands", "recur_commands", "add", "tile", "recur_tiles", "tipoTyle", 
		"size", "path"
	};

	private static final String[] _LITERAL_NAMES = {
		null, "'map'", "'('", "')'", "'quantity'", "'import'", "'{'", "'}'", "'commands'", 
		"'add'", "'type'", "':'", "'size'", "'path'"
	};
	private static final String[] _SYMBOLIC_NAMES = {
		null, null, null, null, null, null, null, null, null, null, null, null, 
		null, null, "ID", "NUM_INT", "NUM_REAL", "CADEIA", "WS"
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
			setState(18);
			match(T__0);
			setState(19);
			match(T__1);
			setState(20);
			size();
			setState(21);
			match(T__2);
			setState(22);
			match(T__3);
			setState(23);
			match(T__1);
			setState(24);
			size();
			setState(25);
			match(T__2);
			setState(26);
			match(T__4);
			setState(27);
			match(T__5);
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ID) {
				{
				setState(28);
				tile();
				}
			}

			setState(31);
			match(T__6);
			setState(32);
			match(T__7);
			setState(33);
			match(T__5);
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__8) {
				{
				setState(34);
				commands();
				}
			}

			setState(37);
			match(T__6);
			setState(38);
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
			{
			setState(40);
			add();
			}
			setState(41);
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
			setState(45);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__8:
				enterOuterAlt(_localctx, 1);
				{
				setState(43);
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
			setState(47);
			match(T__8);
			setState(48);
			tipoTyle();
			setState(49);
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
		enterRule(_localctx, 8, RULE_tile);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(51);
			match(ID);
			setState(52);
			match(T__5);
			setState(53);
			path();
			setState(54);
			match(T__9);
			setState(55);
			match(T__10);
			setState(56);
			tipoTyle();
			setState(57);
			match(T__6);
			setState(58);
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
		enterRule(_localctx, 10, RULE_recur_tiles);
		try {
			setState(62);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(60);
				tile();
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

	public static class TipoTyleContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(TileMapParser.ID, 0); }
		public TipoTyleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_tipoTyle; }
	}

	public final TipoTyleContext tipoTyle() throws RecognitionException {
		TipoTyleContext _localctx = new TipoTyleContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_tipoTyle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
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
		enterRule(_localctx, 14, RULE_size);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(66);
			match(T__11);
			setState(67);
			match(T__10);
			setState(68);
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
		enterRule(_localctx, 16, RULE_path);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(T__12);
			setState(71);
			match(T__10);
			setState(72);
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
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24M\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2"+
		"\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\5\2 \n\2\3\2\3\2\3\2\3\2\5\2&\n\2\3\2"+
		"\3\2\3\2\3\3\3\3\3\3\3\4\3\4\5\4\60\n\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3"+
		"\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\5\7A\n\7\3\b\3\b\3\t\3\t\3\t\3\t\3\n\3"+
		"\n\3\n\3\n\3\n\2\2\13\2\4\6\b\n\f\16\20\22\2\2\2G\2\24\3\2\2\2\4*\3\2"+
		"\2\2\6/\3\2\2\2\b\61\3\2\2\2\n\65\3\2\2\2\f@\3\2\2\2\16B\3\2\2\2\20D\3"+
		"\2\2\2\22H\3\2\2\2\24\25\7\3\2\2\25\26\7\4\2\2\26\27\5\20\t\2\27\30\7"+
		"\5\2\2\30\31\7\6\2\2\31\32\7\4\2\2\32\33\5\20\t\2\33\34\7\5\2\2\34\35"+
		"\7\7\2\2\35\37\7\b\2\2\36 \5\n\6\2\37\36\3\2\2\2\37 \3\2\2\2 !\3\2\2\2"+
		"!\"\7\t\2\2\"#\7\n\2\2#%\7\b\2\2$&\5\4\3\2%$\3\2\2\2%&\3\2\2\2&\'\3\2"+
		"\2\2\'(\7\t\2\2()\7\2\2\3)\3\3\2\2\2*+\5\b\5\2+,\5\6\4\2,\5\3\2\2\2-\60"+
		"\5\4\3\2.\60\3\2\2\2/-\3\2\2\2/.\3\2\2\2\60\7\3\2\2\2\61\62\7\13\2\2\62"+
		"\63\5\16\b\2\63\64\7\21\2\2\64\t\3\2\2\2\65\66\7\20\2\2\66\67\7\b\2\2"+
		"\678\5\22\n\289\7\f\2\29:\7\r\2\2:;\5\16\b\2;<\7\t\2\2<=\5\f\7\2=\13\3"+
		"\2\2\2>A\5\n\6\2?A\3\2\2\2@>\3\2\2\2@?\3\2\2\2A\r\3\2\2\2BC\7\20\2\2C"+
		"\17\3\2\2\2DE\7\16\2\2EF\7\r\2\2FG\7\21\2\2G\21\3\2\2\2HI\7\17\2\2IJ\7"+
		"\r\2\2JK\7\23\2\2K\23\3\2\2\2\6\37%/@";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}