# Generated from grammars/StatementParser.g4 by ANTLR 4.13.2
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
        4,1,279,574,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,
        52,2,53,7,53,2,54,7,54,1,0,5,0,112,8,0,10,0,12,0,115,9,0,1,1,1,1,
        4,1,119,8,1,11,1,12,1,120,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,131,
        8,2,1,3,1,3,3,3,135,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        5,5,147,8,5,10,5,12,5,150,9,5,1,6,1,6,1,6,5,6,155,8,6,10,6,12,6,
        158,9,6,1,7,1,7,1,7,1,7,1,7,3,7,165,8,7,1,7,3,7,168,8,7,1,8,1,8,
        1,8,3,8,173,8,8,1,8,1,8,5,8,177,8,8,10,8,12,8,180,9,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,3,9,190,8,9,1,9,1,9,1,9,1,9,3,9,196,8,9,1,
        9,1,9,1,9,4,9,201,8,9,11,9,12,9,202,1,10,1,10,1,10,1,10,1,10,3,10,
        210,8,10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,
        1,14,1,14,1,14,1,14,3,14,227,8,14,1,15,1,15,1,15,1,15,3,15,233,8,
        15,1,15,1,15,3,15,237,8,15,1,15,1,15,1,15,3,15,242,8,15,1,15,1,15,
        3,15,246,8,15,1,15,1,15,1,15,3,15,251,8,15,1,16,1,16,1,16,5,16,256,
        8,16,10,16,12,16,259,9,16,1,17,1,17,3,17,263,8,17,1,18,1,18,1,18,
        5,18,268,8,18,10,18,12,18,271,9,18,1,19,1,19,3,19,275,8,19,1,19,
        3,19,278,8,19,1,19,1,19,3,19,282,8,19,3,19,284,8,19,1,20,1,20,5,
        20,288,8,20,10,20,12,20,291,9,20,1,21,3,21,294,8,21,1,21,1,21,1,
        21,1,21,1,21,1,22,1,22,1,22,3,22,304,8,22,1,22,1,22,3,22,308,8,22,
        1,22,1,22,3,22,312,8,22,3,22,314,8,22,1,23,1,23,3,23,318,8,23,1,
        23,3,23,321,8,23,1,23,1,23,1,23,1,23,3,23,327,8,23,1,23,1,23,3,23,
        331,8,23,1,24,1,24,3,24,335,8,24,1,24,1,24,1,24,1,24,1,24,3,24,342,
        8,24,1,24,1,24,3,24,346,8,24,1,25,1,25,1,25,5,25,351,8,25,10,25,
        12,25,354,9,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        5,26,366,8,26,10,26,12,26,369,9,26,1,27,1,27,1,27,1,27,1,27,1,27,
        3,27,377,8,27,1,28,1,28,1,28,5,28,382,8,28,10,28,12,28,385,9,28,
        1,29,1,29,1,29,1,29,1,30,1,30,3,30,393,8,30,1,30,1,30,1,30,3,30,
        398,8,30,1,31,1,31,1,31,3,31,403,8,31,1,32,1,32,1,32,1,32,1,32,1,
        32,1,32,1,32,3,32,413,8,32,1,32,1,32,1,32,3,32,418,8,32,1,33,1,33,
        3,33,422,8,33,1,34,1,34,3,34,426,8,34,1,35,1,35,1,35,5,35,431,8,
        35,10,35,12,35,434,9,35,1,35,1,35,1,36,1,36,1,36,5,36,441,8,36,10,
        36,12,36,444,9,36,1,36,1,36,1,36,1,36,1,36,5,36,451,8,36,10,36,12,
        36,454,9,36,1,36,1,36,1,36,1,37,1,37,3,37,461,8,37,1,38,1,38,1,38,
        1,38,1,38,3,38,468,8,38,1,39,1,39,1,39,3,39,473,8,39,1,39,1,39,1,
        39,1,40,1,40,1,40,3,40,481,8,40,1,40,3,40,484,8,40,1,41,1,41,1,41,
        1,41,5,41,490,8,41,10,41,12,41,493,9,41,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,1,42,3,42,504,8,42,1,42,1,42,1,42,1,42,3,42,510,8,
        42,1,43,1,43,1,44,1,44,1,44,5,44,517,8,44,10,44,12,44,520,9,44,1,
        45,1,45,1,46,1,46,1,46,1,46,3,46,528,8,46,1,47,1,47,1,48,1,48,1,
        48,3,48,535,8,48,1,48,1,48,3,48,539,8,48,1,48,1,48,1,49,1,49,4,49,
        545,8,49,11,49,12,49,546,1,49,3,49,550,8,49,1,49,1,49,1,50,1,50,
        1,50,1,50,1,50,1,51,1,51,1,51,1,52,1,52,1,53,1,53,1,53,5,53,567,
        8,53,10,53,12,53,570,9,53,1,54,1,54,1,54,0,0,55,0,2,4,6,8,10,12,
        14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,
        58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,
        102,104,106,108,0,6,2,0,21,21,100,100,2,0,24,24,27,27,2,0,7,7,48,
        48,8,0,4,4,11,11,83,83,89,89,94,94,101,101,114,114,279,279,3,0,102,
        102,273,274,278,278,3,0,1,12,14,28,30,264,617,0,113,1,0,0,0,2,118,
        1,0,0,0,4,130,1,0,0,0,6,134,1,0,0,0,8,136,1,0,0,0,10,143,1,0,0,0,
        12,151,1,0,0,0,14,164,1,0,0,0,16,169,1,0,0,0,18,200,1,0,0,0,20,204,
        1,0,0,0,22,211,1,0,0,0,24,214,1,0,0,0,26,218,1,0,0,0,28,226,1,0,
        0,0,30,228,1,0,0,0,32,252,1,0,0,0,34,260,1,0,0,0,36,264,1,0,0,0,
        38,274,1,0,0,0,40,285,1,0,0,0,42,293,1,0,0,0,44,313,1,0,0,0,46,330,
        1,0,0,0,48,332,1,0,0,0,50,347,1,0,0,0,52,355,1,0,0,0,54,370,1,0,
        0,0,56,378,1,0,0,0,58,386,1,0,0,0,60,390,1,0,0,0,62,402,1,0,0,0,
        64,404,1,0,0,0,66,421,1,0,0,0,68,425,1,0,0,0,70,427,1,0,0,0,72,437,
        1,0,0,0,74,460,1,0,0,0,76,462,1,0,0,0,78,469,1,0,0,0,80,477,1,0,
        0,0,82,485,1,0,0,0,84,509,1,0,0,0,86,511,1,0,0,0,88,513,1,0,0,0,
        90,521,1,0,0,0,92,527,1,0,0,0,94,529,1,0,0,0,96,534,1,0,0,0,98,542,
        1,0,0,0,100,553,1,0,0,0,102,558,1,0,0,0,104,561,1,0,0,0,106,563,
        1,0,0,0,108,571,1,0,0,0,110,112,3,2,1,0,111,110,1,0,0,0,112,115,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,1,1,0,0,0,115,113,1,
        0,0,0,116,119,3,4,2,0,117,119,5,235,0,0,118,116,1,0,0,0,118,117,
        1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,3,1,
        0,0,0,122,131,3,6,3,0,123,131,3,28,14,0,124,131,3,62,31,0,125,131,
        3,74,37,0,126,131,3,80,40,0,127,131,3,26,13,0,128,131,3,70,35,0,
        129,131,5,267,0,0,130,122,1,0,0,0,130,123,1,0,0,0,130,124,1,0,0,
        0,130,125,1,0,0,0,130,126,1,0,0,0,130,127,1,0,0,0,130,128,1,0,0,
        0,130,129,1,0,0,0,131,5,1,0,0,0,132,135,3,8,4,0,133,135,3,20,10,
        0,134,132,1,0,0,0,134,133,1,0,0,0,135,7,1,0,0,0,136,137,5,33,0,0,
        137,138,5,151,0,0,138,139,3,106,53,0,139,140,5,268,0,0,140,141,3,
        10,5,0,141,142,5,269,0,0,142,9,1,0,0,0,143,148,3,12,6,0,144,145,
        5,266,0,0,145,147,3,12,6,0,146,144,1,0,0,0,147,150,1,0,0,0,148,146,
        1,0,0,0,148,149,1,0,0,0,149,11,1,0,0,0,150,148,1,0,0,0,151,152,3,
        108,54,0,152,156,3,14,7,0,153,155,3,18,9,0,154,153,1,0,0,0,155,158,
        1,0,0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,13,1,0,0,0,158,156,1,
        0,0,0,159,165,5,178,0,0,160,165,5,237,0,0,161,165,5,179,0,0,162,
        165,5,194,0,0,163,165,3,92,46,0,164,159,1,0,0,0,164,160,1,0,0,0,
        164,161,1,0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,167,1,0,0,0,
        166,168,3,16,8,0,167,166,1,0,0,0,167,168,1,0,0,0,168,15,1,0,0,0,
        169,172,5,268,0,0,170,173,5,278,0,0,171,173,3,92,46,0,172,170,1,
        0,0,0,172,171,1,0,0,0,173,178,1,0,0,0,174,175,5,266,0,0,175,177,
        5,278,0,0,176,174,1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,
        1,0,0,0,179,181,1,0,0,0,180,178,1,0,0,0,181,182,5,269,0,0,182,17,
        1,0,0,0,183,184,5,101,0,0,184,201,5,102,0,0,185,201,5,102,0,0,186,
        187,5,121,0,0,187,189,5,91,0,0,188,190,7,0,0,0,189,188,1,0,0,0,189,
        190,1,0,0,0,190,195,1,0,0,0,191,192,5,268,0,0,192,193,3,50,25,0,
        193,194,5,269,0,0,194,196,1,0,0,0,195,191,1,0,0,0,195,196,1,0,0,
        0,196,201,1,0,0,0,197,198,5,45,0,0,198,201,3,82,41,0,199,201,3,92,
        46,0,200,183,1,0,0,0,200,185,1,0,0,0,200,186,1,0,0,0,200,197,1,0,
        0,0,200,199,1,0,0,0,201,202,1,0,0,0,202,200,1,0,0,0,202,203,1,0,
        0,0,203,19,1,0,0,0,204,205,5,3,0,0,205,206,5,151,0,0,206,209,3,106,
        53,0,207,210,3,22,11,0,208,210,3,24,12,0,209,207,1,0,0,0,209,208,
        1,0,0,0,210,21,1,0,0,0,211,212,5,1,0,0,212,213,3,12,6,0,213,23,1,
        0,0,0,214,215,5,52,0,0,215,216,7,1,0,0,216,217,3,92,46,0,217,25,
        1,0,0,0,218,219,5,160,0,0,219,220,5,151,0,0,220,221,3,106,53,0,221,
        27,1,0,0,0,222,227,3,30,15,0,223,227,3,48,24,0,224,227,3,54,27,0,
        225,227,3,60,30,0,226,222,1,0,0,0,226,223,1,0,0,0,226,224,1,0,0,
        0,226,225,1,0,0,0,227,29,1,0,0,0,228,229,5,224,0,0,229,232,3,36,
        18,0,230,231,5,71,0,0,231,233,3,40,20,0,232,230,1,0,0,0,232,233,
        1,0,0,0,233,236,1,0,0,0,234,235,5,174,0,0,235,237,3,104,52,0,236,
        234,1,0,0,0,236,237,1,0,0,0,237,241,1,0,0,0,238,239,5,76,0,0,239,
        240,5,15,0,0,240,242,3,88,44,0,241,238,1,0,0,0,241,242,1,0,0,0,242,
        245,1,0,0,0,243,244,5,77,0,0,244,246,3,104,52,0,245,243,1,0,0,0,
        245,246,1,0,0,0,246,250,1,0,0,0,247,248,5,115,0,0,248,249,5,15,0,
        0,249,251,3,32,16,0,250,247,1,0,0,0,250,251,1,0,0,0,251,31,1,0,0,
        0,252,257,3,34,17,0,253,254,5,266,0,0,254,256,3,34,17,0,255,253,
        1,0,0,0,256,259,1,0,0,0,257,255,1,0,0,0,257,258,1,0,0,0,258,33,1,
        0,0,0,259,257,1,0,0,0,260,262,3,82,41,0,261,263,7,2,0,0,262,261,
        1,0,0,0,262,263,1,0,0,0,263,35,1,0,0,0,264,269,3,38,19,0,265,266,
        5,266,0,0,266,268,3,38,19,0,267,265,1,0,0,0,268,271,1,0,0,0,269,
        267,1,0,0,0,269,270,1,0,0,0,270,37,1,0,0,0,271,269,1,0,0,0,272,275,
        5,279,0,0,273,275,3,82,41,0,274,272,1,0,0,0,274,273,1,0,0,0,275,
        283,1,0,0,0,276,278,5,6,0,0,277,276,1,0,0,0,277,278,1,0,0,0,278,
        281,1,0,0,0,279,282,3,108,54,0,280,282,3,90,45,0,281,279,1,0,0,0,
        281,280,1,0,0,0,282,284,1,0,0,0,283,277,1,0,0,0,283,284,1,0,0,0,
        284,39,1,0,0,0,285,289,3,46,23,0,286,288,3,42,21,0,287,286,1,0,0,
        0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,1,0,0,0,290,41,1,0,0,0,
        291,289,1,0,0,0,292,294,3,44,22,0,293,292,1,0,0,0,293,294,1,0,0,
        0,294,295,1,0,0,0,295,296,5,90,0,0,296,297,3,46,23,0,297,298,5,107,
        0,0,298,299,3,104,52,0,299,43,1,0,0,0,300,314,5,85,0,0,301,303,5,
        93,0,0,302,304,5,116,0,0,303,302,1,0,0,0,303,304,1,0,0,0,304,314,
        1,0,0,0,305,307,5,137,0,0,306,308,5,116,0,0,307,306,1,0,0,0,307,
        308,1,0,0,0,308,314,1,0,0,0,309,311,5,72,0,0,310,312,5,116,0,0,311,
        310,1,0,0,0,311,312,1,0,0,0,312,314,1,0,0,0,313,300,1,0,0,0,313,
        301,1,0,0,0,313,305,1,0,0,0,313,309,1,0,0,0,314,45,1,0,0,0,315,320,
        3,106,53,0,316,318,5,6,0,0,317,316,1,0,0,0,317,318,1,0,0,0,318,319,
        1,0,0,0,319,321,3,92,46,0,320,317,1,0,0,0,320,321,1,0,0,0,321,331,
        1,0,0,0,322,323,5,268,0,0,323,324,3,30,15,0,324,326,5,269,0,0,325,
        327,5,6,0,0,326,325,1,0,0,0,326,327,1,0,0,0,327,328,1,0,0,0,328,
        329,3,92,46,0,329,331,1,0,0,0,330,315,1,0,0,0,330,322,1,0,0,0,331,
        47,1,0,0,0,332,334,5,86,0,0,333,335,5,88,0,0,334,333,1,0,0,0,334,
        335,1,0,0,0,335,336,1,0,0,0,336,341,3,106,53,0,337,338,5,268,0,0,
        338,339,3,50,25,0,339,340,5,269,0,0,340,342,1,0,0,0,341,337,1,0,
        0,0,341,342,1,0,0,0,342,345,1,0,0,0,343,346,3,52,26,0,344,346,3,
        30,15,0,345,343,1,0,0,0,345,344,1,0,0,0,346,49,1,0,0,0,347,352,3,
        108,54,0,348,349,5,266,0,0,349,351,3,108,54,0,350,348,1,0,0,0,351,
        354,1,0,0,0,352,350,1,0,0,0,352,353,1,0,0,0,353,51,1,0,0,0,354,352,
        1,0,0,0,355,356,5,169,0,0,356,357,5,268,0,0,357,358,3,88,44,0,358,
        359,5,269,0,0,359,367,1,0,0,0,360,361,5,266,0,0,361,362,5,268,0,
        0,362,363,3,88,44,0,363,364,5,269,0,0,364,366,1,0,0,0,365,360,1,
        0,0,0,366,369,1,0,0,0,367,365,1,0,0,0,367,368,1,0,0,0,368,53,1,0,
        0,0,369,367,1,0,0,0,370,371,5,165,0,0,371,372,3,106,53,0,372,373,
        5,145,0,0,373,376,3,56,28,0,374,375,5,174,0,0,375,377,3,104,52,0,
        376,374,1,0,0,0,376,377,1,0,0,0,377,55,1,0,0,0,378,383,3,58,29,0,
        379,380,5,266,0,0,380,382,3,58,29,0,381,379,1,0,0,0,382,385,1,0,
        0,0,383,381,1,0,0,0,383,384,1,0,0,0,384,57,1,0,0,0,385,383,1,0,0,
        0,386,387,3,108,54,0,387,388,5,279,0,0,388,389,3,82,41,0,389,59,
        1,0,0,0,390,392,5,46,0,0,391,393,5,71,0,0,392,391,1,0,0,0,392,393,
        1,0,0,0,393,394,1,0,0,0,394,397,3,106,53,0,395,396,5,174,0,0,396,
        398,3,104,52,0,397,395,1,0,0,0,397,398,1,0,0,0,398,61,1,0,0,0,399,
        403,3,64,32,0,400,403,3,72,36,0,401,403,3,70,35,0,402,399,1,0,0,
        0,402,400,1,0,0,0,402,401,1,0,0,0,403,63,1,0,0,0,404,412,5,82,0,
        0,405,406,5,101,0,0,406,407,5,61,0,0,407,408,5,268,0,0,408,409,3,
        30,15,0,409,410,5,269,0,0,410,413,1,0,0,0,411,413,3,104,52,0,412,
        405,1,0,0,0,412,411,1,0,0,0,412,413,1,0,0,0,413,414,1,0,0,0,414,
        417,3,66,33,0,415,416,5,54,0,0,416,418,3,68,34,0,417,415,1,0,0,0,
        417,418,1,0,0,0,418,65,1,0,0,0,419,422,3,70,35,0,420,422,3,4,2,0,
        421,419,1,0,0,0,421,420,1,0,0,0,422,67,1,0,0,0,423,426,3,70,35,0,
        424,426,3,4,2,0,425,423,1,0,0,0,425,424,1,0,0,0,426,69,1,0,0,0,427,
        432,5,10,0,0,428,431,3,4,2,0,429,431,5,235,0,0,430,428,1,0,0,0,430,
        429,1,0,0,0,431,434,1,0,0,0,432,430,1,0,0,0,432,433,1,0,0,0,433,
        435,1,0,0,0,434,432,1,0,0,0,435,436,5,55,0,0,436,71,1,0,0,0,437,
        438,5,10,0,0,438,442,5,233,0,0,439,441,3,4,2,0,440,439,1,0,0,0,441,
        444,1,0,0,0,442,440,1,0,0,0,442,443,1,0,0,0,443,445,1,0,0,0,444,
        442,1,0,0,0,445,446,5,55,0,0,446,447,5,233,0,0,447,448,5,10,0,0,
        448,452,5,234,0,0,449,451,3,4,2,0,450,449,1,0,0,0,451,454,1,0,0,
        0,452,450,1,0,0,0,452,453,1,0,0,0,453,455,1,0,0,0,454,452,1,0,0,
        0,455,456,5,55,0,0,456,457,5,234,0,0,457,73,1,0,0,0,458,461,3,76,
        38,0,459,461,3,78,39,0,460,458,1,0,0,0,460,459,1,0,0,0,461,75,1,
        0,0,0,462,463,5,44,0,0,463,464,5,276,0,0,464,467,3,14,7,0,465,466,
        5,279,0,0,466,468,3,82,41,0,467,465,1,0,0,0,467,468,1,0,0,0,468,
        77,1,0,0,0,469,472,5,145,0,0,470,473,5,276,0,0,471,473,3,108,54,
        0,472,470,1,0,0,0,472,471,1,0,0,0,473,474,1,0,0,0,474,475,5,279,
        0,0,475,476,3,82,41,0,476,79,1,0,0,0,477,480,5,59,0,0,478,481,3,
        92,46,0,479,481,5,254,0,0,480,478,1,0,0,0,480,479,1,0,0,0,481,483,
        1,0,0,0,482,484,3,88,44,0,483,482,1,0,0,0,483,484,1,0,0,0,484,81,
        1,0,0,0,485,491,3,84,42,0,486,487,3,86,43,0,487,488,3,84,42,0,488,
        490,1,0,0,0,489,486,1,0,0,0,490,493,1,0,0,0,491,489,1,0,0,0,491,
        492,1,0,0,0,492,83,1,0,0,0,493,491,1,0,0,0,494,510,3,90,45,0,495,
        510,3,96,48,0,496,510,3,98,49,0,497,510,3,92,46,0,498,510,5,276,
        0,0,499,503,5,268,0,0,500,504,3,30,15,0,501,504,3,82,41,0,502,504,
        3,88,44,0,503,500,1,0,0,0,503,501,1,0,0,0,503,502,1,0,0,0,504,505,
        1,0,0,0,505,506,5,269,0,0,506,510,1,0,0,0,507,508,5,279,0,0,508,
        510,3,84,42,0,509,494,1,0,0,0,509,495,1,0,0,0,509,496,1,0,0,0,509,
        497,1,0,0,0,509,498,1,0,0,0,509,499,1,0,0,0,509,507,1,0,0,0,510,
        85,1,0,0,0,511,512,7,3,0,0,512,87,1,0,0,0,513,518,3,82,41,0,514,
        515,5,266,0,0,515,517,3,82,41,0,516,514,1,0,0,0,517,520,1,0,0,0,
        518,516,1,0,0,0,518,519,1,0,0,0,519,89,1,0,0,0,520,518,1,0,0,0,521,
        522,7,4,0,0,522,91,1,0,0,0,523,528,5,277,0,0,524,528,5,275,0,0,525,
        528,5,274,0,0,526,528,3,94,47,0,527,523,1,0,0,0,527,524,1,0,0,0,
        527,525,1,0,0,0,527,526,1,0,0,0,528,93,1,0,0,0,529,530,7,5,0,0,530,
        95,1,0,0,0,531,535,5,202,0,0,532,535,5,204,0,0,533,535,3,92,46,0,
        534,531,1,0,0,0,534,532,1,0,0,0,534,533,1,0,0,0,535,536,1,0,0,0,
        536,538,5,268,0,0,537,539,3,88,44,0,538,537,1,0,0,0,538,539,1,0,
        0,0,539,540,1,0,0,0,540,541,5,269,0,0,541,97,1,0,0,0,542,544,5,17,
        0,0,543,545,3,100,50,0,544,543,1,0,0,0,545,546,1,0,0,0,546,544,1,
        0,0,0,546,547,1,0,0,0,547,549,1,0,0,0,548,550,3,102,51,0,549,548,
        1,0,0,0,549,550,1,0,0,0,550,551,1,0,0,0,551,552,5,55,0,0,552,99,
        1,0,0,0,553,554,5,173,0,0,554,555,3,104,52,0,555,556,5,154,0,0,556,
        557,3,82,41,0,557,101,1,0,0,0,558,559,5,54,0,0,559,560,3,82,41,0,
        560,103,1,0,0,0,561,562,3,82,41,0,562,105,1,0,0,0,563,568,3,92,46,
        0,564,565,5,265,0,0,565,567,3,92,46,0,566,564,1,0,0,0,567,570,1,
        0,0,0,568,566,1,0,0,0,568,569,1,0,0,0,569,107,1,0,0,0,570,568,1,
        0,0,0,571,572,3,92,46,0,572,109,1,0,0,0,72,113,118,120,130,134,148,
        156,164,167,172,178,189,195,200,202,209,226,232,236,241,245,250,
        257,262,269,274,277,281,283,289,293,303,307,311,313,317,320,326,
        330,334,341,345,352,367,376,383,392,397,402,412,417,421,425,430,
        432,442,452,460,467,472,480,483,491,503,509,518,527,534,538,546,
        549,568
    ]

class StatementParser ( Parser ):

    grammarFileName = "StatementParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'.'", "','", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "ADD", "ALL", "ALTER", "AND", "ANY", 
                      "AS", "ASC", "AUTHORIZATION", "BACKUP", "BEGIN", "BETWEEN", 
                      "BREAK", "BROWSE", "BULK", "BY", "CASCADE", "CASE", 
                      "CHECK", "CHECKPOINT", "CLOSE", "CLUSTERED", "COALESCE", 
                      "COLLATE", "COLUMN", "COMMIT", "COMPUTE", "CONSTRAINT", 
                      "CONTAINS", "CONTAINSTABLE", "CONTINUE", "CONVERT", 
                      "CAST", "CREATE", "CROSS", "CURRENT", "CURRENT_DATE", 
                      "CURRENT_TIME", "CURRENT_TIMESTAMP", "CURRENT_USER", 
                      "CURSOR", "DATABASE", "DBCC", "DEALLOCATE", "DECLARE", 
                      "DEFAULT", "DELETE", "DENY", "DESC", "DISTINCT", "DISTRIBUTED", 
                      "DOUBLE", "DROP", "DUMP", "ELSE", "END", "ERRLVL", 
                      "ESCAPE", "EXCEPT", "EXEC", "EXECUTE", "EXISTS", "EXIT", 
                      "EXTERNAL", "FETCH", "FILE", "FILLFACTOR", "FOR", 
                      "FOREIGN", "FREETEXT", "FREETEXTTABLE", "FROM", "FULL", 
                      "FUNCTION", "GOTO", "GRANT", "GROUP", "HAVING", "HOLDLOCK", 
                      "IDENTITY", "IDENTITY_INSERT", "IDENTITYCOL", "IF", 
                      "IN", "INDEX", "INNER", "INSERT", "INTERSECT", "INTO", 
                      "IS", "JOIN", "KEY", "KILL", "LEFT", "LIKE", "LINENO", 
                      "LOAD", "MERGE", "NATIONAL", "NOCHECK", "NONCLUSTERED", 
                      "NOT", "NULL", "NULLIF", "OF", "OFF", "OFFSETS", "ON", 
                      "OPEN", "OPENDATASOURCE", "OPENQUERY", "OPENROWSET", 
                      "OPENXML", "OPTION", "OR", "ORDER", "OUTER", "OVER", 
                      "PERCENT", "PLAN", "PRECISION", "PRIMARY", "PRINT", 
                      "PROC", "PROCEDURE", "PUBLIC", "RAISERROR", "READ", 
                      "READTEXT", "RECONFIGURE", "REFERENCES", "REPLICATION", 
                      "RESTORE", "RESTRICT", "RETURN", "REVERT", "REVOKE", 
                      "RIGHT", "ROLLBACK", "ROWCOUNT", "ROWGUIDCOL", "RULE", 
                      "SAVE", "SAVEPOINT", "SESSION_USER", "SET", "SETUSER", 
                      "SHUTDOWN", "SOME", "STATISTICS", "SYSTEM_USER", "TABLE", 
                      "TABLESAMPLE", "TEXTSIZE", "THEN", "TO", "TOP", "TRAN", 
                      "TRANSACTION", "TRIGGER", "TRUNCATE", "TSEQUAL", "UNION", 
                      "UNIQUE", "UNPIVOT", "UPDATE", "UPDATETEXT", "USE", 
                      "USER", "VALUES", "VARYING", "VIEW", "WAITFOR", "WHEN", 
                      "WHERE", "WHILE", "WITH", "WRITETEXT", "INT", "BIGINT", 
                      "SMALLINT", "TINYINT", "BIT", "DECIMAL", "NUMERIC", 
                      "FLOAT", "REAL", "MONEY", "SMALLMONEY", "CHAR", "NCHAR", 
                      "VARCHAR", "TEXT", "NTEXT", "DATE", "DATETIME", "TIME", 
                      "TIMESTAMP", "UNIQUEIDENTIFIER", "SQL_VARIANT", "XML", 
                      "COUNT", "MAX", "MIN", "AVG", "SUM", "LEN", "UPPER", 
                      "LOWER", "GETDATE", "ISNULL", "SUBSTRING", "DATEADD", 
                      "DATEDIFF", "ROUND", "CEILING", "FLOOR", "FALSE", 
                      "ILIKE", "LIMIT", "NATURAL", "PARTITION", "OFFSET", 
                      "RETURNING", "SELECT", "UNNEST", "WINDOW", "TEMP", 
                      "TEMPORARY", "LOOP", "REPLACE", "MATERIALIZED", "FIRST", 
                      "TRY", "CATCH", "GO", "QUOTENAME", "NVARCHAR", "ERROR_MESSAGE", 
                      "ERROR_SEVERITY", "ERROR_STATE", "SCHEMA_NAME", "SCHEMA", 
                      "OBJECT", "TYPE", "INFORMATION_SCHEMA", "TABLES", 
                      "BASE", "COLUMNS", "KEYS", "PARENT", "SEQUENCES", 
                      "OUTPUT", "OPENJSON", "SP_EXECUTESQL", "FOREIGN_KEYS", 
                      "PARENT_OBJECT_ID", "EXECPT", "OBJECT_ID", "OBJECT_NAME", 
                      "OBJECT_SCHEMA_NAME", "TABLE_SCHEMA", "TABLE_NAME", 
                      "TABLE_TYPE", "VERSION", "DOT", "COMMA", "SEMI", "LPAREN", 
                      "RPAREN", "LINE_COMMENT", "BLOCK_COMMENT", "WS", "STRING_SINGLE", 
                      "STRING_DOUBLE", "BRACKET_IDENTIFIER", "VARIABLE", 
                      "IDENTIFIER", "NUMBER", "OPERATOR" ]

    RULE_sqlScript = 0
    RULE_batch = 1
    RULE_statement = 2
    RULE_ddlStatement = 3
    RULE_createTableStatement = 4
    RULE_columnDefinitionList = 5
    RULE_columnDefinition = 6
    RULE_dataType = 7
    RULE_typeSize = 8
    RULE_constraint = 9
    RULE_alterTableStatement = 10
    RULE_addColumnClause = 11
    RULE_dropConstraintClause = 12
    RULE_truncateStatement = 13
    RULE_dmlStatement = 14
    RULE_selectStatement = 15
    RULE_orderByList = 16
    RULE_orderByItem = 17
    RULE_selectList = 18
    RULE_selectItem = 19
    RULE_tableList = 20
    RULE_joinClause = 21
    RULE_joinType = 22
    RULE_tableRef = 23
    RULE_insertStatement = 24
    RULE_columnList = 25
    RULE_insertValues = 26
    RULE_updateStatement = 27
    RULE_assignments = 28
    RULE_assignment = 29
    RULE_deleteStatement = 30
    RULE_controlFlowStatement = 31
    RULE_ifStatement = 32
    RULE_thenBlock = 33
    RULE_elseBlock = 34
    RULE_blockStatement = 35
    RULE_tryCatchStatement = 36
    RULE_variableStatement = 37
    RULE_declareStatement = 38
    RULE_setStatement = 39
    RULE_execStatement = 40
    RULE_expression = 41
    RULE_primary = 42
    RULE_binaryOp = 43
    RULE_expressionList = 44
    RULE_literal = 45
    RULE_identifier = 46
    RULE_keywordAsIdentifier = 47
    RULE_functionCall = 48
    RULE_caseExpression = 49
    RULE_whenClause = 50
    RULE_elseClause = 51
    RULE_condition = 52
    RULE_tableName = 53
    RULE_columnName = 54

    ruleNames =  [ "sqlScript", "batch", "statement", "ddlStatement", "createTableStatement", 
                   "columnDefinitionList", "columnDefinition", "dataType", 
                   "typeSize", "constraint", "alterTableStatement", "addColumnClause", 
                   "dropConstraintClause", "truncateStatement", "dmlStatement", 
                   "selectStatement", "orderByList", "orderByItem", "selectList", 
                   "selectItem", "tableList", "joinClause", "joinType", 
                   "tableRef", "insertStatement", "columnList", "insertValues", 
                   "updateStatement", "assignments", "assignment", "deleteStatement", 
                   "controlFlowStatement", "ifStatement", "thenBlock", "elseBlock", 
                   "blockStatement", "tryCatchStatement", "variableStatement", 
                   "declareStatement", "setStatement", "execStatement", 
                   "expression", "primary", "binaryOp", "expressionList", 
                   "literal", "identifier", "keywordAsIdentifier", "functionCall", 
                   "caseExpression", "whenClause", "elseClause", "condition", 
                   "tableName", "columnName" ]

    EOF = Token.EOF
    ADD=1
    ALL=2
    ALTER=3
    AND=4
    ANY=5
    AS=6
    ASC=7
    AUTHORIZATION=8
    BACKUP=9
    BEGIN=10
    BETWEEN=11
    BREAK=12
    BROWSE=13
    BULK=14
    BY=15
    CASCADE=16
    CASE=17
    CHECK=18
    CHECKPOINT=19
    CLOSE=20
    CLUSTERED=21
    COALESCE=22
    COLLATE=23
    COLUMN=24
    COMMIT=25
    COMPUTE=26
    CONSTRAINT=27
    CONTAINS=28
    CONTAINSTABLE=29
    CONTINUE=30
    CONVERT=31
    CAST=32
    CREATE=33
    CROSS=34
    CURRENT=35
    CURRENT_DATE=36
    CURRENT_TIME=37
    CURRENT_TIMESTAMP=38
    CURRENT_USER=39
    CURSOR=40
    DATABASE=41
    DBCC=42
    DEALLOCATE=43
    DECLARE=44
    DEFAULT=45
    DELETE=46
    DENY=47
    DESC=48
    DISTINCT=49
    DISTRIBUTED=50
    DOUBLE=51
    DROP=52
    DUMP=53
    ELSE=54
    END=55
    ERRLVL=56
    ESCAPE=57
    EXCEPT=58
    EXEC=59
    EXECUTE=60
    EXISTS=61
    EXIT=62
    EXTERNAL=63
    FETCH=64
    FILE=65
    FILLFACTOR=66
    FOR=67
    FOREIGN=68
    FREETEXT=69
    FREETEXTTABLE=70
    FROM=71
    FULL=72
    FUNCTION=73
    GOTO=74
    GRANT=75
    GROUP=76
    HAVING=77
    HOLDLOCK=78
    IDENTITY=79
    IDENTITY_INSERT=80
    IDENTITYCOL=81
    IF=82
    IN=83
    INDEX=84
    INNER=85
    INSERT=86
    INTERSECT=87
    INTO=88
    IS=89
    JOIN=90
    KEY=91
    KILL=92
    LEFT=93
    LIKE=94
    LINENO=95
    LOAD=96
    MERGE=97
    NATIONAL=98
    NOCHECK=99
    NONCLUSTERED=100
    NOT=101
    NULL=102
    NULLIF=103
    OF=104
    OFF=105
    OFFSETS=106
    ON=107
    OPEN=108
    OPENDATASOURCE=109
    OPENQUERY=110
    OPENROWSET=111
    OPENXML=112
    OPTION=113
    OR=114
    ORDER=115
    OUTER=116
    OVER=117
    PERCENT=118
    PLAN=119
    PRECISION=120
    PRIMARY=121
    PRINT=122
    PROC=123
    PROCEDURE=124
    PUBLIC=125
    RAISERROR=126
    READ=127
    READTEXT=128
    RECONFIGURE=129
    REFERENCES=130
    REPLICATION=131
    RESTORE=132
    RESTRICT=133
    RETURN=134
    REVERT=135
    REVOKE=136
    RIGHT=137
    ROLLBACK=138
    ROWCOUNT=139
    ROWGUIDCOL=140
    RULE=141
    SAVE=142
    SAVEPOINT=143
    SESSION_USER=144
    SET=145
    SETUSER=146
    SHUTDOWN=147
    SOME=148
    STATISTICS=149
    SYSTEM_USER=150
    TABLE=151
    TABLESAMPLE=152
    TEXTSIZE=153
    THEN=154
    TO=155
    TOP=156
    TRAN=157
    TRANSACTION=158
    TRIGGER=159
    TRUNCATE=160
    TSEQUAL=161
    UNION=162
    UNIQUE=163
    UNPIVOT=164
    UPDATE=165
    UPDATETEXT=166
    USE=167
    USER=168
    VALUES=169
    VARYING=170
    VIEW=171
    WAITFOR=172
    WHEN=173
    WHERE=174
    WHILE=175
    WITH=176
    WRITETEXT=177
    INT=178
    BIGINT=179
    SMALLINT=180
    TINYINT=181
    BIT=182
    DECIMAL=183
    NUMERIC=184
    FLOAT=185
    REAL=186
    MONEY=187
    SMALLMONEY=188
    CHAR=189
    NCHAR=190
    VARCHAR=191
    TEXT=192
    NTEXT=193
    DATE=194
    DATETIME=195
    TIME=196
    TIMESTAMP=197
    UNIQUEIDENTIFIER=198
    SQL_VARIANT=199
    XML=200
    COUNT=201
    MAX=202
    MIN=203
    AVG=204
    SUM=205
    LEN=206
    UPPER=207
    LOWER=208
    GETDATE=209
    ISNULL=210
    SUBSTRING=211
    DATEADD=212
    DATEDIFF=213
    ROUND=214
    CEILING=215
    FLOOR=216
    FALSE=217
    ILIKE=218
    LIMIT=219
    NATURAL=220
    PARTITION=221
    OFFSET=222
    RETURNING=223
    SELECT=224
    UNNEST=225
    WINDOW=226
    TEMP=227
    TEMPORARY=228
    LOOP=229
    REPLACE=230
    MATERIALIZED=231
    FIRST=232
    TRY=233
    CATCH=234
    GO=235
    QUOTENAME=236
    NVARCHAR=237
    ERROR_MESSAGE=238
    ERROR_SEVERITY=239
    ERROR_STATE=240
    SCHEMA_NAME=241
    SCHEMA=242
    OBJECT=243
    TYPE=244
    INFORMATION_SCHEMA=245
    TABLES=246
    BASE=247
    COLUMNS=248
    KEYS=249
    PARENT=250
    SEQUENCES=251
    OUTPUT=252
    OPENJSON=253
    SP_EXECUTESQL=254
    FOREIGN_KEYS=255
    PARENT_OBJECT_ID=256
    EXECPT=257
    OBJECT_ID=258
    OBJECT_NAME=259
    OBJECT_SCHEMA_NAME=260
    TABLE_SCHEMA=261
    TABLE_NAME=262
    TABLE_TYPE=263
    VERSION=264
    DOT=265
    COMMA=266
    SEMI=267
    LPAREN=268
    RPAREN=269
    LINE_COMMENT=270
    BLOCK_COMMENT=271
    WS=272
    STRING_SINGLE=273
    STRING_DOUBLE=274
    BRACKET_IDENTIFIER=275
    VARIABLE=276
    IDENTIFIER=277
    NUMBER=278
    OPERATOR=279

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

        def batch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.BatchContext)
            else:
                return self.getTypedRuleContext(StatementParser.BatchContext,i)


        def getRuleIndex(self):
            return StatementParser.RULE_sqlScript

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

        localctx = StatementParser.SqlScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sqlScript)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576548721823581192) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & -9223372036854775791) != 0) or _la==160 or _la==165 or ((((_la - 224)) & ~0x3f) == 0 and ((1 << (_la - 224)) & 8796093024257) != 0):
                self.state = 110
                self.batch()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BatchContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.StatementContext)
            else:
                return self.getTypedRuleContext(StatementParser.StatementContext,i)


        def GO(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.GO)
            else:
                return self.getToken(StatementParser.GO, i)

        def getRuleIndex(self):
            return StatementParser.RULE_batch

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBatch" ):
                listener.enterBatch(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBatch" ):
                listener.exitBatch(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBatch" ):
                return visitor.visitBatch(self)
            else:
                return visitor.visitChildren(self)




    def batch(self):

        localctx = StatementParser.BatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_batch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 118
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3, 10, 33, 44, 46, 59, 82, 86, 145, 160, 165, 224, 267]:
                        self.state = 116
                        self.statement()
                        pass
                    elif token in [235]:
                        self.state = 117
                        self.match(StatementParser.GO)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 120 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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

        def ddlStatement(self):
            return self.getTypedRuleContext(StatementParser.DdlStatementContext,0)


        def dmlStatement(self):
            return self.getTypedRuleContext(StatementParser.DmlStatementContext,0)


        def controlFlowStatement(self):
            return self.getTypedRuleContext(StatementParser.ControlFlowStatementContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(StatementParser.VariableStatementContext,0)


        def execStatement(self):
            return self.getTypedRuleContext(StatementParser.ExecStatementContext,0)


        def truncateStatement(self):
            return self.getTypedRuleContext(StatementParser.TruncateStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(StatementParser.BlockStatementContext,0)


        def SEMI(self):
            return self.getToken(StatementParser.SEMI, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_statement

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

        localctx = StatementParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 122
                self.ddlStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 123
                self.dmlStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 124
                self.controlFlowStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 125
                self.variableStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 126
                self.execStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 127
                self.truncateStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 128
                self.blockStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 129
                self.match(StatementParser.SEMI)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DdlStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def createTableStatement(self):
            return self.getTypedRuleContext(StatementParser.CreateTableStatementContext,0)


        def alterTableStatement(self):
            return self.getTypedRuleContext(StatementParser.AlterTableStatementContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_ddlStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDdlStatement" ):
                listener.enterDdlStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDdlStatement" ):
                listener.exitDdlStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDdlStatement" ):
                return visitor.visitDdlStatement(self)
            else:
                return visitor.visitChildren(self)




    def ddlStatement(self):

        localctx = StatementParser.DdlStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_ddlStatement)
        try:
            self.state = 134
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.createTableStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.alterTableStatement()
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


    class CreateTableStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CREATE(self):
            return self.getToken(StatementParser.CREATE, 0)

        def TABLE(self):
            return self.getToken(StatementParser.TABLE, 0)

        def tableName(self):
            return self.getTypedRuleContext(StatementParser.TableNameContext,0)


        def LPAREN(self):
            return self.getToken(StatementParser.LPAREN, 0)

        def columnDefinitionList(self):
            return self.getTypedRuleContext(StatementParser.ColumnDefinitionListContext,0)


        def RPAREN(self):
            return self.getToken(StatementParser.RPAREN, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_createTableStatement

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

        localctx = StatementParser.CreateTableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_createTableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.match(StatementParser.CREATE)
            self.state = 137
            self.match(StatementParser.TABLE)
            self.state = 138
            self.tableName()
            self.state = 139
            self.match(StatementParser.LPAREN)
            self.state = 140
            self.columnDefinitionList()
            self.state = 141
            self.match(StatementParser.RPAREN)
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
                return self.getTypedRuleContexts(StatementParser.ColumnDefinitionContext)
            else:
                return self.getTypedRuleContext(StatementParser.ColumnDefinitionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.COMMA)
            else:
                return self.getToken(StatementParser.COMMA, i)

        def getRuleIndex(self):
            return StatementParser.RULE_columnDefinitionList

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

        localctx = StatementParser.ColumnDefinitionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_columnDefinitionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.columnDefinition()
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 144
                self.match(StatementParser.COMMA)
                self.state = 145
                self.columnDefinition()
                self.state = 150
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getTypedRuleContext(StatementParser.ColumnNameContext,0)


        def dataType(self):
            return self.getTypedRuleContext(StatementParser.DataTypeContext,0)


        def constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.ConstraintContext)
            else:
                return self.getTypedRuleContext(StatementParser.ConstraintContext,i)


        def getRuleIndex(self):
            return StatementParser.RULE_columnDefinition

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

        localctx = StatementParser.ColumnDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columnDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.columnName()
            self.state = 152
            self.dataType()
            self.state = 156
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 153
                    self.constraint() 
                self.state = 158
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def INT(self):
            return self.getToken(StatementParser.INT, 0)

        def NVARCHAR(self):
            return self.getToken(StatementParser.NVARCHAR, 0)

        def BIGINT(self):
            return self.getToken(StatementParser.BIGINT, 0)

        def DATE(self):
            return self.getToken(StatementParser.DATE, 0)

        def identifier(self):
            return self.getTypedRuleContext(StatementParser.IdentifierContext,0)


        def typeSize(self):
            return self.getTypedRuleContext(StatementParser.TypeSizeContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_dataType

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

        localctx = StatementParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 159
                self.match(StatementParser.INT)
                pass

            elif la_ == 2:
                self.state = 160
                self.match(StatementParser.NVARCHAR)
                pass

            elif la_ == 3:
                self.state = 161
                self.match(StatementParser.BIGINT)
                pass

            elif la_ == 4:
                self.state = 162
                self.match(StatementParser.DATE)
                pass

            elif la_ == 5:
                self.state = 163
                self.identifier()
                pass


            self.state = 167
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==268:
                self.state = 166
                self.typeSize()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSizeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(StatementParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(StatementParser.RPAREN, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.NUMBER)
            else:
                return self.getToken(StatementParser.NUMBER, i)

        def identifier(self):
            return self.getTypedRuleContext(StatementParser.IdentifierContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.COMMA)
            else:
                return self.getToken(StatementParser.COMMA, i)

        def getRuleIndex(self):
            return StatementParser.RULE_typeSize

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSize" ):
                listener.enterTypeSize(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSize" ):
                listener.exitTypeSize(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSize" ):
                return visitor.visitTypeSize(self)
            else:
                return visitor.visitChildren(self)




    def typeSize(self):

        localctx = StatementParser.TypeSizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_typeSize)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(StatementParser.LPAREN)
            self.state = 172
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [278]:
                self.state = 170
                self.match(StatementParser.NUMBER)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 274, 275, 277]:
                self.state = 171
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 174
                self.match(StatementParser.COMMA)
                self.state = 175
                self.match(StatementParser.NUMBER)
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self.match(StatementParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstraintContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.NOT)
            else:
                return self.getToken(StatementParser.NOT, i)

        def NULL(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.NULL)
            else:
                return self.getToken(StatementParser.NULL, i)

        def PRIMARY(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.PRIMARY)
            else:
                return self.getToken(StatementParser.PRIMARY, i)

        def KEY(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.KEY)
            else:
                return self.getToken(StatementParser.KEY, i)

        def DEFAULT(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.DEFAULT)
            else:
                return self.getToken(StatementParser.DEFAULT, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(StatementParser.ExpressionContext,i)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(StatementParser.IdentifierContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.LPAREN)
            else:
                return self.getToken(StatementParser.LPAREN, i)

        def columnList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.ColumnListContext)
            else:
                return self.getTypedRuleContext(StatementParser.ColumnListContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.RPAREN)
            else:
                return self.getToken(StatementParser.RPAREN, i)

        def CLUSTERED(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.CLUSTERED)
            else:
                return self.getToken(StatementParser.CLUSTERED, i)

        def NONCLUSTERED(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.NONCLUSTERED)
            else:
                return self.getToken(StatementParser.NONCLUSTERED, i)

        def getRuleIndex(self):
            return StatementParser.RULE_constraint

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstraint" ):
                listener.enterConstraint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstraint" ):
                listener.exitConstraint(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstraint" ):
                return visitor.visitConstraint(self)
            else:
                return visitor.visitChildren(self)




    def constraint(self):

        localctx = StatementParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 200
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 183
                        self.match(StatementParser.NOT)
                        self.state = 184
                        self.match(StatementParser.NULL)
                        pass

                    elif la_ == 2:
                        self.state = 185
                        self.match(StatementParser.NULL)
                        pass

                    elif la_ == 3:
                        self.state = 186
                        self.match(StatementParser.PRIMARY)
                        self.state = 187
                        self.match(StatementParser.KEY)
                        self.state = 189
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                        if la_ == 1:
                            self.state = 188
                            _la = self._input.LA(1)
                            if not(_la==21 or _la==100):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()


                        self.state = 195
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==268:
                            self.state = 191
                            self.match(StatementParser.LPAREN)
                            self.state = 192
                            self.columnList()
                            self.state = 193
                            self.match(StatementParser.RPAREN)


                        pass

                    elif la_ == 4:
                        self.state = 197
                        self.match(StatementParser.DEFAULT)
                        self.state = 198
                        self.expression()
                        pass

                    elif la_ == 5:
                        self.state = 199
                        self.identifier()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 202 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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

        def ALTER(self):
            return self.getToken(StatementParser.ALTER, 0)

        def TABLE(self):
            return self.getToken(StatementParser.TABLE, 0)

        def tableName(self):
            return self.getTypedRuleContext(StatementParser.TableNameContext,0)


        def addColumnClause(self):
            return self.getTypedRuleContext(StatementParser.AddColumnClauseContext,0)


        def dropConstraintClause(self):
            return self.getTypedRuleContext(StatementParser.DropConstraintClauseContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_alterTableStatement

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

        localctx = StatementParser.AlterTableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_alterTableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(StatementParser.ALTER)
            self.state = 205
            self.match(StatementParser.TABLE)
            self.state = 206
            self.tableName()
            self.state = 209
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 207
                self.addColumnClause()
                pass
            elif token in [52]:
                self.state = 208
                self.dropConstraintClause()
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


    class AddColumnClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(StatementParser.ADD, 0)

        def columnDefinition(self):
            return self.getTypedRuleContext(StatementParser.ColumnDefinitionContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_addColumnClause

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

        localctx = StatementParser.AddColumnClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_addColumnClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.match(StatementParser.ADD)
            self.state = 212
            self.columnDefinition()
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

        def DROP(self):
            return self.getToken(StatementParser.DROP, 0)

        def identifier(self):
            return self.getTypedRuleContext(StatementParser.IdentifierContext,0)


        def CONSTRAINT(self):
            return self.getToken(StatementParser.CONSTRAINT, 0)

        def COLUMN(self):
            return self.getToken(StatementParser.COLUMN, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_dropConstraintClause

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

        localctx = StatementParser.DropConstraintClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_dropConstraintClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 214
            self.match(StatementParser.DROP)
            self.state = 215
            _la = self._input.LA(1)
            if not(_la==24 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 216
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TruncateStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRUNCATE(self):
            return self.getToken(StatementParser.TRUNCATE, 0)

        def TABLE(self):
            return self.getToken(StatementParser.TABLE, 0)

        def tableName(self):
            return self.getTypedRuleContext(StatementParser.TableNameContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_truncateStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTruncateStatement" ):
                listener.enterTruncateStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTruncateStatement" ):
                listener.exitTruncateStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTruncateStatement" ):
                return visitor.visitTruncateStatement(self)
            else:
                return visitor.visitChildren(self)




    def truncateStatement(self):

        localctx = StatementParser.TruncateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_truncateStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.match(StatementParser.TRUNCATE)
            self.state = 219
            self.match(StatementParser.TABLE)
            self.state = 220
            self.tableName()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DmlStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectStatement(self):
            return self.getTypedRuleContext(StatementParser.SelectStatementContext,0)


        def insertStatement(self):
            return self.getTypedRuleContext(StatementParser.InsertStatementContext,0)


        def updateStatement(self):
            return self.getTypedRuleContext(StatementParser.UpdateStatementContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(StatementParser.DeleteStatementContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_dmlStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDmlStatement" ):
                listener.enterDmlStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDmlStatement" ):
                listener.exitDmlStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDmlStatement" ):
                return visitor.visitDmlStatement(self)
            else:
                return visitor.visitChildren(self)




    def dmlStatement(self):

        localctx = StatementParser.DmlStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_dmlStatement)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [224]:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.selectStatement()
                pass
            elif token in [86]:
                self.enterOuterAlt(localctx, 2)
                self.state = 223
                self.insertStatement()
                pass
            elif token in [165]:
                self.enterOuterAlt(localctx, 3)
                self.state = 224
                self.updateStatement()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.deleteStatement()
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


    class SelectStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(StatementParser.SELECT, 0)

        def selectList(self):
            return self.getTypedRuleContext(StatementParser.SelectListContext,0)


        def FROM(self):
            return self.getToken(StatementParser.FROM, 0)

        def tableList(self):
            return self.getTypedRuleContext(StatementParser.TableListContext,0)


        def WHERE(self):
            return self.getToken(StatementParser.WHERE, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.ConditionContext)
            else:
                return self.getTypedRuleContext(StatementParser.ConditionContext,i)


        def GROUP(self):
            return self.getToken(StatementParser.GROUP, 0)

        def BY(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.BY)
            else:
                return self.getToken(StatementParser.BY, i)

        def expressionList(self):
            return self.getTypedRuleContext(StatementParser.ExpressionListContext,0)


        def HAVING(self):
            return self.getToken(StatementParser.HAVING, 0)

        def ORDER(self):
            return self.getToken(StatementParser.ORDER, 0)

        def orderByList(self):
            return self.getTypedRuleContext(StatementParser.OrderByListContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_selectStatement

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

        localctx = StatementParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_selectStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 228
            self.match(StatementParser.SELECT)
            self.state = 229
            self.selectList()
            self.state = 232
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 230
                self.match(StatementParser.FROM)
                self.state = 231
                self.tableList()


            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==174:
                self.state = 234
                self.match(StatementParser.WHERE)
                self.state = 235
                self.condition()


            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==76:
                self.state = 238
                self.match(StatementParser.GROUP)
                self.state = 239
                self.match(StatementParser.BY)
                self.state = 240
                self.expressionList()


            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==77:
                self.state = 243
                self.match(StatementParser.HAVING)
                self.state = 244
                self.condition()


            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==115:
                self.state = 247
                self.match(StatementParser.ORDER)
                self.state = 248
                self.match(StatementParser.BY)
                self.state = 249
                self.orderByList()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OrderByListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def orderByItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.OrderByItemContext)
            else:
                return self.getTypedRuleContext(StatementParser.OrderByItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.COMMA)
            else:
                return self.getToken(StatementParser.COMMA, i)

        def getRuleIndex(self):
            return StatementParser.RULE_orderByList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrderByList" ):
                listener.enterOrderByList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrderByList" ):
                listener.exitOrderByList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOrderByList" ):
                return visitor.visitOrderByList(self)
            else:
                return visitor.visitChildren(self)




    def orderByList(self):

        localctx = StatementParser.OrderByListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_orderByList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.orderByItem()
            self.state = 257
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 253
                self.match(StatementParser.COMMA)
                self.state = 254
                self.orderByItem()
                self.state = 259
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def ASC(self):
            return self.getToken(StatementParser.ASC, 0)

        def DESC(self):
            return self.getToken(StatementParser.DESC, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_orderByItem

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

        localctx = StatementParser.OrderByItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_orderByItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.expression()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==48:
                self.state = 261
                _la = self._input.LA(1)
                if not(_la==7 or _la==48):
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


    class SelectListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def selectItem(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.SelectItemContext)
            else:
                return self.getTypedRuleContext(StatementParser.SelectItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.COMMA)
            else:
                return self.getToken(StatementParser.COMMA, i)

        def getRuleIndex(self):
            return StatementParser.RULE_selectList

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

        localctx = StatementParser.SelectListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_selectList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.selectItem()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 265
                self.match(StatementParser.COMMA)
                self.state = 266
                self.selectItem()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def OPERATOR(self):
            return self.getToken(StatementParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def columnName(self):
            return self.getTypedRuleContext(StatementParser.ColumnNameContext,0)


        def literal(self):
            return self.getTypedRuleContext(StatementParser.LiteralContext,0)


        def AS(self):
            return self.getToken(StatementParser.AS, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_selectItem

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

        localctx = StatementParser.SelectItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_selectItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 272
                self.match(StatementParser.OPERATOR)
                pass

            elif la_ == 2:
                self.state = 273
                self.expression()
                pass


            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 277
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 276
                    self.match(StatementParser.AS)


                self.state = 281
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 279
                    self.columnName()
                    pass

                elif la_ == 2:
                    self.state = 280
                    self.literal()
                    pass




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TableListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableRef(self):
            return self.getTypedRuleContext(StatementParser.TableRefContext,0)


        def joinClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.JoinClauseContext)
            else:
                return self.getTypedRuleContext(StatementParser.JoinClauseContext,i)


        def getRuleIndex(self):
            return StatementParser.RULE_tableList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableList" ):
                listener.enterTableList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableList" ):
                listener.exitTableList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableList" ):
                return visitor.visitTableList(self)
            else:
                return visitor.visitChildren(self)




    def tableList(self):

        localctx = StatementParser.TableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_tableList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.tableRef()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & 2367489) != 0) or _la==137:
                self.state = 286
                self.joinClause()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(StatementParser.JOIN, 0)

        def tableRef(self):
            return self.getTypedRuleContext(StatementParser.TableRefContext,0)


        def ON(self):
            return self.getToken(StatementParser.ON, 0)

        def condition(self):
            return self.getTypedRuleContext(StatementParser.ConditionContext,0)


        def joinType(self):
            return self.getTypedRuleContext(StatementParser.JoinTypeContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_joinClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinClause" ):
                listener.enterJoinClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinClause" ):
                listener.exitJoinClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoinClause" ):
                return visitor.visitJoinClause(self)
            else:
                return visitor.visitChildren(self)




    def joinClause(self):

        localctx = StatementParser.JoinClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_joinClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & 2105345) != 0) or _la==137:
                self.state = 292
                self.joinType()


            self.state = 295
            self.match(StatementParser.JOIN)
            self.state = 296
            self.tableRef()
            self.state = 297
            self.match(StatementParser.ON)
            self.state = 298
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JoinTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INNER(self):
            return self.getToken(StatementParser.INNER, 0)

        def LEFT(self):
            return self.getToken(StatementParser.LEFT, 0)

        def OUTER(self):
            return self.getToken(StatementParser.OUTER, 0)

        def RIGHT(self):
            return self.getToken(StatementParser.RIGHT, 0)

        def FULL(self):
            return self.getToken(StatementParser.FULL, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_joinType

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoinType" ):
                listener.enterJoinType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoinType" ):
                listener.exitJoinType(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJoinType" ):
                return visitor.visitJoinType(self)
            else:
                return visitor.visitChildren(self)




    def joinType(self):

        localctx = StatementParser.JoinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_joinType)
        self._la = 0 # Token type
        try:
            self.state = 313
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [85]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(StatementParser.INNER)
                pass
            elif token in [93]:
                self.enterOuterAlt(localctx, 2)
                self.state = 301
                self.match(StatementParser.LEFT)
                self.state = 303
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==116:
                    self.state = 302
                    self.match(StatementParser.OUTER)


                pass
            elif token in [137]:
                self.enterOuterAlt(localctx, 3)
                self.state = 305
                self.match(StatementParser.RIGHT)
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==116:
                    self.state = 306
                    self.match(StatementParser.OUTER)


                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 4)
                self.state = 309
                self.match(StatementParser.FULL)
                self.state = 311
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==116:
                    self.state = 310
                    self.match(StatementParser.OUTER)


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


    class TableRefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tableName(self):
            return self.getTypedRuleContext(StatementParser.TableNameContext,0)


        def identifier(self):
            return self.getTypedRuleContext(StatementParser.IdentifierContext,0)


        def AS(self):
            return self.getToken(StatementParser.AS, 0)

        def LPAREN(self):
            return self.getToken(StatementParser.LPAREN, 0)

        def selectStatement(self):
            return self.getTypedRuleContext(StatementParser.SelectStatementContext,0)


        def RPAREN(self):
            return self.getToken(StatementParser.RPAREN, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_tableRef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTableRef" ):
                listener.enterTableRef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTableRef" ):
                listener.exitTableRef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTableRef" ):
                return visitor.visitTableRef(self)
            else:
                return visitor.visitChildren(self)




    def tableRef(self):

        localctx = StatementParser.TableRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_tableRef)
        try:
            self.state = 330
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 274, 275, 277]:
                self.enterOuterAlt(localctx, 1)
                self.state = 315
                self.tableName()
                self.state = 320
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 317
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 316
                        self.match(StatementParser.AS)


                    self.state = 319
                    self.identifier()


                pass
            elif token in [268]:
                self.enterOuterAlt(localctx, 2)
                self.state = 322
                self.match(StatementParser.LPAREN)
                self.state = 323
                self.selectStatement()
                self.state = 324
                self.match(StatementParser.RPAREN)

                self.state = 326
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 325
                    self.match(StatementParser.AS)


                self.state = 328
                self.identifier()
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


    class InsertStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INSERT(self):
            return self.getToken(StatementParser.INSERT, 0)

        def tableName(self):
            return self.getTypedRuleContext(StatementParser.TableNameContext,0)


        def insertValues(self):
            return self.getTypedRuleContext(StatementParser.InsertValuesContext,0)


        def selectStatement(self):
            return self.getTypedRuleContext(StatementParser.SelectStatementContext,0)


        def INTO(self):
            return self.getToken(StatementParser.INTO, 0)

        def LPAREN(self):
            return self.getToken(StatementParser.LPAREN, 0)

        def columnList(self):
            return self.getTypedRuleContext(StatementParser.ColumnListContext,0)


        def RPAREN(self):
            return self.getToken(StatementParser.RPAREN, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_insertStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertStatement" ):
                listener.enterInsertStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertStatement" ):
                listener.exitInsertStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertStatement" ):
                return visitor.visitInsertStatement(self)
            else:
                return visitor.visitChildren(self)




    def insertStatement(self):

        localctx = StatementParser.InsertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_insertStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 332
            self.match(StatementParser.INSERT)
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 333
                self.match(StatementParser.INTO)


            self.state = 336
            self.tableName()
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==268:
                self.state = 337
                self.match(StatementParser.LPAREN)
                self.state = 338
                self.columnList()
                self.state = 339
                self.match(StatementParser.RPAREN)


            self.state = 345
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [169]:
                self.state = 343
                self.insertValues()
                pass
            elif token in [224]:
                self.state = 344
                self.selectStatement()
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


    class ColumnListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def columnName(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(StatementParser.ColumnNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.COMMA)
            else:
                return self.getToken(StatementParser.COMMA, i)

        def getRuleIndex(self):
            return StatementParser.RULE_columnList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumnList" ):
                listener.enterColumnList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumnList" ):
                listener.exitColumnList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitColumnList" ):
                return visitor.visitColumnList(self)
            else:
                return visitor.visitChildren(self)




    def columnList(self):

        localctx = StatementParser.ColumnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
            self.columnName()
            self.state = 352
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 348
                self.match(StatementParser.COMMA)
                self.state = 349
                self.columnName()
                self.state = 354
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InsertValuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VALUES(self):
            return self.getToken(StatementParser.VALUES, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.LPAREN)
            else:
                return self.getToken(StatementParser.LPAREN, i)

        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(StatementParser.ExpressionListContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.RPAREN)
            else:
                return self.getToken(StatementParser.RPAREN, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.COMMA)
            else:
                return self.getToken(StatementParser.COMMA, i)

        def getRuleIndex(self):
            return StatementParser.RULE_insertValues

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInsertValues" ):
                listener.enterInsertValues(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInsertValues" ):
                listener.exitInsertValues(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInsertValues" ):
                return visitor.visitInsertValues(self)
            else:
                return visitor.visitChildren(self)




    def insertValues(self):

        localctx = StatementParser.InsertValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_insertValues)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(StatementParser.VALUES)

            self.state = 356
            self.match(StatementParser.LPAREN)
            self.state = 357
            self.expressionList()
            self.state = 358
            self.match(StatementParser.RPAREN)
            self.state = 367
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 360
                self.match(StatementParser.COMMA)
                self.state = 361
                self.match(StatementParser.LPAREN)
                self.state = 362
                self.expressionList()
                self.state = 363
                self.match(StatementParser.RPAREN)
                self.state = 369
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def UPDATE(self):
            return self.getToken(StatementParser.UPDATE, 0)

        def tableName(self):
            return self.getTypedRuleContext(StatementParser.TableNameContext,0)


        def SET(self):
            return self.getToken(StatementParser.SET, 0)

        def assignments(self):
            return self.getTypedRuleContext(StatementParser.AssignmentsContext,0)


        def WHERE(self):
            return self.getToken(StatementParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(StatementParser.ConditionContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_updateStatement

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

        localctx = StatementParser.UpdateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_updateStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 370
            self.match(StatementParser.UPDATE)
            self.state = 371
            self.tableName()
            self.state = 372
            self.match(StatementParser.SET)
            self.state = 373
            self.assignments()
            self.state = 376
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==174:
                self.state = 374
                self.match(StatementParser.WHERE)
                self.state = 375
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(StatementParser.AssignmentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.COMMA)
            else:
                return self.getToken(StatementParser.COMMA, i)

        def getRuleIndex(self):
            return StatementParser.RULE_assignments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignments" ):
                listener.enterAssignments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignments" ):
                listener.exitAssignments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignments" ):
                return visitor.visitAssignments(self)
            else:
                return visitor.visitChildren(self)




    def assignments(self):

        localctx = StatementParser.AssignmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_assignments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.assignment()
            self.state = 383
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 379
                self.match(StatementParser.COMMA)
                self.state = 380
                self.assignment()
                self.state = 385
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getTypedRuleContext(StatementParser.ColumnNameContext,0)


        def OPERATOR(self):
            return self.getToken(StatementParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_assignment

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

        localctx = StatementParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self.columnName()
            self.state = 387
            self.match(StatementParser.OPERATOR)
            self.state = 388
            self.expression()
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

        def DELETE(self):
            return self.getToken(StatementParser.DELETE, 0)

        def tableName(self):
            return self.getTypedRuleContext(StatementParser.TableNameContext,0)


        def FROM(self):
            return self.getToken(StatementParser.FROM, 0)

        def WHERE(self):
            return self.getToken(StatementParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(StatementParser.ConditionContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_deleteStatement

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

        localctx = StatementParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_deleteStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 390
            self.match(StatementParser.DELETE)
            self.state = 392
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 391
                self.match(StatementParser.FROM)


            self.state = 394
            self.tableName()
            self.state = 397
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==174:
                self.state = 395
                self.match(StatementParser.WHERE)
                self.state = 396
                self.condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ControlFlowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifStatement(self):
            return self.getTypedRuleContext(StatementParser.IfStatementContext,0)


        def tryCatchStatement(self):
            return self.getTypedRuleContext(StatementParser.TryCatchStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(StatementParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_controlFlowStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterControlFlowStatement" ):
                listener.enterControlFlowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitControlFlowStatement" ):
                listener.exitControlFlowStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitControlFlowStatement" ):
                return visitor.visitControlFlowStatement(self)
            else:
                return visitor.visitChildren(self)




    def controlFlowStatement(self):

        localctx = StatementParser.ControlFlowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_controlFlowStatement)
        try:
            self.state = 402
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 399
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 400
                self.tryCatchStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 401
                self.blockStatement()
                pass


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

        def IF(self):
            return self.getToken(StatementParser.IF, 0)

        def thenBlock(self):
            return self.getTypedRuleContext(StatementParser.ThenBlockContext,0)


        def NOT(self):
            return self.getToken(StatementParser.NOT, 0)

        def EXISTS(self):
            return self.getToken(StatementParser.EXISTS, 0)

        def LPAREN(self):
            return self.getToken(StatementParser.LPAREN, 0)

        def selectStatement(self):
            return self.getTypedRuleContext(StatementParser.SelectStatementContext,0)


        def RPAREN(self):
            return self.getToken(StatementParser.RPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(StatementParser.ConditionContext,0)


        def ELSE(self):
            return self.getToken(StatementParser.ELSE, 0)

        def elseBlock(self):
            return self.getTypedRuleContext(StatementParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_ifStatement

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

        localctx = StatementParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 404
            self.match(StatementParser.IF)
            self.state = 412
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 405
                self.match(StatementParser.NOT)
                self.state = 406
                self.match(StatementParser.EXISTS)
                self.state = 407
                self.match(StatementParser.LPAREN)
                self.state = 408
                self.selectStatement()
                self.state = 409
                self.match(StatementParser.RPAREN)

            elif la_ == 2:
                self.state = 411
                self.condition()


            self.state = 414
            self.thenBlock()
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 415
                self.match(StatementParser.ELSE)
                self.state = 416
                self.elseBlock()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThenBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(StatementParser.BlockStatementContext,0)


        def statement(self):
            return self.getTypedRuleContext(StatementParser.StatementContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_thenBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThenBlock" ):
                listener.enterThenBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThenBlock" ):
                listener.exitThenBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitThenBlock" ):
                return visitor.visitThenBlock(self)
            else:
                return visitor.visitChildren(self)




    def thenBlock(self):

        localctx = StatementParser.ThenBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_thenBlock)
        try:
            self.state = 421
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 420
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def blockStatement(self):
            return self.getTypedRuleContext(StatementParser.BlockStatementContext,0)


        def statement(self):
            return self.getTypedRuleContext(StatementParser.StatementContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_elseBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseBlock" ):
                listener.enterElseBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseBlock" ):
                listener.exitElseBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseBlock" ):
                return visitor.visitElseBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseBlock(self):

        localctx = StatementParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_elseBlock)
        try:
            self.state = 425
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 423
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 424
                self.statement()
                pass


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

        def BEGIN(self):
            return self.getToken(StatementParser.BEGIN, 0)

        def END(self):
            return self.getToken(StatementParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.StatementContext)
            else:
                return self.getTypedRuleContext(StatementParser.StatementContext,i)


        def GO(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.GO)
            else:
                return self.getToken(StatementParser.GO, i)

        def getRuleIndex(self):
            return StatementParser.RULE_blockStatement

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

        localctx = StatementParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 427
            self.match(StatementParser.BEGIN)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576548721823581192) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & -9223372036854775791) != 0) or _la==160 or _la==165 or ((((_la - 224)) & ~0x3f) == 0 and ((1 << (_la - 224)) & 8796093024257) != 0):
                self.state = 430
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 10, 33, 44, 46, 59, 82, 86, 145, 160, 165, 224, 267]:
                    self.state = 428
                    self.statement()
                    pass
                elif token in [235]:
                    self.state = 429
                    self.match(StatementParser.GO)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 434
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 435
            self.match(StatementParser.END)
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

        def BEGIN(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.BEGIN)
            else:
                return self.getToken(StatementParser.BEGIN, i)

        def TRY(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.TRY)
            else:
                return self.getToken(StatementParser.TRY, i)

        def END(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.END)
            else:
                return self.getToken(StatementParser.END, i)

        def CATCH(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.CATCH)
            else:
                return self.getToken(StatementParser.CATCH, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.StatementContext)
            else:
                return self.getTypedRuleContext(StatementParser.StatementContext,i)


        def getRuleIndex(self):
            return StatementParser.RULE_tryCatchStatement

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

        localctx = StatementParser.TryCatchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_tryCatchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 437
            self.match(StatementParser.BEGIN)
            self.state = 438
            self.match(StatementParser.TRY)
            self.state = 442
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576548721823581192) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & -9223372036854775791) != 0) or _la==160 or _la==165 or _la==224 or _la==267:
                self.state = 439
                self.statement()
                self.state = 444
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 445
            self.match(StatementParser.END)
            self.state = 446
            self.match(StatementParser.TRY)
            self.state = 447
            self.match(StatementParser.BEGIN)
            self.state = 448
            self.match(StatementParser.CATCH)
            self.state = 452
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576548721823581192) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & -9223372036854775791) != 0) or _la==160 or _la==165 or _la==224 or _la==267:
                self.state = 449
                self.statement()
                self.state = 454
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 455
            self.match(StatementParser.END)
            self.state = 456
            self.match(StatementParser.CATCH)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declareStatement(self):
            return self.getTypedRuleContext(StatementParser.DeclareStatementContext,0)


        def setStatement(self):
            return self.getTypedRuleContext(StatementParser.SetStatementContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_variableStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableStatement" ):
                listener.enterVariableStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableStatement" ):
                listener.exitVariableStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableStatement" ):
                return visitor.visitVariableStatement(self)
            else:
                return visitor.visitChildren(self)




    def variableStatement(self):

        localctx = StatementParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_variableStatement)
        try:
            self.state = 460
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 458
                self.declareStatement()
                pass
            elif token in [145]:
                self.enterOuterAlt(localctx, 2)
                self.state = 459
                self.setStatement()
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


    class DeclareStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECLARE(self):
            return self.getToken(StatementParser.DECLARE, 0)

        def VARIABLE(self):
            return self.getToken(StatementParser.VARIABLE, 0)

        def dataType(self):
            return self.getTypedRuleContext(StatementParser.DataTypeContext,0)


        def OPERATOR(self):
            return self.getToken(StatementParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_declareStatement

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

        localctx = StatementParser.DeclareStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_declareStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 462
            self.match(StatementParser.DECLARE)
            self.state = 463
            self.match(StatementParser.VARIABLE)
            self.state = 464
            self.dataType()
            self.state = 467
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==279:
                self.state = 465
                self.match(StatementParser.OPERATOR)
                self.state = 466
                self.expression()


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

        def SET(self):
            return self.getToken(StatementParser.SET, 0)

        def OPERATOR(self):
            return self.getToken(StatementParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def VARIABLE(self):
            return self.getToken(StatementParser.VARIABLE, 0)

        def columnName(self):
            return self.getTypedRuleContext(StatementParser.ColumnNameContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_setStatement

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

        localctx = StatementParser.SetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_setStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 469
            self.match(StatementParser.SET)
            self.state = 472
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [276]:
                self.state = 470
                self.match(StatementParser.VARIABLE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 274, 275, 277]:
                self.state = 471
                self.columnName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 474
            self.match(StatementParser.OPERATOR)
            self.state = 475
            self.expression()
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

        def EXEC(self):
            return self.getToken(StatementParser.EXEC, 0)

        def identifier(self):
            return self.getTypedRuleContext(StatementParser.IdentifierContext,0)


        def SP_EXECUTESQL(self):
            return self.getToken(StatementParser.SP_EXECUTESQL, 0)

        def expressionList(self):
            return self.getTypedRuleContext(StatementParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_execStatement

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

        localctx = StatementParser.ExecStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_execStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 477
            self.match(StatementParser.EXEC)
            self.state = 480
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 478
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 479
                self.match(StatementParser.SP_EXECUTESQL)
                pass


            self.state = 483
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 482
                self.expressionList()


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

        def primary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(StatementParser.PrimaryContext,i)


        def binaryOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.BinaryOpContext)
            else:
                return self.getTypedRuleContext(StatementParser.BinaryOpContext,i)


        def getRuleIndex(self):
            return StatementParser.RULE_expression

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




    def expression(self):

        localctx = StatementParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.primary()
            self.state = 491
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 486
                    self.binaryOp()
                    self.state = 487
                    self.primary() 
                self.state = 493
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(StatementParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(StatementParser.FunctionCallContext,0)


        def caseExpression(self):
            return self.getTypedRuleContext(StatementParser.CaseExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(StatementParser.IdentifierContext,0)


        def VARIABLE(self):
            return self.getToken(StatementParser.VARIABLE, 0)

        def LPAREN(self):
            return self.getToken(StatementParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(StatementParser.RPAREN, 0)

        def selectStatement(self):
            return self.getTypedRuleContext(StatementParser.SelectStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(StatementParser.ExpressionListContext,0)


        def OPERATOR(self):
            return self.getToken(StatementParser.OPERATOR, 0)

        def primary(self):
            return self.getTypedRuleContext(StatementParser.PrimaryContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = StatementParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_primary)
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 494
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 495
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 496
                self.caseExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 497
                self.identifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 498
                self.match(StatementParser.VARIABLE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 499
                self.match(StatementParser.LPAREN)
                self.state = 503
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 500
                    self.selectStatement()
                    pass

                elif la_ == 2:
                    self.state = 501
                    self.expression()
                    pass

                elif la_ == 3:
                    self.state = 502
                    self.expressionList()
                    pass


                self.state = 505
                self.match(StatementParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 507
                self.match(StatementParser.OPERATOR)
                self.state = 508
                self.primary()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(StatementParser.OPERATOR, 0)

        def AND(self):
            return self.getToken(StatementParser.AND, 0)

        def OR(self):
            return self.getToken(StatementParser.OR, 0)

        def IN(self):
            return self.getToken(StatementParser.IN, 0)

        def IS(self):
            return self.getToken(StatementParser.IS, 0)

        def NOT(self):
            return self.getToken(StatementParser.NOT, 0)

        def LIKE(self):
            return self.getToken(StatementParser.LIKE, 0)

        def BETWEEN(self):
            return self.getToken(StatementParser.BETWEEN, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = StatementParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            _la = self._input.LA(1)
            if not(_la==4 or _la==11 or ((((_la - 83)) & ~0x3f) == 0 and ((1 << (_la - 83)) & 2147747905) != 0) or _la==279):
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


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(StatementParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.COMMA)
            else:
                return self.getToken(StatementParser.COMMA, i)

        def getRuleIndex(self):
            return StatementParser.RULE_expressionList

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

        localctx = StatementParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 513
            self.expression()
            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 514
                self.match(StatementParser.COMMA)
                self.state = 515
                self.expression()
                self.state = 520
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
            return self.getToken(StatementParser.NUMBER, 0)

        def STRING_SINGLE(self):
            return self.getToken(StatementParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(StatementParser.STRING_DOUBLE, 0)

        def NULL(self):
            return self.getToken(StatementParser.NULL, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_literal

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

        localctx = StatementParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 521
            _la = self._input.LA(1)
            if not(_la==102 or ((((_la - 273)) & ~0x3f) == 0 and ((1 << (_la - 273)) & 35) != 0)):
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


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(StatementParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(StatementParser.BRACKET_IDENTIFIER, 0)

        def STRING_DOUBLE(self):
            return self.getToken(StatementParser.STRING_DOUBLE, 0)

        def keywordAsIdentifier(self):
            return self.getTypedRuleContext(StatementParser.KeywordAsIdentifierContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_identifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifier" ):
                listener.enterIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifier" ):
                listener.exitIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = StatementParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_identifier)
        try:
            self.state = 527
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [277]:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.match(StatementParser.IDENTIFIER)
                pass
            elif token in [275]:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.match(StatementParser.BRACKET_IDENTIFIER)
                pass
            elif token in [274]:
                self.enterOuterAlt(localctx, 3)
                self.state = 525
                self.match(StatementParser.STRING_DOUBLE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264]:
                self.enterOuterAlt(localctx, 4)
                self.state = 526
                self.keywordAsIdentifier()
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


    class KeywordAsIdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ADD(self):
            return self.getToken(StatementParser.ADD, 0)

        def ALL(self):
            return self.getToken(StatementParser.ALL, 0)

        def ALTER(self):
            return self.getToken(StatementParser.ALTER, 0)

        def AND(self):
            return self.getToken(StatementParser.AND, 0)

        def ANY(self):
            return self.getToken(StatementParser.ANY, 0)

        def AS(self):
            return self.getToken(StatementParser.AS, 0)

        def ASC(self):
            return self.getToken(StatementParser.ASC, 0)

        def AUTHORIZATION(self):
            return self.getToken(StatementParser.AUTHORIZATION, 0)

        def BACKUP(self):
            return self.getToken(StatementParser.BACKUP, 0)

        def BEGIN(self):
            return self.getToken(StatementParser.BEGIN, 0)

        def BETWEEN(self):
            return self.getToken(StatementParser.BETWEEN, 0)

        def BREAK(self):
            return self.getToken(StatementParser.BREAK, 0)

        def BULK(self):
            return self.getToken(StatementParser.BULK, 0)

        def BY(self):
            return self.getToken(StatementParser.BY, 0)

        def CASCADE(self):
            return self.getToken(StatementParser.CASCADE, 0)

        def CASE(self):
            return self.getToken(StatementParser.CASE, 0)

        def CHECK(self):
            return self.getToken(StatementParser.CHECK, 0)

        def CHECKPOINT(self):
            return self.getToken(StatementParser.CHECKPOINT, 0)

        def CLOSE(self):
            return self.getToken(StatementParser.CLOSE, 0)

        def CLUSTERED(self):
            return self.getToken(StatementParser.CLUSTERED, 0)

        def COALESCE(self):
            return self.getToken(StatementParser.COALESCE, 0)

        def COLLATE(self):
            return self.getToken(StatementParser.COLLATE, 0)

        def COLUMN(self):
            return self.getToken(StatementParser.COLUMN, 0)

        def COMMIT(self):
            return self.getToken(StatementParser.COMMIT, 0)

        def COMPUTE(self):
            return self.getToken(StatementParser.COMPUTE, 0)

        def CONSTRAINT(self):
            return self.getToken(StatementParser.CONSTRAINT, 0)

        def CONTAINS(self):
            return self.getToken(StatementParser.CONTAINS, 0)

        def CONTINUE(self):
            return self.getToken(StatementParser.CONTINUE, 0)

        def CONVERT(self):
            return self.getToken(StatementParser.CONVERT, 0)

        def CAST(self):
            return self.getToken(StatementParser.CAST, 0)

        def CREATE(self):
            return self.getToken(StatementParser.CREATE, 0)

        def CROSS(self):
            return self.getToken(StatementParser.CROSS, 0)

        def CURRENT(self):
            return self.getToken(StatementParser.CURRENT, 0)

        def CURRENT_DATE(self):
            return self.getToken(StatementParser.CURRENT_DATE, 0)

        def CURRENT_TIME(self):
            return self.getToken(StatementParser.CURRENT_TIME, 0)

        def CURRENT_TIMESTAMP(self):
            return self.getToken(StatementParser.CURRENT_TIMESTAMP, 0)

        def CURRENT_USER(self):
            return self.getToken(StatementParser.CURRENT_USER, 0)

        def CURSOR(self):
            return self.getToken(StatementParser.CURSOR, 0)

        def DATABASE(self):
            return self.getToken(StatementParser.DATABASE, 0)

        def DBCC(self):
            return self.getToken(StatementParser.DBCC, 0)

        def DEALLOCATE(self):
            return self.getToken(StatementParser.DEALLOCATE, 0)

        def DECLARE(self):
            return self.getToken(StatementParser.DECLARE, 0)

        def DEFAULT(self):
            return self.getToken(StatementParser.DEFAULT, 0)

        def DELETE(self):
            return self.getToken(StatementParser.DELETE, 0)

        def DENY(self):
            return self.getToken(StatementParser.DENY, 0)

        def DESC(self):
            return self.getToken(StatementParser.DESC, 0)

        def DISTINCT(self):
            return self.getToken(StatementParser.DISTINCT, 0)

        def DISTRIBUTED(self):
            return self.getToken(StatementParser.DISTRIBUTED, 0)

        def DOUBLE(self):
            return self.getToken(StatementParser.DOUBLE, 0)

        def DROP(self):
            return self.getToken(StatementParser.DROP, 0)

        def DUMP(self):
            return self.getToken(StatementParser.DUMP, 0)

        def ELSE(self):
            return self.getToken(StatementParser.ELSE, 0)

        def END(self):
            return self.getToken(StatementParser.END, 0)

        def ERRLVL(self):
            return self.getToken(StatementParser.ERRLVL, 0)

        def ESCAPE(self):
            return self.getToken(StatementParser.ESCAPE, 0)

        def EXCEPT(self):
            return self.getToken(StatementParser.EXCEPT, 0)

        def EXEC(self):
            return self.getToken(StatementParser.EXEC, 0)

        def EXECUTE(self):
            return self.getToken(StatementParser.EXECUTE, 0)

        def EXISTS(self):
            return self.getToken(StatementParser.EXISTS, 0)

        def EXIT(self):
            return self.getToken(StatementParser.EXIT, 0)

        def EXTERNAL(self):
            return self.getToken(StatementParser.EXTERNAL, 0)

        def FETCH(self):
            return self.getToken(StatementParser.FETCH, 0)

        def FILE(self):
            return self.getToken(StatementParser.FILE, 0)

        def FILLFACTOR(self):
            return self.getToken(StatementParser.FILLFACTOR, 0)

        def FOR(self):
            return self.getToken(StatementParser.FOR, 0)

        def FOREIGN(self):
            return self.getToken(StatementParser.FOREIGN, 0)

        def FREETEXT(self):
            return self.getToken(StatementParser.FREETEXT, 0)

        def FREETEXTTABLE(self):
            return self.getToken(StatementParser.FREETEXTTABLE, 0)

        def FROM(self):
            return self.getToken(StatementParser.FROM, 0)

        def FULL(self):
            return self.getToken(StatementParser.FULL, 0)

        def FUNCTION(self):
            return self.getToken(StatementParser.FUNCTION, 0)

        def GOTO(self):
            return self.getToken(StatementParser.GOTO, 0)

        def GRANT(self):
            return self.getToken(StatementParser.GRANT, 0)

        def GROUP(self):
            return self.getToken(StatementParser.GROUP, 0)

        def HAVING(self):
            return self.getToken(StatementParser.HAVING, 0)

        def HOLDLOCK(self):
            return self.getToken(StatementParser.HOLDLOCK, 0)

        def IDENTITY(self):
            return self.getToken(StatementParser.IDENTITY, 0)

        def IDENTITY_INSERT(self):
            return self.getToken(StatementParser.IDENTITY_INSERT, 0)

        def IDENTITYCOL(self):
            return self.getToken(StatementParser.IDENTITYCOL, 0)

        def IF(self):
            return self.getToken(StatementParser.IF, 0)

        def IN(self):
            return self.getToken(StatementParser.IN, 0)

        def INDEX(self):
            return self.getToken(StatementParser.INDEX, 0)

        def INNER(self):
            return self.getToken(StatementParser.INNER, 0)

        def INSERT(self):
            return self.getToken(StatementParser.INSERT, 0)

        def INTERSECT(self):
            return self.getToken(StatementParser.INTERSECT, 0)

        def INTO(self):
            return self.getToken(StatementParser.INTO, 0)

        def IS(self):
            return self.getToken(StatementParser.IS, 0)

        def JOIN(self):
            return self.getToken(StatementParser.JOIN, 0)

        def KEY(self):
            return self.getToken(StatementParser.KEY, 0)

        def KILL(self):
            return self.getToken(StatementParser.KILL, 0)

        def LEFT(self):
            return self.getToken(StatementParser.LEFT, 0)

        def LIKE(self):
            return self.getToken(StatementParser.LIKE, 0)

        def LINENO(self):
            return self.getToken(StatementParser.LINENO, 0)

        def LOAD(self):
            return self.getToken(StatementParser.LOAD, 0)

        def MERGE(self):
            return self.getToken(StatementParser.MERGE, 0)

        def NATIONAL(self):
            return self.getToken(StatementParser.NATIONAL, 0)

        def NOCHECK(self):
            return self.getToken(StatementParser.NOCHECK, 0)

        def NONCLUSTERED(self):
            return self.getToken(StatementParser.NONCLUSTERED, 0)

        def NOT(self):
            return self.getToken(StatementParser.NOT, 0)

        def NULL(self):
            return self.getToken(StatementParser.NULL, 0)

        def NULLIF(self):
            return self.getToken(StatementParser.NULLIF, 0)

        def OF(self):
            return self.getToken(StatementParser.OF, 0)

        def OFF(self):
            return self.getToken(StatementParser.OFF, 0)

        def OFFSETS(self):
            return self.getToken(StatementParser.OFFSETS, 0)

        def ON(self):
            return self.getToken(StatementParser.ON, 0)

        def OPEN(self):
            return self.getToken(StatementParser.OPEN, 0)

        def OPENDATASOURCE(self):
            return self.getToken(StatementParser.OPENDATASOURCE, 0)

        def OPENQUERY(self):
            return self.getToken(StatementParser.OPENQUERY, 0)

        def OPENROWSET(self):
            return self.getToken(StatementParser.OPENROWSET, 0)

        def OPENXML(self):
            return self.getToken(StatementParser.OPENXML, 0)

        def OPTION(self):
            return self.getToken(StatementParser.OPTION, 0)

        def OR(self):
            return self.getToken(StatementParser.OR, 0)

        def ORDER(self):
            return self.getToken(StatementParser.ORDER, 0)

        def OUTER(self):
            return self.getToken(StatementParser.OUTER, 0)

        def OVER(self):
            return self.getToken(StatementParser.OVER, 0)

        def PERCENT(self):
            return self.getToken(StatementParser.PERCENT, 0)

        def PLAN(self):
            return self.getToken(StatementParser.PLAN, 0)

        def PRECISION(self):
            return self.getToken(StatementParser.PRECISION, 0)

        def PRIMARY(self):
            return self.getToken(StatementParser.PRIMARY, 0)

        def PRINT(self):
            return self.getToken(StatementParser.PRINT, 0)

        def PROC(self):
            return self.getToken(StatementParser.PROC, 0)

        def PROCEDURE(self):
            return self.getToken(StatementParser.PROCEDURE, 0)

        def PUBLIC(self):
            return self.getToken(StatementParser.PUBLIC, 0)

        def RAISERROR(self):
            return self.getToken(StatementParser.RAISERROR, 0)

        def READ(self):
            return self.getToken(StatementParser.READ, 0)

        def READTEXT(self):
            return self.getToken(StatementParser.READTEXT, 0)

        def RECONFIGURE(self):
            return self.getToken(StatementParser.RECONFIGURE, 0)

        def REFERENCES(self):
            return self.getToken(StatementParser.REFERENCES, 0)

        def REPLICATION(self):
            return self.getToken(StatementParser.REPLICATION, 0)

        def RESTORE(self):
            return self.getToken(StatementParser.RESTORE, 0)

        def RESTRICT(self):
            return self.getToken(StatementParser.RESTRICT, 0)

        def RETURN(self):
            return self.getToken(StatementParser.RETURN, 0)

        def REVERT(self):
            return self.getToken(StatementParser.REVERT, 0)

        def REVOKE(self):
            return self.getToken(StatementParser.REVOKE, 0)

        def RIGHT(self):
            return self.getToken(StatementParser.RIGHT, 0)

        def ROLLBACK(self):
            return self.getToken(StatementParser.ROLLBACK, 0)

        def ROWCOUNT(self):
            return self.getToken(StatementParser.ROWCOUNT, 0)

        def ROWGUIDCOL(self):
            return self.getToken(StatementParser.ROWGUIDCOL, 0)

        def RULE(self):
            return self.getToken(StatementParser.RULE, 0)

        def SAVE(self):
            return self.getToken(StatementParser.SAVE, 0)

        def SAVEPOINT(self):
            return self.getToken(StatementParser.SAVEPOINT, 0)

        def SCHEMA(self):
            return self.getToken(StatementParser.SCHEMA, 0)

        def SCHEMA_NAME(self):
            return self.getToken(StatementParser.SCHEMA_NAME, 0)

        def SESSION_USER(self):
            return self.getToken(StatementParser.SESSION_USER, 0)

        def SET(self):
            return self.getToken(StatementParser.SET, 0)

        def SETUSER(self):
            return self.getToken(StatementParser.SETUSER, 0)

        def SHUTDOWN(self):
            return self.getToken(StatementParser.SHUTDOWN, 0)

        def SOME(self):
            return self.getToken(StatementParser.SOME, 0)

        def STATISTICS(self):
            return self.getToken(StatementParser.STATISTICS, 0)

        def SYSTEM_USER(self):
            return self.getToken(StatementParser.SYSTEM_USER, 0)

        def TABLE(self):
            return self.getToken(StatementParser.TABLE, 0)

        def TABLESAMPLE(self):
            return self.getToken(StatementParser.TABLESAMPLE, 0)

        def TEXTSIZE(self):
            return self.getToken(StatementParser.TEXTSIZE, 0)

        def THEN(self):
            return self.getToken(StatementParser.THEN, 0)

        def TO(self):
            return self.getToken(StatementParser.TO, 0)

        def TOP(self):
            return self.getToken(StatementParser.TOP, 0)

        def TRAN(self):
            return self.getToken(StatementParser.TRAN, 0)

        def TRANSACTION(self):
            return self.getToken(StatementParser.TRANSACTION, 0)

        def TRIGGER(self):
            return self.getToken(StatementParser.TRIGGER, 0)

        def TRUNCATE(self):
            return self.getToken(StatementParser.TRUNCATE, 0)

        def TSEQUAL(self):
            return self.getToken(StatementParser.TSEQUAL, 0)

        def UNION(self):
            return self.getToken(StatementParser.UNION, 0)

        def UNIQUE(self):
            return self.getToken(StatementParser.UNIQUE, 0)

        def UNPIVOT(self):
            return self.getToken(StatementParser.UNPIVOT, 0)

        def UPDATE(self):
            return self.getToken(StatementParser.UPDATE, 0)

        def UPDATETEXT(self):
            return self.getToken(StatementParser.UPDATETEXT, 0)

        def USE(self):
            return self.getToken(StatementParser.USE, 0)

        def USER(self):
            return self.getToken(StatementParser.USER, 0)

        def VALUES(self):
            return self.getToken(StatementParser.VALUES, 0)

        def VARYING(self):
            return self.getToken(StatementParser.VARYING, 0)

        def VIEW(self):
            return self.getToken(StatementParser.VIEW, 0)

        def WAITFOR(self):
            return self.getToken(StatementParser.WAITFOR, 0)

        def WHEN(self):
            return self.getToken(StatementParser.WHEN, 0)

        def WHERE(self):
            return self.getToken(StatementParser.WHERE, 0)

        def WHILE(self):
            return self.getToken(StatementParser.WHILE, 0)

        def WITH(self):
            return self.getToken(StatementParser.WITH, 0)

        def WRITETEXT(self):
            return self.getToken(StatementParser.WRITETEXT, 0)

        def INT(self):
            return self.getToken(StatementParser.INT, 0)

        def BIGINT(self):
            return self.getToken(StatementParser.BIGINT, 0)

        def SMALLINT(self):
            return self.getToken(StatementParser.SMALLINT, 0)

        def TINYINT(self):
            return self.getToken(StatementParser.TINYINT, 0)

        def BIT(self):
            return self.getToken(StatementParser.BIT, 0)

        def DECIMAL(self):
            return self.getToken(StatementParser.DECIMAL, 0)

        def NUMERIC(self):
            return self.getToken(StatementParser.NUMERIC, 0)

        def FLOAT(self):
            return self.getToken(StatementParser.FLOAT, 0)

        def REAL(self):
            return self.getToken(StatementParser.REAL, 0)

        def MONEY(self):
            return self.getToken(StatementParser.MONEY, 0)

        def SMALLMONEY(self):
            return self.getToken(StatementParser.SMALLMONEY, 0)

        def CHAR(self):
            return self.getToken(StatementParser.CHAR, 0)

        def NCHAR(self):
            return self.getToken(StatementParser.NCHAR, 0)

        def VARCHAR(self):
            return self.getToken(StatementParser.VARCHAR, 0)

        def NVARCHAR(self):
            return self.getToken(StatementParser.NVARCHAR, 0)

        def TEXT(self):
            return self.getToken(StatementParser.TEXT, 0)

        def NTEXT(self):
            return self.getToken(StatementParser.NTEXT, 0)

        def DATE(self):
            return self.getToken(StatementParser.DATE, 0)

        def DATETIME(self):
            return self.getToken(StatementParser.DATETIME, 0)

        def TIME(self):
            return self.getToken(StatementParser.TIME, 0)

        def TIMESTAMP(self):
            return self.getToken(StatementParser.TIMESTAMP, 0)

        def UNIQUEIDENTIFIER(self):
            return self.getToken(StatementParser.UNIQUEIDENTIFIER, 0)

        def SQL_VARIANT(self):
            return self.getToken(StatementParser.SQL_VARIANT, 0)

        def XML(self):
            return self.getToken(StatementParser.XML, 0)

        def COUNT(self):
            return self.getToken(StatementParser.COUNT, 0)

        def MAX(self):
            return self.getToken(StatementParser.MAX, 0)

        def MIN(self):
            return self.getToken(StatementParser.MIN, 0)

        def AVG(self):
            return self.getToken(StatementParser.AVG, 0)

        def SUM(self):
            return self.getToken(StatementParser.SUM, 0)

        def LEN(self):
            return self.getToken(StatementParser.LEN, 0)

        def UPPER(self):
            return self.getToken(StatementParser.UPPER, 0)

        def LOWER(self):
            return self.getToken(StatementParser.LOWER, 0)

        def GETDATE(self):
            return self.getToken(StatementParser.GETDATE, 0)

        def ISNULL(self):
            return self.getToken(StatementParser.ISNULL, 0)

        def SUBSTRING(self):
            return self.getToken(StatementParser.SUBSTRING, 0)

        def DATEADD(self):
            return self.getToken(StatementParser.DATEADD, 0)

        def DATEDIFF(self):
            return self.getToken(StatementParser.DATEDIFF, 0)

        def ROUND(self):
            return self.getToken(StatementParser.ROUND, 0)

        def CEILING(self):
            return self.getToken(StatementParser.CEILING, 0)

        def FLOOR(self):
            return self.getToken(StatementParser.FLOOR, 0)

        def FALSE(self):
            return self.getToken(StatementParser.FALSE, 0)

        def ILIKE(self):
            return self.getToken(StatementParser.ILIKE, 0)

        def LIMIT(self):
            return self.getToken(StatementParser.LIMIT, 0)

        def NATURAL(self):
            return self.getToken(StatementParser.NATURAL, 0)

        def PARTITION(self):
            return self.getToken(StatementParser.PARTITION, 0)

        def OFFSET(self):
            return self.getToken(StatementParser.OFFSET, 0)

        def RETURNING(self):
            return self.getToken(StatementParser.RETURNING, 0)

        def SELECT(self):
            return self.getToken(StatementParser.SELECT, 0)

        def UNNEST(self):
            return self.getToken(StatementParser.UNNEST, 0)

        def WINDOW(self):
            return self.getToken(StatementParser.WINDOW, 0)

        def TEMP(self):
            return self.getToken(StatementParser.TEMP, 0)

        def TEMPORARY(self):
            return self.getToken(StatementParser.TEMPORARY, 0)

        def LOOP(self):
            return self.getToken(StatementParser.LOOP, 0)

        def REPLACE(self):
            return self.getToken(StatementParser.REPLACE, 0)

        def MATERIALIZED(self):
            return self.getToken(StatementParser.MATERIALIZED, 0)

        def FIRST(self):
            return self.getToken(StatementParser.FIRST, 0)

        def TRY(self):
            return self.getToken(StatementParser.TRY, 0)

        def CATCH(self):
            return self.getToken(StatementParser.CATCH, 0)

        def GO(self):
            return self.getToken(StatementParser.GO, 0)

        def QUOTENAME(self):
            return self.getToken(StatementParser.QUOTENAME, 0)

        def ERROR_MESSAGE(self):
            return self.getToken(StatementParser.ERROR_MESSAGE, 0)

        def ERROR_SEVERITY(self):
            return self.getToken(StatementParser.ERROR_SEVERITY, 0)

        def ERROR_STATE(self):
            return self.getToken(StatementParser.ERROR_STATE, 0)

        def OBJECT(self):
            return self.getToken(StatementParser.OBJECT, 0)

        def TYPE(self):
            return self.getToken(StatementParser.TYPE, 0)

        def INFORMATION_SCHEMA(self):
            return self.getToken(StatementParser.INFORMATION_SCHEMA, 0)

        def TABLES(self):
            return self.getToken(StatementParser.TABLES, 0)

        def BASE(self):
            return self.getToken(StatementParser.BASE, 0)

        def COLUMNS(self):
            return self.getToken(StatementParser.COLUMNS, 0)

        def KEYS(self):
            return self.getToken(StatementParser.KEYS, 0)

        def PARENT(self):
            return self.getToken(StatementParser.PARENT, 0)

        def SEQUENCES(self):
            return self.getToken(StatementParser.SEQUENCES, 0)

        def OUTPUT(self):
            return self.getToken(StatementParser.OUTPUT, 0)

        def OPENJSON(self):
            return self.getToken(StatementParser.OPENJSON, 0)

        def SP_EXECUTESQL(self):
            return self.getToken(StatementParser.SP_EXECUTESQL, 0)

        def FOREIGN_KEYS(self):
            return self.getToken(StatementParser.FOREIGN_KEYS, 0)

        def PARENT_OBJECT_ID(self):
            return self.getToken(StatementParser.PARENT_OBJECT_ID, 0)

        def EXECPT(self):
            return self.getToken(StatementParser.EXECPT, 0)

        def OBJECT_ID(self):
            return self.getToken(StatementParser.OBJECT_ID, 0)

        def OBJECT_NAME(self):
            return self.getToken(StatementParser.OBJECT_NAME, 0)

        def OBJECT_SCHEMA_NAME(self):
            return self.getToken(StatementParser.OBJECT_SCHEMA_NAME, 0)

        def TABLE_SCHEMA(self):
            return self.getToken(StatementParser.TABLE_SCHEMA, 0)

        def TABLE_NAME(self):
            return self.getToken(StatementParser.TABLE_NAME, 0)

        def TABLE_TYPE(self):
            return self.getToken(StatementParser.TABLE_TYPE, 0)

        def VERSION(self):
            return self.getToken(StatementParser.VERSION, 0)

        def getRuleIndex(self):
            return StatementParser.RULE_keywordAsIdentifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKeywordAsIdentifier" ):
                listener.enterKeywordAsIdentifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKeywordAsIdentifier" ):
                listener.exitKeywordAsIdentifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKeywordAsIdentifier" ):
                return visitor.visitKeywordAsIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def keywordAsIdentifier(self):

        localctx = StatementParser.KeywordAsIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_keywordAsIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 529
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & -536879106) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & -1) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & -1) != 0) or ((((_la - 192)) & ~0x3f) == 0 and ((1 << (_la - 192)) & -1) != 0) or ((((_la - 256)) & ~0x3f) == 0 and ((1 << (_la - 256)) & 511) != 0)):
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


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(StatementParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(StatementParser.RPAREN, 0)

        def MAX(self):
            return self.getToken(StatementParser.MAX, 0)

        def AVG(self):
            return self.getToken(StatementParser.AVG, 0)

        def identifier(self):
            return self.getTypedRuleContext(StatementParser.IdentifierContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(StatementParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_functionCall

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

        localctx = StatementParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 531
                self.match(StatementParser.MAX)
                pass

            elif la_ == 2:
                self.state = 532
                self.match(StatementParser.AVG)
                pass

            elif la_ == 3:
                self.state = 533
                self.identifier()
                pass


            self.state = 536
            self.match(StatementParser.LPAREN)
            self.state = 538
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -536879106) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & -1) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & -1) != 0) or ((((_la - 192)) & ~0x3f) == 0 and ((1 << (_la - 192)) & -1) != 0) or ((((_la - 256)) & ~0x3f) == 0 and ((1 << (_la - 256)) & 16650751) != 0):
                self.state = 537
                self.expressionList()


            self.state = 540
            self.match(StatementParser.RPAREN)
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

        def CASE(self):
            return self.getToken(StatementParser.CASE, 0)

        def END(self):
            return self.getToken(StatementParser.END, 0)

        def whenClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.WhenClauseContext)
            else:
                return self.getTypedRuleContext(StatementParser.WhenClauseContext,i)


        def elseClause(self):
            return self.getTypedRuleContext(StatementParser.ElseClauseContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_caseExpression

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

        localctx = StatementParser.CaseExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_caseExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 542
            self.match(StatementParser.CASE)
            self.state = 544 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 543
                self.whenClause()
                self.state = 546 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==173):
                    break

            self.state = 549
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 548
                self.elseClause()


            self.state = 551
            self.match(StatementParser.END)
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

        def WHEN(self):
            return self.getToken(StatementParser.WHEN, 0)

        def condition(self):
            return self.getTypedRuleContext(StatementParser.ConditionContext,0)


        def THEN(self):
            return self.getToken(StatementParser.THEN, 0)

        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_whenClause

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

        localctx = StatementParser.WhenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_whenClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(StatementParser.WHEN)
            self.state = 554
            self.condition()
            self.state = 555
            self.match(StatementParser.THEN)
            self.state = 556
            self.expression()
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

        def ELSE(self):
            return self.getToken(StatementParser.ELSE, 0)

        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_elseClause

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

        localctx = StatementParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(StatementParser.ELSE)
            self.state = 559
            self.expression()
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

        def expression(self):
            return self.getTypedRuleContext(StatementParser.ExpressionContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_condition

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




    def condition(self):

        localctx = StatementParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self.expression()
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

        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(StatementParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(StatementParser.IdentifierContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(StatementParser.DOT)
            else:
                return self.getToken(StatementParser.DOT, i)

        def getRuleIndex(self):
            return StatementParser.RULE_tableName

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

        localctx = StatementParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_tableName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.identifier()
            self.state = 568
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==265:
                self.state = 564
                self.match(StatementParser.DOT)
                self.state = 565
                self.identifier()
                self.state = 570
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def identifier(self):
            return self.getTypedRuleContext(StatementParser.IdentifierContext,0)


        def getRuleIndex(self):
            return StatementParser.RULE_columnName

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

        localctx = StatementParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





