// Generated from c:\Users\Makoto\Desktop\cc2\cc2\TileMap.g4 by ANTLR 4.7.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class TileMapLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.7.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, ID=14, NUM_INT=15, NUM_REAL=16, 
		CADEIA=17, WS=18;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	public static final String[] ruleNames = {
		"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
		"T__9", "T__10", "T__11", "T__12", "ID", "NUM_INT", "NUM_REAL", "CADEIA", 
		"WS"
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


	public TileMapLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "TileMap.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\24\u0088\b\1\4\2"+
		"\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4"+
		"\13\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22"+
		"\t\22\4\23\t\23\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3"+
		"\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\t"+
		"\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f"+
		"\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\7\17d\n\17"+
		"\f\17\16\17g\13\17\3\20\6\20j\n\20\r\20\16\20k\3\21\6\21o\n\21\r\21\16"+
		"\21p\3\21\3\21\6\21u\n\21\r\21\16\21v\3\22\3\22\7\22{\n\22\f\22\16\22"+
		"~\13\22\3\22\3\22\3\23\6\23\u0083\n\23\r\23\16\23\u0084\3\23\3\23\2\2"+
		"\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35"+
		"\20\37\21!\22#\23%\24\3\2\6\5\2C\\aac|\6\2\62;C\\aac|\5\2\f\f\17\17$$"+
		"\5\2\13\f\17\17\"\"\2\u008d\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3"+
		"\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2"+
		"\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37"+
		"\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5+\3\2\2\2\7-\3"+
		"\2\2\2\t/\3\2\2\2\138\3\2\2\2\r?\3\2\2\2\17A\3\2\2\2\21C\3\2\2\2\23L\3"+
		"\2\2\2\25P\3\2\2\2\27U\3\2\2\2\31W\3\2\2\2\33\\\3\2\2\2\35a\3\2\2\2\37"+
		"i\3\2\2\2!n\3\2\2\2#x\3\2\2\2%\u0082\3\2\2\2\'(\7o\2\2()\7c\2\2)*\7r\2"+
		"\2*\4\3\2\2\2+,\7*\2\2,\6\3\2\2\2-.\7+\2\2.\b\3\2\2\2/\60\7s\2\2\60\61"+
		"\7w\2\2\61\62\7c\2\2\62\63\7p\2\2\63\64\7v\2\2\64\65\7k\2\2\65\66\7v\2"+
		"\2\66\67\7{\2\2\67\n\3\2\2\289\7k\2\29:\7o\2\2:;\7r\2\2;<\7q\2\2<=\7t"+
		"\2\2=>\7v\2\2>\f\3\2\2\2?@\7}\2\2@\16\3\2\2\2AB\7\177\2\2B\20\3\2\2\2"+
		"CD\7e\2\2DE\7q\2\2EF\7o\2\2FG\7o\2\2GH\7c\2\2HI\7p\2\2IJ\7f\2\2JK\7u\2"+
		"\2K\22\3\2\2\2LM\7c\2\2MN\7f\2\2NO\7f\2\2O\24\3\2\2\2PQ\7v\2\2QR\7{\2"+
		"\2RS\7r\2\2ST\7g\2\2T\26\3\2\2\2UV\7<\2\2V\30\3\2\2\2WX\7u\2\2XY\7k\2"+
		"\2YZ\7|\2\2Z[\7g\2\2[\32\3\2\2\2\\]\7r\2\2]^\7c\2\2^_\7v\2\2_`\7j\2\2"+
		"`\34\3\2\2\2ae\t\2\2\2bd\t\3\2\2cb\3\2\2\2dg\3\2\2\2ec\3\2\2\2ef\3\2\2"+
		"\2f\36\3\2\2\2ge\3\2\2\2hj\4\62;\2ih\3\2\2\2jk\3\2\2\2ki\3\2\2\2kl\3\2"+
		"\2\2l \3\2\2\2mo\4\62;\2nm\3\2\2\2op\3\2\2\2pn\3\2\2\2pq\3\2\2\2qr\3\2"+
		"\2\2rt\7\60\2\2su\4\62;\2ts\3\2\2\2uv\3\2\2\2vt\3\2\2\2vw\3\2\2\2w\"\3"+
		"\2\2\2x|\7$\2\2y{\n\4\2\2zy\3\2\2\2{~\3\2\2\2|z\3\2\2\2|}\3\2\2\2}\177"+
		"\3\2\2\2~|\3\2\2\2\177\u0080\7$\2\2\u0080$\3\2\2\2\u0081\u0083\t\5\2\2"+
		"\u0082\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0082\3\2\2\2\u0084\u0085"+
		"\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\b\23\2\2\u0087&\3\2\2\2\t\2e"+
		"kpv|\u0084\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}