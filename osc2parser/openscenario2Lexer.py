# Generated from openscenario2.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from .openscenario2Parser import openscenario2Parser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2k")
        buf.write("\u0330\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4")
        buf.write("^\t^\4_\t_\4`\t`\4a\ta\4b\tb\4c\tc\4d\td\4e\te\4f\tf\4")
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13")
        buf.write("\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22\3\22")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27\3\30")
        buf.write("\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\37")
        buf.write("\3\37\3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%\3%\3%")
        buf.write("\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3")
        buf.write(")\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39\39\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3=\3>\3")
        buf.write(">\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3A\3A\3A\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3D\3D\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3G\3G\3G\3")
        buf.write("G\3G\3H\3H\3H\3H\3H\3H\3I\3I\3J\3J\3J\3K\3K\3K\3L\3L\3")
        buf.write("L\3L\3M\3M\3M\3M\3N\3N\3N\3O\3O\3P\3P\3P\3Q\3Q\3R\3R\3")
        buf.write("R\3S\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3Y\3Z\3")
        buf.write("Z\3Z\3Z\3Z\3Z\3[\3[\3[\3\\\3\\\5\\\u027e\n\\\3]\3]\3]")
        buf.write("\3]\7]\u0284\n]\f]\16]\u0287\13]\3]\3]\3]\3]\3]\7]\u028e")
        buf.write("\n]\f]\16]\u0291\13]\3]\5]\u0294\n]\3^\3^\3^\3^\3^\3^")
        buf.write("\3^\7^\u029d\n^\f^\16^\u02a0\13^\3^\3^\3^\3^\3^\3^\3^")
        buf.write("\3^\3^\3^\7^\u02ac\n^\f^\16^\u02af\13^\3^\3^\3^\5^\u02b4")
        buf.write("\n^\3_\3_\3_\3_\3_\3_\3_\3_\3_\5_\u02bf\n_\3`\3`\3`\5")
        buf.write("`\u02c4\n`\3a\6a\u02c7\na\ra\16a\u02c8\3b\3b\3b\3b\6b")
        buf.write("\u02cf\nb\rb\16b\u02d0\3c\3c\6c\u02d5\nc\rc\16c\u02d6")
        buf.write("\3d\3d\3e\3e\5e\u02dd\ne\3f\5f\u02e0\nf\3f\7f\u02e3\n")
        buf.write("f\ff\16f\u02e6\13f\3f\3f\6f\u02ea\nf\rf\16f\u02eb\3f\3")
        buf.write("f\5f\u02f0\nf\3f\6f\u02f3\nf\rf\16f\u02f4\5f\u02f7\nf")
        buf.write("\3g\3g\7g\u02fb\ng\fg\16g\u02fe\13g\3g\3g\6g\u0302\ng")
        buf.write("\rg\16g\u0303\3g\5g\u0307\ng\3h\3h\5h\u030b\nh\3h\3h\3")
        buf.write("i\3i\5i\u0311\ni\3i\3i\3i\3i\3j\5j\u0318\nj\3j\3j\7j\u031c")
        buf.write("\nj\fj\16j\u031f\13j\3k\6k\u0322\nk\rk\16k\u0323\3k\3")
        buf.write("k\3l\3l\7l\u032a\nl\fl\16l\u032d\13l\3l\3l\2\2m\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q:s;u<w=y>")
        buf.write("{?}@\177A\u0081B\u0083C\u0085D\u0087E\u0089F\u008bG\u008d")
        buf.write("H\u008fI\u0091J\u0093K\u0095L\u0097M\u0099N\u009bO\u009d")
        buf.write("P\u009fQ\u00a1R\u00a3S\u00a5T\u00a7U\u00a9V\u00abW\u00ad")
        buf.write("X\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7]\u00b9^\u00bb_\u00bd")
        buf.write("`\u00bfa\u00c1b\u00c3c\u00c5d\u00c7\2\u00c9\2\u00cbe\u00cd")
        buf.write("f\u00cfg\u00d1h\u00d3i\u00d5j\u00d7k\3\2\f\7\2\f\f\17")
        buf.write("\17$$))^^\4\2\f\f\17\17\5\2$$))^^\4\2CHch\4\2--//\4\2")
        buf.write("GGgg\4\2C\\c|\6\2\62;C\\aac|\3\2~~\4\2\13\13\"\"\2\u034e")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q")
        buf.write("\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2")
        buf.write("{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083")
        buf.write("\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2")
        buf.write("\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091")
        buf.write("\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2")
        buf.write("\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f")
        buf.write("\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2")
        buf.write("\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad")
        buf.write("\3\2\2\2\2\u00af\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2")
        buf.write("\2\2\u00b5\3\2\2\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb")
        buf.write("\3\2\2\2\2\u00bd\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2")
        buf.write("\2\2\u00c3\3\2\2\2\2\u00c5\3\2\2\2\2\u00cb\3\2\2\2\2\u00cd")
        buf.write("\3\2\2\2\2\u00cf\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2")
        buf.write("\2\2\u00d5\3\2\2\2\2\u00d7\3\2\2\2\3\u00d9\3\2\2\2\5\u00e0")
        buf.write("\3\2\2\2\7\u00e2\3\2\2\2\t\u00e7\3\2\2\2\13\u00ea\3\2")
        buf.write("\2\2\r\u00ee\3\2\2\2\17\u00f3\3\2\2\2\21\u00f9\3\2\2\2")
        buf.write("\23\u00fe\3\2\2\2\25\u0105\3\2\2\2\27\u010a\3\2\2\2\31")
        buf.write("\u010d\3\2\2\2\33\u0112\3\2\2\2\35\u0115\3\2\2\2\37\u0117")
        buf.write("\3\2\2\2!\u0119\3\2\2\2#\u011b\3\2\2\2%\u011d\3\2\2\2")
        buf.write("\'\u0124\3\2\2\2)\u012b\3\2\2\2+\u012e\3\2\2\2-\u0130")
        buf.write("\3\2\2\2/\u0132\3\2\2\2\61\u0134\3\2\2\2\63\u0136\3\2")
        buf.write("\2\2\65\u013a\3\2\2\2\67\u013d\3\2\2\29\u0141\3\2\2\2")
        buf.write(";\u0146\3\2\2\2=\u0148\3\2\2\2?\u014a\3\2\2\2A\u014c\3")
        buf.write("\2\2\2C\u0153\3\2\2\2E\u015c\3\2\2\2G\u015f\3\2\2\2I\u0165")
        buf.write("\3\2\2\2K\u016e\3\2\2\2M\u0175\3\2\2\2O\u017e\3\2\2\2")
        buf.write("Q\u0185\3\2\2\2S\u018b\3\2\2\2U\u018e\3\2\2\2W\u0190\3")
        buf.write("\2\2\2Y\u0193\3\2\2\2[\u0198\3\2\2\2]\u019d\3\2\2\2_\u01a5")
        buf.write("\3\2\2\2a\u01ab\3\2\2\2c\u01af\3\2\2\2e\u01b6\3\2\2\2")
        buf.write("g\u01bb\3\2\2\2i\u01c0\3\2\2\2k\u01c8\3\2\2\2m\u01cd\3")
        buf.write("\2\2\2o\u01dc\3\2\2\2q\u01e0\3\2\2\2s\u01e3\3\2\2\2u\u01ee")
        buf.write("\3\2\2\2w\u01f8\3\2\2\2y\u0201\3\2\2\2{\u0206\3\2\2\2")
        buf.write("}\u020c\3\2\2\2\177\u0213\3\2\2\2\u0081\u0216\3\2\2\2")
        buf.write("\u0083\u0219\3\2\2\2\u0085\u0220\3\2\2\2\u0087\u0227\3")
        buf.write("\2\2\2\u0089\u0230\3\2\2\2\u008b\u0235\3\2\2\2\u008d\u023a")
        buf.write("\3\2\2\2\u008f\u023f\3\2\2\2\u0091\u0245\3\2\2\2\u0093")
        buf.write("\u0247\3\2\2\2\u0095\u024a\3\2\2\2\u0097\u024d\3\2\2\2")
        buf.write("\u0099\u0251\3\2\2\2\u009b\u0255\3\2\2\2\u009d\u0258\3")
        buf.write("\2\2\2\u009f\u025a\3\2\2\2\u00a1\u025d\3\2\2\2\u00a3\u025f")
        buf.write("\3\2\2\2\u00a5\u0262\3\2\2\2\u00a7\u0265\3\2\2\2\u00a9")
        buf.write("\u0267\3\2\2\2\u00ab\u0269\3\2\2\2\u00ad\u026b\3\2\2\2")
        buf.write("\u00af\u026d\3\2\2\2\u00b1\u026f\3\2\2\2\u00b3\u0272\3")
        buf.write("\2\2\2\u00b5\u0278\3\2\2\2\u00b7\u027d\3\2\2\2\u00b9\u0293")
        buf.write("\3\2\2\2\u00bb\u02b3\3\2\2\2\u00bd\u02be\3\2\2\2\u00bf")
        buf.write("\u02c3\3\2\2\2\u00c1\u02c6\3\2\2\2\u00c3\u02ca\3\2\2\2")
        buf.write("\u00c5\u02d2\3\2\2\2\u00c7\u02d8\3\2\2\2\u00c9\u02dc\3")
        buf.write("\2\2\2\u00cb\u02df\3\2\2\2\u00cd\u0306\3\2\2\2\u00cf\u030a")
        buf.write("\3\2\2\2\u00d1\u030e\3\2\2\2\u00d3\u0317\3\2\2\2\u00d5")
        buf.write("\u0321\3\2\2\2\u00d7\u0327\3\2\2\2\u00d9\u00da\7k\2\2")
        buf.write("\u00da\u00db\7o\2\2\u00db\u00dc\7r\2\2\u00dc\u00dd\7q")
        buf.write("\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7v\2\2\u00df\4\3\2")
        buf.write("\2\2\u00e0\u00e1\7\60\2\2\u00e1\6\3\2\2\2\u00e2\u00e3")
        buf.write("\7n\2\2\u00e3\u00e4\7k\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6")
        buf.write("\7v\2\2\u00e6\b\3\2\2\2\u00e7\u00e8\7q\2\2\u00e8\u00e9")
        buf.write("\7h\2\2\u00e9\n\3\2\2\2\u00ea\u00eb\7k\2\2\u00eb\u00ec")
        buf.write("\7p\2\2\u00ec\u00ed\7v\2\2\u00ed\f\3\2\2\2\u00ee\u00ef")
        buf.write("\7w\2\2\u00ef\u00f0\7k\2\2\u00f0\u00f1\7p\2\2\u00f1\u00f2")
        buf.write("\7v\2\2\u00f2\16\3\2\2\2\u00f3\u00f4\7h\2\2\u00f4\u00f5")
        buf.write("\7n\2\2\u00f5\u00f6\7q\2\2\u00f6\u00f7\7c\2\2\u00f7\u00f8")
        buf.write("\7v\2\2\u00f8\20\3\2\2\2\u00f9\u00fa\7d\2\2\u00fa\u00fb")
        buf.write("\7q\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7n\2\2\u00fd\22")
        buf.write("\3\2\2\2\u00fe\u00ff\7u\2\2\u00ff\u0100\7v\2\2\u0100\u0101")
        buf.write("\7t\2\2\u0101\u0102\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104")
        buf.write("\7i\2\2\u0104\24\3\2\2\2\u0105\u0106\7v\2\2\u0106\u0107")
        buf.write("\7{\2\2\u0107\u0108\7r\2\2\u0108\u0109\7g\2\2\u0109\26")
        buf.write("\3\2\2\2\u010a\u010b\7k\2\2\u010b\u010c\7u\2\2\u010c\30")
        buf.write("\3\2\2\2\u010d\u010e\7w\2\2\u010e\u010f\7p\2\2\u010f\u0110")
        buf.write("\7k\2\2\u0110\u0111\7v\2\2\u0111\32\3\2\2\2\u0112\u0113")
        buf.write("\7U\2\2\u0113\u0114\7K\2\2\u0114\34\3\2\2\2\u0115\u0116")
        buf.write("\7*\2\2\u0116\36\3\2\2\2\u0117\u0118\7+\2\2\u0118 \3\2")
        buf.write("\2\2\u0119\u011a\7.\2\2\u011a\"\3\2\2\2\u011b\u011c\7")
        buf.write("<\2\2\u011c$\3\2\2\2\u011d\u011e\7h\2\2\u011e\u011f\7")
        buf.write("c\2\2\u011f\u0120\7e\2\2\u0120\u0121\7v\2\2\u0121\u0122")
        buf.write("\7q\2\2\u0122\u0123\7t\2\2\u0123&\3\2\2\2\u0124\u0125")
        buf.write("\7q\2\2\u0125\u0126\7h\2\2\u0126\u0127\7h\2\2\u0127\u0128")
        buf.write("\7u\2\2\u0128\u0129\7g\2\2\u0129\u012a\7v\2\2\u012a(\3")
        buf.write("\2\2\2\u012b\u012c\7m\2\2\u012c\u012d\7i\2\2\u012d*\3")
        buf.write("\2\2\2\u012e\u012f\7o\2\2\u012f,\3\2\2\2\u0130\u0131\7")
        buf.write("u\2\2\u0131.\3\2\2\2\u0132\u0133\7C\2\2\u0133\60\3\2\2")
        buf.write("\2\u0134\u0135\7M\2\2\u0135\62\3\2\2\2\u0136\u0137\7o")
        buf.write("\2\2\u0137\u0138\7q\2\2\u0138\u0139\7n\2\2\u0139\64\3")
        buf.write("\2\2\2\u013a\u013b\7e\2\2\u013b\u013c\7f\2\2\u013c\66")
        buf.write("\3\2\2\2\u013d\u013e\7t\2\2\u013e\u013f\7c\2\2\u013f\u0140")
        buf.write("\7f\2\2\u01408\3\2\2\2\u0141\u0142\7g\2\2\u0142\u0143")
        buf.write("\7p\2\2\u0143\u0144\7w\2\2\u0144\u0145\7o\2\2\u0145:\3")
        buf.write("\2\2\2\u0146\u0147\7]\2\2\u0147<\3\2\2\2\u0148\u0149\7")
        buf.write("_\2\2\u0149>\3\2\2\2\u014a\u014b\7?\2\2\u014b@\3\2\2\2")
        buf.write("\u014c\u014d\7u\2\2\u014d\u014e\7v\2\2\u014e\u014f\7t")
        buf.write("\2\2\u014f\u0150\7w\2\2\u0150\u0151\7e\2\2\u0151\u0152")
        buf.write("\7v\2\2\u0152B\3\2\2\2\u0153\u0154\7k\2\2\u0154\u0155")
        buf.write("\7p\2\2\u0155\u0156\7j\2\2\u0156\u0157\7g\2\2\u0157\u0158")
        buf.write("\7t\2\2\u0158\u0159\7k\2\2\u0159\u015a\7v\2\2\u015a\u015b")
        buf.write("\7u\2\2\u015bD\3\2\2\2\u015c\u015d\7?\2\2\u015d\u015e")
        buf.write("\7?\2\2\u015eF\3\2\2\2\u015f\u0160\7c\2\2\u0160\u0161")
        buf.write("\7e\2\2\u0161\u0162\7v\2\2\u0162\u0163\7q\2\2\u0163\u0164")
        buf.write("\7t\2\2\u0164H\3\2\2\2\u0165\u0166\7u\2\2\u0166\u0167")
        buf.write("\7e\2\2\u0167\u0168\7g\2\2\u0168\u0169\7p\2\2\u0169\u016a")
        buf.write("\7c\2\2\u016a\u016b\7t\2\2\u016b\u016c\7k\2\2\u016c\u016d")
        buf.write("\7q\2\2\u016dJ\3\2\2\2\u016e\u016f\7c\2\2\u016f\u0170")
        buf.write("\7e\2\2\u0170\u0171\7v\2\2\u0171\u0172\7k\2\2\u0172\u0173")
        buf.write("\7q\2\2\u0173\u0174\7p\2\2\u0174L\3\2\2\2\u0175\u0176")
        buf.write("\7o\2\2\u0176\u0177\7q\2\2\u0177\u0178\7f\2\2\u0178\u0179")
        buf.write("\7k\2\2\u0179\u017a\7h\2\2\u017a\u017b\7k\2\2\u017b\u017c")
        buf.write("\7g\2\2\u017c\u017d\7t\2\2\u017dN\3\2\2\2\u017e\u017f")
        buf.write("\7g\2\2\u017f\u0180\7z\2\2\u0180\u0181\7v\2\2\u0181\u0182")
        buf.write("\7g\2\2\u0182\u0183\7p\2\2\u0183\u0184\7f\2\2\u0184P\3")
        buf.write("\2\2\2\u0185\u0186\7g\2\2\u0186\u0187\7x\2\2\u0187\u0188")
        buf.write("\7g\2\2\u0188\u0189\7p\2\2\u0189\u018a\7v\2\2\u018aR\3")
        buf.write("\2\2\2\u018b\u018c\7k\2\2\u018c\u018d\7h\2\2\u018dT\3")
        buf.write("\2\2\2\u018e\u018f\7B\2\2\u018fV\3\2\2\2\u0190\u0191\7")
        buf.write("c\2\2\u0191\u0192\7u\2\2\u0192X\3\2\2\2\u0193\u0194\7")
        buf.write("t\2\2\u0194\u0195\7k\2\2\u0195\u0196\7u\2\2\u0196\u0197")
        buf.write("\7g\2\2\u0197Z\3\2\2\2\u0198\u0199\7h\2\2\u0199\u019a")
        buf.write("\7c\2\2\u019a\u019b\7n\2\2\u019b\u019c\7n\2\2\u019c\\")
        buf.write("\3\2\2\2\u019d\u019e\7g\2\2\u019e\u019f\7n\2\2\u019f\u01a0")
        buf.write("\7c\2\2\u01a0\u01a1\7r\2\2\u01a1\u01a2\7u\2\2\u01a2\u01a3")
        buf.write("\7g\2\2\u01a3\u01a4\7f\2\2\u01a4^\3\2\2\2\u01a5\u01a6")
        buf.write("\7g\2\2\u01a6\u01a7\7x\2\2\u01a7\u01a8\7g\2\2\u01a8\u01a9")
        buf.write("\7t\2\2\u01a9\u01aa\7{\2\2\u01aa`\3\2\2\2\u01ab\u01ac")
        buf.write("\7x\2\2\u01ac\u01ad\7c\2\2\u01ad\u01ae\7t\2\2\u01aeb\3")
        buf.write("\2\2\2\u01af\u01b0\7u\2\2\u01b0\u01b1\7c\2\2\u01b1\u01b2")
        buf.write("\7o\2\2\u01b2\u01b3\7r\2\2\u01b3\u01b4\7n\2\2\u01b4\u01b5")
        buf.write("\7g\2\2\u01b5d\3\2\2\2\u01b6\u01b7\7y\2\2\u01b7\u01b8")
        buf.write("\7k\2\2\u01b8\u01b9\7v\2\2\u01b9\u01ba\7j\2\2\u01baf\3")
        buf.write("\2\2\2\u01bb\u01bc\7m\2\2\u01bc\u01bd\7g\2\2\u01bd\u01be")
        buf.write("\7g\2\2\u01be\u01bf\7r\2\2\u01bfh\3\2\2\2\u01c0\u01c1")
        buf.write("\7f\2\2\u01c1\u01c2\7g\2\2\u01c2\u01c3\7h\2\2\u01c3\u01c4")
        buf.write("\7c\2\2\u01c4\u01c5\7w\2\2\u01c5\u01c6\7n\2\2\u01c6\u01c7")
        buf.write("\7v\2\2\u01c7j\3\2\2\2\u01c8\u01c9\7j\2\2\u01c9\u01ca")
        buf.write("\7c\2\2\u01ca\u01cb\7t\2\2\u01cb\u01cc\7f\2\2\u01ccl\3")
        buf.write("\2\2\2\u01cd\u01ce\7t\2\2\u01ce\u01cf\7g\2\2\u01cf\u01d0")
        buf.write("\7o\2\2\u01d0\u01d1\7q\2\2\u01d1\u01d2\7x\2\2\u01d2\u01d3")
        buf.write("\7g\2\2\u01d3\u01d4\7a\2\2\u01d4\u01d5\7f\2\2\u01d5\u01d6")
        buf.write("\7g\2\2\u01d6\u01d7\7h\2\2\u01d7\u01d8\7c\2\2\u01d8\u01d9")
        buf.write("\7w\2\2\u01d9\u01da\7n\2\2\u01da\u01db\7v\2\2\u01dbn\3")
        buf.write("\2\2\2\u01dc\u01dd\7f\2\2\u01dd\u01de\7g\2\2\u01de\u01df")
        buf.write("\7h\2\2\u01dfp\3\2\2\2\u01e0\u01e1\7/\2\2\u01e1\u01e2")
        buf.write("\7@\2\2\u01e2r\3\2\2\2\u01e3\u01e4\7g\2\2\u01e4\u01e5")
        buf.write("\7z\2\2\u01e5\u01e6\7r\2\2\u01e6\u01e7\7t\2\2\u01e7\u01e8")
        buf.write("\7g\2\2\u01e8\u01e9\7u\2\2\u01e9\u01ea\7u\2\2\u01ea\u01eb")
        buf.write("\7k\2\2\u01eb\u01ec\7q\2\2\u01ec\u01ed\7p\2\2\u01edt\3")
        buf.write("\2\2\2\u01ee\u01ef\7w\2\2\u01ef\u01f0\7p\2\2\u01f0\u01f1")
        buf.write("\7f\2\2\u01f1\u01f2\7g\2\2\u01f2\u01f3\7h\2\2\u01f3\u01f4")
        buf.write("\7k\2\2\u01f4\u01f5\7p\2\2\u01f5\u01f6\7g\2\2\u01f6\u01f7")
        buf.write("\7f\2\2\u01f7v\3\2\2\2\u01f8\u01f9\7g\2\2\u01f9\u01fa")
        buf.write("\7z\2\2\u01fa\u01fb\7v\2\2\u01fb\u01fc\7g\2\2\u01fc\u01fd")
        buf.write("\7t\2\2\u01fd\u01fe\7p\2\2\u01fe\u01ff\7c\2\2\u01ff\u0200")
        buf.write("\7n\2\2\u0200x\3\2\2\2\u0201\u0202\7q\2\2\u0202\u0203")
        buf.write("\7p\2\2\u0203\u0204\7n\2\2\u0204\u0205\7{\2\2\u0205z\3")
        buf.write("\2\2\2\u0206\u0207\7e\2\2\u0207\u0208\7q\2\2\u0208\u0209")
        buf.write("\7x\2\2\u0209\u020a\7g\2\2\u020a\u020b\7t\2\2\u020b|\3")
        buf.write("\2\2\2\u020c\u020d\7t\2\2\u020d\u020e\7g\2\2\u020e\u020f")
        buf.write("\7e\2\2\u020f\u0210\7q\2\2\u0210\u0211\7t\2\2\u0211\u0212")
        buf.write("\7f\2\2\u0212~\3\2\2\2\u0213\u0214\7q\2\2\u0214\u0215")
        buf.write("\7p\2\2\u0215\u0080\3\2\2\2\u0216\u0217\7f\2\2\u0217\u0218")
        buf.write("\7q\2\2\u0218\u0082\3\2\2\2\u0219\u021a\7u\2\2\u021a\u021b")
        buf.write("\7g\2\2\u021b\u021c\7t\2\2\u021c\u021d\7k\2\2\u021d\u021e")
        buf.write("\7c\2\2\u021e\u021f\7n\2\2\u021f\u0084\3\2\2\2\u0220\u0221")
        buf.write("\7q\2\2\u0221\u0222\7p\2\2\u0222\u0223\7g\2\2\u0223\u0224")
        buf.write("\7a\2\2\u0224\u0225\7q\2\2\u0225\u0226\7h\2\2\u0226\u0086")
        buf.write("\3\2\2\2\u0227\u0228\7r\2\2\u0228\u0229\7c\2\2\u0229\u022a")
        buf.write("\7t\2\2\u022a\u022b\7c\2\2\u022b\u022c\7n\2\2\u022c\u022d")
        buf.write("\7n\2\2\u022d\u022e\7g\2\2\u022e\u022f\7n\2\2\u022f\u0088")
        buf.write("\3\2\2\2\u0230\u0231\7y\2\2\u0231\u0232\7c\2\2\u0232\u0233")
        buf.write("\7k\2\2\u0233\u0234\7v\2\2\u0234\u008a\3\2\2\2\u0235\u0236")
        buf.write("\7g\2\2\u0236\u0237\7o\2\2\u0237\u0238\7k\2\2\u0238\u0239")
        buf.write("\7v\2\2\u0239\u008c\3\2\2\2\u023a\u023b\7e\2\2\u023b\u023c")
        buf.write("\7c\2\2\u023c\u023d\7n\2\2\u023d\u023e\7n\2\2\u023e\u008e")
        buf.write("\3\2\2\2\u023f\u0240\7w\2\2\u0240\u0241\7p\2\2\u0241\u0242")
        buf.write("\7v\2\2\u0242\u0243\7k\2\2\u0243\u0244\7n\2\2\u0244\u0090")
        buf.write("\3\2\2\2\u0245\u0246\7A\2\2\u0246\u0092\3\2\2\2\u0247")
        buf.write("\u0248\7?\2\2\u0248\u0249\7@\2\2\u0249\u0094\3\2\2\2\u024a")
        buf.write("\u024b\7q\2\2\u024b\u024c\7t\2\2\u024c\u0096\3\2\2\2\u024d")
        buf.write("\u024e\7c\2\2\u024e\u024f\7p\2\2\u024f\u0250\7f\2\2\u0250")
        buf.write("\u0098\3\2\2\2\u0251\u0252\7p\2\2\u0252\u0253\7q\2\2\u0253")
        buf.write("\u0254\7v\2\2\u0254\u009a\3\2\2\2\u0255\u0256\7#\2\2\u0256")
        buf.write("\u0257\7?\2\2\u0257\u009c\3\2\2\2\u0258\u0259\7>\2\2\u0259")
        buf.write("\u009e\3\2\2\2\u025a\u025b\7>\2\2\u025b\u025c\7?\2\2\u025c")
        buf.write("\u00a0\3\2\2\2\u025d\u025e\7@\2\2\u025e\u00a2\3\2\2\2")
        buf.write("\u025f\u0260\7@\2\2\u0260\u0261\7?\2\2\u0261\u00a4\3\2")
        buf.write("\2\2\u0262\u0263\7k\2\2\u0263\u0264\7p\2\2\u0264\u00a6")
        buf.write("\3\2\2\2\u0265\u0266\7-\2\2\u0266\u00a8\3\2\2\2\u0267")
        buf.write("\u0268\7/\2\2\u0268\u00aa\3\2\2\2\u0269\u026a\7,\2\2\u026a")
        buf.write("\u00ac\3\2\2\2\u026b\u026c\7\61\2\2\u026c\u00ae\3\2\2")
        buf.write("\2\u026d\u026e\7\'\2\2\u026e\u00b0\3\2\2\2\u026f\u0270")
        buf.write("\7k\2\2\u0270\u0271\7v\2\2\u0271\u00b2\3\2\2\2\u0272\u0273")
        buf.write("\7t\2\2\u0273\u0274\7c\2\2\u0274\u0275\7p\2\2\u0275\u0276")
        buf.write("\7i\2\2\u0276\u0277\7g\2\2\u0277\u00b4\3\2\2\2\u0278\u0279")
        buf.write("\7\60\2\2\u0279\u027a\7\60\2\2\u027a\u00b6\3\2\2\2\u027b")
        buf.write("\u027e\5\u00b9]\2\u027c\u027e\5\u00bb^\2\u027d\u027b\3")
        buf.write("\2\2\2\u027d\u027c\3\2\2\2\u027e\u00b8\3\2\2\2\u027f\u0285")
        buf.write("\7$\2\2\u0280\u0284\n\2\2\2\u0281\u0282\7^\2\2\u0282\u0284")
        buf.write("\n\3\2\2\u0283\u0280\3\2\2\2\u0283\u0281\3\2\2\2\u0284")
        buf.write("\u0287\3\2\2\2\u0285\u0283\3\2\2\2\u0285\u0286\3\2\2\2")
        buf.write("\u0286\u0288\3\2\2\2\u0287\u0285\3\2\2\2\u0288\u0294\7")
        buf.write("$\2\2\u0289\u028f\7)\2\2\u028a\u028e\n\2\2\2\u028b\u028c")
        buf.write("\7^\2\2\u028c\u028e\n\3\2\2\u028d\u028a\3\2\2\2\u028d")
        buf.write("\u028b\3\2\2\2\u028e\u0291\3\2\2\2\u028f\u028d\3\2\2\2")
        buf.write("\u028f\u0290\3\2\2\2\u0290\u0292\3\2\2\2\u0291\u028f\3")
        buf.write("\2\2\2\u0292\u0294\7)\2\2\u0293\u027f\3\2\2\2\u0293\u0289")
        buf.write("\3\2\2\2\u0294\u00ba\3\2\2\2\u0295\u0296\7$\2\2\u0296")
        buf.write("\u0297\7$\2\2\u0297\u0298\7$\2\2\u0298\u029e\3\2\2\2\u0299")
        buf.write("\u029d\n\4\2\2\u029a\u029b\7^\2\2\u029b\u029d\n\3\2\2")
        buf.write("\u029c\u0299\3\2\2\2\u029c\u029a\3\2\2\2\u029d\u02a0\3")
        buf.write("\2\2\2\u029e\u029c\3\2\2\2\u029e\u029f\3\2\2\2\u029f\u02a1")
        buf.write("\3\2\2\2\u02a0\u029e\3\2\2\2\u02a1\u02a2\7$\2\2\u02a2")
        buf.write("\u02a3\7$\2\2\u02a3\u02b4\7$\2\2\u02a4\u02a5\7)\2\2\u02a5")
        buf.write("\u02a6\7)\2\2\u02a6\u02a7\7)\2\2\u02a7\u02ad\3\2\2\2\u02a8")
        buf.write("\u02ac\n\4\2\2\u02a9\u02aa\7^\2\2\u02aa\u02ac\n\3\2\2")
        buf.write("\u02ab\u02a8\3\2\2\2\u02ab\u02a9\3\2\2\2\u02ac\u02af\3")
        buf.write("\2\2\2\u02ad\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u02b0")
        buf.write("\3\2\2\2\u02af\u02ad\3\2\2\2\u02b0\u02b1\7)\2\2\u02b1")
        buf.write("\u02b2\7)\2\2\u02b2\u02b4\7)\2\2\u02b3\u0295\3\2\2\2\u02b3")
        buf.write("\u02a4\3\2\2\2\u02b4\u00bc\3\2\2\2\u02b5\u02b6\7v\2\2")
        buf.write("\u02b6\u02b7\7t\2\2\u02b7\u02b8\7w\2\2\u02b8\u02bf\7g")
        buf.write("\2\2\u02b9\u02ba\7h\2\2\u02ba\u02bb\7c\2\2\u02bb\u02bc")
        buf.write("\7n\2\2\u02bc\u02bd\7u\2\2\u02bd\u02bf\7g\2\2\u02be\u02b5")
        buf.write("\3\2\2\2\u02be\u02b9\3\2\2\2\u02bf\u00be\3\2\2\2\u02c0")
        buf.write("\u02c4\5\u00c1a\2\u02c1\u02c4\5\u00c3b\2\u02c2\u02c4\5")
        buf.write("\u00c5c\2\u02c3\u02c0\3\2\2\2\u02c3\u02c1\3\2\2\2\u02c3")
        buf.write("\u02c2\3\2\2\2\u02c4\u00c0\3\2\2\2\u02c5\u02c7\5\u00c7")
        buf.write("d\2\u02c6\u02c5\3\2\2\2\u02c7\u02c8\3\2\2\2\u02c8\u02c6")
        buf.write("\3\2\2\2\u02c8\u02c9\3\2\2\2\u02c9\u00c2\3\2\2\2\u02ca")
        buf.write("\u02cb\7\62\2\2\u02cb\u02cc\7z\2\2\u02cc\u02ce\3\2\2\2")
        buf.write("\u02cd\u02cf\5\u00c9e\2\u02ce\u02cd\3\2\2\2\u02cf\u02d0")
        buf.write("\3\2\2\2\u02d0\u02ce\3\2\2\2\u02d0\u02d1\3\2\2\2\u02d1")
        buf.write("\u00c4\3\2\2\2\u02d2\u02d4\7/\2\2\u02d3\u02d5\5\u00c7")
        buf.write("d\2\u02d4\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6\u02d4")
        buf.write("\3\2\2\2\u02d6\u02d7\3\2\2\2\u02d7\u00c6\3\2\2\2\u02d8")
        buf.write("\u02d9\4\62;\2\u02d9\u00c8\3\2\2\2\u02da\u02dd\5\u00c7")
        buf.write("d\2\u02db\u02dd\t\5\2\2\u02dc\u02da\3\2\2\2\u02dc\u02db")
        buf.write("\3\2\2\2\u02dd\u00ca\3\2\2\2\u02de\u02e0\t\6\2\2\u02df")
        buf.write("\u02de\3\2\2\2\u02df\u02e0\3\2\2\2\u02e0\u02e4\3\2\2\2")
        buf.write("\u02e1\u02e3\5\u00c7d\2\u02e2\u02e1\3\2\2\2\u02e3\u02e6")
        buf.write("\3\2\2\2\u02e4\u02e2\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5")
        buf.write("\u02e7\3\2\2\2\u02e6\u02e4\3\2\2\2\u02e7\u02e9\7\60\2")
        buf.write("\2\u02e8\u02ea\5\u00c7d\2\u02e9\u02e8\3\2\2\2\u02ea\u02eb")
        buf.write("\3\2\2\2\u02eb\u02e9\3\2\2\2\u02eb\u02ec\3\2\2\2\u02ec")
        buf.write("\u02f6\3\2\2\2\u02ed\u02ef\t\7\2\2\u02ee\u02f0\t\6\2\2")
        buf.write("\u02ef\u02ee\3\2\2\2\u02ef\u02f0\3\2\2\2\u02f0\u02f2\3")
        buf.write("\2\2\2\u02f1\u02f3\5\u00c7d\2\u02f2\u02f1\3\2\2\2\u02f3")
        buf.write("\u02f4\3\2\2\2\u02f4\u02f2\3\2\2\2\u02f4\u02f5\3\2\2\2")
        buf.write("\u02f5\u02f7\3\2\2\2\u02f6\u02ed\3\2\2\2\u02f6\u02f7\3")
        buf.write("\2\2\2\u02f7\u00cc\3\2\2\2\u02f8\u02fc\t\b\2\2\u02f9\u02fb")
        buf.write("\t\t\2\2\u02fa\u02f9\3\2\2\2\u02fb\u02fe\3\2\2\2\u02fc")
        buf.write("\u02fa\3\2\2\2\u02fc\u02fd\3\2\2\2\u02fd\u0307\3\2\2\2")
        buf.write("\u02fe\u02fc\3\2\2\2\u02ff\u0301\7~\2\2\u0300\u0302\n")
        buf.write("\n\2\2\u0301\u0300\3\2\2\2\u0302\u0303\3\2\2\2\u0303\u0301")
        buf.write("\3\2\2\2\u0303\u0304\3\2\2\2\u0304\u0305\3\2\2\2\u0305")
        buf.write("\u0307\7~\2\2\u0306\u02f8\3\2\2\2\u0306\u02ff\3\2\2\2")
        buf.write("\u0307\u00ce\3\2\2\2\u0308\u030b\5\u00cbf\2\u0309\u030b")
        buf.write("\5\u00bf`\2\u030a\u0308\3\2\2\2\u030a\u0309\3\2\2\2\u030b")
        buf.write("\u030c\3\2\2\2\u030c\u030d\5\u00cdg\2\u030d\u00d0\3\2")
        buf.write("\2\2\u030e\u0310\7^\2\2\u030f\u0311\7\17\2\2\u0310\u030f")
        buf.write("\3\2\2\2\u0310\u0311\3\2\2\2\u0311\u0312\3\2\2\2\u0312")
        buf.write("\u0313\7\f\2\2\u0313\u0314\3\2\2\2\u0314\u0315\bi\2\2")
        buf.write("\u0315\u00d2\3\2\2\2\u0316\u0318\7\17\2\2\u0317\u0316")
        buf.write("\3\2\2\2\u0317\u0318\3\2\2\2\u0318\u0319\3\2\2\2\u0319")
        buf.write("\u031d\7\f\2\2\u031a\u031c\7\"\2\2\u031b\u031a\3\2\2\2")
        buf.write("\u031c\u031f\3\2\2\2\u031d\u031b\3\2\2\2\u031d\u031e\3")
        buf.write("\2\2\2\u031e\u00d4\3\2\2\2\u031f\u031d\3\2\2\2\u0320\u0322")
        buf.write("\t\13\2\2\u0321\u0320\3\2\2\2\u0322\u0323\3\2\2\2\u0323")
        buf.write("\u0321\3\2\2\2\u0323\u0324\3\2\2\2\u0324\u0325\3\2\2\2")
        buf.write("\u0325\u0326\bk\2\2\u0326\u00d6\3\2\2\2\u0327\u032b\7")
        buf.write("%\2\2\u0328\u032a\n\3\2\2\u0329\u0328\3\2\2\2\u032a\u032d")
        buf.write("\3\2\2\2\u032b\u0329\3\2\2\2\u032b\u032c\3\2\2\2\u032c")
        buf.write("\u032e\3\2\2\2\u032d\u032b\3\2\2\2\u032e\u032f\bl\2\2")
        buf.write("\u032f\u00d8\3\2\2\2#\2\u027d\u0283\u0285\u028d\u028f")
        buf.write("\u0293\u029c\u029e\u02ab\u02ad\u02b3\u02be\u02c3\u02c8")
        buf.write("\u02d0\u02d6\u02dc\u02df\u02e4\u02eb\u02ef\u02f4\u02f6")
        buf.write("\u02fc\u0303\u0306\u030a\u0310\u0317\u031d\u0323\u032b")
        buf.write("\3\b\2\2")
        return buf.getvalue()


class openscenario2Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    T__33 = 34
    T__34 = 35
    T__35 = 36
    T__36 = 37
    T__37 = 38
    T__38 = 39
    T__39 = 40
    T__40 = 41
    T__41 = 42
    T__42 = 43
    T__43 = 44
    T__44 = 45
    T__45 = 46
    T__46 = 47
    T__47 = 48
    T__48 = 49
    T__49 = 50
    T__50 = 51
    T__51 = 52
    T__52 = 53
    T__53 = 54
    T__54 = 55
    T__55 = 56
    T__56 = 57
    T__57 = 58
    T__58 = 59
    T__59 = 60
    T__60 = 61
    T__61 = 62
    T__62 = 63
    T__63 = 64
    T__64 = 65
    T__65 = 66
    T__66 = 67
    T__67 = 68
    T__68 = 69
    T__69 = 70
    T__70 = 71
    T__71 = 72
    T__72 = 73
    T__73 = 74
    T__74 = 75
    T__75 = 76
    T__76 = 77
    T__77 = 78
    T__78 = 79
    T__79 = 80
    T__80 = 81
    T__81 = 82
    T__82 = 83
    T__83 = 84
    T__84 = 85
    T__85 = 86
    T__86 = 87
    T__87 = 88
    T__88 = 89
    T__89 = 90
    STRING_LITERAL = 91
    SHORTSTRING = 92
    LONGSTRING = 93
    BOOL_LITERAL = 94
    INTEGER_LITERAL = 95
    UINT_LITERAL = 96
    HEX_UINT_LITERAL = 97
    INT_LITERAL = 98
    FLOAT_LITERAL = 99
    IDENTIFIER = 100
    PHYSICAL_LITERAL = 101
    LINEJOINER = 102
    NEWLINE = 103
    WS = 104
    COMMENT = 105

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'.'", "'list'", "'of'", "'int'", "'uint'", "'float'", 
            "'bool'", "'string'", "'type'", "'is'", "'unit'", "'SI'", "'('", 
            "')'", "','", "':'", "'factor'", "'offset'", "'kg'", "'m'", 
            "'s'", "'A'", "'K'", "'mol'", "'cd'", "'rad'", "'enum'", "'['", 
            "']'", "'='", "'struct'", "'inherits'", "'=='", "'actor'", "'scenario'", 
            "'action'", "'modifier'", "'extend'", "'event'", "'if'", "'@'", 
            "'as'", "'rise'", "'fall'", "'elapsed'", "'every'", "'var'", 
            "'sample'", "'with'", "'keep'", "'default'", "'hard'", "'remove_default'", 
            "'def'", "'->'", "'expression'", "'undefined'", "'external'", 
            "'only'", "'cover'", "'record'", "'on'", "'do'", "'serial'", 
            "'one_of'", "'parallel'", "'wait'", "'emit'", "'call'", "'until'", 
            "'?'", "'=>'", "'or'", "'and'", "'not'", "'!='", "'<'", "'<='", 
            "'>'", "'>='", "'in'", "'+'", "'-'", "'*'", "'/'", "'%'", "'it'", 
            "'range'", "'..'" ]

    symbolicNames = [ "<INVALID>",
            "STRING_LITERAL", "SHORTSTRING", "LONGSTRING", "BOOL_LITERAL", 
            "INTEGER_LITERAL", "UINT_LITERAL", "HEX_UINT_LITERAL", "INT_LITERAL", 
            "FLOAT_LITERAL", "IDENTIFIER", "PHYSICAL_LITERAL", "LINEJOINER", 
            "NEWLINE", "WS", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "T__28", "T__29", "T__30", "T__31", 
                  "T__32", "T__33", "T__34", "T__35", "T__36", "T__37", 
                  "T__38", "T__39", "T__40", "T__41", "T__42", "T__43", 
                  "T__44", "T__45", "T__46", "T__47", "T__48", "T__49", 
                  "T__50", "T__51", "T__52", "T__53", "T__54", "T__55", 
                  "T__56", "T__57", "T__58", "T__59", "T__60", "T__61", 
                  "T__62", "T__63", "T__64", "T__65", "T__66", "T__67", 
                  "T__68", "T__69", "T__70", "T__71", "T__72", "T__73", 
                  "T__74", "T__75", "T__76", "T__77", "T__78", "T__79", 
                  "T__80", "T__81", "T__82", "T__83", "T__84", "T__85", 
                  "T__86", "T__87", "T__88", "T__89", "STRING_LITERAL", 
                  "SHORTSTRING", "LONGSTRING", "BOOL_LITERAL", "INTEGER_LITERAL", 
                  "UINT_LITERAL", "HEX_UINT_LITERAL", "INT_LITERAL", "DIGIT", 
                  "HEX_DIGIT", "FLOAT_LITERAL", "IDENTIFIER", "PHYSICAL_LITERAL", 
                  "LINEJOINER", "NEWLINE", "WS", "COMMENT" ]

    grammarFileName = "openscenario2.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    class openscenario2Denter(DenterHelper):
        def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
            super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
            self.lexer: openscenario2Lexer = lexer

        def pull_token(self):
            return super(openscenario2Lexer, self.lexer).nextToken()

    denter = None

    def nextToken(self):
        if not self.denter:
            self.denter = self.openscenario2Denter(self, self.NEWLINE, openscenario2Parser.INDENT, openscenario2Parser.DEDENT, False)
        return self.denter.next_token()



