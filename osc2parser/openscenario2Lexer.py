# Generated from openscenario2.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from .openscenario2Parser import openscenario2Parser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2m")
        buf.write("\u033d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\4n\tn\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21")
        buf.write("\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27")
        buf.write("\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3")
        buf.write("\"\3#\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3$\3%\3%\3%\3%\3%")
        buf.write("\3%\3&\3&\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'")
        buf.write("\3\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3")
        buf.write("*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3-\3-\3")
        buf.write(".\3.\3.\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66\3\66\3\66")
        buf.write("\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\3")
        buf.write("8\38\38\39\39\39\39\39\39\39\39\39\39\39\39\39\39\39\3")
        buf.write(":\3:\3:\3:\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3")
        buf.write("=\3=\3=\3=\3=\3=\3=\3=\3=\3=\3>\3>\3>\3>\3>\3>\3>\3>\3")
        buf.write(">\3?\3?\3?\3?\3?\3@\3@\3@\3@\3@\3@\3A\3A\3A\3A\3A\3A\3")
        buf.write("A\3B\3B\3B\3C\3C\3C\3D\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3")
        buf.write("E\3E\3E\3F\3F\3F\3F\3F\3F\3F\3F\3F\3G\3G\3G\3G\3G\3H\3")
        buf.write("H\3H\3H\3H\3I\3I\3I\3I\3I\3J\3J\3J\3J\3J\3J\3K\3K\3L\3")
        buf.write("L\3L\3M\3M\3M\3N\3N\3N\3N\3O\3O\3O\3O\3P\3P\3P\3Q\3Q\3")
        buf.write("R\3R\3R\3S\3S\3T\3T\3T\3U\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3")
        buf.write("Y\3Z\3Z\3[\3[\3[\3\\\3\\\3\\\3\\\3\\\3\\\3]\3]\3]\3^\3")
        buf.write("^\5^\u028b\n^\3_\3_\3_\3_\7_\u0291\n_\f_\16_\u0294\13")
        buf.write("_\3_\3_\3_\3_\3_\7_\u029b\n_\f_\16_\u029e\13_\3_\5_\u02a1")
        buf.write("\n_\3`\3`\3`\3`\3`\3`\3`\7`\u02aa\n`\f`\16`\u02ad\13`")
        buf.write("\3`\3`\3`\3`\3`\3`\3`\3`\3`\3`\7`\u02b9\n`\f`\16`\u02bc")
        buf.write("\13`\3`\3`\3`\5`\u02c1\n`\3a\3a\3a\3a\3a\3a\3a\3a\3a\5")
        buf.write("a\u02cc\na\3b\3b\3b\5b\u02d1\nb\3c\6c\u02d4\nc\rc\16c")
        buf.write("\u02d5\3d\3d\3d\3d\6d\u02dc\nd\rd\16d\u02dd\3e\3e\6e\u02e2")
        buf.write("\ne\re\16e\u02e3\3f\3f\3g\3g\5g\u02ea\ng\3h\5h\u02ed\n")
        buf.write("h\3h\7h\u02f0\nh\fh\16h\u02f3\13h\3h\3h\6h\u02f7\nh\r")
        buf.write("h\16h\u02f8\3h\3h\5h\u02fd\nh\3h\6h\u0300\nh\rh\16h\u0301")
        buf.write("\5h\u0304\nh\3i\3i\7i\u0308\ni\fi\16i\u030b\13i\3i\3i")
        buf.write("\6i\u030f\ni\ri\16i\u0310\3i\5i\u0314\ni\3j\3j\5j\u0318")
        buf.write("\nj\3j\3j\3k\3k\5k\u031e\nk\3k\3k\3k\3k\3l\5l\u0325\n")
        buf.write("l\3l\3l\7l\u0329\nl\fl\16l\u032c\13l\3m\6m\u032f\nm\r")
        buf.write("m\16m\u0330\3m\3m\3n\3n\7n\u0337\nn\fn\16n\u033a\13n\3")
        buf.write("n\3n\2\2o\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097")
        buf.write("M\u0099N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7")
        buf.write("U\u00a9V\u00abW\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7")
        buf.write("]\u00b9^\u00bb_\u00bd`\u00bfa\u00c1b\u00c3c\u00c5d\u00c7")
        buf.write("e\u00c9f\u00cb\2\u00cd\2\u00cfg\u00d1h\u00d3i\u00d5j\u00d7")
        buf.write("k\u00d9l\u00dbm\3\2\f\7\2\f\f\17\17$$))^^\4\2\f\f\17\17")
        buf.write("\5\2$$))^^\4\2CHch\4\2--//\4\2GGgg\4\2C\\c|\6\2\62;C\\")
        buf.write("aac|\3\2~~\4\2\13\13\"\"\2\u035b\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3")
        buf.write("\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2")
        buf.write(")\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2")
        buf.write("\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2")
        buf.write(";\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2")
        buf.write("\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2")
        buf.write("\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2")
        buf.write("\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3")
        buf.write("\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k")
        buf.write("\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2")
        buf.write("u\3\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2")
        buf.write("\2\177\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093")
        buf.write("\3\2\2\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af")
        buf.write("\3\2\2\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2")
        buf.write("\2\2\u00b7\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd")
        buf.write("\3\2\2\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2")
        buf.write("\2\2\u00c5\3\2\2\2\2\u00c7\3\2\2\2\2\u00c9\3\2\2\2\2\u00cf")
        buf.write("\3\2\2\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2")
        buf.write("\2\2\u00d7\3\2\2\2\2\u00d9\3\2\2\2\2\u00db\3\2\2\2\3\u00dd")
        buf.write("\3\2\2\2\5\u00e4\3\2\2\2\7\u00e6\3\2\2\2\t\u00eb\3\2\2")
        buf.write("\2\13\u00ee\3\2\2\2\r\u00f2\3\2\2\2\17\u00f7\3\2\2\2\21")
        buf.write("\u00fd\3\2\2\2\23\u0102\3\2\2\2\25\u0109\3\2\2\2\27\u010e")
        buf.write("\3\2\2\2\31\u0111\3\2\2\2\33\u0116\3\2\2\2\35\u0119\3")
        buf.write("\2\2\2\37\u011b\3\2\2\2!\u011d\3\2\2\2#\u011f\3\2\2\2")
        buf.write("%\u0121\3\2\2\2\'\u0128\3\2\2\2)\u012f\3\2\2\2+\u0132")
        buf.write("\3\2\2\2-\u0134\3\2\2\2/\u0136\3\2\2\2\61\u0138\3\2\2")
        buf.write("\2\63\u013a\3\2\2\2\65\u013e\3\2\2\2\67\u0141\3\2\2\2")
        buf.write("9\u0145\3\2\2\2;\u014a\3\2\2\2=\u014c\3\2\2\2?\u014e\3")
        buf.write("\2\2\2A\u0150\3\2\2\2C\u0152\3\2\2\2E\u0159\3\2\2\2G\u0162")
        buf.write("\3\2\2\2I\u0165\3\2\2\2K\u016b\3\2\2\2M\u0174\3\2\2\2")
        buf.write("O\u017b\3\2\2\2Q\u0184\3\2\2\2S\u018b\3\2\2\2U\u0192\3")
        buf.write("\2\2\2W\u0198\3\2\2\2Y\u019b\3\2\2\2[\u019d\3\2\2\2]\u01a0")
        buf.write("\3\2\2\2_\u01a5\3\2\2\2a\u01aa\3\2\2\2c\u01b2\3\2\2\2")
        buf.write("e\u01b8\3\2\2\2g\u01bc\3\2\2\2i\u01c3\3\2\2\2k\u01c8\3")
        buf.write("\2\2\2m\u01cd\3\2\2\2o\u01d5\3\2\2\2q\u01da\3\2\2\2s\u01e9")
        buf.write("\3\2\2\2u\u01ed\3\2\2\2w\u01f0\3\2\2\2y\u01fb\3\2\2\2")
        buf.write("{\u0205\3\2\2\2}\u020e\3\2\2\2\177\u0213\3\2\2\2\u0081")
        buf.write("\u0219\3\2\2\2\u0083\u0220\3\2\2\2\u0085\u0223\3\2\2\2")
        buf.write("\u0087\u0226\3\2\2\2\u0089\u022d\3\2\2\2\u008b\u0234\3")
        buf.write("\2\2\2\u008d\u023d\3\2\2\2\u008f\u0242\3\2\2\2\u0091\u0247")
        buf.write("\3\2\2\2\u0093\u024c\3\2\2\2\u0095\u0252\3\2\2\2\u0097")
        buf.write("\u0254\3\2\2\2\u0099\u0257\3\2\2\2\u009b\u025a\3\2\2\2")
        buf.write("\u009d\u025e\3\2\2\2\u009f\u0262\3\2\2\2\u00a1\u0265\3")
        buf.write("\2\2\2\u00a3\u0267\3\2\2\2\u00a5\u026a\3\2\2\2\u00a7\u026c")
        buf.write("\3\2\2\2\u00a9\u026f\3\2\2\2\u00ab\u0272\3\2\2\2\u00ad")
        buf.write("\u0274\3\2\2\2\u00af\u0276\3\2\2\2\u00b1\u0278\3\2\2\2")
        buf.write("\u00b3\u027a\3\2\2\2\u00b5\u027c\3\2\2\2\u00b7\u027f\3")
        buf.write("\2\2\2\u00b9\u0285\3\2\2\2\u00bb\u028a\3\2\2\2\u00bd\u02a0")
        buf.write("\3\2\2\2\u00bf\u02c0\3\2\2\2\u00c1\u02cb\3\2\2\2\u00c3")
        buf.write("\u02d0\3\2\2\2\u00c5\u02d3\3\2\2\2\u00c7\u02d7\3\2\2\2")
        buf.write("\u00c9\u02df\3\2\2\2\u00cb\u02e5\3\2\2\2\u00cd\u02e9\3")
        buf.write("\2\2\2\u00cf\u02ec\3\2\2\2\u00d1\u0313\3\2\2\2\u00d3\u0317")
        buf.write("\3\2\2\2\u00d5\u031b\3\2\2\2\u00d7\u0324\3\2\2\2\u00d9")
        buf.write("\u032e\3\2\2\2\u00db\u0334\3\2\2\2\u00dd\u00de\7k\2\2")
        buf.write("\u00de\u00df\7o\2\2\u00df\u00e0\7r\2\2\u00e0\u00e1\7q")
        buf.write("\2\2\u00e1\u00e2\7t\2\2\u00e2\u00e3\7v\2\2\u00e3\4\3\2")
        buf.write("\2\2\u00e4\u00e5\7\60\2\2\u00e5\6\3\2\2\2\u00e6\u00e7")
        buf.write("\7n\2\2\u00e7\u00e8\7k\2\2\u00e8\u00e9\7u\2\2\u00e9\u00ea")
        buf.write("\7v\2\2\u00ea\b\3\2\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed")
        buf.write("\7h\2\2\u00ed\n\3\2\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0")
        buf.write("\7p\2\2\u00f0\u00f1\7v\2\2\u00f1\f\3\2\2\2\u00f2\u00f3")
        buf.write("\7w\2\2\u00f3\u00f4\7k\2\2\u00f4\u00f5\7p\2\2\u00f5\u00f6")
        buf.write("\7v\2\2\u00f6\16\3\2\2\2\u00f7\u00f8\7h\2\2\u00f8\u00f9")
        buf.write("\7n\2\2\u00f9\u00fa\7q\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc")
        buf.write("\7v\2\2\u00fc\20\3\2\2\2\u00fd\u00fe\7d\2\2\u00fe\u00ff")
        buf.write("\7q\2\2\u00ff\u0100\7q\2\2\u0100\u0101\7n\2\2\u0101\22")
        buf.write("\3\2\2\2\u0102\u0103\7u\2\2\u0103\u0104\7v\2\2\u0104\u0105")
        buf.write("\7t\2\2\u0105\u0106\7k\2\2\u0106\u0107\7p\2\2\u0107\u0108")
        buf.write("\7i\2\2\u0108\24\3\2\2\2\u0109\u010a\7v\2\2\u010a\u010b")
        buf.write("\7{\2\2\u010b\u010c\7r\2\2\u010c\u010d\7g\2\2\u010d\26")
        buf.write("\3\2\2\2\u010e\u010f\7k\2\2\u010f\u0110\7u\2\2\u0110\30")
        buf.write("\3\2\2\2\u0111\u0112\7w\2\2\u0112\u0113\7p\2\2\u0113\u0114")
        buf.write("\7k\2\2\u0114\u0115\7v\2\2\u0115\32\3\2\2\2\u0116\u0117")
        buf.write("\7U\2\2\u0117\u0118\7K\2\2\u0118\34\3\2\2\2\u0119\u011a")
        buf.write("\7*\2\2\u011a\36\3\2\2\2\u011b\u011c\7+\2\2\u011c \3\2")
        buf.write("\2\2\u011d\u011e\7.\2\2\u011e\"\3\2\2\2\u011f\u0120\7")
        buf.write("<\2\2\u0120$\3\2\2\2\u0121\u0122\7h\2\2\u0122\u0123\7")
        buf.write("c\2\2\u0123\u0124\7e\2\2\u0124\u0125\7v\2\2\u0125\u0126")
        buf.write("\7q\2\2\u0126\u0127\7t\2\2\u0127&\3\2\2\2\u0128\u0129")
        buf.write("\7q\2\2\u0129\u012a\7h\2\2\u012a\u012b\7h\2\2\u012b\u012c")
        buf.write("\7u\2\2\u012c\u012d\7g\2\2\u012d\u012e\7v\2\2\u012e(\3")
        buf.write("\2\2\2\u012f\u0130\7m\2\2\u0130\u0131\7i\2\2\u0131*\3")
        buf.write("\2\2\2\u0132\u0133\7o\2\2\u0133,\3\2\2\2\u0134\u0135\7")
        buf.write("u\2\2\u0135.\3\2\2\2\u0136\u0137\7C\2\2\u0137\60\3\2\2")
        buf.write("\2\u0138\u0139\7M\2\2\u0139\62\3\2\2\2\u013a\u013b\7o")
        buf.write("\2\2\u013b\u013c\7q\2\2\u013c\u013d\7n\2\2\u013d\64\3")
        buf.write("\2\2\2\u013e\u013f\7e\2\2\u013f\u0140\7f\2\2\u0140\66")
        buf.write("\3\2\2\2\u0141\u0142\7t\2\2\u0142\u0143\7c\2\2\u0143\u0144")
        buf.write("\7f\2\2\u01448\3\2\2\2\u0145\u0146\7g\2\2\u0146\u0147")
        buf.write("\7p\2\2\u0147\u0148\7w\2\2\u0148\u0149\7o\2\2\u0149:\3")
        buf.write("\2\2\2\u014a\u014b\7]\2\2\u014b<\3\2\2\2\u014c\u014d\7")
        buf.write("_\2\2\u014d>\3\2\2\2\u014e\u014f\7?\2\2\u014f@\3\2\2\2")
        buf.write("\u0150\u0151\7#\2\2\u0151B\3\2\2\2\u0152\u0153\7u\2\2")
        buf.write("\u0153\u0154\7v\2\2\u0154\u0155\7t\2\2\u0155\u0156\7w")
        buf.write("\2\2\u0156\u0157\7e\2\2\u0157\u0158\7v\2\2\u0158D\3\2")
        buf.write("\2\2\u0159\u015a\7k\2\2\u015a\u015b\7p\2\2\u015b\u015c")
        buf.write("\7j\2\2\u015c\u015d\7g\2\2\u015d\u015e\7t\2\2\u015e\u015f")
        buf.write("\7k\2\2\u015f\u0160\7v\2\2\u0160\u0161\7u\2\2\u0161F\3")
        buf.write("\2\2\2\u0162\u0163\7?\2\2\u0163\u0164\7?\2\2\u0164H\3")
        buf.write("\2\2\2\u0165\u0166\7c\2\2\u0166\u0167\7e\2\2\u0167\u0168")
        buf.write("\7v\2\2\u0168\u0169\7q\2\2\u0169\u016a\7t\2\2\u016aJ\3")
        buf.write("\2\2\2\u016b\u016c\7u\2\2\u016c\u016d\7e\2\2\u016d\u016e")
        buf.write("\7g\2\2\u016e\u016f\7p\2\2\u016f\u0170\7c\2\2\u0170\u0171")
        buf.write("\7t\2\2\u0171\u0172\7k\2\2\u0172\u0173\7q\2\2\u0173L\3")
        buf.write("\2\2\2\u0174\u0175\7c\2\2\u0175\u0176\7e\2\2\u0176\u0177")
        buf.write("\7v\2\2\u0177\u0178\7k\2\2\u0178\u0179\7q\2\2\u0179\u017a")
        buf.write("\7p\2\2\u017aN\3\2\2\2\u017b\u017c\7o\2\2\u017c\u017d")
        buf.write("\7q\2\2\u017d\u017e\7f\2\2\u017e\u017f\7k\2\2\u017f\u0180")
        buf.write("\7h\2\2\u0180\u0181\7k\2\2\u0181\u0182\7g\2\2\u0182\u0183")
        buf.write("\7t\2\2\u0183P\3\2\2\2\u0184\u0185\7i\2\2\u0185\u0186")
        buf.write("\7n\2\2\u0186\u0187\7q\2\2\u0187\u0188\7d\2\2\u0188\u0189")
        buf.write("\7c\2\2\u0189\u018a\7n\2\2\u018aR\3\2\2\2\u018b\u018c")
        buf.write("\7g\2\2\u018c\u018d\7z\2\2\u018d\u018e\7v\2\2\u018e\u018f")
        buf.write("\7g\2\2\u018f\u0190\7p\2\2\u0190\u0191\7f\2\2\u0191T\3")
        buf.write("\2\2\2\u0192\u0193\7g\2\2\u0193\u0194\7x\2\2\u0194\u0195")
        buf.write("\7g\2\2\u0195\u0196\7p\2\2\u0196\u0197\7v\2\2\u0197V\3")
        buf.write("\2\2\2\u0198\u0199\7k\2\2\u0199\u019a\7h\2\2\u019aX\3")
        buf.write("\2\2\2\u019b\u019c\7B\2\2\u019cZ\3\2\2\2\u019d\u019e\7")
        buf.write("c\2\2\u019e\u019f\7u\2\2\u019f\\\3\2\2\2\u01a0\u01a1\7")
        buf.write("t\2\2\u01a1\u01a2\7k\2\2\u01a2\u01a3\7u\2\2\u01a3\u01a4")
        buf.write("\7g\2\2\u01a4^\3\2\2\2\u01a5\u01a6\7h\2\2\u01a6\u01a7")
        buf.write("\7c\2\2\u01a7\u01a8\7n\2\2\u01a8\u01a9\7n\2\2\u01a9`\3")
        buf.write("\2\2\2\u01aa\u01ab\7g\2\2\u01ab\u01ac\7n\2\2\u01ac\u01ad")
        buf.write("\7c\2\2\u01ad\u01ae\7r\2\2\u01ae\u01af\7u\2\2\u01af\u01b0")
        buf.write("\7g\2\2\u01b0\u01b1\7f\2\2\u01b1b\3\2\2\2\u01b2\u01b3")
        buf.write("\7g\2\2\u01b3\u01b4\7x\2\2\u01b4\u01b5\7g\2\2\u01b5\u01b6")
        buf.write("\7t\2\2\u01b6\u01b7\7{\2\2\u01b7d\3\2\2\2\u01b8\u01b9")
        buf.write("\7x\2\2\u01b9\u01ba\7c\2\2\u01ba\u01bb\7t\2\2\u01bbf\3")
        buf.write("\2\2\2\u01bc\u01bd\7u\2\2\u01bd\u01be\7c\2\2\u01be\u01bf")
        buf.write("\7o\2\2\u01bf\u01c0\7r\2\2\u01c0\u01c1\7n\2\2\u01c1\u01c2")
        buf.write("\7g\2\2\u01c2h\3\2\2\2\u01c3\u01c4\7y\2\2\u01c4\u01c5")
        buf.write("\7k\2\2\u01c5\u01c6\7v\2\2\u01c6\u01c7\7j\2\2\u01c7j\3")
        buf.write("\2\2\2\u01c8\u01c9\7m\2\2\u01c9\u01ca\7g\2\2\u01ca\u01cb")
        buf.write("\7g\2\2\u01cb\u01cc\7r\2\2\u01ccl\3\2\2\2\u01cd\u01ce")
        buf.write("\7f\2\2\u01ce\u01cf\7g\2\2\u01cf\u01d0\7h\2\2\u01d0\u01d1")
        buf.write("\7c\2\2\u01d1\u01d2\7w\2\2\u01d2\u01d3\7n\2\2\u01d3\u01d4")
        buf.write("\7v\2\2\u01d4n\3\2\2\2\u01d5\u01d6\7j\2\2\u01d6\u01d7")
        buf.write("\7c\2\2\u01d7\u01d8\7t\2\2\u01d8\u01d9\7f\2\2\u01d9p\3")
        buf.write("\2\2\2\u01da\u01db\7t\2\2\u01db\u01dc\7g\2\2\u01dc\u01dd")
        buf.write("\7o\2\2\u01dd\u01de\7q\2\2\u01de\u01df\7x\2\2\u01df\u01e0")
        buf.write("\7g\2\2\u01e0\u01e1\7a\2\2\u01e1\u01e2\7f\2\2\u01e2\u01e3")
        buf.write("\7g\2\2\u01e3\u01e4\7h\2\2\u01e4\u01e5\7c\2\2\u01e5\u01e6")
        buf.write("\7w\2\2\u01e6\u01e7\7n\2\2\u01e7\u01e8\7v\2\2\u01e8r\3")
        buf.write("\2\2\2\u01e9\u01ea\7f\2\2\u01ea\u01eb\7g\2\2\u01eb\u01ec")
        buf.write("\7h\2\2\u01ect\3\2\2\2\u01ed\u01ee\7/\2\2\u01ee\u01ef")
        buf.write("\7@\2\2\u01efv\3\2\2\2\u01f0\u01f1\7g\2\2\u01f1\u01f2")
        buf.write("\7z\2\2\u01f2\u01f3\7r\2\2\u01f3\u01f4\7t\2\2\u01f4\u01f5")
        buf.write("\7g\2\2\u01f5\u01f6\7u\2\2\u01f6\u01f7\7u\2\2\u01f7\u01f8")
        buf.write("\7k\2\2\u01f8\u01f9\7q\2\2\u01f9\u01fa\7p\2\2\u01fax\3")
        buf.write("\2\2\2\u01fb\u01fc\7w\2\2\u01fc\u01fd\7p\2\2\u01fd\u01fe")
        buf.write("\7f\2\2\u01fe\u01ff\7g\2\2\u01ff\u0200\7h\2\2\u0200\u0201")
        buf.write("\7k\2\2\u0201\u0202\7p\2\2\u0202\u0203\7g\2\2\u0203\u0204")
        buf.write("\7f\2\2\u0204z\3\2\2\2\u0205\u0206\7g\2\2\u0206\u0207")
        buf.write("\7z\2\2\u0207\u0208\7v\2\2\u0208\u0209\7g\2\2\u0209\u020a")
        buf.write("\7t\2\2\u020a\u020b\7p\2\2\u020b\u020c\7c\2\2\u020c\u020d")
        buf.write("\7n\2\2\u020d|\3\2\2\2\u020e\u020f\7q\2\2\u020f\u0210")
        buf.write("\7p\2\2\u0210\u0211\7n\2\2\u0211\u0212\7{\2\2\u0212~\3")
        buf.write("\2\2\2\u0213\u0214\7e\2\2\u0214\u0215\7q\2\2\u0215\u0216")
        buf.write("\7x\2\2\u0216\u0217\7g\2\2\u0217\u0218\7t\2\2\u0218\u0080")
        buf.write("\3\2\2\2\u0219\u021a\7t\2\2\u021a\u021b\7g\2\2\u021b\u021c")
        buf.write("\7e\2\2\u021c\u021d\7q\2\2\u021d\u021e\7t\2\2\u021e\u021f")
        buf.write("\7f\2\2\u021f\u0082\3\2\2\2\u0220\u0221\7q\2\2\u0221\u0222")
        buf.write("\7p\2\2\u0222\u0084\3\2\2\2\u0223\u0224\7f\2\2\u0224\u0225")
        buf.write("\7q\2\2\u0225\u0086\3\2\2\2\u0226\u0227\7u\2\2\u0227\u0228")
        buf.write("\7g\2\2\u0228\u0229\7t\2\2\u0229\u022a\7k\2\2\u022a\u022b")
        buf.write("\7c\2\2\u022b\u022c\7n\2\2\u022c\u0088\3\2\2\2\u022d\u022e")
        buf.write("\7q\2\2\u022e\u022f\7p\2\2\u022f\u0230\7g\2\2\u0230\u0231")
        buf.write("\7a\2\2\u0231\u0232\7q\2\2\u0232\u0233\7h\2\2\u0233\u008a")
        buf.write("\3\2\2\2\u0234\u0235\7r\2\2\u0235\u0236\7c\2\2\u0236\u0237")
        buf.write("\7t\2\2\u0237\u0238\7c\2\2\u0238\u0239\7n\2\2\u0239\u023a")
        buf.write("\7n\2\2\u023a\u023b\7g\2\2\u023b\u023c\7n\2\2\u023c\u008c")
        buf.write("\3\2\2\2\u023d\u023e\7y\2\2\u023e\u023f\7c\2\2\u023f\u0240")
        buf.write("\7k\2\2\u0240\u0241\7v\2\2\u0241\u008e\3\2\2\2\u0242\u0243")
        buf.write("\7g\2\2\u0243\u0244\7o\2\2\u0244\u0245\7k\2\2\u0245\u0246")
        buf.write("\7v\2\2\u0246\u0090\3\2\2\2\u0247\u0248\7e\2\2\u0248\u0249")
        buf.write("\7c\2\2\u0249\u024a\7n\2\2\u024a\u024b\7n\2\2\u024b\u0092")
        buf.write("\3\2\2\2\u024c\u024d\7w\2\2\u024d\u024e\7p\2\2\u024e\u024f")
        buf.write("\7v\2\2\u024f\u0250\7k\2\2\u0250\u0251\7n\2\2\u0251\u0094")
        buf.write("\3\2\2\2\u0252\u0253\7A\2\2\u0253\u0096\3\2\2\2\u0254")
        buf.write("\u0255\7?\2\2\u0255\u0256\7@\2\2\u0256\u0098\3\2\2\2\u0257")
        buf.write("\u0258\7q\2\2\u0258\u0259\7t\2\2\u0259\u009a\3\2\2\2\u025a")
        buf.write("\u025b\7c\2\2\u025b\u025c\7p\2\2\u025c\u025d\7f\2\2\u025d")
        buf.write("\u009c\3\2\2\2\u025e\u025f\7p\2\2\u025f\u0260\7q\2\2\u0260")
        buf.write("\u0261\7v\2\2\u0261\u009e\3\2\2\2\u0262\u0263\7#\2\2\u0263")
        buf.write("\u0264\7?\2\2\u0264\u00a0\3\2\2\2\u0265\u0266\7>\2\2\u0266")
        buf.write("\u00a2\3\2\2\2\u0267\u0268\7>\2\2\u0268\u0269\7?\2\2\u0269")
        buf.write("\u00a4\3\2\2\2\u026a\u026b\7@\2\2\u026b\u00a6\3\2\2\2")
        buf.write("\u026c\u026d\7@\2\2\u026d\u026e\7?\2\2\u026e\u00a8\3\2")
        buf.write("\2\2\u026f\u0270\7k\2\2\u0270\u0271\7p\2\2\u0271\u00aa")
        buf.write("\3\2\2\2\u0272\u0273\7-\2\2\u0273\u00ac\3\2\2\2\u0274")
        buf.write("\u0275\7/\2\2\u0275\u00ae\3\2\2\2\u0276\u0277\7,\2\2\u0277")
        buf.write("\u00b0\3\2\2\2\u0278\u0279\7\61\2\2\u0279\u00b2\3\2\2")
        buf.write("\2\u027a\u027b\7\'\2\2\u027b\u00b4\3\2\2\2\u027c\u027d")
        buf.write("\7k\2\2\u027d\u027e\7v\2\2\u027e\u00b6\3\2\2\2\u027f\u0280")
        buf.write("\7t\2\2\u0280\u0281\7c\2\2\u0281\u0282\7p\2\2\u0282\u0283")
        buf.write("\7i\2\2\u0283\u0284\7g\2\2\u0284\u00b8\3\2\2\2\u0285\u0286")
        buf.write("\7\60\2\2\u0286\u0287\7\60\2\2\u0287\u00ba\3\2\2\2\u0288")
        buf.write("\u028b\5\u00bd_\2\u0289\u028b\5\u00bf`\2\u028a\u0288\3")
        buf.write("\2\2\2\u028a\u0289\3\2\2\2\u028b\u00bc\3\2\2\2\u028c\u0292")
        buf.write("\7$\2\2\u028d\u0291\n\2\2\2\u028e\u028f\7^\2\2\u028f\u0291")
        buf.write("\n\3\2\2\u0290\u028d\3\2\2\2\u0290\u028e\3\2\2\2\u0291")
        buf.write("\u0294\3\2\2\2\u0292\u0290\3\2\2\2\u0292\u0293\3\2\2\2")
        buf.write("\u0293\u0295\3\2\2\2\u0294\u0292\3\2\2\2\u0295\u02a1\7")
        buf.write("$\2\2\u0296\u029c\7)\2\2\u0297\u029b\n\2\2\2\u0298\u0299")
        buf.write("\7^\2\2\u0299\u029b\n\3\2\2\u029a\u0297\3\2\2\2\u029a")
        buf.write("\u0298\3\2\2\2\u029b\u029e\3\2\2\2\u029c\u029a\3\2\2\2")
        buf.write("\u029c\u029d\3\2\2\2\u029d\u029f\3\2\2\2\u029e\u029c\3")
        buf.write("\2\2\2\u029f\u02a1\7)\2\2\u02a0\u028c\3\2\2\2\u02a0\u0296")
        buf.write("\3\2\2\2\u02a1\u00be\3\2\2\2\u02a2\u02a3\7$\2\2\u02a3")
        buf.write("\u02a4\7$\2\2\u02a4\u02a5\7$\2\2\u02a5\u02ab\3\2\2\2\u02a6")
        buf.write("\u02aa\n\4\2\2\u02a7\u02a8\7^\2\2\u02a8\u02aa\n\3\2\2")
        buf.write("\u02a9\u02a6\3\2\2\2\u02a9\u02a7\3\2\2\2\u02aa\u02ad\3")
        buf.write("\2\2\2\u02ab\u02a9\3\2\2\2\u02ab\u02ac\3\2\2\2\u02ac\u02ae")
        buf.write("\3\2\2\2\u02ad\u02ab\3\2\2\2\u02ae\u02af\7$\2\2\u02af")
        buf.write("\u02b0\7$\2\2\u02b0\u02c1\7$\2\2\u02b1\u02b2\7)\2\2\u02b2")
        buf.write("\u02b3\7)\2\2\u02b3\u02b4\7)\2\2\u02b4\u02ba\3\2\2\2\u02b5")
        buf.write("\u02b9\n\4\2\2\u02b6\u02b7\7^\2\2\u02b7\u02b9\n\3\2\2")
        buf.write("\u02b8\u02b5\3\2\2\2\u02b8\u02b6\3\2\2\2\u02b9\u02bc\3")
        buf.write("\2\2\2\u02ba\u02b8\3\2\2\2\u02ba\u02bb\3\2\2\2\u02bb\u02bd")
        buf.write("\3\2\2\2\u02bc\u02ba\3\2\2\2\u02bd\u02be\7)\2\2\u02be")
        buf.write("\u02bf\7)\2\2\u02bf\u02c1\7)\2\2\u02c0\u02a2\3\2\2\2\u02c0")
        buf.write("\u02b1\3\2\2\2\u02c1\u00c0\3\2\2\2\u02c2\u02c3\7v\2\2")
        buf.write("\u02c3\u02c4\7t\2\2\u02c4\u02c5\7w\2\2\u02c5\u02cc\7g")
        buf.write("\2\2\u02c6\u02c7\7h\2\2\u02c7\u02c8\7c\2\2\u02c8\u02c9")
        buf.write("\7n\2\2\u02c9\u02ca\7u\2\2\u02ca\u02cc\7g\2\2\u02cb\u02c2")
        buf.write("\3\2\2\2\u02cb\u02c6\3\2\2\2\u02cc\u00c2\3\2\2\2\u02cd")
        buf.write("\u02d1\5\u00c5c\2\u02ce\u02d1\5\u00c7d\2\u02cf\u02d1\5")
        buf.write("\u00c9e\2\u02d0\u02cd\3\2\2\2\u02d0\u02ce\3\2\2\2\u02d0")
        buf.write("\u02cf\3\2\2\2\u02d1\u00c4\3\2\2\2\u02d2\u02d4\5\u00cb")
        buf.write("f\2\u02d3\u02d2\3\2\2\2\u02d4\u02d5\3\2\2\2\u02d5\u02d3")
        buf.write("\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6\u00c6\3\2\2\2\u02d7")
        buf.write("\u02d8\7\62\2\2\u02d8\u02d9\7z\2\2\u02d9\u02db\3\2\2\2")
        buf.write("\u02da\u02dc\5\u00cdg\2\u02db\u02da\3\2\2\2\u02dc\u02dd")
        buf.write("\3\2\2\2\u02dd\u02db\3\2\2\2\u02dd\u02de\3\2\2\2\u02de")
        buf.write("\u00c8\3\2\2\2\u02df\u02e1\7/\2\2\u02e0\u02e2\5\u00cb")
        buf.write("f\2\u02e1\u02e0\3\2\2\2\u02e2\u02e3\3\2\2\2\u02e3\u02e1")
        buf.write("\3\2\2\2\u02e3\u02e4\3\2\2\2\u02e4\u00ca\3\2\2\2\u02e5")
        buf.write("\u02e6\4\62;\2\u02e6\u00cc\3\2\2\2\u02e7\u02ea\5\u00cb")
        buf.write("f\2\u02e8\u02ea\t\5\2\2\u02e9\u02e7\3\2\2\2\u02e9\u02e8")
        buf.write("\3\2\2\2\u02ea\u00ce\3\2\2\2\u02eb\u02ed\t\6\2\2\u02ec")
        buf.write("\u02eb\3\2\2\2\u02ec\u02ed\3\2\2\2\u02ed\u02f1\3\2\2\2")
        buf.write("\u02ee\u02f0\5\u00cbf\2\u02ef\u02ee\3\2\2\2\u02f0\u02f3")
        buf.write("\3\2\2\2\u02f1\u02ef\3\2\2\2\u02f1\u02f2\3\2\2\2\u02f2")
        buf.write("\u02f4\3\2\2\2\u02f3\u02f1\3\2\2\2\u02f4\u02f6\7\60\2")
        buf.write("\2\u02f5\u02f7\5\u00cbf\2\u02f6\u02f5\3\2\2\2\u02f7\u02f8")
        buf.write("\3\2\2\2\u02f8\u02f6\3\2\2\2\u02f8\u02f9\3\2\2\2\u02f9")
        buf.write("\u0303\3\2\2\2\u02fa\u02fc\t\7\2\2\u02fb\u02fd\t\6\2\2")
        buf.write("\u02fc\u02fb\3\2\2\2\u02fc\u02fd\3\2\2\2\u02fd\u02ff\3")
        buf.write("\2\2\2\u02fe\u0300\5\u00cbf\2\u02ff\u02fe\3\2\2\2\u0300")
        buf.write("\u0301\3\2\2\2\u0301\u02ff\3\2\2\2\u0301\u0302\3\2\2\2")
        buf.write("\u0302\u0304\3\2\2\2\u0303\u02fa\3\2\2\2\u0303\u0304\3")
        buf.write("\2\2\2\u0304\u00d0\3\2\2\2\u0305\u0309\t\b\2\2\u0306\u0308")
        buf.write("\t\t\2\2\u0307\u0306\3\2\2\2\u0308\u030b\3\2\2\2\u0309")
        buf.write("\u0307\3\2\2\2\u0309\u030a\3\2\2\2\u030a\u0314\3\2\2\2")
        buf.write("\u030b\u0309\3\2\2\2\u030c\u030e\7~\2\2\u030d\u030f\n")
        buf.write("\n\2\2\u030e\u030d\3\2\2\2\u030f\u0310\3\2\2\2\u0310\u030e")
        buf.write("\3\2\2\2\u0310\u0311\3\2\2\2\u0311\u0312\3\2\2\2\u0312")
        buf.write("\u0314\7~\2\2\u0313\u0305\3\2\2\2\u0313\u030c\3\2\2\2")
        buf.write("\u0314\u00d2\3\2\2\2\u0315\u0318\5\u00cfh\2\u0316\u0318")
        buf.write("\5\u00c3b\2\u0317\u0315\3\2\2\2\u0317\u0316\3\2\2\2\u0318")
        buf.write("\u0319\3\2\2\2\u0319\u031a\5\u00d1i\2\u031a\u00d4\3\2")
        buf.write("\2\2\u031b\u031d\7^\2\2\u031c\u031e\7\17\2\2\u031d\u031c")
        buf.write("\3\2\2\2\u031d\u031e\3\2\2\2\u031e\u031f\3\2\2\2\u031f")
        buf.write("\u0320\7\f\2\2\u0320\u0321\3\2\2\2\u0321\u0322\bk\2\2")
        buf.write("\u0322\u00d6\3\2\2\2\u0323\u0325\7\17\2\2\u0324\u0323")
        buf.write("\3\2\2\2\u0324\u0325\3\2\2\2\u0325\u0326\3\2\2\2\u0326")
        buf.write("\u032a\7\f\2\2\u0327\u0329\7\"\2\2\u0328\u0327\3\2\2\2")
        buf.write("\u0329\u032c\3\2\2\2\u032a\u0328\3\2\2\2\u032a\u032b\3")
        buf.write("\2\2\2\u032b\u00d8\3\2\2\2\u032c\u032a\3\2\2\2\u032d\u032f")
        buf.write("\t\13\2\2\u032e\u032d\3\2\2\2\u032f\u0330\3\2\2\2\u0330")
        buf.write("\u032e\3\2\2\2\u0330\u0331\3\2\2\2\u0331\u0332\3\2\2\2")
        buf.write("\u0332\u0333\bm\2\2\u0333\u00da\3\2\2\2\u0334\u0338\7")
        buf.write("%\2\2\u0335\u0337\n\3\2\2\u0336\u0335\3\2\2\2\u0337\u033a")
        buf.write("\3\2\2\2\u0338\u0336\3\2\2\2\u0338\u0339\3\2\2\2\u0339")
        buf.write("\u033b\3\2\2\2\u033a\u0338\3\2\2\2\u033b\u033c\bn\2\2")
        buf.write("\u033c\u00dc\3\2\2\2#\2\u028a\u0290\u0292\u029a\u029c")
        buf.write("\u02a0\u02a9\u02ab\u02b8\u02ba\u02c0\u02cb\u02d0\u02d5")
        buf.write("\u02dd\u02e3\u02e9\u02ec\u02f1\u02f8\u02fc\u0301\u0303")
        buf.write("\u0309\u0310\u0313\u0317\u031d\u0324\u032a\u0330\u0338")
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
    T__90 = 91
    T__91 = 92
    STRING_LITERAL = 93
    SHORTSTRING = 94
    LONGSTRING = 95
    BOOL_LITERAL = 96
    INTEGER_LITERAL = 97
    UINT_LITERAL = 98
    HEX_UINT_LITERAL = 99
    INT_LITERAL = 100
    FLOAT_LITERAL = 101
    IDENTIFIER = 102
    PHYSICAL_LITERAL = 103
    LINEJOINER = 104
    NEWLINE = 105
    WS = 106
    COMMENT = 107

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'import'", "'.'", "'list'", "'of'", "'int'", "'uint'", "'float'", 
            "'bool'", "'string'", "'type'", "'is'", "'unit'", "'SI'", "'('", 
            "')'", "','", "':'", "'factor'", "'offset'", "'kg'", "'m'", 
            "'s'", "'A'", "'K'", "'mol'", "'cd'", "'rad'", "'enum'", "'['", 
            "']'", "'='", "'!'", "'struct'", "'inherits'", "'=='", "'actor'", 
            "'scenario'", "'action'", "'modifier'", "'global'", "'extend'", 
            "'event'", "'if'", "'@'", "'as'", "'rise'", "'fall'", "'elapsed'", 
            "'every'", "'var'", "'sample'", "'with'", "'keep'", "'default'", 
            "'hard'", "'remove_default'", "'def'", "'->'", "'expression'", 
            "'undefined'", "'external'", "'only'", "'cover'", "'record'", 
            "'on'", "'do'", "'serial'", "'one_of'", "'parallel'", "'wait'", 
            "'emit'", "'call'", "'until'", "'?'", "'=>'", "'or'", "'and'", 
            "'not'", "'!='", "'<'", "'<='", "'>'", "'>='", "'in'", "'+'", 
            "'-'", "'*'", "'/'", "'%'", "'it'", "'range'", "'..'" ]

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
                  "T__86", "T__87", "T__88", "T__89", "T__90", "T__91", 
                  "STRING_LITERAL", "SHORTSTRING", "LONGSTRING", "BOOL_LITERAL", 
                  "INTEGER_LITERAL", "UINT_LITERAL", "HEX_UINT_LITERAL", 
                  "INT_LITERAL", "DIGIT", "HEX_DIGIT", "FLOAT_LITERAL", 
                  "IDENTIFIER", "PHYSICAL_LITERAL", "LINEJOINER", "NEWLINE", 
                  "WS", "COMMENT" ]

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



