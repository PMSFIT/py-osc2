# Generated from openscenario2.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from antlr_denter.DenterHelper import DenterHelper
from .openscenario2Parser import openscenario2Parser


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2l")
        buf.write("\u0335\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("g\tg\4h\th\4i\ti\4j\tj\4k\tk\4l\tl\4m\tm\3\2\3\2\3\2\3")
        buf.write("\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\16\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3\21\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\37\3\37\3 \3 \3!\3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3$\3$\3$\3$\3$\3$\3%\3%")
        buf.write("\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3")
        buf.write(")\3)\3)\3)\3*\3*\3*\3+\3+\3,\3,\3,\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3/\3/\3/\3/\3/\3/\3/\3/\3\60\3\60\3\60\3\60")
        buf.write("\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\3\62\3\62\3\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3\64")
        buf.write("\3\64\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\38\38\38\38\39\39")
        buf.write("\39\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3:\3;\3;\3;\3;\3;\3")
        buf.write(";\3;\3;\3;\3;\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\3=\3=\3")
        buf.write("=\3>\3>\3>\3>\3>\3>\3?\3?\3?\3?\3?\3?\3?\3@\3@\3@\3A\3")
        buf.write("A\3A\3B\3B\3B\3B\3B\3B\3B\3C\3C\3C\3C\3C\3C\3C\3D\3D\3")
        buf.write("D\3D\3D\3D\3D\3D\3D\3E\3E\3E\3E\3E\3F\3F\3F\3F\3F\3G\3")
        buf.write("G\3G\3G\3G\3H\3H\3H\3H\3H\3H\3I\3I\3J\3J\3J\3K\3K\3K\3")
        buf.write("L\3L\3L\3L\3M\3M\3M\3M\3N\3N\3N\3O\3O\3P\3P\3P\3Q\3Q\3")
        buf.write("R\3R\3R\3S\3S\3S\3T\3T\3U\3U\3V\3V\3W\3W\3X\3X\3Y\3Y\3")
        buf.write("Y\3Z\3Z\3Z\3[\3[\3[\3[\3[\3[\3\\\3\\\3\\\3]\3]\5]\u0283")
        buf.write("\n]\3^\3^\3^\3^\7^\u0289\n^\f^\16^\u028c\13^\3^\3^\3^")
        buf.write("\3^\3^\7^\u0293\n^\f^\16^\u0296\13^\3^\5^\u0299\n^\3_")
        buf.write("\3_\3_\3_\3_\3_\3_\7_\u02a2\n_\f_\16_\u02a5\13_\3_\3_")
        buf.write("\3_\3_\3_\3_\3_\3_\3_\3_\7_\u02b1\n_\f_\16_\u02b4\13_")
        buf.write("\3_\3_\3_\5_\u02b9\n_\3`\3`\3`\3`\3`\3`\3`\3`\3`\5`\u02c4")
        buf.write("\n`\3a\3a\3a\5a\u02c9\na\3b\6b\u02cc\nb\rb\16b\u02cd\3")
        buf.write("c\3c\3c\3c\6c\u02d4\nc\rc\16c\u02d5\3d\3d\6d\u02da\nd")
        buf.write("\rd\16d\u02db\3e\3e\3f\3f\5f\u02e2\nf\3g\5g\u02e5\ng\3")
        buf.write("g\7g\u02e8\ng\fg\16g\u02eb\13g\3g\3g\6g\u02ef\ng\rg\16")
        buf.write("g\u02f0\3g\3g\5g\u02f5\ng\3g\6g\u02f8\ng\rg\16g\u02f9")
        buf.write("\5g\u02fc\ng\3h\3h\7h\u0300\nh\fh\16h\u0303\13h\3h\3h")
        buf.write("\6h\u0307\nh\rh\16h\u0308\3h\5h\u030c\nh\3i\3i\5i\u0310")
        buf.write("\ni\3i\3i\3j\3j\5j\u0316\nj\3j\3j\3j\3j\3k\5k\u031d\n")
        buf.write("k\3k\3k\7k\u0321\nk\fk\16k\u0324\13k\3l\6l\u0327\nl\r")
        buf.write("l\16l\u0328\3l\3l\3m\3m\7m\u032f\nm\fm\16m\u0332\13m\3")
        buf.write("m\3m\2\2n\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25")
        buf.write("\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+")
        buf.write("\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E")
        buf.write("$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k")
        buf.write("\67m8o9q:s;u<w=y>{?}@\177A\u0081B\u0083C\u0085D\u0087")
        buf.write("E\u0089F\u008bG\u008dH\u008fI\u0091J\u0093K\u0095L\u0097")
        buf.write("M\u0099N\u009bO\u009dP\u009fQ\u00a1R\u00a3S\u00a5T\u00a7")
        buf.write("U\u00a9V\u00abW\u00adX\u00afY\u00b1Z\u00b3[\u00b5\\\u00b7")
        buf.write("]\u00b9^\u00bb_\u00bd`\u00bfa\u00c1b\u00c3c\u00c5d\u00c7")
        buf.write("e\u00c9\2\u00cb\2\u00cdf\u00cfg\u00d1h\u00d3i\u00d5j\u00d7")
        buf.write("k\u00d9l\3\2\f\7\2\f\f\17\17$$))^^\4\2\f\f\17\17\5\2$")
        buf.write("$))^^\4\2CHch\4\2--//\4\2GGgg\4\2C\\c|\6\2\62;C\\aac|")
        buf.write("\3\2~~\4\2\13\13\"\"\2\u0353\2\3\3\2\2\2\2\5\3\2\2\2\2")
        buf.write("\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write("\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2")
        buf.write("\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2")
        buf.write("\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2")
        buf.write("\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63")
        buf.write("\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2")
        buf.write("\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2")
        buf.write("\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3")
        buf.write("\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y")
        buf.write("\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2")
        buf.write("c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2")
        buf.write("\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2")
        buf.write("\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3")
        buf.write("\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2")
        buf.write("\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2")
        buf.write("\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9")
        buf.write("\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\2\u00af\3\2\2")
        buf.write("\2\2\u00b1\3\2\2\2\2\u00b3\3\2\2\2\2\u00b5\3\2\2\2\2\u00b7")
        buf.write("\3\2\2\2\2\u00b9\3\2\2\2\2\u00bb\3\2\2\2\2\u00bd\3\2\2")
        buf.write("\2\2\u00bf\3\2\2\2\2\u00c1\3\2\2\2\2\u00c3\3\2\2\2\2\u00c5")
        buf.write("\3\2\2\2\2\u00c7\3\2\2\2\2\u00cd\3\2\2\2\2\u00cf\3\2\2")
        buf.write("\2\2\u00d1\3\2\2\2\2\u00d3\3\2\2\2\2\u00d5\3\2\2\2\2\u00d7")
        buf.write("\3\2\2\2\2\u00d9\3\2\2\2\3\u00db\3\2\2\2\5\u00e2\3\2\2")
        buf.write("\2\7\u00e4\3\2\2\2\t\u00e9\3\2\2\2\13\u00ec\3\2\2\2\r")
        buf.write("\u00f0\3\2\2\2\17\u00f5\3\2\2\2\21\u00fb\3\2\2\2\23\u0100")
        buf.write("\3\2\2\2\25\u0107\3\2\2\2\27\u010c\3\2\2\2\31\u010f\3")
        buf.write("\2\2\2\33\u0114\3\2\2\2\35\u0117\3\2\2\2\37\u0119\3\2")
        buf.write("\2\2!\u011b\3\2\2\2#\u011d\3\2\2\2%\u011f\3\2\2\2\'\u0126")
        buf.write("\3\2\2\2)\u012d\3\2\2\2+\u0130\3\2\2\2-\u0132\3\2\2\2")
        buf.write("/\u0134\3\2\2\2\61\u0136\3\2\2\2\63\u0138\3\2\2\2\65\u013c")
        buf.write("\3\2\2\2\67\u013f\3\2\2\29\u0143\3\2\2\2;\u0148\3\2\2")
        buf.write("\2=\u014a\3\2\2\2?\u014c\3\2\2\2A\u014e\3\2\2\2C\u0155")
        buf.write("\3\2\2\2E\u015e\3\2\2\2G\u0161\3\2\2\2I\u0167\3\2\2\2")
        buf.write("K\u0170\3\2\2\2M\u0177\3\2\2\2O\u0180\3\2\2\2Q\u0187\3")
        buf.write("\2\2\2S\u018d\3\2\2\2U\u0190\3\2\2\2W\u0192\3\2\2\2Y\u0195")
        buf.write("\3\2\2\2[\u019a\3\2\2\2]\u019f\3\2\2\2_\u01a7\3\2\2\2")
        buf.write("a\u01ad\3\2\2\2c\u01b1\3\2\2\2e\u01b8\3\2\2\2g\u01bd\3")
        buf.write("\2\2\2i\u01c2\3\2\2\2k\u01ca\3\2\2\2m\u01cf\3\2\2\2o\u01de")
        buf.write("\3\2\2\2q\u01e2\3\2\2\2s\u01e5\3\2\2\2u\u01f0\3\2\2\2")
        buf.write("w\u01fa\3\2\2\2y\u0203\3\2\2\2{\u0208\3\2\2\2}\u020e\3")
        buf.write("\2\2\2\177\u0215\3\2\2\2\u0081\u0218\3\2\2\2\u0083\u021b")
        buf.write("\3\2\2\2\u0085\u0222\3\2\2\2\u0087\u0229\3\2\2\2\u0089")
        buf.write("\u0232\3\2\2\2\u008b\u0237\3\2\2\2\u008d\u023c\3\2\2\2")
        buf.write("\u008f\u0241\3\2\2\2\u0091\u0247\3\2\2\2\u0093\u0249\3")
        buf.write("\2\2\2\u0095\u024c\3\2\2\2\u0097\u024f\3\2\2\2\u0099\u0253")
        buf.write("\3\2\2\2\u009b\u0257\3\2\2\2\u009d\u025a\3\2\2\2\u009f")
        buf.write("\u025c\3\2\2\2\u00a1\u025f\3\2\2\2\u00a3\u0261\3\2\2\2")
        buf.write("\u00a5\u0264\3\2\2\2\u00a7\u0267\3\2\2\2\u00a9\u0269\3")
        buf.write("\2\2\2\u00ab\u026b\3\2\2\2\u00ad\u026d\3\2\2\2\u00af\u026f")
        buf.write("\3\2\2\2\u00b1\u0271\3\2\2\2\u00b3\u0274\3\2\2\2\u00b5")
        buf.write("\u0277\3\2\2\2\u00b7\u027d\3\2\2\2\u00b9\u0282\3\2\2\2")
        buf.write("\u00bb\u0298\3\2\2\2\u00bd\u02b8\3\2\2\2\u00bf\u02c3\3")
        buf.write("\2\2\2\u00c1\u02c8\3\2\2\2\u00c3\u02cb\3\2\2\2\u00c5\u02cf")
        buf.write("\3\2\2\2\u00c7\u02d7\3\2\2\2\u00c9\u02dd\3\2\2\2\u00cb")
        buf.write("\u02e1\3\2\2\2\u00cd\u02e4\3\2\2\2\u00cf\u030b\3\2\2\2")
        buf.write("\u00d1\u030f\3\2\2\2\u00d3\u0313\3\2\2\2\u00d5\u031c\3")
        buf.write("\2\2\2\u00d7\u0326\3\2\2\2\u00d9\u032c\3\2\2\2\u00db\u00dc")
        buf.write("\7k\2\2\u00dc\u00dd\7o\2\2\u00dd\u00de\7r\2\2\u00de\u00df")
        buf.write("\7q\2\2\u00df\u00e0\7t\2\2\u00e0\u00e1\7v\2\2\u00e1\4")
        buf.write("\3\2\2\2\u00e2\u00e3\7\60\2\2\u00e3\6\3\2\2\2\u00e4\u00e5")
        buf.write("\7n\2\2\u00e5\u00e6\7k\2\2\u00e6\u00e7\7u\2\2\u00e7\u00e8")
        buf.write("\7v\2\2\u00e8\b\3\2\2\2\u00e9\u00ea\7q\2\2\u00ea\u00eb")
        buf.write("\7h\2\2\u00eb\n\3\2\2\2\u00ec\u00ed\7k\2\2\u00ed\u00ee")
        buf.write("\7p\2\2\u00ee\u00ef\7v\2\2\u00ef\f\3\2\2\2\u00f0\u00f1")
        buf.write("\7w\2\2\u00f1\u00f2\7k\2\2\u00f2\u00f3\7p\2\2\u00f3\u00f4")
        buf.write("\7v\2\2\u00f4\16\3\2\2\2\u00f5\u00f6\7h\2\2\u00f6\u00f7")
        buf.write("\7n\2\2\u00f7\u00f8\7q\2\2\u00f8\u00f9\7c\2\2\u00f9\u00fa")
        buf.write("\7v\2\2\u00fa\20\3\2\2\2\u00fb\u00fc\7d\2\2\u00fc\u00fd")
        buf.write("\7q\2\2\u00fd\u00fe\7q\2\2\u00fe\u00ff\7n\2\2\u00ff\22")
        buf.write("\3\2\2\2\u0100\u0101\7u\2\2\u0101\u0102\7v\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7k\2\2\u0104\u0105\7p\2\2\u0105\u0106")
        buf.write("\7i\2\2\u0106\24\3\2\2\2\u0107\u0108\7v\2\2\u0108\u0109")
        buf.write("\7{\2\2\u0109\u010a\7r\2\2\u010a\u010b\7g\2\2\u010b\26")
        buf.write("\3\2\2\2\u010c\u010d\7k\2\2\u010d\u010e\7u\2\2\u010e\30")
        buf.write("\3\2\2\2\u010f\u0110\7w\2\2\u0110\u0111\7p\2\2\u0111\u0112")
        buf.write("\7k\2\2\u0112\u0113\7v\2\2\u0113\32\3\2\2\2\u0114\u0115")
        buf.write("\7U\2\2\u0115\u0116\7K\2\2\u0116\34\3\2\2\2\u0117\u0118")
        buf.write("\7*\2\2\u0118\36\3\2\2\2\u0119\u011a\7+\2\2\u011a \3\2")
        buf.write("\2\2\u011b\u011c\7.\2\2\u011c\"\3\2\2\2\u011d\u011e\7")
        buf.write("<\2\2\u011e$\3\2\2\2\u011f\u0120\7h\2\2\u0120\u0121\7")
        buf.write("c\2\2\u0121\u0122\7e\2\2\u0122\u0123\7v\2\2\u0123\u0124")
        buf.write("\7q\2\2\u0124\u0125\7t\2\2\u0125&\3\2\2\2\u0126\u0127")
        buf.write("\7q\2\2\u0127\u0128\7h\2\2\u0128\u0129\7h\2\2\u0129\u012a")
        buf.write("\7u\2\2\u012a\u012b\7g\2\2\u012b\u012c\7v\2\2\u012c(\3")
        buf.write("\2\2\2\u012d\u012e\7m\2\2\u012e\u012f\7i\2\2\u012f*\3")
        buf.write("\2\2\2\u0130\u0131\7o\2\2\u0131,\3\2\2\2\u0132\u0133\7")
        buf.write("u\2\2\u0133.\3\2\2\2\u0134\u0135\7C\2\2\u0135\60\3\2\2")
        buf.write("\2\u0136\u0137\7M\2\2\u0137\62\3\2\2\2\u0138\u0139\7o")
        buf.write("\2\2\u0139\u013a\7q\2\2\u013a\u013b\7n\2\2\u013b\64\3")
        buf.write("\2\2\2\u013c\u013d\7e\2\2\u013d\u013e\7f\2\2\u013e\66")
        buf.write("\3\2\2\2\u013f\u0140\7t\2\2\u0140\u0141\7c\2\2\u0141\u0142")
        buf.write("\7f\2\2\u01428\3\2\2\2\u0143\u0144\7g\2\2\u0144\u0145")
        buf.write("\7p\2\2\u0145\u0146\7w\2\2\u0146\u0147\7o\2\2\u0147:\3")
        buf.write("\2\2\2\u0148\u0149\7]\2\2\u0149<\3\2\2\2\u014a\u014b\7")
        buf.write("_\2\2\u014b>\3\2\2\2\u014c\u014d\7?\2\2\u014d@\3\2\2\2")
        buf.write("\u014e\u014f\7u\2\2\u014f\u0150\7v\2\2\u0150\u0151\7t")
        buf.write("\2\2\u0151\u0152\7w\2\2\u0152\u0153\7e\2\2\u0153\u0154")
        buf.write("\7v\2\2\u0154B\3\2\2\2\u0155\u0156\7k\2\2\u0156\u0157")
        buf.write("\7p\2\2\u0157\u0158\7j\2\2\u0158\u0159\7g\2\2\u0159\u015a")
        buf.write("\7t\2\2\u015a\u015b\7k\2\2\u015b\u015c\7v\2\2\u015c\u015d")
        buf.write("\7u\2\2\u015dD\3\2\2\2\u015e\u015f\7?\2\2\u015f\u0160")
        buf.write("\7?\2\2\u0160F\3\2\2\2\u0161\u0162\7c\2\2\u0162\u0163")
        buf.write("\7e\2\2\u0163\u0164\7v\2\2\u0164\u0165\7q\2\2\u0165\u0166")
        buf.write("\7t\2\2\u0166H\3\2\2\2\u0167\u0168\7u\2\2\u0168\u0169")
        buf.write("\7e\2\2\u0169\u016a\7g\2\2\u016a\u016b\7p\2\2\u016b\u016c")
        buf.write("\7c\2\2\u016c\u016d\7t\2\2\u016d\u016e\7k\2\2\u016e\u016f")
        buf.write("\7q\2\2\u016fJ\3\2\2\2\u0170\u0171\7c\2\2\u0171\u0172")
        buf.write("\7e\2\2\u0172\u0173\7v\2\2\u0173\u0174\7k\2\2\u0174\u0175")
        buf.write("\7q\2\2\u0175\u0176\7p\2\2\u0176L\3\2\2\2\u0177\u0178")
        buf.write("\7o\2\2\u0178\u0179\7q\2\2\u0179\u017a\7f\2\2\u017a\u017b")
        buf.write("\7k\2\2\u017b\u017c\7h\2\2\u017c\u017d\7k\2\2\u017d\u017e")
        buf.write("\7g\2\2\u017e\u017f\7t\2\2\u017fN\3\2\2\2\u0180\u0181")
        buf.write("\7g\2\2\u0181\u0182\7z\2\2\u0182\u0183\7v\2\2\u0183\u0184")
        buf.write("\7g\2\2\u0184\u0185\7p\2\2\u0185\u0186\7f\2\2\u0186P\3")
        buf.write("\2\2\2\u0187\u0188\7g\2\2\u0188\u0189\7x\2\2\u0189\u018a")
        buf.write("\7g\2\2\u018a\u018b\7p\2\2\u018b\u018c\7v\2\2\u018cR\3")
        buf.write("\2\2\2\u018d\u018e\7k\2\2\u018e\u018f\7h\2\2\u018fT\3")
        buf.write("\2\2\2\u0190\u0191\7B\2\2\u0191V\3\2\2\2\u0192\u0193\7")
        buf.write("c\2\2\u0193\u0194\7u\2\2\u0194X\3\2\2\2\u0195\u0196\7")
        buf.write("t\2\2\u0196\u0197\7k\2\2\u0197\u0198\7u\2\2\u0198\u0199")
        buf.write("\7g\2\2\u0199Z\3\2\2\2\u019a\u019b\7h\2\2\u019b\u019c")
        buf.write("\7c\2\2\u019c\u019d\7n\2\2\u019d\u019e\7n\2\2\u019e\\")
        buf.write("\3\2\2\2\u019f\u01a0\7g\2\2\u01a0\u01a1\7n\2\2\u01a1\u01a2")
        buf.write("\7c\2\2\u01a2\u01a3\7r\2\2\u01a3\u01a4\7u\2\2\u01a4\u01a5")
        buf.write("\7g\2\2\u01a5\u01a6\7f\2\2\u01a6^\3\2\2\2\u01a7\u01a8")
        buf.write("\7g\2\2\u01a8\u01a9\7x\2\2\u01a9\u01aa\7g\2\2\u01aa\u01ab")
        buf.write("\7t\2\2\u01ab\u01ac\7{\2\2\u01ac`\3\2\2\2\u01ad\u01ae")
        buf.write("\7x\2\2\u01ae\u01af\7c\2\2\u01af\u01b0\7t\2\2\u01b0b\3")
        buf.write("\2\2\2\u01b1\u01b2\7u\2\2\u01b2\u01b3\7c\2\2\u01b3\u01b4")
        buf.write("\7o\2\2\u01b4\u01b5\7r\2\2\u01b5\u01b6\7n\2\2\u01b6\u01b7")
        buf.write("\7g\2\2\u01b7d\3\2\2\2\u01b8\u01b9\7y\2\2\u01b9\u01ba")
        buf.write("\7k\2\2\u01ba\u01bb\7v\2\2\u01bb\u01bc\7j\2\2\u01bcf\3")
        buf.write("\2\2\2\u01bd\u01be\7m\2\2\u01be\u01bf\7g\2\2\u01bf\u01c0")
        buf.write("\7g\2\2\u01c0\u01c1\7r\2\2\u01c1h\3\2\2\2\u01c2\u01c3")
        buf.write("\7f\2\2\u01c3\u01c4\7g\2\2\u01c4\u01c5\7h\2\2\u01c5\u01c6")
        buf.write("\7c\2\2\u01c6\u01c7\7w\2\2\u01c7\u01c8\7n\2\2\u01c8\u01c9")
        buf.write("\7v\2\2\u01c9j\3\2\2\2\u01ca\u01cb\7j\2\2\u01cb\u01cc")
        buf.write("\7c\2\2\u01cc\u01cd\7t\2\2\u01cd\u01ce\7f\2\2\u01cel\3")
        buf.write("\2\2\2\u01cf\u01d0\7t\2\2\u01d0\u01d1\7g\2\2\u01d1\u01d2")
        buf.write("\7o\2\2\u01d2\u01d3\7q\2\2\u01d3\u01d4\7x\2\2\u01d4\u01d5")
        buf.write("\7g\2\2\u01d5\u01d6\7a\2\2\u01d6\u01d7\7f\2\2\u01d7\u01d8")
        buf.write("\7g\2\2\u01d8\u01d9\7h\2\2\u01d9\u01da\7c\2\2\u01da\u01db")
        buf.write("\7w\2\2\u01db\u01dc\7n\2\2\u01dc\u01dd\7v\2\2\u01ddn\3")
        buf.write("\2\2\2\u01de\u01df\7f\2\2\u01df\u01e0\7g\2\2\u01e0\u01e1")
        buf.write("\7h\2\2\u01e1p\3\2\2\2\u01e2\u01e3\7/\2\2\u01e3\u01e4")
        buf.write("\7@\2\2\u01e4r\3\2\2\2\u01e5\u01e6\7g\2\2\u01e6\u01e7")
        buf.write("\7z\2\2\u01e7\u01e8\7r\2\2\u01e8\u01e9\7t\2\2\u01e9\u01ea")
        buf.write("\7g\2\2\u01ea\u01eb\7u\2\2\u01eb\u01ec\7u\2\2\u01ec\u01ed")
        buf.write("\7k\2\2\u01ed\u01ee\7q\2\2\u01ee\u01ef\7p\2\2\u01eft\3")
        buf.write("\2\2\2\u01f0\u01f1\7w\2\2\u01f1\u01f2\7p\2\2\u01f2\u01f3")
        buf.write("\7f\2\2\u01f3\u01f4\7g\2\2\u01f4\u01f5\7h\2\2\u01f5\u01f6")
        buf.write("\7k\2\2\u01f6\u01f7\7p\2\2\u01f7\u01f8\7g\2\2\u01f8\u01f9")
        buf.write("\7f\2\2\u01f9v\3\2\2\2\u01fa\u01fb\7g\2\2\u01fb\u01fc")
        buf.write("\7z\2\2\u01fc\u01fd\7v\2\2\u01fd\u01fe\7g\2\2\u01fe\u01ff")
        buf.write("\7t\2\2\u01ff\u0200\7p\2\2\u0200\u0201\7c\2\2\u0201\u0202")
        buf.write("\7n\2\2\u0202x\3\2\2\2\u0203\u0204\7q\2\2\u0204\u0205")
        buf.write("\7p\2\2\u0205\u0206\7n\2\2\u0206\u0207\7{\2\2\u0207z\3")
        buf.write("\2\2\2\u0208\u0209\7e\2\2\u0209\u020a\7q\2\2\u020a\u020b")
        buf.write("\7x\2\2\u020b\u020c\7g\2\2\u020c\u020d\7t\2\2\u020d|\3")
        buf.write("\2\2\2\u020e\u020f\7t\2\2\u020f\u0210\7g\2\2\u0210\u0211")
        buf.write("\7e\2\2\u0211\u0212\7q\2\2\u0212\u0213\7t\2\2\u0213\u0214")
        buf.write("\7f\2\2\u0214~\3\2\2\2\u0215\u0216\7q\2\2\u0216\u0217")
        buf.write("\7p\2\2\u0217\u0080\3\2\2\2\u0218\u0219\7f\2\2\u0219\u021a")
        buf.write("\7q\2\2\u021a\u0082\3\2\2\2\u021b\u021c\7u\2\2\u021c\u021d")
        buf.write("\7g\2\2\u021d\u021e\7t\2\2\u021e\u021f\7k\2\2\u021f\u0220")
        buf.write("\7c\2\2\u0220\u0221\7n\2\2\u0221\u0084\3\2\2\2\u0222\u0223")
        buf.write("\7q\2\2\u0223\u0224\7p\2\2\u0224\u0225\7g\2\2\u0225\u0226")
        buf.write("\7a\2\2\u0226\u0227\7q\2\2\u0227\u0228\7h\2\2\u0228\u0086")
        buf.write("\3\2\2\2\u0229\u022a\7r\2\2\u022a\u022b\7c\2\2\u022b\u022c")
        buf.write("\7t\2\2\u022c\u022d\7c\2\2\u022d\u022e\7n\2\2\u022e\u022f")
        buf.write("\7n\2\2\u022f\u0230\7g\2\2\u0230\u0231\7n\2\2\u0231\u0088")
        buf.write("\3\2\2\2\u0232\u0233\7y\2\2\u0233\u0234\7c\2\2\u0234\u0235")
        buf.write("\7k\2\2\u0235\u0236\7v\2\2\u0236\u008a\3\2\2\2\u0237\u0238")
        buf.write("\7g\2\2\u0238\u0239\7o\2\2\u0239\u023a\7k\2\2\u023a\u023b")
        buf.write("\7v\2\2\u023b\u008c\3\2\2\2\u023c\u023d\7e\2\2\u023d\u023e")
        buf.write("\7c\2\2\u023e\u023f\7n\2\2\u023f\u0240\7n\2\2\u0240\u008e")
        buf.write("\3\2\2\2\u0241\u0242\7w\2\2\u0242\u0243\7p\2\2\u0243\u0244")
        buf.write("\7v\2\2\u0244\u0245\7k\2\2\u0245\u0246\7n\2\2\u0246\u0090")
        buf.write("\3\2\2\2\u0247\u0248\7A\2\2\u0248\u0092\3\2\2\2\u0249")
        buf.write("\u024a\7?\2\2\u024a\u024b\7@\2\2\u024b\u0094\3\2\2\2\u024c")
        buf.write("\u024d\7q\2\2\u024d\u024e\7t\2\2\u024e\u0096\3\2\2\2\u024f")
        buf.write("\u0250\7c\2\2\u0250\u0251\7p\2\2\u0251\u0252\7f\2\2\u0252")
        buf.write("\u0098\3\2\2\2\u0253\u0254\7p\2\2\u0254\u0255\7q\2\2\u0255")
        buf.write("\u0256\7v\2\2\u0256\u009a\3\2\2\2\u0257\u0258\7#\2\2\u0258")
        buf.write("\u0259\7?\2\2\u0259\u009c\3\2\2\2\u025a\u025b\7>\2\2\u025b")
        buf.write("\u009e\3\2\2\2\u025c\u025d\7>\2\2\u025d\u025e\7?\2\2\u025e")
        buf.write("\u00a0\3\2\2\2\u025f\u0260\7@\2\2\u0260\u00a2\3\2\2\2")
        buf.write("\u0261\u0262\7@\2\2\u0262\u0263\7?\2\2\u0263\u00a4\3\2")
        buf.write("\2\2\u0264\u0265\7k\2\2\u0265\u0266\7p\2\2\u0266\u00a6")
        buf.write("\3\2\2\2\u0267\u0268\7-\2\2\u0268\u00a8\3\2\2\2\u0269")
        buf.write("\u026a\7/\2\2\u026a\u00aa\3\2\2\2\u026b\u026c\7,\2\2\u026c")
        buf.write("\u00ac\3\2\2\2\u026d\u026e\7\61\2\2\u026e\u00ae\3\2\2")
        buf.write("\2\u026f\u0270\7\'\2\2\u0270\u00b0\3\2\2\2\u0271\u0272")
        buf.write("\7+\2\2\u0272\u0273\7A\2\2\u0273\u00b2\3\2\2\2\u0274\u0275")
        buf.write("\7k\2\2\u0275\u0276\7v\2\2\u0276\u00b4\3\2\2\2\u0277\u0278")
        buf.write("\7t\2\2\u0278\u0279\7c\2\2\u0279\u027a\7p\2\2\u027a\u027b")
        buf.write("\7i\2\2\u027b\u027c\7g\2\2\u027c\u00b6\3\2\2\2\u027d\u027e")
        buf.write("\7\60\2\2\u027e\u027f\7\60\2\2\u027f\u00b8\3\2\2\2\u0280")
        buf.write("\u0283\5\u00bb^\2\u0281\u0283\5\u00bd_\2\u0282\u0280\3")
        buf.write("\2\2\2\u0282\u0281\3\2\2\2\u0283\u00ba\3\2\2\2\u0284\u028a")
        buf.write("\7$\2\2\u0285\u0289\n\2\2\2\u0286\u0287\7^\2\2\u0287\u0289")
        buf.write("\n\3\2\2\u0288\u0285\3\2\2\2\u0288\u0286\3\2\2\2\u0289")
        buf.write("\u028c\3\2\2\2\u028a\u0288\3\2\2\2\u028a\u028b\3\2\2\2")
        buf.write("\u028b\u028d\3\2\2\2\u028c\u028a\3\2\2\2\u028d\u0299\7")
        buf.write("$\2\2\u028e\u0294\7)\2\2\u028f\u0293\n\2\2\2\u0290\u0291")
        buf.write("\7^\2\2\u0291\u0293\n\3\2\2\u0292\u028f\3\2\2\2\u0292")
        buf.write("\u0290\3\2\2\2\u0293\u0296\3\2\2\2\u0294\u0292\3\2\2\2")
        buf.write("\u0294\u0295\3\2\2\2\u0295\u0297\3\2\2\2\u0296\u0294\3")
        buf.write("\2\2\2\u0297\u0299\7)\2\2\u0298\u0284\3\2\2\2\u0298\u028e")
        buf.write("\3\2\2\2\u0299\u00bc\3\2\2\2\u029a\u029b\7$\2\2\u029b")
        buf.write("\u029c\7$\2\2\u029c\u029d\7$\2\2\u029d\u02a3\3\2\2\2\u029e")
        buf.write("\u02a2\n\4\2\2\u029f\u02a0\7^\2\2\u02a0\u02a2\n\3\2\2")
        buf.write("\u02a1\u029e\3\2\2\2\u02a1\u029f\3\2\2\2\u02a2\u02a5\3")
        buf.write("\2\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4\3\2\2\2\u02a4\u02a6")
        buf.write("\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a6\u02a7\7$\2\2\u02a7")
        buf.write("\u02a8\7$\2\2\u02a8\u02b9\7$\2\2\u02a9\u02aa\7)\2\2\u02aa")
        buf.write("\u02ab\7)\2\2\u02ab\u02ac\7)\2\2\u02ac\u02b2\3\2\2\2\u02ad")
        buf.write("\u02b1\n\4\2\2\u02ae\u02af\7^\2\2\u02af\u02b1\n\3\2\2")
        buf.write("\u02b0\u02ad\3\2\2\2\u02b0\u02ae\3\2\2\2\u02b1\u02b4\3")
        buf.write("\2\2\2\u02b2\u02b0\3\2\2\2\u02b2\u02b3\3\2\2\2\u02b3\u02b5")
        buf.write("\3\2\2\2\u02b4\u02b2\3\2\2\2\u02b5\u02b6\7)\2\2\u02b6")
        buf.write("\u02b7\7)\2\2\u02b7\u02b9\7)\2\2\u02b8\u029a\3\2\2\2\u02b8")
        buf.write("\u02a9\3\2\2\2\u02b9\u00be\3\2\2\2\u02ba\u02bb\7v\2\2")
        buf.write("\u02bb\u02bc\7t\2\2\u02bc\u02bd\7w\2\2\u02bd\u02c4\7g")
        buf.write("\2\2\u02be\u02bf\7h\2\2\u02bf\u02c0\7c\2\2\u02c0\u02c1")
        buf.write("\7n\2\2\u02c1\u02c2\7u\2\2\u02c2\u02c4\7g\2\2\u02c3\u02ba")
        buf.write("\3\2\2\2\u02c3\u02be\3\2\2\2\u02c4\u00c0\3\2\2\2\u02c5")
        buf.write("\u02c9\5\u00c3b\2\u02c6\u02c9\5\u00c5c\2\u02c7\u02c9\5")
        buf.write("\u00c7d\2\u02c8\u02c5\3\2\2\2\u02c8\u02c6\3\2\2\2\u02c8")
        buf.write("\u02c7\3\2\2\2\u02c9\u00c2\3\2\2\2\u02ca\u02cc\5\u00c9")
        buf.write("e\2\u02cb\u02ca\3\2\2\2\u02cc\u02cd\3\2\2\2\u02cd\u02cb")
        buf.write("\3\2\2\2\u02cd\u02ce\3\2\2\2\u02ce\u00c4\3\2\2\2\u02cf")
        buf.write("\u02d0\7\62\2\2\u02d0\u02d1\7z\2\2\u02d1\u02d3\3\2\2\2")
        buf.write("\u02d2\u02d4\5\u00cbf\2\u02d3\u02d2\3\2\2\2\u02d4\u02d5")
        buf.write("\3\2\2\2\u02d5\u02d3\3\2\2\2\u02d5\u02d6\3\2\2\2\u02d6")
        buf.write("\u00c6\3\2\2\2\u02d7\u02d9\7/\2\2\u02d8\u02da\5\u00c9")
        buf.write("e\2\u02d9\u02d8\3\2\2\2\u02da\u02db\3\2\2\2\u02db\u02d9")
        buf.write("\3\2\2\2\u02db\u02dc\3\2\2\2\u02dc\u00c8\3\2\2\2\u02dd")
        buf.write("\u02de\4\62;\2\u02de\u00ca\3\2\2\2\u02df\u02e2\5\u00c9")
        buf.write("e\2\u02e0\u02e2\t\5\2\2\u02e1\u02df\3\2\2\2\u02e1\u02e0")
        buf.write("\3\2\2\2\u02e2\u00cc\3\2\2\2\u02e3\u02e5\t\6\2\2\u02e4")
        buf.write("\u02e3\3\2\2\2\u02e4\u02e5\3\2\2\2\u02e5\u02e9\3\2\2\2")
        buf.write("\u02e6\u02e8\5\u00c9e\2\u02e7\u02e6\3\2\2\2\u02e8\u02eb")
        buf.write("\3\2\2\2\u02e9\u02e7\3\2\2\2\u02e9\u02ea\3\2\2\2\u02ea")
        buf.write("\u02ec\3\2\2\2\u02eb\u02e9\3\2\2\2\u02ec\u02ee\7\60\2")
        buf.write("\2\u02ed\u02ef\5\u00c9e\2\u02ee\u02ed\3\2\2\2\u02ef\u02f0")
        buf.write("\3\2\2\2\u02f0\u02ee\3\2\2\2\u02f0\u02f1\3\2\2\2\u02f1")
        buf.write("\u02fb\3\2\2\2\u02f2\u02f4\t\7\2\2\u02f3\u02f5\t\6\2\2")
        buf.write("\u02f4\u02f3\3\2\2\2\u02f4\u02f5\3\2\2\2\u02f5\u02f7\3")
        buf.write("\2\2\2\u02f6\u02f8\5\u00c9e\2\u02f7\u02f6\3\2\2\2\u02f8")
        buf.write("\u02f9\3\2\2\2\u02f9\u02f7\3\2\2\2\u02f9\u02fa\3\2\2\2")
        buf.write("\u02fa\u02fc\3\2\2\2\u02fb\u02f2\3\2\2\2\u02fb\u02fc\3")
        buf.write("\2\2\2\u02fc\u00ce\3\2\2\2\u02fd\u0301\t\b\2\2\u02fe\u0300")
        buf.write("\t\t\2\2\u02ff\u02fe\3\2\2\2\u0300\u0303\3\2\2\2\u0301")
        buf.write("\u02ff\3\2\2\2\u0301\u0302\3\2\2\2\u0302\u030c\3\2\2\2")
        buf.write("\u0303\u0301\3\2\2\2\u0304\u0306\7~\2\2\u0305\u0307\n")
        buf.write("\n\2\2\u0306\u0305\3\2\2\2\u0307\u0308\3\2\2\2\u0308\u0306")
        buf.write("\3\2\2\2\u0308\u0309\3\2\2\2\u0309\u030a\3\2\2\2\u030a")
        buf.write("\u030c\7~\2\2\u030b\u02fd\3\2\2\2\u030b\u0304\3\2\2\2")
        buf.write("\u030c\u00d0\3\2\2\2\u030d\u0310\5\u00cdg\2\u030e\u0310")
        buf.write("\5\u00c1a\2\u030f\u030d\3\2\2\2\u030f\u030e\3\2\2\2\u0310")
        buf.write("\u0311\3\2\2\2\u0311\u0312\5\u00cfh\2\u0312\u00d2\3\2")
        buf.write("\2\2\u0313\u0315\7^\2\2\u0314\u0316\7\17\2\2\u0315\u0314")
        buf.write("\3\2\2\2\u0315\u0316\3\2\2\2\u0316\u0317\3\2\2\2\u0317")
        buf.write("\u0318\7\f\2\2\u0318\u0319\3\2\2\2\u0319\u031a\bj\2\2")
        buf.write("\u031a\u00d4\3\2\2\2\u031b\u031d\7\17\2\2\u031c\u031b")
        buf.write("\3\2\2\2\u031c\u031d\3\2\2\2\u031d\u031e\3\2\2\2\u031e")
        buf.write("\u0322\7\f\2\2\u031f\u0321\7\"\2\2\u0320\u031f\3\2\2\2")
        buf.write("\u0321\u0324\3\2\2\2\u0322\u0320\3\2\2\2\u0322\u0323\3")
        buf.write("\2\2\2\u0323\u00d6\3\2\2\2\u0324\u0322\3\2\2\2\u0325\u0327")
        buf.write("\t\13\2\2\u0326\u0325\3\2\2\2\u0327\u0328\3\2\2\2\u0328")
        buf.write("\u0326\3\2\2\2\u0328\u0329\3\2\2\2\u0329\u032a\3\2\2\2")
        buf.write("\u032a\u032b\bl\2\2\u032b\u00d8\3\2\2\2\u032c\u0330\7")
        buf.write("%\2\2\u032d\u032f\n\3\2\2\u032e\u032d\3\2\2\2\u032f\u0332")
        buf.write("\3\2\2\2\u0330\u032e\3\2\2\2\u0330\u0331\3\2\2\2\u0331")
        buf.write("\u0333\3\2\2\2\u0332\u0330\3\2\2\2\u0333\u0334\bm\2\2")
        buf.write("\u0334\u00da\3\2\2\2#\2\u0282\u0288\u028a\u0292\u0294")
        buf.write("\u0298\u02a1\u02a3\u02b0\u02b2\u02b8\u02c3\u02c8\u02cd")
        buf.write("\u02d5\u02db\u02e1\u02e4\u02e9\u02f0\u02f4\u02f9\u02fb")
        buf.write("\u0301\u0308\u030b\u030f\u0315\u031c\u0322\u0328\u0330")
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
    STRING_LITERAL = 92
    SHORTSTRING = 93
    LONGSTRING = 94
    BOOL_LITERAL = 95
    INTEGER_LITERAL = 96
    UINT_LITERAL = 97
    HEX_UINT_LITERAL = 98
    INT_LITERAL = 99
    FLOAT_LITERAL = 100
    IDENTIFIER = 101
    PHYSICAL_LITERAL = 102
    LINEJOINER = 103
    NEWLINE = 104
    WS = 105
    COMMENT = 106

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
            "'>'", "'>='", "'in'", "'+'", "'-'", "'*'", "'/'", "'%'", "')?'", 
            "'it'", "'range'", "'..'" ]

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
                  "T__86", "T__87", "T__88", "T__89", "T__90", "STRING_LITERAL", 
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



