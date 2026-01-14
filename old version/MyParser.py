# Generated from MyParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,426,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,1,0,1,0,1,0,1,1,1,1,3,1,90,8,1,5,1,92,8,1,10,
        1,12,1,95,9,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,3,2,110,8,2,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,3,5,123,
        8,5,1,5,1,5,1,5,3,5,128,8,5,1,6,1,6,1,6,5,6,133,8,6,10,6,12,6,136,
        9,6,1,7,1,7,1,7,5,7,141,8,7,10,7,12,7,144,9,7,1,8,1,8,1,9,1,9,1,
        9,1,9,3,9,152,8,9,1,9,1,9,1,9,1,9,3,9,158,8,9,3,9,160,8,9,1,10,1,
        10,3,10,164,8,10,1,11,1,11,1,11,1,11,1,11,3,11,171,8,11,1,12,1,12,
        1,12,1,13,1,13,1,13,3,13,179,8,13,1,13,3,13,182,8,13,1,14,1,14,1,
        14,1,14,1,15,1,15,1,16,1,16,1,16,1,16,1,16,3,16,195,8,16,1,17,1,
        17,1,17,5,17,200,8,17,10,17,12,17,203,9,17,1,18,1,18,1,18,1,18,1,
        19,1,19,1,19,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,
        20,1,21,1,21,1,21,3,21,226,8,21,1,21,1,21,1,21,1,21,1,21,1,22,1,
        22,1,22,1,22,1,23,1,23,1,23,1,23,1,23,3,23,242,8,23,1,24,1,24,1,
        24,1,24,1,24,1,25,1,25,1,25,3,25,252,8,25,1,26,1,26,1,26,3,26,257,
        8,26,1,26,3,26,260,8,26,1,26,3,26,263,8,26,1,27,1,27,1,27,1,27,1,
        27,5,27,270,8,27,10,27,12,27,273,9,27,1,27,3,27,276,8,27,1,28,1,
        28,3,28,280,8,28,1,29,1,29,1,29,5,29,285,8,29,10,29,12,29,288,9,
        29,1,30,1,30,3,30,292,8,30,1,30,3,30,295,8,30,1,30,3,30,298,8,30,
        1,31,1,31,1,31,1,31,5,31,304,8,31,10,31,12,31,307,9,31,1,32,1,32,
        3,32,311,8,32,1,32,3,32,314,8,32,1,33,1,33,1,33,1,33,1,33,1,33,1,
        33,1,33,1,33,1,33,1,33,1,33,3,33,328,8,33,1,33,1,33,1,33,1,33,1,
        33,1,33,5,33,336,8,33,10,33,12,33,339,9,33,1,34,1,34,1,34,5,34,344,
        8,34,10,34,12,34,347,9,34,1,35,1,35,4,35,351,8,35,11,35,12,35,352,
        1,35,3,35,356,8,35,1,35,1,35,1,36,1,36,1,36,1,36,1,36,1,37,1,37,
        1,37,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,375,8,38,1,38,1,38,
        1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,1,38,3,38,390,
        8,38,1,38,1,38,1,38,5,38,395,8,38,10,38,12,38,398,9,38,1,39,1,39,
        1,39,3,39,403,8,39,1,39,1,39,1,39,3,39,408,8,39,1,40,1,40,1,40,3,
        40,413,8,40,1,40,1,40,1,40,1,40,3,40,419,8,40,1,40,3,40,422,8,40,
        1,41,1,41,1,41,0,2,66,76,42,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,
        72,74,76,78,80,82,0,3,2,0,9,9,11,11,2,0,1,1,13,13,3,0,1,1,5,6,12,
        12,450,0,84,1,0,0,0,2,93,1,0,0,0,4,109,1,0,0,0,6,111,1,0,0,0,8,113,
        1,0,0,0,10,127,1,0,0,0,12,129,1,0,0,0,14,137,1,0,0,0,16,145,1,0,
        0,0,18,159,1,0,0,0,20,161,1,0,0,0,22,165,1,0,0,0,24,172,1,0,0,0,
        26,175,1,0,0,0,28,183,1,0,0,0,30,187,1,0,0,0,32,189,1,0,0,0,34,196,
        1,0,0,0,36,204,1,0,0,0,38,208,1,0,0,0,40,211,1,0,0,0,42,222,1,0,
        0,0,44,232,1,0,0,0,46,236,1,0,0,0,48,243,1,0,0,0,50,248,1,0,0,0,
        52,253,1,0,0,0,54,264,1,0,0,0,56,279,1,0,0,0,58,281,1,0,0,0,60,297,
        1,0,0,0,62,299,1,0,0,0,64,308,1,0,0,0,66,327,1,0,0,0,68,340,1,0,
        0,0,70,348,1,0,0,0,72,359,1,0,0,0,74,364,1,0,0,0,76,389,1,0,0,0,
        78,407,1,0,0,0,80,421,1,0,0,0,82,423,1,0,0,0,84,85,3,2,1,0,85,86,
        5,0,0,1,86,1,1,0,0,0,87,89,3,4,2,0,88,90,5,14,0,0,89,88,1,0,0,0,
        89,90,1,0,0,0,90,92,1,0,0,0,91,87,1,0,0,0,92,95,1,0,0,0,93,91,1,
        0,0,0,93,94,1,0,0,0,94,3,1,0,0,0,95,93,1,0,0,0,96,110,3,8,4,0,97,
        110,3,22,11,0,98,110,3,32,16,0,99,110,3,46,23,0,100,110,3,48,24,
        0,101,110,3,42,21,0,102,110,3,40,20,0,103,110,3,26,13,0,104,110,
        3,6,3,0,105,110,3,44,22,0,106,110,3,52,26,0,107,110,3,50,25,0,108,
        110,5,14,0,0,109,96,1,0,0,0,109,97,1,0,0,0,109,98,1,0,0,0,109,99,
        1,0,0,0,109,100,1,0,0,0,109,101,1,0,0,0,109,102,1,0,0,0,109,103,
        1,0,0,0,109,104,1,0,0,0,109,105,1,0,0,0,109,106,1,0,0,0,109,107,
        1,0,0,0,109,108,1,0,0,0,110,5,1,0,0,0,111,112,5,1,0,0,112,7,1,0,
        0,0,113,114,5,1,0,0,114,115,5,1,0,0,115,116,3,10,5,0,116,117,5,14,
        0,0,117,118,3,12,6,0,118,119,5,14,0,0,119,9,1,0,0,0,120,121,5,11,
        0,0,121,123,5,14,0,0,122,120,1,0,0,0,122,123,1,0,0,0,123,124,1,0,
        0,0,124,128,5,11,0,0,125,128,5,9,0,0,126,128,5,11,0,0,127,122,1,
        0,0,0,127,125,1,0,0,0,127,126,1,0,0,0,128,11,1,0,0,0,129,134,3,14,
        7,0,130,131,5,14,0,0,131,133,3,14,7,0,132,130,1,0,0,0,133,136,1,
        0,0,0,134,132,1,0,0,0,134,135,1,0,0,0,135,13,1,0,0,0,136,134,1,0,
        0,0,137,138,3,16,8,0,138,142,3,18,9,0,139,141,3,20,10,0,140,139,
        1,0,0,0,141,144,1,0,0,0,142,140,1,0,0,0,142,143,1,0,0,0,143,15,1,
        0,0,0,144,142,1,0,0,0,145,146,7,0,0,0,146,17,1,0,0,0,147,151,5,1,
        0,0,148,149,5,14,0,0,149,150,5,12,0,0,150,152,5,14,0,0,151,148,1,
        0,0,0,151,152,1,0,0,0,152,160,1,0,0,0,153,157,5,11,0,0,154,155,5,
        14,0,0,155,156,5,12,0,0,156,158,5,14,0,0,157,154,1,0,0,0,157,158,
        1,0,0,0,158,160,1,0,0,0,159,147,1,0,0,0,159,153,1,0,0,0,160,19,1,
        0,0,0,161,163,5,1,0,0,162,164,5,1,0,0,163,162,1,0,0,0,163,164,1,
        0,0,0,164,21,1,0,0,0,165,166,5,1,0,0,166,167,5,1,0,0,167,170,3,10,
        5,0,168,171,3,24,12,0,169,171,3,28,14,0,170,168,1,0,0,0,170,169,
        1,0,0,0,171,23,1,0,0,0,172,173,5,1,0,0,173,174,3,14,7,0,174,25,1,
        0,0,0,175,178,5,1,0,0,176,179,3,10,5,0,177,179,3,62,31,0,178,176,
        1,0,0,0,178,177,1,0,0,0,179,181,1,0,0,0,180,182,3,38,19,0,181,180,
        1,0,0,0,181,182,1,0,0,0,182,27,1,0,0,0,183,184,5,1,0,0,184,185,5,
        1,0,0,185,186,3,30,15,0,186,29,1,0,0,0,187,188,7,0,0,0,188,31,1,
        0,0,0,189,190,5,1,0,0,190,191,3,10,5,0,191,192,5,1,0,0,192,194,3,
        34,17,0,193,195,3,38,19,0,194,193,1,0,0,0,194,195,1,0,0,0,195,33,
        1,0,0,0,196,201,3,36,18,0,197,198,5,14,0,0,198,200,3,36,18,0,199,
        197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,
        35,1,0,0,0,203,201,1,0,0,0,204,205,3,16,8,0,205,206,5,13,0,0,206,
        207,3,66,33,0,207,37,1,0,0,0,208,209,5,1,0,0,209,210,3,76,38,0,210,
        39,1,0,0,0,211,212,5,1,0,0,212,213,5,1,0,0,213,214,3,2,1,0,214,215,
        5,1,0,0,215,216,5,1,0,0,216,217,5,1,0,0,217,218,5,1,0,0,218,219,
        3,2,1,0,219,220,5,1,0,0,220,221,5,1,0,0,221,41,1,0,0,0,222,223,5,
        1,0,0,223,225,5,1,0,0,224,226,5,1,0,0,225,224,1,0,0,0,225,226,1,
        0,0,0,226,227,1,0,0,0,227,228,5,14,0,0,228,229,3,52,26,0,229,230,
        5,14,0,0,230,231,3,44,22,0,231,43,1,0,0,0,232,233,5,1,0,0,233,234,
        3,2,1,0,234,235,5,1,0,0,235,45,1,0,0,0,236,237,5,1,0,0,237,238,5,
        10,0,0,238,241,3,18,9,0,239,240,5,13,0,0,240,242,3,66,33,0,241,239,
        1,0,0,0,241,242,1,0,0,0,242,47,1,0,0,0,243,244,5,1,0,0,244,245,5,
        10,0,0,245,246,5,13,0,0,246,247,3,66,33,0,247,49,1,0,0,0,248,249,
        5,1,0,0,249,251,5,11,0,0,250,252,3,68,34,0,251,250,1,0,0,0,251,252,
        1,0,0,0,252,51,1,0,0,0,253,254,5,1,0,0,254,256,3,58,29,0,255,257,
        3,62,31,0,256,255,1,0,0,0,256,257,1,0,0,0,257,259,1,0,0,0,258,260,
        3,38,19,0,259,258,1,0,0,0,259,260,1,0,0,0,260,262,1,0,0,0,261,263,
        3,54,27,0,262,261,1,0,0,0,262,263,1,0,0,0,263,53,1,0,0,0,264,265,
        5,1,0,0,265,266,5,1,0,0,266,271,3,56,28,0,267,268,5,14,0,0,268,270,
        3,56,28,0,269,267,1,0,0,0,270,273,1,0,0,0,271,269,1,0,0,0,271,272,
        1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,274,276,5,1,0,0,275,274,
        1,0,0,0,275,276,1,0,0,0,276,55,1,0,0,0,277,280,5,11,0,0,278,280,
        3,66,33,0,279,277,1,0,0,0,279,278,1,0,0,0,280,57,1,0,0,0,281,286,
        3,60,30,0,282,283,5,14,0,0,283,285,3,60,30,0,284,282,1,0,0,0,285,
        288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,59,1,0,0,0,288,286,
        1,0,0,0,289,294,3,66,33,0,290,292,5,1,0,0,291,290,1,0,0,0,291,292,
        1,0,0,0,292,293,1,0,0,0,293,295,5,11,0,0,294,291,1,0,0,0,294,295,
        1,0,0,0,295,298,1,0,0,0,296,298,5,13,0,0,297,289,1,0,0,0,297,296,
        1,0,0,0,298,61,1,0,0,0,299,300,5,1,0,0,300,305,3,64,32,0,301,302,
        5,14,0,0,302,304,3,64,32,0,303,301,1,0,0,0,304,307,1,0,0,0,305,303,
        1,0,0,0,305,306,1,0,0,0,306,63,1,0,0,0,307,305,1,0,0,0,308,313,3,
        10,5,0,309,311,5,1,0,0,310,309,1,0,0,0,310,311,1,0,0,0,311,312,1,
        0,0,0,312,314,5,11,0,0,313,310,1,0,0,0,313,314,1,0,0,0,314,65,1,
        0,0,0,315,316,6,33,-1,0,316,328,3,82,41,0,317,328,3,78,39,0,318,
        328,3,80,40,0,319,328,3,70,35,0,320,321,5,14,0,0,321,322,3,66,33,
        0,322,323,5,14,0,0,323,328,1,0,0,0,324,328,5,10,0,0,325,328,5,5,
        0,0,326,328,5,6,0,0,327,315,1,0,0,0,327,317,1,0,0,0,327,318,1,0,
        0,0,327,319,1,0,0,0,327,320,1,0,0,0,327,324,1,0,0,0,327,325,1,0,
        0,0,327,326,1,0,0,0,328,337,1,0,0,0,329,330,10,5,0,0,330,331,5,13,
        0,0,331,336,3,66,33,6,332,333,10,4,0,0,333,334,5,1,0,0,334,336,3,
        66,33,5,335,329,1,0,0,0,335,332,1,0,0,0,336,339,1,0,0,0,337,335,
        1,0,0,0,337,338,1,0,0,0,338,67,1,0,0,0,339,337,1,0,0,0,340,345,3,
        66,33,0,341,342,5,14,0,0,342,344,3,66,33,0,343,341,1,0,0,0,344,347,
        1,0,0,0,345,343,1,0,0,0,345,346,1,0,0,0,346,69,1,0,0,0,347,345,1,
        0,0,0,348,350,5,1,0,0,349,351,3,72,36,0,350,349,1,0,0,0,351,352,
        1,0,0,0,352,350,1,0,0,0,352,353,1,0,0,0,353,355,1,0,0,0,354,356,
        3,74,37,0,355,354,1,0,0,0,355,356,1,0,0,0,356,357,1,0,0,0,357,358,
        5,1,0,0,358,71,1,0,0,0,359,360,5,1,0,0,360,361,3,76,38,0,361,362,
        5,1,0,0,362,363,3,66,33,0,363,73,1,0,0,0,364,365,5,1,0,0,365,366,
        3,66,33,0,366,75,1,0,0,0,367,368,6,38,-1,0,368,369,3,66,33,0,369,
        370,7,1,0,0,370,371,3,66,33,0,371,390,1,0,0,0,372,374,3,66,33,0,
        373,375,5,1,0,0,374,373,1,0,0,0,374,375,1,0,0,0,375,376,1,0,0,0,
        376,377,5,1,0,0,377,378,5,14,0,0,378,379,3,68,34,0,379,380,5,14,
        0,0,380,390,1,0,0,0,381,382,3,66,33,0,382,383,5,1,0,0,383,384,5,
        1,0,0,384,390,1,0,0,0,385,386,5,14,0,0,386,387,3,76,38,0,387,388,
        5,14,0,0,388,390,1,0,0,0,389,367,1,0,0,0,389,372,1,0,0,0,389,381,
        1,0,0,0,389,385,1,0,0,0,390,396,1,0,0,0,391,392,10,1,0,0,392,393,
        5,1,0,0,393,395,3,76,38,2,394,391,1,0,0,0,395,398,1,0,0,0,396,394,
        1,0,0,0,396,397,1,0,0,0,397,77,1,0,0,0,398,396,1,0,0,0,399,400,3,
        10,5,0,400,401,5,14,0,0,401,403,1,0,0,0,402,399,1,0,0,0,402,403,
        1,0,0,0,403,404,1,0,0,0,404,408,3,16,8,0,405,408,5,11,0,0,406,408,
        5,9,0,0,407,402,1,0,0,0,407,405,1,0,0,0,407,406,1,0,0,0,408,79,1,
        0,0,0,409,410,5,11,0,0,410,412,5,14,0,0,411,413,3,68,34,0,412,411,
        1,0,0,0,412,413,1,0,0,0,413,414,1,0,0,0,414,422,5,14,0,0,415,416,
        5,1,0,0,416,418,5,14,0,0,417,419,3,68,34,0,418,417,1,0,0,0,418,419,
        1,0,0,0,419,420,1,0,0,0,420,422,5,14,0,0,421,409,1,0,0,0,421,415,
        1,0,0,0,422,81,1,0,0,0,423,424,7,2,0,0,424,83,1,0,0,0,46,89,93,109,
        122,127,134,142,151,157,159,163,170,178,181,194,201,225,241,251,
        256,259,262,271,275,279,286,291,294,297,305,310,313,327,335,337,
        345,352,355,374,389,396,402,407,412,418,421
    ]

class MyParser ( Parser ):

    grammarFileName = "MyParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'/*'", "'*/'" ]

    symbolicNames = [ "<INVALID>", "KEYWORD", "LINE_COMMENT", "BLOCK_COMMENT_START", 
                      "WS", "STRING_SINGLE", "STRING_DOUBLE", "HEX_STRING", 
                      "BIT_STRING", "BRACKET_IDENTIFIER", "VARIABLE", "IDENTIFIER", 
                      "NUMBER", "OPERATOR", "PUNCTUATION", "COMMENT_OPEN", 
                      "COMMENT_CLOSE", "COMMENT_TEXT" ]

    RULE_sqlScript = 0
    RULE_statementList = 1
    RULE_statement = 2
    RULE_goStatement = 3
    RULE_createTableStatement = 4
    RULE_tableName = 5
    RULE_columnDefinitionList = 6
    RULE_columnDefinition = 7
    RULE_columnName = 8
    RULE_dataType = 9
    RULE_columnConstraint = 10
    RULE_alterTableStatement = 11
    RULE_addColumnClause = 12
    RULE_deleteStatement = 13
    RULE_dropConstraintClause = 14
    RULE_constraintName = 15
    RULE_updateStatement = 16
    RULE_assignmentList = 17
    RULE_assignment = 18
    RULE_whereClause = 19
    RULE_tryCatchStatement = 20
    RULE_ifStatement = 21
    RULE_blockStatement = 22
    RULE_declareStatement = 23
    RULE_setStatement = 24
    RULE_execStatement = 25
    RULE_selectStatement = 26
    RULE_orderByClause = 27
    RULE_orderByItem = 28
    RULE_selectList = 29
    RULE_selectItem = 30
    RULE_fromClause = 31
    RULE_tableSource = 32
    RULE_expression = 33
    RULE_expressionList = 34
    RULE_caseExpression = 35
    RULE_whenClause = 36
    RULE_elseClause = 37
    RULE_condition = 38
    RULE_columnReference = 39
    RULE_functionCall = 40
    RULE_literal = 41

    ruleNames =  [ "sqlScript", "statementList", "statement", "goStatement", 
                   "createTableStatement", "tableName", "columnDefinitionList", 
                   "columnDefinition", "columnName", "dataType", "columnConstraint", 
                   "alterTableStatement", "addColumnClause", "deleteStatement", 
                   "dropConstraintClause", "constraintName", "updateStatement", 
                   "assignmentList", "assignment", "whereClause", "tryCatchStatement", 
                   "ifStatement", "blockStatement", "declareStatement", 
                   "setStatement", "execStatement", "selectStatement", "orderByClause", 
                   "orderByItem", "selectList", "selectItem", "fromClause", 
                   "tableSource", "expression", "expressionList", "caseExpression", 
                   "whenClause", "elseClause", "condition", "columnReference", 
                   "functionCall", "literal" ]

    EOF = Token.EOF
    KEYWORD=1
    LINE_COMMENT=2
    BLOCK_COMMENT_START=3
    WS=4
    STRING_SINGLE=5
    STRING_DOUBLE=6
    HEX_STRING=7
    BIT_STRING=8
    BRACKET_IDENTIFIER=9
    VARIABLE=10
    IDENTIFIER=11
    NUMBER=12
    OPERATOR=13
    PUNCTUATION=14
    COMMENT_OPEN=15
    COMMENT_CLOSE=16
    COMMENT_TEXT=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SqlScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(MyParser.StatementListContext,0)


        def EOF(self):
            return self.getToken(MyParser.EOF, 0)

        def getRuleIndex(self):
            return MyParser.RULE_sqlScript

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSqlScript" ):
                listener.enterSqlScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSqlScript" ):
                listener.exitSqlScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSqlScript" ):
                return visitor.visitSqlScript(self)
            else:
                return visitor.visitChildren(self)




    def sqlScript(self):

        localctx = MyParser.SqlScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sqlScript)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.statementList()
            self.state = 85
            self.match(MyParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.StatementContext)
            else:
                return self.getTypedRuleContext(MyParser.StatementContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_statementList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatementList" ):
                listener.enterStatementList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatementList" ):
                listener.exitStatementList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MyParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statementList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 87
                    self.statement()
                    self.state = 89
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 88
                        self.match(MyParser.PUNCTUATION)

             
                self.state = 95
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def createTableStatement(self):
            return self.getTypedRuleContext(MyParser.CreateTableStatementContext,0)


        def alterTableStatement(self):
            return self.getTypedRuleContext(MyParser.AlterTableStatementContext,0)


        def updateStatement(self):
            return self.getTypedRuleContext(MyParser.UpdateStatementContext,0)


        def declareStatement(self):
            return self.getTypedRuleContext(MyParser.DeclareStatementContext,0)


        def setStatement(self):
            return self.getTypedRuleContext(MyParser.SetStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MyParser.IfStatementContext,0)


        def tryCatchStatement(self):
            return self.getTypedRuleContext(MyParser.TryCatchStatementContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(MyParser.DeleteStatementContext,0)


        def goStatement(self):
            return self.getTypedRuleContext(MyParser.GoStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MyParser.BlockStatementContext,0)


        def selectStatement(self):
            return self.getTypedRuleContext(MyParser.SelectStatementContext,0)


        def execStatement(self):
            return self.getTypedRuleContext(MyParser.ExecStatementContext,0)


        def PUNCTUATION(self):
            return self.getToken(MyParser.PUNCTUATION, 0)

        def getRuleIndex(self):
            return MyParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MyParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 109
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.createTableStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.alterTableStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.updateStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.declareStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.setStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 101
                self.ifStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 102
                self.tryCatchStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 103
                self.deleteStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 104
                self.goStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 105
                self.blockStatement()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 106
                self.selectStatement()
                pass

            elif la_ == 12:
                self.enterOuterAlt(localctx, 12)
                self.state = 107
                self.execStatement()
                pass

            elif la_ == 13:
                self.enterOuterAlt(localctx, 13)
                self.state = 108
                self.match(MyParser.PUNCTUATION)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GoStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_goStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGoStatement" ):
                listener.enterGoStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGoStatement" ):
                listener.exitGoStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGoStatement" ):
                return visitor.visitGoStatement(self)
            else:
                return visitor.visitChildren(self)




    def goStatement(self):

        localctx = MyParser.GoStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_goStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self.match(MyParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CreateTableStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def columnDefinitionList(self):
            return self.getTypedRuleContext(MyParser.ColumnDefinitionListContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_createTableStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCreateTableStatement" ):
                listener.enterCreateTableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCreateTableStatement" ):
                listener.exitCreateTableStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCreateTableStatement" ):
                return visitor.visitCreateTableStatement(self)
            else:
                return visitor.visitChildren(self)




    def createTableStatement(self):

        localctx = MyParser.CreateTableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_createTableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(MyParser.KEYWORD)
            self.state = 114
            self.match(MyParser.KEYWORD)
            self.state = 115
            self.tableName()
            self.state = 116
            self.match(MyParser.PUNCTUATION)
            self.state = 117
            self.columnDefinitionList()
            self.state = 118
            self.match(MyParser.PUNCTUATION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.IDENTIFIER)
            else:
                return self.getToken(MyParser.IDENTIFIER, i)

        def PUNCTUATION(self):
            return self.getToken(MyParser.PUNCTUATION, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(MyParser.BRACKET_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_tableName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableName" ):
                listener.enterTableName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableName" ):
                listener.exitTableName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableName" ):
                return visitor.visitTableName(self)
            else:
                return visitor.visitChildren(self)




    def tableName(self):

        localctx = MyParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_tableName)
        try:
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 120
                    self.match(MyParser.IDENTIFIER)
                    self.state = 121
                    self.match(MyParser.PUNCTUATION)


                self.state = 124
                self.match(MyParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.match(MyParser.BRACKET_IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 126
                self.match(MyParser.IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnDefinitionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ColumnDefinitionContext)
            else:
                return self.getTypedRuleContext(MyParser.ColumnDefinitionContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_columnDefinitionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDefinitionList" ):
                listener.enterColumnDefinitionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDefinitionList" ):
                listener.exitColumnDefinitionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnDefinitionList" ):
                return visitor.visitColumnDefinitionList(self)
            else:
                return visitor.visitChildren(self)




    def columnDefinitionList(self):

        localctx = MyParser.ColumnDefinitionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columnDefinitionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.columnDefinition()
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 130
                    self.match(MyParser.PUNCTUATION)
                    self.state = 131
                    self.columnDefinition() 
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MyParser.ColumnNameContext,0)


        def dataType(self):
            return self.getTypedRuleContext(MyParser.DataTypeContext,0)


        def columnConstraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ColumnConstraintContext)
            else:
                return self.getTypedRuleContext(MyParser.ColumnConstraintContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_columnDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnDefinition" ):
                listener.enterColumnDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnDefinition" ):
                listener.exitColumnDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnDefinition" ):
                return visitor.visitColumnDefinition(self)
            else:
                return visitor.visitChildren(self)




    def columnDefinition(self):

        localctx = MyParser.ColumnDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_columnDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.columnName()
            self.state = 138
            self.dataType()
            self.state = 142
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 139
                    self.columnConstraint() 
                self.state = 144
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ColumnNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(MyParser.BRACKET_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_columnName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnName" ):
                listener.enterColumnName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnName" ):
                listener.exitColumnName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnName" ):
                return visitor.visitColumnName(self)
            else:
                return visitor.visitChildren(self)




    def columnName(self):

        localctx = MyParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_columnName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            _la = self._input.LA(1)
            if not(_la==9 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DataTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def NUMBER(self):
            return self.getToken(MyParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_dataType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDataType" ):
                listener.enterDataType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDataType" ):
                listener.exitDataType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDataType" ):
                return visitor.visitDataType(self)
            else:
                return visitor.visitChildren(self)




    def dataType(self):

        localctx = MyParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_dataType)
        try:
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 147
                self.match(MyParser.KEYWORD)
                self.state = 151
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
                if la_ == 1:
                    self.state = 148
                    self.match(MyParser.PUNCTUATION)
                    self.state = 149
                    self.match(MyParser.NUMBER)
                    self.state = 150
                    self.match(MyParser.PUNCTUATION)


                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.match(MyParser.IDENTIFIER)
                self.state = 157
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                if la_ == 1:
                    self.state = 154
                    self.match(MyParser.PUNCTUATION)
                    self.state = 155
                    self.match(MyParser.NUMBER)
                    self.state = 156
                    self.match(MyParser.PUNCTUATION)


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


    class ColumnConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def getRuleIndex(self):
            return MyParser.RULE_columnConstraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnConstraint" ):
                listener.enterColumnConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnConstraint" ):
                listener.exitColumnConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnConstraint" ):
                return visitor.visitColumnConstraint(self)
            else:
                return visitor.visitChildren(self)




    def columnConstraint(self):

        localctx = MyParser.ColumnConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_columnConstraint)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(MyParser.KEYWORD)
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 162
                self.match(MyParser.KEYWORD)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AlterTableStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def addColumnClause(self):
            return self.getTypedRuleContext(MyParser.AddColumnClauseContext,0)


        def dropConstraintClause(self):
            return self.getTypedRuleContext(MyParser.DropConstraintClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_alterTableStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAlterTableStatement" ):
                listener.enterAlterTableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAlterTableStatement" ):
                listener.exitAlterTableStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAlterTableStatement" ):
                return visitor.visitAlterTableStatement(self)
            else:
                return visitor.visitChildren(self)




    def alterTableStatement(self):

        localctx = MyParser.AlterTableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_alterTableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(MyParser.KEYWORD)
            self.state = 166
            self.match(MyParser.KEYWORD)
            self.state = 167
            self.tableName()
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 168
                self.addColumnClause()
                pass

            elif la_ == 2:
                self.state = 169
                self.dropConstraintClause()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddColumnClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def columnDefinition(self):
            return self.getTypedRuleContext(MyParser.ColumnDefinitionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_addColumnClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddColumnClause" ):
                listener.enterAddColumnClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddColumnClause" ):
                listener.exitAddColumnClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddColumnClause" ):
                return visitor.visitAddColumnClause(self)
            else:
                return visitor.visitChildren(self)




    def addColumnClause(self):

        localctx = MyParser.AddColumnClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_addColumnClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(MyParser.KEYWORD)
            self.state = 173
            self.columnDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeleteStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def fromClause(self):
            return self.getTypedRuleContext(MyParser.FromClauseContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(MyParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_deleteStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeleteStatement" ):
                listener.enterDeleteStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeleteStatement" ):
                listener.exitDeleteStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeleteStatement" ):
                return visitor.visitDeleteStatement(self)
            else:
                return visitor.visitChildren(self)




    def deleteStatement(self):

        localctx = MyParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_deleteStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(MyParser.KEYWORD)
            self.state = 178
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9, 11]:
                self.state = 176
                self.tableName()
                pass
            elif token in [1]:
                self.state = 177
                self.fromClause()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 181
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 180
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropConstraintClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def constraintName(self):
            return self.getTypedRuleContext(MyParser.ConstraintNameContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_dropConstraintClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropConstraintClause" ):
                listener.enterDropConstraintClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropConstraintClause" ):
                listener.exitDropConstraintClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropConstraintClause" ):
                return visitor.visitDropConstraintClause(self)
            else:
                return visitor.visitChildren(self)




    def dropConstraintClause(self):

        localctx = MyParser.DropConstraintClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dropConstraintClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self.match(MyParser.KEYWORD)
            self.state = 184
            self.match(MyParser.KEYWORD)
            self.state = 185
            self.constraintName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintNameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(MyParser.BRACKET_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_constraintName

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraintName" ):
                listener.enterConstraintName(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraintName" ):
                listener.exitConstraintName(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraintName" ):
                return visitor.visitConstraintName(self)
            else:
                return visitor.visitChildren(self)




    def constraintName(self):

        localctx = MyParser.ConstraintNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_constraintName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            _la = self._input.LA(1)
            if not(_la==9 or _la==11):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def assignmentList(self):
            return self.getTypedRuleContext(MyParser.AssignmentListContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(MyParser.WhereClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_updateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUpdateStatement" ):
                listener.enterUpdateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUpdateStatement" ):
                listener.exitUpdateStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdateStatement" ):
                return visitor.visitUpdateStatement(self)
            else:
                return visitor.visitChildren(self)




    def updateStatement(self):

        localctx = MyParser.UpdateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_updateStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MyParser.KEYWORD)
            self.state = 190
            self.tableName()
            self.state = 191
            self.match(MyParser.KEYWORD)
            self.state = 192
            self.assignmentList()
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 193
                self.whereClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(MyParser.AssignmentContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_assignmentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentList" ):
                listener.enterAssignmentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentList" ):
                listener.exitAssignmentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentList" ):
                return visitor.visitAssignmentList(self)
            else:
                return visitor.visitChildren(self)




    def assignmentList(self):

        localctx = MyParser.AssignmentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_assignmentList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.assignment()
            self.state = 201
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,15,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 197
                    self.match(MyParser.PUNCTUATION)
                    self.state = 198
                    self.assignment() 
                self.state = 203
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MyParser.ColumnNameContext,0)


        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MyParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.columnName()
            self.state = 205
            self.match(MyParser.OPERATOR)
            self.state = 206
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhereClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def condition(self):
            return self.getTypedRuleContext(MyParser.ConditionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_whereClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhereClause" ):
                listener.enterWhereClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhereClause" ):
                listener.exitWhereClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhereClause" ):
                return visitor.visitWhereClause(self)
            else:
                return visitor.visitChildren(self)




    def whereClause(self):

        localctx = MyParser.WhereClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_whereClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(MyParser.KEYWORD)
            self.state = 209
            self.condition(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryCatchStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.StatementListContext)
            else:
                return self.getTypedRuleContext(MyParser.StatementListContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_tryCatchStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryCatchStatement" ):
                listener.enterTryCatchStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryCatchStatement" ):
                listener.exitTryCatchStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTryCatchStatement" ):
                return visitor.visitTryCatchStatement(self)
            else:
                return visitor.visitChildren(self)




    def tryCatchStatement(self):

        localctx = MyParser.TryCatchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_tryCatchStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(MyParser.KEYWORD)
            self.state = 212
            self.match(MyParser.KEYWORD)
            self.state = 213
            self.statementList()
            self.state = 214
            self.match(MyParser.KEYWORD)
            self.state = 215
            self.match(MyParser.KEYWORD)
            self.state = 216
            self.match(MyParser.KEYWORD)
            self.state = 217
            self.match(MyParser.KEYWORD)
            self.state = 218
            self.statementList()
            self.state = 219
            self.match(MyParser.KEYWORD)
            self.state = 220
            self.match(MyParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def selectStatement(self):
            return self.getTypedRuleContext(MyParser.SelectStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(MyParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MyParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            self.match(MyParser.KEYWORD)
            self.state = 223
            self.match(MyParser.KEYWORD)
            self.state = 225
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 224
                self.match(MyParser.KEYWORD)


            self.state = 227
            self.match(MyParser.PUNCTUATION)
            self.state = 228
            self.selectStatement()
            self.state = 229
            self.match(MyParser.PUNCTUATION)
            self.state = 230
            self.blockStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def statementList(self):
            return self.getTypedRuleContext(MyParser.StatementListContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_blockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlockStatement" ):
                listener.enterBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlockStatement" ):
                listener.exitBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlockStatement" ):
                return visitor.visitBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def blockStatement(self):

        localctx = MyParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_blockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(MyParser.KEYWORD)
            self.state = 233
            self.statementList()
            self.state = 234
            self.match(MyParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclareStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def VARIABLE(self):
            return self.getToken(MyParser.VARIABLE, 0)

        def dataType(self):
            return self.getTypedRuleContext(MyParser.DataTypeContext,0)


        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_declareStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclareStatement" ):
                listener.enterDeclareStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclareStatement" ):
                listener.exitDeclareStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclareStatement" ):
                return visitor.visitDeclareStatement(self)
            else:
                return visitor.visitChildren(self)




    def declareStatement(self):

        localctx = MyParser.DeclareStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_declareStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(MyParser.KEYWORD)
            self.state = 237
            self.match(MyParser.VARIABLE)
            self.state = 238
            self.dataType()
            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 239
                self.match(MyParser.OPERATOR)
                self.state = 240
                self.expression(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SetStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def VARIABLE(self):
            return self.getToken(MyParser.VARIABLE, 0)

        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_setStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSetStatement" ):
                listener.enterSetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSetStatement" ):
                listener.exitSetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSetStatement" ):
                return visitor.visitSetStatement(self)
            else:
                return visitor.visitChildren(self)




    def setStatement(self):

        localctx = MyParser.SetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_setStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(MyParser.KEYWORD)
            self.state = 244
            self.match(MyParser.VARIABLE)
            self.state = 245
            self.match(MyParser.OPERATOR)
            self.state = 246
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExecStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def expressionList(self):
            return self.getTypedRuleContext(MyParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_execStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExecStatement" ):
                listener.enterExecStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExecStatement" ):
                listener.exitExecStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExecStatement" ):
                return visitor.visitExecStatement(self)
            else:
                return visitor.visitChildren(self)




    def execStatement(self):

        localctx = MyParser.ExecStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_execStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(MyParser.KEYWORD)
            self.state = 249
            self.match(MyParser.IDENTIFIER)
            self.state = 251
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.state = 250
                self.expressionList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def selectList(self):
            return self.getTypedRuleContext(MyParser.SelectListContext,0)


        def fromClause(self):
            return self.getTypedRuleContext(MyParser.FromClauseContext,0)


        def whereClause(self):
            return self.getTypedRuleContext(MyParser.WhereClauseContext,0)


        def orderByClause(self):
            return self.getTypedRuleContext(MyParser.OrderByClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_selectStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectStatement" ):
                listener.enterSelectStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectStatement" ):
                listener.exitSelectStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectStatement" ):
                return visitor.visitSelectStatement(self)
            else:
                return visitor.visitChildren(self)




    def selectStatement(self):

        localctx = MyParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_selectStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(MyParser.KEYWORD)
            self.state = 254
            self.selectList()
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 255
                self.fromClause()


            self.state = 259
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 258
                self.whereClause()


            self.state = 262
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 261
                self.orderByClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def orderByItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.OrderByItemContext)
            else:
                return self.getTypedRuleContext(MyParser.OrderByItemContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_orderByClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByClause" ):
                listener.enterOrderByClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByClause" ):
                listener.exitOrderByClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByClause" ):
                return visitor.visitOrderByClause(self)
            else:
                return visitor.visitChildren(self)




    def orderByClause(self):

        localctx = MyParser.OrderByClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_orderByClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(MyParser.KEYWORD)
            self.state = 265
            self.match(MyParser.KEYWORD)
            self.state = 266
            self.orderByItem()
            self.state = 271
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 267
                    self.match(MyParser.PUNCTUATION)
                    self.state = 268
                    self.orderByItem() 
                self.state = 273
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 274
                self.match(MyParser.KEYWORD)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_orderByItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByItem" ):
                listener.enterOrderByItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByItem" ):
                listener.exitOrderByItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByItem" ):
                return visitor.visitOrderByItem(self)
            else:
                return visitor.visitChildren(self)




    def orderByItem(self):

        localctx = MyParser.OrderByItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_orderByItem)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 277
                self.match(MyParser.IDENTIFIER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 278
                self.expression(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.SelectItemContext)
            else:
                return self.getTypedRuleContext(MyParser.SelectItemContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_selectList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectList" ):
                listener.enterSelectList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectList" ):
                listener.exitSelectList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectList" ):
                return visitor.visitSelectList(self)
            else:
                return visitor.visitChildren(self)




    def selectList(self):

        localctx = MyParser.SelectListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_selectList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.selectItem()
            self.state = 286
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 282
                    self.match(MyParser.PUNCTUATION)
                    self.state = 283
                    self.selectItem() 
                self.state = 288
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectItemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def getRuleIndex(self):
            return MyParser.RULE_selectItem

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelectItem" ):
                listener.enterSelectItem(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelectItem" ):
                listener.exitSelectItem(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelectItem" ):
                return visitor.visitSelectItem(self)
            else:
                return visitor.visitChildren(self)




    def selectItem(self):

        localctx = MyParser.SelectItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_selectItem)
        self._la = 0 # Token type
        try:
            self.state = 297
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 5, 6, 9, 10, 11, 12, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 289
                self.expression(0)
                self.state = 294
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 291
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==1:
                        self.state = 290
                        self.match(MyParser.KEYWORD)


                    self.state = 293
                    self.match(MyParser.IDENTIFIER)


                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 2)
                self.state = 296
                self.match(MyParser.OPERATOR)
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


    class FromClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def tableSource(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.TableSourceContext)
            else:
                return self.getTypedRuleContext(MyParser.TableSourceContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_fromClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFromClause" ):
                listener.enterFromClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFromClause" ):
                listener.exitFromClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFromClause" ):
                return visitor.visitFromClause(self)
            else:
                return visitor.visitChildren(self)




    def fromClause(self):

        localctx = MyParser.FromClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_fromClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            self.match(MyParser.KEYWORD)
            self.state = 300
            self.tableSource()
            self.state = 305
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 301
                    self.match(MyParser.PUNCTUATION)
                    self.state = 302
                    self.tableSource() 
                self.state = 307
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableSourceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_tableSource

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableSource" ):
                listener.enterTableSource(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableSource" ):
                listener.exitTableSource(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableSource" ):
                return visitor.visitTableSource(self)
            else:
                return visitor.visitChildren(self)




    def tableSource(self):

        localctx = MyParser.TableSourceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_tableSource)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.tableName()
            self.state = 313
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 309
                    self.match(MyParser.KEYWORD)


                self.state = 312
                self.match(MyParser.IDENTIFIER)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MyParser.LiteralContext,0)


        def columnReference(self):
            return self.getTypedRuleContext(MyParser.ColumnReferenceContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(MyParser.FunctionCallContext,0)


        def caseExpression(self):
            return self.getTypedRuleContext(MyParser.CaseExpressionContext,0)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def VARIABLE(self):
            return self.getToken(MyParser.VARIABLE, 0)

        def STRING_SINGLE(self):
            return self.getToken(MyParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(MyParser.STRING_DOUBLE, 0)

        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 66
        self.enterRecursionRule(localctx, 66, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 316
                self.literal()
                pass

            elif la_ == 2:
                self.state = 317
                self.columnReference()
                pass

            elif la_ == 3:
                self.state = 318
                self.functionCall()
                pass

            elif la_ == 4:
                self.state = 319
                self.caseExpression()
                pass

            elif la_ == 5:
                self.state = 320
                self.match(MyParser.PUNCTUATION)
                self.state = 321
                self.expression(0)
                self.state = 322
                self.match(MyParser.PUNCTUATION)
                pass

            elif la_ == 6:
                self.state = 324
                self.match(MyParser.VARIABLE)
                pass

            elif la_ == 7:
                self.state = 325
                self.match(MyParser.STRING_SINGLE)
                pass

            elif la_ == 8:
                self.state = 326
                self.match(MyParser.STRING_DOUBLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 337
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 335
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
                    if la_ == 1:
                        localctx = MyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 329
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 330
                        self.match(MyParser.OPERATOR)
                        self.state = 331
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = MyParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 332
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 333
                        self.match(MyParser.KEYWORD)
                        self.state = 334
                        self.expression(5)
                        pass

             
                self.state = 339
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def getRuleIndex(self):
            return MyParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = MyParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_expressionList)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 340
            self.expression(0)
            self.state = 345
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,35,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 341
                    self.match(MyParser.PUNCTUATION)
                    self.state = 342
                    self.expression(0) 
                self.state = 347
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,35,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CaseExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def whenClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.WhenClauseContext)
            else:
                return self.getTypedRuleContext(MyParser.WhenClauseContext,i)


        def elseClause(self):
            return self.getTypedRuleContext(MyParser.ElseClauseContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_caseExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCaseExpression" ):
                listener.enterCaseExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCaseExpression" ):
                listener.exitCaseExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCaseExpression" ):
                return visitor.visitCaseExpression(self)
            else:
                return visitor.visitChildren(self)




    def caseExpression(self):

        localctx = MyParser.CaseExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_caseExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.match(MyParser.KEYWORD)
            self.state = 350 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 349
                    self.whenClause()

                else:
                    raise NoViableAltException(self)
                self.state = 352 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.state = 354
                self.elseClause()


            self.state = 357
            self.match(MyParser.KEYWORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhenClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def condition(self):
            return self.getTypedRuleContext(MyParser.ConditionContext,0)


        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_whenClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenClause" ):
                listener.enterWhenClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenClause" ):
                listener.exitWhenClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhenClause" ):
                return visitor.visitWhenClause(self)
            else:
                return visitor.visitChildren(self)




    def whenClause(self):

        localctx = MyParser.WhenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_whenClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 359
            self.match(MyParser.KEYWORD)
            self.state = 360
            self.condition(0)
            self.state = 361
            self.match(MyParser.KEYWORD)
            self.state = 362
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def expression(self):
            return self.getTypedRuleContext(MyParser.ExpressionContext,0)


        def getRuleIndex(self):
            return MyParser.RULE_elseClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseClause" ):
                listener.enterElseClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseClause" ):
                listener.exitElseClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseClause" ):
                return visitor.visitElseClause(self)
            else:
                return visitor.visitChildren(self)




    def elseClause(self):

        localctx = MyParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.match(MyParser.KEYWORD)
            self.state = 365
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(MyParser.ExpressionContext,i)


        def OPERATOR(self):
            return self.getToken(MyParser.OPERATOR, 0)

        def KEYWORD(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.KEYWORD)
            else:
                return self.getToken(MyParser.KEYWORD, i)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def expressionList(self):
            return self.getTypedRuleContext(MyParser.ExpressionListContext,0)


        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MyParser.ConditionContext)
            else:
                return self.getTypedRuleContext(MyParser.ConditionContext,i)


        def getRuleIndex(self):
            return MyParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)



    def condition(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MyParser.ConditionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_condition, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 389
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 368
                self.expression(0)
                self.state = 369
                _la = self._input.LA(1)
                if not(_la==1 or _la==13):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 370
                self.expression(0)
                pass

            elif la_ == 2:
                self.state = 372
                self.expression(0)
                self.state = 374
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
                if la_ == 1:
                    self.state = 373
                    self.match(MyParser.KEYWORD)


                self.state = 376
                self.match(MyParser.KEYWORD)
                self.state = 377
                self.match(MyParser.PUNCTUATION)
                self.state = 378
                self.expressionList()
                self.state = 379
                self.match(MyParser.PUNCTUATION)
                pass

            elif la_ == 3:
                self.state = 381
                self.expression(0)
                self.state = 382
                self.match(MyParser.KEYWORD)
                self.state = 383
                self.match(MyParser.KEYWORD)
                pass

            elif la_ == 4:
                self.state = 385
                self.match(MyParser.PUNCTUATION)
                self.state = 386
                self.condition(0)
                self.state = 387
                self.match(MyParser.PUNCTUATION)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 396
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MyParser.ConditionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_condition)
                    self.state = 391
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 392
                    self.match(MyParser.KEYWORD)
                    self.state = 393
                    self.condition(2) 
                self.state = 398
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ColumnReferenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self):
            return self.getTypedRuleContext(MyParser.ColumnNameContext,0)


        def tableName(self):
            return self.getTypedRuleContext(MyParser.TableNameContext,0)


        def PUNCTUATION(self):
            return self.getToken(MyParser.PUNCTUATION, 0)

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(MyParser.BRACKET_IDENTIFIER, 0)

        def getRuleIndex(self):
            return MyParser.RULE_columnReference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnReference" ):
                listener.enterColumnReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnReference" ):
                listener.exitColumnReference(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnReference" ):
                return visitor.visitColumnReference(self)
            else:
                return visitor.visitChildren(self)




    def columnReference(self):

        localctx = MyParser.ColumnReferenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_columnReference)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,42,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
                if la_ == 1:
                    self.state = 399
                    self.tableName()
                    self.state = 400
                    self.match(MyParser.PUNCTUATION)


                self.state = 404
                self.columnName()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.match(MyParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
                self.match(MyParser.BRACKET_IDENTIFIER)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(MyParser.IDENTIFIER, 0)

        def PUNCTUATION(self, i:int=None):
            if i is None:
                return self.getTokens(MyParser.PUNCTUATION)
            else:
                return self.getToken(MyParser.PUNCTUATION, i)

        def expressionList(self):
            return self.getTypedRuleContext(MyParser.ExpressionListContext,0)


        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = MyParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_functionCall)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11]:
                self.enterOuterAlt(localctx, 1)
                self.state = 409
                self.match(MyParser.IDENTIFIER)
                self.state = 410
                self.match(MyParser.PUNCTUATION)
                self.state = 412
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
                if la_ == 1:
                    self.state = 411
                    self.expressionList()


                self.state = 414
                self.match(MyParser.PUNCTUATION)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 415
                self.match(MyParser.KEYWORD)
                self.state = 416
                self.match(MyParser.PUNCTUATION)
                self.state = 418
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
                if la_ == 1:
                    self.state = 417
                    self.expressionList()


                self.state = 420
                self.match(MyParser.PUNCTUATION)
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(MyParser.NUMBER, 0)

        def STRING_SINGLE(self):
            return self.getToken(MyParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(MyParser.STRING_DOUBLE, 0)

        def KEYWORD(self):
            return self.getToken(MyParser.KEYWORD, 0)

        def getRuleIndex(self):
            return MyParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MyParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4194) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[33] = self.expression_sempred
        self._predicates[38] = self.condition_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

    def condition_sempred(self, localctx:ConditionContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 1)
         




