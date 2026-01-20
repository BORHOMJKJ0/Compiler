# Generated from grammars/SQLParser.g4 by ANTLR 4.13.2
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
        4,1,279,579,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,
        52,2,53,7,53,2,54,7,54,2,55,7,55,1,0,1,0,1,0,1,1,5,1,117,8,1,10,
        1,12,1,120,9,1,1,2,1,2,4,2,124,8,2,11,2,12,2,125,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,136,8,3,1,4,1,4,3,4,140,8,4,1,5,1,5,1,5,1,5,
        1,5,1,5,1,5,1,6,1,6,1,6,5,6,152,8,6,10,6,12,6,155,9,6,1,7,1,7,1,
        7,5,7,160,8,7,10,7,12,7,163,9,7,1,8,1,8,1,8,1,8,1,8,3,8,170,8,8,
        1,8,3,8,173,8,8,1,9,1,9,1,9,3,9,178,8,9,1,9,1,9,5,9,182,8,9,10,9,
        12,9,185,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,195,8,10,
        1,10,1,10,1,10,1,10,3,10,201,8,10,1,10,1,10,1,10,4,10,206,8,10,11,
        10,12,10,207,1,11,1,11,1,11,1,11,1,11,3,11,215,8,11,1,12,1,12,1,
        12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,
        15,232,8,15,1,16,1,16,1,16,1,16,3,16,238,8,16,1,16,1,16,3,16,242,
        8,16,1,16,1,16,1,16,3,16,247,8,16,1,16,1,16,3,16,251,8,16,1,16,1,
        16,1,16,3,16,256,8,16,1,17,1,17,1,17,5,17,261,8,17,10,17,12,17,264,
        9,17,1,18,1,18,3,18,268,8,18,1,19,1,19,1,19,5,19,273,8,19,10,19,
        12,19,276,9,19,1,20,1,20,3,20,280,8,20,1,20,3,20,283,8,20,1,20,1,
        20,3,20,287,8,20,3,20,289,8,20,1,21,1,21,5,21,293,8,21,10,21,12,
        21,296,9,21,1,22,3,22,299,8,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,
        1,23,3,23,309,8,23,1,23,1,23,3,23,313,8,23,1,23,1,23,3,23,317,8,
        23,3,23,319,8,23,1,24,1,24,3,24,323,8,24,1,24,3,24,326,8,24,1,24,
        1,24,1,24,1,24,3,24,332,8,24,1,24,1,24,3,24,336,8,24,1,25,1,25,3,
        25,340,8,25,1,25,1,25,1,25,1,25,1,25,3,25,347,8,25,1,25,1,25,3,25,
        351,8,25,1,26,1,26,1,26,5,26,356,8,26,10,26,12,26,359,9,26,1,27,
        1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,1,27,5,27,371,8,27,10,27,
        12,27,374,9,27,1,28,1,28,1,28,1,28,1,28,1,28,3,28,382,8,28,1,29,
        1,29,1,29,5,29,387,8,29,10,29,12,29,390,9,29,1,30,1,30,1,30,1,30,
        1,31,1,31,3,31,398,8,31,1,31,1,31,1,31,3,31,403,8,31,1,32,1,32,1,
        32,3,32,408,8,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,418,
        8,33,1,33,1,33,1,33,3,33,423,8,33,1,34,1,34,3,34,427,8,34,1,35,1,
        35,3,35,431,8,35,1,36,1,36,1,36,5,36,436,8,36,10,36,12,36,439,9,
        36,1,36,1,36,1,37,1,37,1,37,5,37,446,8,37,10,37,12,37,449,9,37,1,
        37,1,37,1,37,1,37,1,37,5,37,456,8,37,10,37,12,37,459,9,37,1,37,1,
        37,1,37,1,38,1,38,3,38,466,8,38,1,39,1,39,1,39,1,39,1,39,3,39,473,
        8,39,1,40,1,40,1,40,3,40,478,8,40,1,40,1,40,1,40,1,41,1,41,1,41,
        3,41,486,8,41,1,41,3,41,489,8,41,1,42,1,42,1,42,1,42,5,42,495,8,
        42,10,42,12,42,498,9,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,
        1,43,3,43,509,8,43,1,43,1,43,1,43,1,43,3,43,515,8,43,1,44,1,44,1,
        45,1,45,1,45,5,45,522,8,45,10,45,12,45,525,9,45,1,46,1,46,1,47,1,
        47,1,47,1,47,3,47,533,8,47,1,48,1,48,1,49,1,49,1,49,3,49,540,8,49,
        1,49,1,49,3,49,544,8,49,1,49,1,49,1,50,1,50,4,50,550,8,50,11,50,
        12,50,551,1,50,3,50,555,8,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,
        1,52,1,52,1,52,1,53,1,53,1,54,1,54,1,54,5,54,572,8,54,10,54,12,54,
        575,9,54,1,55,1,55,1,55,0,0,56,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,68,
        70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,108,
        110,0,6,2,0,21,21,100,100,2,0,24,24,27,27,2,0,7,7,48,48,8,0,4,4,
        11,11,83,83,89,89,94,94,101,101,114,114,279,279,3,0,102,102,273,
        274,278,278,3,0,1,12,14,28,30,264,621,0,112,1,0,0,0,2,118,1,0,0,
        0,4,123,1,0,0,0,6,135,1,0,0,0,8,139,1,0,0,0,10,141,1,0,0,0,12,148,
        1,0,0,0,14,156,1,0,0,0,16,169,1,0,0,0,18,174,1,0,0,0,20,205,1,0,
        0,0,22,209,1,0,0,0,24,216,1,0,0,0,26,219,1,0,0,0,28,223,1,0,0,0,
        30,231,1,0,0,0,32,233,1,0,0,0,34,257,1,0,0,0,36,265,1,0,0,0,38,269,
        1,0,0,0,40,279,1,0,0,0,42,290,1,0,0,0,44,298,1,0,0,0,46,318,1,0,
        0,0,48,335,1,0,0,0,50,337,1,0,0,0,52,352,1,0,0,0,54,360,1,0,0,0,
        56,375,1,0,0,0,58,383,1,0,0,0,60,391,1,0,0,0,62,395,1,0,0,0,64,407,
        1,0,0,0,66,409,1,0,0,0,68,426,1,0,0,0,70,430,1,0,0,0,72,432,1,0,
        0,0,74,442,1,0,0,0,76,465,1,0,0,0,78,467,1,0,0,0,80,474,1,0,0,0,
        82,482,1,0,0,0,84,490,1,0,0,0,86,514,1,0,0,0,88,516,1,0,0,0,90,518,
        1,0,0,0,92,526,1,0,0,0,94,532,1,0,0,0,96,534,1,0,0,0,98,539,1,0,
        0,0,100,547,1,0,0,0,102,558,1,0,0,0,104,563,1,0,0,0,106,566,1,0,
        0,0,108,568,1,0,0,0,110,576,1,0,0,0,112,113,3,2,1,0,113,114,5,0,
        0,1,114,1,1,0,0,0,115,117,3,4,2,0,116,115,1,0,0,0,117,120,1,0,0,
        0,118,116,1,0,0,0,118,119,1,0,0,0,119,3,1,0,0,0,120,118,1,0,0,0,
        121,124,3,6,3,0,122,124,5,235,0,0,123,121,1,0,0,0,123,122,1,0,0,
        0,124,125,1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,5,1,0,0,0,
        127,136,3,8,4,0,128,136,3,30,15,0,129,136,3,64,32,0,130,136,3,76,
        38,0,131,136,3,82,41,0,132,136,3,28,14,0,133,136,3,72,36,0,134,136,
        5,267,0,0,135,127,1,0,0,0,135,128,1,0,0,0,135,129,1,0,0,0,135,130,
        1,0,0,0,135,131,1,0,0,0,135,132,1,0,0,0,135,133,1,0,0,0,135,134,
        1,0,0,0,136,7,1,0,0,0,137,140,3,10,5,0,138,140,3,22,11,0,139,137,
        1,0,0,0,139,138,1,0,0,0,140,9,1,0,0,0,141,142,5,33,0,0,142,143,5,
        151,0,0,143,144,3,108,54,0,144,145,5,268,0,0,145,146,3,12,6,0,146,
        147,5,269,0,0,147,11,1,0,0,0,148,153,3,14,7,0,149,150,5,266,0,0,
        150,152,3,14,7,0,151,149,1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,
        153,154,1,0,0,0,154,13,1,0,0,0,155,153,1,0,0,0,156,157,3,110,55,
        0,157,161,3,16,8,0,158,160,3,20,10,0,159,158,1,0,0,0,160,163,1,0,
        0,0,161,159,1,0,0,0,161,162,1,0,0,0,162,15,1,0,0,0,163,161,1,0,0,
        0,164,170,5,178,0,0,165,170,5,237,0,0,166,170,5,179,0,0,167,170,
        5,194,0,0,168,170,3,94,47,0,169,164,1,0,0,0,169,165,1,0,0,0,169,
        166,1,0,0,0,169,167,1,0,0,0,169,168,1,0,0,0,170,172,1,0,0,0,171,
        173,3,18,9,0,172,171,1,0,0,0,172,173,1,0,0,0,173,17,1,0,0,0,174,
        177,5,268,0,0,175,178,5,278,0,0,176,178,3,94,47,0,177,175,1,0,0,
        0,177,176,1,0,0,0,178,183,1,0,0,0,179,180,5,266,0,0,180,182,5,278,
        0,0,181,179,1,0,0,0,182,185,1,0,0,0,183,181,1,0,0,0,183,184,1,0,
        0,0,184,186,1,0,0,0,185,183,1,0,0,0,186,187,5,269,0,0,187,19,1,0,
        0,0,188,189,5,101,0,0,189,206,5,102,0,0,190,206,5,102,0,0,191,192,
        5,121,0,0,192,194,5,91,0,0,193,195,7,0,0,0,194,193,1,0,0,0,194,195,
        1,0,0,0,195,200,1,0,0,0,196,197,5,268,0,0,197,198,3,52,26,0,198,
        199,5,269,0,0,199,201,1,0,0,0,200,196,1,0,0,0,200,201,1,0,0,0,201,
        206,1,0,0,0,202,203,5,45,0,0,203,206,3,84,42,0,204,206,3,94,47,0,
        205,188,1,0,0,0,205,190,1,0,0,0,205,191,1,0,0,0,205,202,1,0,0,0,
        205,204,1,0,0,0,206,207,1,0,0,0,207,205,1,0,0,0,207,208,1,0,0,0,
        208,21,1,0,0,0,209,210,5,3,0,0,210,211,5,151,0,0,211,214,3,108,54,
        0,212,215,3,24,12,0,213,215,3,26,13,0,214,212,1,0,0,0,214,213,1,
        0,0,0,215,23,1,0,0,0,216,217,5,1,0,0,217,218,3,14,7,0,218,25,1,0,
        0,0,219,220,5,52,0,0,220,221,7,1,0,0,221,222,3,94,47,0,222,27,1,
        0,0,0,223,224,5,160,0,0,224,225,5,151,0,0,225,226,3,108,54,0,226,
        29,1,0,0,0,227,232,3,32,16,0,228,232,3,50,25,0,229,232,3,56,28,0,
        230,232,3,62,31,0,231,227,1,0,0,0,231,228,1,0,0,0,231,229,1,0,0,
        0,231,230,1,0,0,0,232,31,1,0,0,0,233,234,5,224,0,0,234,237,3,38,
        19,0,235,236,5,71,0,0,236,238,3,42,21,0,237,235,1,0,0,0,237,238,
        1,0,0,0,238,241,1,0,0,0,239,240,5,174,0,0,240,242,3,106,53,0,241,
        239,1,0,0,0,241,242,1,0,0,0,242,246,1,0,0,0,243,244,5,76,0,0,244,
        245,5,15,0,0,245,247,3,90,45,0,246,243,1,0,0,0,246,247,1,0,0,0,247,
        250,1,0,0,0,248,249,5,77,0,0,249,251,3,106,53,0,250,248,1,0,0,0,
        250,251,1,0,0,0,251,255,1,0,0,0,252,253,5,115,0,0,253,254,5,15,0,
        0,254,256,3,34,17,0,255,252,1,0,0,0,255,256,1,0,0,0,256,33,1,0,0,
        0,257,262,3,36,18,0,258,259,5,266,0,0,259,261,3,36,18,0,260,258,
        1,0,0,0,261,264,1,0,0,0,262,260,1,0,0,0,262,263,1,0,0,0,263,35,1,
        0,0,0,264,262,1,0,0,0,265,267,3,84,42,0,266,268,7,2,0,0,267,266,
        1,0,0,0,267,268,1,0,0,0,268,37,1,0,0,0,269,274,3,40,20,0,270,271,
        5,266,0,0,271,273,3,40,20,0,272,270,1,0,0,0,273,276,1,0,0,0,274,
        272,1,0,0,0,274,275,1,0,0,0,275,39,1,0,0,0,276,274,1,0,0,0,277,280,
        5,279,0,0,278,280,3,84,42,0,279,277,1,0,0,0,279,278,1,0,0,0,280,
        288,1,0,0,0,281,283,5,6,0,0,282,281,1,0,0,0,282,283,1,0,0,0,283,
        286,1,0,0,0,284,287,3,110,55,0,285,287,3,92,46,0,286,284,1,0,0,0,
        286,285,1,0,0,0,287,289,1,0,0,0,288,282,1,0,0,0,288,289,1,0,0,0,
        289,41,1,0,0,0,290,294,3,48,24,0,291,293,3,44,22,0,292,291,1,0,0,
        0,293,296,1,0,0,0,294,292,1,0,0,0,294,295,1,0,0,0,295,43,1,0,0,0,
        296,294,1,0,0,0,297,299,3,46,23,0,298,297,1,0,0,0,298,299,1,0,0,
        0,299,300,1,0,0,0,300,301,5,90,0,0,301,302,3,48,24,0,302,303,5,107,
        0,0,303,304,3,106,53,0,304,45,1,0,0,0,305,319,5,85,0,0,306,308,5,
        93,0,0,307,309,5,116,0,0,308,307,1,0,0,0,308,309,1,0,0,0,309,319,
        1,0,0,0,310,312,5,137,0,0,311,313,5,116,0,0,312,311,1,0,0,0,312,
        313,1,0,0,0,313,319,1,0,0,0,314,316,5,72,0,0,315,317,5,116,0,0,316,
        315,1,0,0,0,316,317,1,0,0,0,317,319,1,0,0,0,318,305,1,0,0,0,318,
        306,1,0,0,0,318,310,1,0,0,0,318,314,1,0,0,0,319,47,1,0,0,0,320,325,
        3,108,54,0,321,323,5,6,0,0,322,321,1,0,0,0,322,323,1,0,0,0,323,324,
        1,0,0,0,324,326,3,94,47,0,325,322,1,0,0,0,325,326,1,0,0,0,326,336,
        1,0,0,0,327,328,5,268,0,0,328,329,3,32,16,0,329,331,5,269,0,0,330,
        332,5,6,0,0,331,330,1,0,0,0,331,332,1,0,0,0,332,333,1,0,0,0,333,
        334,3,94,47,0,334,336,1,0,0,0,335,320,1,0,0,0,335,327,1,0,0,0,336,
        49,1,0,0,0,337,339,5,86,0,0,338,340,5,88,0,0,339,338,1,0,0,0,339,
        340,1,0,0,0,340,341,1,0,0,0,341,346,3,108,54,0,342,343,5,268,0,0,
        343,344,3,52,26,0,344,345,5,269,0,0,345,347,1,0,0,0,346,342,1,0,
        0,0,346,347,1,0,0,0,347,350,1,0,0,0,348,351,3,54,27,0,349,351,3,
        32,16,0,350,348,1,0,0,0,350,349,1,0,0,0,351,51,1,0,0,0,352,357,3,
        110,55,0,353,354,5,266,0,0,354,356,3,110,55,0,355,353,1,0,0,0,356,
        359,1,0,0,0,357,355,1,0,0,0,357,358,1,0,0,0,358,53,1,0,0,0,359,357,
        1,0,0,0,360,361,5,169,0,0,361,362,5,268,0,0,362,363,3,90,45,0,363,
        364,5,269,0,0,364,372,1,0,0,0,365,366,5,266,0,0,366,367,5,268,0,
        0,367,368,3,90,45,0,368,369,5,269,0,0,369,371,1,0,0,0,370,365,1,
        0,0,0,371,374,1,0,0,0,372,370,1,0,0,0,372,373,1,0,0,0,373,55,1,0,
        0,0,374,372,1,0,0,0,375,376,5,165,0,0,376,377,3,108,54,0,377,378,
        5,145,0,0,378,381,3,58,29,0,379,380,5,174,0,0,380,382,3,106,53,0,
        381,379,1,0,0,0,381,382,1,0,0,0,382,57,1,0,0,0,383,388,3,60,30,0,
        384,385,5,266,0,0,385,387,3,60,30,0,386,384,1,0,0,0,387,390,1,0,
        0,0,388,386,1,0,0,0,388,389,1,0,0,0,389,59,1,0,0,0,390,388,1,0,0,
        0,391,392,3,110,55,0,392,393,5,279,0,0,393,394,3,84,42,0,394,61,
        1,0,0,0,395,397,5,46,0,0,396,398,5,71,0,0,397,396,1,0,0,0,397,398,
        1,0,0,0,398,399,1,0,0,0,399,402,3,108,54,0,400,401,5,174,0,0,401,
        403,3,106,53,0,402,400,1,0,0,0,402,403,1,0,0,0,403,63,1,0,0,0,404,
        408,3,66,33,0,405,408,3,74,37,0,406,408,3,72,36,0,407,404,1,0,0,
        0,407,405,1,0,0,0,407,406,1,0,0,0,408,65,1,0,0,0,409,417,5,82,0,
        0,410,411,5,101,0,0,411,412,5,61,0,0,412,413,5,268,0,0,413,414,3,
        32,16,0,414,415,5,269,0,0,415,418,1,0,0,0,416,418,3,106,53,0,417,
        410,1,0,0,0,417,416,1,0,0,0,417,418,1,0,0,0,418,419,1,0,0,0,419,
        422,3,68,34,0,420,421,5,54,0,0,421,423,3,70,35,0,422,420,1,0,0,0,
        422,423,1,0,0,0,423,67,1,0,0,0,424,427,3,72,36,0,425,427,3,6,3,0,
        426,424,1,0,0,0,426,425,1,0,0,0,427,69,1,0,0,0,428,431,3,72,36,0,
        429,431,3,6,3,0,430,428,1,0,0,0,430,429,1,0,0,0,431,71,1,0,0,0,432,
        437,5,10,0,0,433,436,3,6,3,0,434,436,5,235,0,0,435,433,1,0,0,0,435,
        434,1,0,0,0,436,439,1,0,0,0,437,435,1,0,0,0,437,438,1,0,0,0,438,
        440,1,0,0,0,439,437,1,0,0,0,440,441,5,55,0,0,441,73,1,0,0,0,442,
        443,5,10,0,0,443,447,5,233,0,0,444,446,3,6,3,0,445,444,1,0,0,0,446,
        449,1,0,0,0,447,445,1,0,0,0,447,448,1,0,0,0,448,450,1,0,0,0,449,
        447,1,0,0,0,450,451,5,55,0,0,451,452,5,233,0,0,452,453,5,10,0,0,
        453,457,5,234,0,0,454,456,3,6,3,0,455,454,1,0,0,0,456,459,1,0,0,
        0,457,455,1,0,0,0,457,458,1,0,0,0,458,460,1,0,0,0,459,457,1,0,0,
        0,460,461,5,55,0,0,461,462,5,234,0,0,462,75,1,0,0,0,463,466,3,78,
        39,0,464,466,3,80,40,0,465,463,1,0,0,0,465,464,1,0,0,0,466,77,1,
        0,0,0,467,468,5,44,0,0,468,469,5,276,0,0,469,472,3,16,8,0,470,471,
        5,279,0,0,471,473,3,84,42,0,472,470,1,0,0,0,472,473,1,0,0,0,473,
        79,1,0,0,0,474,477,5,145,0,0,475,478,5,276,0,0,476,478,3,110,55,
        0,477,475,1,0,0,0,477,476,1,0,0,0,478,479,1,0,0,0,479,480,5,279,
        0,0,480,481,3,84,42,0,481,81,1,0,0,0,482,485,5,59,0,0,483,486,3,
        94,47,0,484,486,5,254,0,0,485,483,1,0,0,0,485,484,1,0,0,0,486,488,
        1,0,0,0,487,489,3,90,45,0,488,487,1,0,0,0,488,489,1,0,0,0,489,83,
        1,0,0,0,490,496,3,86,43,0,491,492,3,88,44,0,492,493,3,86,43,0,493,
        495,1,0,0,0,494,491,1,0,0,0,495,498,1,0,0,0,496,494,1,0,0,0,496,
        497,1,0,0,0,497,85,1,0,0,0,498,496,1,0,0,0,499,515,3,92,46,0,500,
        515,3,98,49,0,501,515,3,100,50,0,502,515,3,94,47,0,503,515,5,276,
        0,0,504,508,5,268,0,0,505,509,3,32,16,0,506,509,3,84,42,0,507,509,
        3,90,45,0,508,505,1,0,0,0,508,506,1,0,0,0,508,507,1,0,0,0,509,510,
        1,0,0,0,510,511,5,269,0,0,511,515,1,0,0,0,512,513,5,279,0,0,513,
        515,3,86,43,0,514,499,1,0,0,0,514,500,1,0,0,0,514,501,1,0,0,0,514,
        502,1,0,0,0,514,503,1,0,0,0,514,504,1,0,0,0,514,512,1,0,0,0,515,
        87,1,0,0,0,516,517,7,3,0,0,517,89,1,0,0,0,518,523,3,84,42,0,519,
        520,5,266,0,0,520,522,3,84,42,0,521,519,1,0,0,0,522,525,1,0,0,0,
        523,521,1,0,0,0,523,524,1,0,0,0,524,91,1,0,0,0,525,523,1,0,0,0,526,
        527,7,4,0,0,527,93,1,0,0,0,528,533,5,277,0,0,529,533,5,275,0,0,530,
        533,5,274,0,0,531,533,3,96,48,0,532,528,1,0,0,0,532,529,1,0,0,0,
        532,530,1,0,0,0,532,531,1,0,0,0,533,95,1,0,0,0,534,535,7,5,0,0,535,
        97,1,0,0,0,536,540,5,202,0,0,537,540,5,204,0,0,538,540,3,94,47,0,
        539,536,1,0,0,0,539,537,1,0,0,0,539,538,1,0,0,0,540,541,1,0,0,0,
        541,543,5,268,0,0,542,544,3,90,45,0,543,542,1,0,0,0,543,544,1,0,
        0,0,544,545,1,0,0,0,545,546,5,269,0,0,546,99,1,0,0,0,547,549,5,17,
        0,0,548,550,3,102,51,0,549,548,1,0,0,0,550,551,1,0,0,0,551,549,1,
        0,0,0,551,552,1,0,0,0,552,554,1,0,0,0,553,555,3,104,52,0,554,553,
        1,0,0,0,554,555,1,0,0,0,555,556,1,0,0,0,556,557,5,55,0,0,557,101,
        1,0,0,0,558,559,5,173,0,0,559,560,3,106,53,0,560,561,5,154,0,0,561,
        562,3,84,42,0,562,103,1,0,0,0,563,564,5,54,0,0,564,565,3,84,42,0,
        565,105,1,0,0,0,566,567,3,84,42,0,567,107,1,0,0,0,568,573,3,94,47,
        0,569,570,5,265,0,0,570,572,3,94,47,0,571,569,1,0,0,0,572,575,1,
        0,0,0,573,571,1,0,0,0,573,574,1,0,0,0,574,109,1,0,0,0,575,573,1,
        0,0,0,576,577,3,94,47,0,577,111,1,0,0,0,72,118,123,125,135,139,153,
        161,169,172,177,183,194,200,205,207,214,231,237,241,246,250,255,
        262,267,274,279,282,286,288,294,298,308,312,316,318,322,325,331,
        335,339,346,350,357,372,381,388,397,402,407,417,422,426,430,435,
        437,447,457,465,472,477,485,488,496,508,514,523,532,539,543,551,
        554,573
    ]

class SQLParser ( Parser ):

    grammarFileName = "SQLParser.g4"

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

    RULE_parse = 0
    RULE_sqlScript = 1
    RULE_batch = 2
    RULE_statement = 3
    RULE_ddlStatement = 4
    RULE_createTableStatement = 5
    RULE_columnDefinitionList = 6
    RULE_columnDefinition = 7
    RULE_dataType = 8
    RULE_typeSize = 9
    RULE_constraint = 10
    RULE_alterTableStatement = 11
    RULE_addColumnClause = 12
    RULE_dropConstraintClause = 13
    RULE_truncateStatement = 14
    RULE_dmlStatement = 15
    RULE_selectStatement = 16
    RULE_orderByList = 17
    RULE_orderByItem = 18
    RULE_selectList = 19
    RULE_selectItem = 20
    RULE_tableList = 21
    RULE_joinClause = 22
    RULE_joinType = 23
    RULE_tableRef = 24
    RULE_insertStatement = 25
    RULE_columnList = 26
    RULE_insertValues = 27
    RULE_updateStatement = 28
    RULE_assignments = 29
    RULE_assignment = 30
    RULE_deleteStatement = 31
    RULE_controlFlowStatement = 32
    RULE_ifStatement = 33
    RULE_thenBlock = 34
    RULE_elseBlock = 35
    RULE_blockStatement = 36
    RULE_tryCatchStatement = 37
    RULE_variableStatement = 38
    RULE_declareStatement = 39
    RULE_setStatement = 40
    RULE_execStatement = 41
    RULE_expression = 42
    RULE_primary = 43
    RULE_binaryOp = 44
    RULE_expressionList = 45
    RULE_literal = 46
    RULE_identifier = 47
    RULE_keywordAsIdentifier = 48
    RULE_functionCall = 49
    RULE_caseExpression = 50
    RULE_whenClause = 51
    RULE_elseClause = 52
    RULE_condition = 53
    RULE_tableName = 54
    RULE_columnName = 55

    ruleNames =  [ "parse", "sqlScript", "batch", "statement", "ddlStatement", 
                   "createTableStatement", "columnDefinitionList", "columnDefinition", 
                   "dataType", "typeSize", "constraint", "alterTableStatement", 
                   "addColumnClause", "dropConstraintClause", "truncateStatement", 
                   "dmlStatement", "selectStatement", "orderByList", "orderByItem", 
                   "selectList", "selectItem", "tableList", "joinClause", 
                   "joinType", "tableRef", "insertStatement", "columnList", 
                   "insertValues", "updateStatement", "assignments", "assignment", 
                   "deleteStatement", "controlFlowStatement", "ifStatement", 
                   "thenBlock", "elseBlock", "blockStatement", "tryCatchStatement", 
                   "variableStatement", "declareStatement", "setStatement", 
                   "execStatement", "expression", "primary", "binaryOp", 
                   "expressionList", "literal", "identifier", "keywordAsIdentifier", 
                   "functionCall", "caseExpression", "whenClause", "elseClause", 
                   "condition", "tableName", "columnName" ]

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




    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sqlScript(self):
            return self.getTypedRuleContext(SQLParser.SqlScriptContext,0)


        def EOF(self):
            return self.getToken(SQLParser.EOF, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParse" ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParse" ):
                listener.exitParse(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParse" ):
                return visitor.visitParse(self)
            else:
                return visitor.visitChildren(self)




    def parse(self):

        localctx = SQLParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.sqlScript()
            self.state = 113
            self.match(SQLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SqlScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def batch(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.BatchContext)
            else:
                return self.getTypedRuleContext(SQLParser.BatchContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_sqlScript

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

        localctx = SQLParser.SqlScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sqlScript)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576548721823581192) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & -9223372036854775791) != 0) or _la==160 or _la==165 or ((((_la - 224)) & ~0x3f) == 0 and ((1 << (_la - 224)) & 8796093024257) != 0):
                self.state = 115
                self.batch()
                self.state = 120
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
                return self.getTypedRuleContexts(SQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(SQLParser.StatementContext,i)


        def GO(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.GO)
            else:
                return self.getToken(SQLParser.GO, i)

        def getRuleIndex(self):
            return SQLParser.RULE_batch

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

        localctx = SQLParser.BatchContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_batch)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 123
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [3, 10, 33, 44, 46, 59, 82, 86, 145, 160, 165, 224, 267]:
                        self.state = 121
                        self.statement()
                        pass
                    elif token in [235]:
                        self.state = 122
                        self.match(SQLParser.GO)
                        pass
                    else:
                        raise NoViableAltException(self)


                else:
                    raise NoViableAltException(self)
                self.state = 125 
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
            return self.getTypedRuleContext(SQLParser.DdlStatementContext,0)


        def dmlStatement(self):
            return self.getTypedRuleContext(SQLParser.DmlStatementContext,0)


        def controlFlowStatement(self):
            return self.getTypedRuleContext(SQLParser.ControlFlowStatementContext,0)


        def variableStatement(self):
            return self.getTypedRuleContext(SQLParser.VariableStatementContext,0)


        def execStatement(self):
            return self.getTypedRuleContext(SQLParser.ExecStatementContext,0)


        def truncateStatement(self):
            return self.getTypedRuleContext(SQLParser.TruncateStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(SQLParser.BlockStatementContext,0)


        def SEMI(self):
            return self.getToken(SQLParser.SEMI, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_statement

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

        localctx = SQLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.ddlStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 128
                self.dmlStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 129
                self.controlFlowStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 130
                self.variableStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 131
                self.execStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 132
                self.truncateStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 133
                self.blockStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 134
                self.match(SQLParser.SEMI)
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
            return self.getTypedRuleContext(SQLParser.CreateTableStatementContext,0)


        def alterTableStatement(self):
            return self.getTypedRuleContext(SQLParser.AlterTableStatementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_ddlStatement

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

        localctx = SQLParser.DdlStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ddlStatement)
        try:
            self.state = 139
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [33]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.createTableStatement()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
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
            return self.getToken(SQLParser.CREATE, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def tableName(self):
            return self.getTypedRuleContext(SQLParser.TableNameContext,0)


        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def columnDefinitionList(self):
            return self.getTypedRuleContext(SQLParser.ColumnDefinitionListContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_createTableStatement

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

        localctx = SQLParser.CreateTableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_createTableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(SQLParser.CREATE)
            self.state = 142
            self.match(SQLParser.TABLE)
            self.state = 143
            self.tableName()
            self.state = 144
            self.match(SQLParser.LPAREN)
            self.state = 145
            self.columnDefinitionList()
            self.state = 146
            self.match(SQLParser.RPAREN)
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
                return self.getTypedRuleContexts(SQLParser.ColumnDefinitionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnDefinitionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_columnDefinitionList

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

        localctx = SQLParser.ColumnDefinitionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_columnDefinitionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148
            self.columnDefinition()
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 149
                self.match(SQLParser.COMMA)
                self.state = 150
                self.columnDefinition()
                self.state = 155
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
            return self.getTypedRuleContext(SQLParser.ColumnNameContext,0)


        def dataType(self):
            return self.getTypedRuleContext(SQLParser.DataTypeContext,0)


        def constraint(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ConstraintContext)
            else:
                return self.getTypedRuleContext(SQLParser.ConstraintContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_columnDefinition

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

        localctx = SQLParser.ColumnDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_columnDefinition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.columnName()
            self.state = 157
            self.dataType()
            self.state = 161
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 158
                    self.constraint() 
                self.state = 163
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
            return self.getToken(SQLParser.INT, 0)

        def NVARCHAR(self):
            return self.getToken(SQLParser.NVARCHAR, 0)

        def BIGINT(self):
            return self.getToken(SQLParser.BIGINT, 0)

        def DATE(self):
            return self.getToken(SQLParser.DATE, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def typeSize(self):
            return self.getTypedRuleContext(SQLParser.TypeSizeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_dataType

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

        localctx = SQLParser.DataTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_dataType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 164
                self.match(SQLParser.INT)
                pass

            elif la_ == 2:
                self.state = 165
                self.match(SQLParser.NVARCHAR)
                pass

            elif la_ == 3:
                self.state = 166
                self.match(SQLParser.BIGINT)
                pass

            elif la_ == 4:
                self.state = 167
                self.match(SQLParser.DATE)
                pass

            elif la_ == 5:
                self.state = 168
                self.identifier()
                pass


            self.state = 172
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==268:
                self.state = 171
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
            return self.getToken(SQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.NUMBER)
            else:
                return self.getToken(SQLParser.NUMBER, i)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_typeSize

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

        localctx = SQLParser.TypeSizeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_typeSize)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(SQLParser.LPAREN)
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [278]:
                self.state = 175
                self.match(SQLParser.NUMBER)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 274, 275, 277]:
                self.state = 176
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 179
                self.match(SQLParser.COMMA)
                self.state = 180
                self.match(SQLParser.NUMBER)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 186
            self.match(SQLParser.RPAREN)
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
                return self.getTokens(SQLParser.NOT)
            else:
                return self.getToken(SQLParser.NOT, i)

        def NULL(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.NULL)
            else:
                return self.getToken(SQLParser.NULL, i)

        def PRIMARY(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.PRIMARY)
            else:
                return self.getToken(SQLParser.PRIMARY, i)

        def KEY(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.KEY)
            else:
                return self.getToken(SQLParser.KEY, i)

        def DEFAULT(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.DEFAULT)
            else:
                return self.getToken(SQLParser.DEFAULT, i)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def identifier(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SQLParser.IdentifierContext,i)


        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.LPAREN)
            else:
                return self.getToken(SQLParser.LPAREN, i)

        def columnList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ColumnListContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnListContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.RPAREN)
            else:
                return self.getToken(SQLParser.RPAREN, i)

        def CLUSTERED(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.CLUSTERED)
            else:
                return self.getToken(SQLParser.CLUSTERED, i)

        def NONCLUSTERED(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.NONCLUSTERED)
            else:
                return self.getToken(SQLParser.NONCLUSTERED, i)

        def getRuleIndex(self):
            return SQLParser.RULE_constraint

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

        localctx = SQLParser.ConstraintContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_constraint)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 205
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        self.state = 188
                        self.match(SQLParser.NOT)
                        self.state = 189
                        self.match(SQLParser.NULL)
                        pass

                    elif la_ == 2:
                        self.state = 190
                        self.match(SQLParser.NULL)
                        pass

                    elif la_ == 3:
                        self.state = 191
                        self.match(SQLParser.PRIMARY)
                        self.state = 192
                        self.match(SQLParser.KEY)
                        self.state = 194
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                        if la_ == 1:
                            self.state = 193
                            _la = self._input.LA(1)
                            if not(_la==21 or _la==100):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()


                        self.state = 200
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==268:
                            self.state = 196
                            self.match(SQLParser.LPAREN)
                            self.state = 197
                            self.columnList()
                            self.state = 198
                            self.match(SQLParser.RPAREN)


                        pass

                    elif la_ == 4:
                        self.state = 202
                        self.match(SQLParser.DEFAULT)
                        self.state = 203
                        self.expression()
                        pass

                    elif la_ == 5:
                        self.state = 204
                        self.identifier()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 207 
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
            return self.getToken(SQLParser.ALTER, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def tableName(self):
            return self.getTypedRuleContext(SQLParser.TableNameContext,0)


        def addColumnClause(self):
            return self.getTypedRuleContext(SQLParser.AddColumnClauseContext,0)


        def dropConstraintClause(self):
            return self.getTypedRuleContext(SQLParser.DropConstraintClauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_alterTableStatement

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

        localctx = SQLParser.AlterTableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_alterTableStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(SQLParser.ALTER)
            self.state = 210
            self.match(SQLParser.TABLE)
            self.state = 211
            self.tableName()
            self.state = 214
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 212
                self.addColumnClause()
                pass
            elif token in [52]:
                self.state = 213
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
            return self.getToken(SQLParser.ADD, 0)

        def columnDefinition(self):
            return self.getTypedRuleContext(SQLParser.ColumnDefinitionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_addColumnClause

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

        localctx = SQLParser.AddColumnClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_addColumnClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.match(SQLParser.ADD)
            self.state = 217
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
            return self.getToken(SQLParser.DROP, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def CONSTRAINT(self):
            return self.getToken(SQLParser.CONSTRAINT, 0)

        def COLUMN(self):
            return self.getToken(SQLParser.COLUMN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_dropConstraintClause

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

        localctx = SQLParser.DropConstraintClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_dropConstraintClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(SQLParser.DROP)
            self.state = 220
            _la = self._input.LA(1)
            if not(_la==24 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 221
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
            return self.getToken(SQLParser.TRUNCATE, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def tableName(self):
            return self.getTypedRuleContext(SQLParser.TableNameContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_truncateStatement

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

        localctx = SQLParser.TruncateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_truncateStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(SQLParser.TRUNCATE)
            self.state = 224
            self.match(SQLParser.TABLE)
            self.state = 225
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
            return self.getTypedRuleContext(SQLParser.SelectStatementContext,0)


        def insertStatement(self):
            return self.getTypedRuleContext(SQLParser.InsertStatementContext,0)


        def updateStatement(self):
            return self.getTypedRuleContext(SQLParser.UpdateStatementContext,0)


        def deleteStatement(self):
            return self.getTypedRuleContext(SQLParser.DeleteStatementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_dmlStatement

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

        localctx = SQLParser.DmlStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_dmlStatement)
        try:
            self.state = 231
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [224]:
                self.enterOuterAlt(localctx, 1)
                self.state = 227
                self.selectStatement()
                pass
            elif token in [86]:
                self.enterOuterAlt(localctx, 2)
                self.state = 228
                self.insertStatement()
                pass
            elif token in [165]:
                self.enterOuterAlt(localctx, 3)
                self.state = 229
                self.updateStatement()
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 230
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
            return self.getToken(SQLParser.SELECT, 0)

        def selectList(self):
            return self.getTypedRuleContext(SQLParser.SelectListContext,0)


        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def tableList(self):
            return self.getTypedRuleContext(SQLParser.TableListContext,0)


        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def condition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ConditionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ConditionContext,i)


        def GROUP(self):
            return self.getToken(SQLParser.GROUP, 0)

        def BY(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.BY)
            else:
                return self.getToken(SQLParser.BY, i)

        def expressionList(self):
            return self.getTypedRuleContext(SQLParser.ExpressionListContext,0)


        def HAVING(self):
            return self.getToken(SQLParser.HAVING, 0)

        def ORDER(self):
            return self.getToken(SQLParser.ORDER, 0)

        def orderByList(self):
            return self.getTypedRuleContext(SQLParser.OrderByListContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_selectStatement

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

        localctx = SQLParser.SelectStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_selectStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(SQLParser.SELECT)
            self.state = 234
            self.selectList()
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==71:
                self.state = 235
                self.match(SQLParser.FROM)
                self.state = 236
                self.tableList()


            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==174:
                self.state = 239
                self.match(SQLParser.WHERE)
                self.state = 240
                self.condition()


            self.state = 246
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==76:
                self.state = 243
                self.match(SQLParser.GROUP)
                self.state = 244
                self.match(SQLParser.BY)
                self.state = 245
                self.expressionList()


            self.state = 250
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==77:
                self.state = 248
                self.match(SQLParser.HAVING)
                self.state = 249
                self.condition()


            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==115:
                self.state = 252
                self.match(SQLParser.ORDER)
                self.state = 253
                self.match(SQLParser.BY)
                self.state = 254
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
                return self.getTypedRuleContexts(SQLParser.OrderByItemContext)
            else:
                return self.getTypedRuleContext(SQLParser.OrderByItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_orderByList

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

        localctx = SQLParser.OrderByListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_orderByList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.orderByItem()
            self.state = 262
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 258
                self.match(SQLParser.COMMA)
                self.state = 259
                self.orderByItem()
                self.state = 264
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
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def ASC(self):
            return self.getToken(SQLParser.ASC, 0)

        def DESC(self):
            return self.getToken(SQLParser.DESC, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_orderByItem

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

        localctx = SQLParser.OrderByItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_orderByItem)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 265
            self.expression()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7 or _la==48:
                self.state = 266
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
                return self.getTypedRuleContexts(SQLParser.SelectItemContext)
            else:
                return self.getTypedRuleContext(SQLParser.SelectItemContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_selectList

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

        localctx = SQLParser.SelectListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_selectList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.selectItem()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 270
                self.match(SQLParser.COMMA)
                self.state = 271
                self.selectItem()
                self.state = 276
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
            return self.getToken(SQLParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def columnName(self):
            return self.getTypedRuleContext(SQLParser.ColumnNameContext,0)


        def literal(self):
            return self.getTypedRuleContext(SQLParser.LiteralContext,0)


        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_selectItem

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

        localctx = SQLParser.SelectItemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_selectItem)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 277
                self.match(SQLParser.OPERATOR)
                pass

            elif la_ == 2:
                self.state = 278
                self.expression()
                pass


            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 282
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 281
                    self.match(SQLParser.AS)


                self.state = 286
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 284
                    self.columnName()
                    pass

                elif la_ == 2:
                    self.state = 285
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
            return self.getTypedRuleContext(SQLParser.TableRefContext,0)


        def joinClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.JoinClauseContext)
            else:
                return self.getTypedRuleContext(SQLParser.JoinClauseContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_tableList

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

        localctx = SQLParser.TableListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_tableList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.tableRef()
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & 2367489) != 0) or _la==137:
                self.state = 291
                self.joinClause()
                self.state = 296
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
            return self.getToken(SQLParser.JOIN, 0)

        def tableRef(self):
            return self.getTypedRuleContext(SQLParser.TableRefContext,0)


        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def condition(self):
            return self.getTypedRuleContext(SQLParser.ConditionContext,0)


        def joinType(self):
            return self.getTypedRuleContext(SQLParser.JoinTypeContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_joinClause

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

        localctx = SQLParser.JoinClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_joinClause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 72)) & ~0x3f) == 0 and ((1 << (_la - 72)) & 2105345) != 0) or _la==137:
                self.state = 297
                self.joinType()


            self.state = 300
            self.match(SQLParser.JOIN)
            self.state = 301
            self.tableRef()
            self.state = 302
            self.match(SQLParser.ON)
            self.state = 303
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
            return self.getToken(SQLParser.INNER, 0)

        def LEFT(self):
            return self.getToken(SQLParser.LEFT, 0)

        def OUTER(self):
            return self.getToken(SQLParser.OUTER, 0)

        def RIGHT(self):
            return self.getToken(SQLParser.RIGHT, 0)

        def FULL(self):
            return self.getToken(SQLParser.FULL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_joinType

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

        localctx = SQLParser.JoinTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_joinType)
        self._la = 0 # Token type
        try:
            self.state = 318
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [85]:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.match(SQLParser.INNER)
                pass
            elif token in [93]:
                self.enterOuterAlt(localctx, 2)
                self.state = 306
                self.match(SQLParser.LEFT)
                self.state = 308
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==116:
                    self.state = 307
                    self.match(SQLParser.OUTER)


                pass
            elif token in [137]:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.match(SQLParser.RIGHT)
                self.state = 312
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==116:
                    self.state = 311
                    self.match(SQLParser.OUTER)


                pass
            elif token in [72]:
                self.enterOuterAlt(localctx, 4)
                self.state = 314
                self.match(SQLParser.FULL)
                self.state = 316
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==116:
                    self.state = 315
                    self.match(SQLParser.OUTER)


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
            return self.getTypedRuleContext(SQLParser.TableNameContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def selectStatement(self):
            return self.getTypedRuleContext(SQLParser.SelectStatementContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_tableRef

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

        localctx = SQLParser.TableRefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_tableRef)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 274, 275, 277]:
                self.enterOuterAlt(localctx, 1)
                self.state = 320
                self.tableName()
                self.state = 325
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 322
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 321
                        self.match(SQLParser.AS)


                    self.state = 324
                    self.identifier()


                pass
            elif token in [268]:
                self.enterOuterAlt(localctx, 2)
                self.state = 327
                self.match(SQLParser.LPAREN)
                self.state = 328
                self.selectStatement()
                self.state = 329
                self.match(SQLParser.RPAREN)

                self.state = 331
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 330
                    self.match(SQLParser.AS)


                self.state = 333
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
            return self.getToken(SQLParser.INSERT, 0)

        def tableName(self):
            return self.getTypedRuleContext(SQLParser.TableNameContext,0)


        def insertValues(self):
            return self.getTypedRuleContext(SQLParser.InsertValuesContext,0)


        def selectStatement(self):
            return self.getTypedRuleContext(SQLParser.SelectStatementContext,0)


        def INTO(self):
            return self.getToken(SQLParser.INTO, 0)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def columnList(self):
            return self.getTypedRuleContext(SQLParser.ColumnListContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_insertStatement

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

        localctx = SQLParser.InsertStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_insertStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 337
            self.match(SQLParser.INSERT)
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 338
                self.match(SQLParser.INTO)


            self.state = 341
            self.tableName()
            self.state = 346
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==268:
                self.state = 342
                self.match(SQLParser.LPAREN)
                self.state = 343
                self.columnList()
                self.state = 344
                self.match(SQLParser.RPAREN)


            self.state = 350
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [169]:
                self.state = 348
                self.insertValues()
                pass
            elif token in [224]:
                self.state = 349
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
                return self.getTypedRuleContexts(SQLParser.ColumnNameContext)
            else:
                return self.getTypedRuleContext(SQLParser.ColumnNameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_columnList

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

        localctx = SQLParser.ColumnListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_columnList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 352
            self.columnName()
            self.state = 357
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 353
                self.match(SQLParser.COMMA)
                self.state = 354
                self.columnName()
                self.state = 359
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
            return self.getToken(SQLParser.VALUES, 0)

        def LPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.LPAREN)
            else:
                return self.getToken(SQLParser.LPAREN, i)

        def expressionList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.ExpressionListContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionListContext,i)


        def RPAREN(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.RPAREN)
            else:
                return self.getToken(SQLParser.RPAREN, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_insertValues

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

        localctx = SQLParser.InsertValuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_insertValues)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 360
            self.match(SQLParser.VALUES)

            self.state = 361
            self.match(SQLParser.LPAREN)
            self.state = 362
            self.expressionList()
            self.state = 363
            self.match(SQLParser.RPAREN)
            self.state = 372
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 365
                self.match(SQLParser.COMMA)
                self.state = 366
                self.match(SQLParser.LPAREN)
                self.state = 367
                self.expressionList()
                self.state = 368
                self.match(SQLParser.RPAREN)
                self.state = 374
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
            return self.getToken(SQLParser.UPDATE, 0)

        def tableName(self):
            return self.getTypedRuleContext(SQLParser.TableNameContext,0)


        def SET(self):
            return self.getToken(SQLParser.SET, 0)

        def assignments(self):
            return self.getTypedRuleContext(SQLParser.AssignmentsContext,0)


        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(SQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_updateStatement

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

        localctx = SQLParser.UpdateStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_updateStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 375
            self.match(SQLParser.UPDATE)
            self.state = 376
            self.tableName()
            self.state = 377
            self.match(SQLParser.SET)
            self.state = 378
            self.assignments()
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==174:
                self.state = 379
                self.match(SQLParser.WHERE)
                self.state = 380
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
                return self.getTypedRuleContexts(SQLParser.AssignmentContext)
            else:
                return self.getTypedRuleContext(SQLParser.AssignmentContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_assignments

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

        localctx = SQLParser.AssignmentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_assignments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 383
            self.assignment()
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 384
                self.match(SQLParser.COMMA)
                self.state = 385
                self.assignment()
                self.state = 390
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
            return self.getTypedRuleContext(SQLParser.ColumnNameContext,0)


        def OPERATOR(self):
            return self.getToken(SQLParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_assignment

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

        localctx = SQLParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.columnName()
            self.state = 392
            self.match(SQLParser.OPERATOR)
            self.state = 393
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
            return self.getToken(SQLParser.DELETE, 0)

        def tableName(self):
            return self.getTypedRuleContext(SQLParser.TableNameContext,0)


        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(SQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_deleteStatement

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

        localctx = SQLParser.DeleteStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_deleteStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 395
            self.match(SQLParser.DELETE)
            self.state = 397
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 396
                self.match(SQLParser.FROM)


            self.state = 399
            self.tableName()
            self.state = 402
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==174:
                self.state = 400
                self.match(SQLParser.WHERE)
                self.state = 401
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
            return self.getTypedRuleContext(SQLParser.IfStatementContext,0)


        def tryCatchStatement(self):
            return self.getTypedRuleContext(SQLParser.TryCatchStatementContext,0)


        def blockStatement(self):
            return self.getTypedRuleContext(SQLParser.BlockStatementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_controlFlowStatement

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

        localctx = SQLParser.ControlFlowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_controlFlowStatement)
        try:
            self.state = 407
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 404
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 405
                self.tryCatchStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 406
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
            return self.getToken(SQLParser.IF, 0)

        def thenBlock(self):
            return self.getTypedRuleContext(SQLParser.ThenBlockContext,0)


        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def EXISTS(self):
            return self.getToken(SQLParser.EXISTS, 0)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def selectStatement(self):
            return self.getTypedRuleContext(SQLParser.SelectStatementContext,0)


        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def condition(self):
            return self.getTypedRuleContext(SQLParser.ConditionContext,0)


        def ELSE(self):
            return self.getToken(SQLParser.ELSE, 0)

        def elseBlock(self):
            return self.getTypedRuleContext(SQLParser.ElseBlockContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_ifStatement

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

        localctx = SQLParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.match(SQLParser.IF)
            self.state = 417
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 410
                self.match(SQLParser.NOT)
                self.state = 411
                self.match(SQLParser.EXISTS)
                self.state = 412
                self.match(SQLParser.LPAREN)
                self.state = 413
                self.selectStatement()
                self.state = 414
                self.match(SQLParser.RPAREN)

            elif la_ == 2:
                self.state = 416
                self.condition()


            self.state = 419
            self.thenBlock()
            self.state = 422
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 420
                self.match(SQLParser.ELSE)
                self.state = 421
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
            return self.getTypedRuleContext(SQLParser.BlockStatementContext,0)


        def statement(self):
            return self.getTypedRuleContext(SQLParser.StatementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_thenBlock

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

        localctx = SQLParser.ThenBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_thenBlock)
        try:
            self.state = 426
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 425
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
            return self.getTypedRuleContext(SQLParser.BlockStatementContext,0)


        def statement(self):
            return self.getTypedRuleContext(SQLParser.StatementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_elseBlock

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

        localctx = SQLParser.ElseBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_elseBlock)
        try:
            self.state = 430
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 428
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 429
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
            return self.getToken(SQLParser.BEGIN, 0)

        def END(self):
            return self.getToken(SQLParser.END, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(SQLParser.StatementContext,i)


        def GO(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.GO)
            else:
                return self.getToken(SQLParser.GO, i)

        def getRuleIndex(self):
            return SQLParser.RULE_blockStatement

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

        localctx = SQLParser.BlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_blockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self.match(SQLParser.BEGIN)
            self.state = 437
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576548721823581192) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & -9223372036854775791) != 0) or _la==160 or _la==165 or ((((_la - 224)) & ~0x3f) == 0 and ((1 << (_la - 224)) & 8796093024257) != 0):
                self.state = 435
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [3, 10, 33, 44, 46, 59, 82, 86, 145, 160, 165, 224, 267]:
                    self.state = 433
                    self.statement()
                    pass
                elif token in [235]:
                    self.state = 434
                    self.match(SQLParser.GO)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 439
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 440
            self.match(SQLParser.END)
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
                return self.getTokens(SQLParser.BEGIN)
            else:
                return self.getToken(SQLParser.BEGIN, i)

        def TRY(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.TRY)
            else:
                return self.getToken(SQLParser.TRY, i)

        def END(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.END)
            else:
                return self.getToken(SQLParser.END, i)

        def CATCH(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.CATCH)
            else:
                return self.getToken(SQLParser.CATCH, i)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.StatementContext)
            else:
                return self.getTypedRuleContext(SQLParser.StatementContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_tryCatchStatement

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

        localctx = SQLParser.TryCatchStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_tryCatchStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 442
            self.match(SQLParser.BEGIN)
            self.state = 443
            self.match(SQLParser.TRY)
            self.state = 447
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576548721823581192) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & -9223372036854775791) != 0) or _la==160 or _la==165 or _la==224 or _la==267:
                self.state = 444
                self.statement()
                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 450
            self.match(SQLParser.END)
            self.state = 451
            self.match(SQLParser.TRY)
            self.state = 452
            self.match(SQLParser.BEGIN)
            self.state = 453
            self.match(SQLParser.CATCH)
            self.state = 457
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 576548721823581192) != 0) or ((((_la - 82)) & ~0x3f) == 0 and ((1 << (_la - 82)) & -9223372036854775791) != 0) or _la==160 or _la==165 or _la==224 or _la==267:
                self.state = 454
                self.statement()
                self.state = 459
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 460
            self.match(SQLParser.END)
            self.state = 461
            self.match(SQLParser.CATCH)
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
            return self.getTypedRuleContext(SQLParser.DeclareStatementContext,0)


        def setStatement(self):
            return self.getTypedRuleContext(SQLParser.SetStatementContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_variableStatement

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

        localctx = SQLParser.VariableStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_variableStatement)
        try:
            self.state = 465
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 463
                self.declareStatement()
                pass
            elif token in [145]:
                self.enterOuterAlt(localctx, 2)
                self.state = 464
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
            return self.getToken(SQLParser.DECLARE, 0)

        def VARIABLE(self):
            return self.getToken(SQLParser.VARIABLE, 0)

        def dataType(self):
            return self.getTypedRuleContext(SQLParser.DataTypeContext,0)


        def OPERATOR(self):
            return self.getToken(SQLParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_declareStatement

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

        localctx = SQLParser.DeclareStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_declareStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            self.match(SQLParser.DECLARE)
            self.state = 468
            self.match(SQLParser.VARIABLE)
            self.state = 469
            self.dataType()
            self.state = 472
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==279:
                self.state = 470
                self.match(SQLParser.OPERATOR)
                self.state = 471
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
            return self.getToken(SQLParser.SET, 0)

        def OPERATOR(self):
            return self.getToken(SQLParser.OPERATOR, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def VARIABLE(self):
            return self.getToken(SQLParser.VARIABLE, 0)

        def columnName(self):
            return self.getTypedRuleContext(SQLParser.ColumnNameContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_setStatement

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

        localctx = SQLParser.SetStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_setStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.match(SQLParser.SET)
            self.state = 477
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [276]:
                self.state = 475
                self.match(SQLParser.VARIABLE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264, 274, 275, 277]:
                self.state = 476
                self.columnName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 479
            self.match(SQLParser.OPERATOR)
            self.state = 480
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
            return self.getToken(SQLParser.EXEC, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def SP_EXECUTESQL(self):
            return self.getToken(SQLParser.SP_EXECUTESQL, 0)

        def expressionList(self):
            return self.getTypedRuleContext(SQLParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_execStatement

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

        localctx = SQLParser.ExecStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_execStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 482
            self.match(SQLParser.EXEC)
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 483
                self.identifier()
                pass

            elif la_ == 2:
                self.state = 484
                self.match(SQLParser.SP_EXECUTESQL)
                pass


            self.state = 488
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 487
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
                return self.getTypedRuleContexts(SQLParser.PrimaryContext)
            else:
                return self.getTypedRuleContext(SQLParser.PrimaryContext,i)


        def binaryOp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.BinaryOpContext)
            else:
                return self.getTypedRuleContext(SQLParser.BinaryOpContext,i)


        def getRuleIndex(self):
            return SQLParser.RULE_expression

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

        localctx = SQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.primary()
            self.state = 496
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 491
                    self.binaryOp()
                    self.state = 492
                    self.primary() 
                self.state = 498
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
            return self.getTypedRuleContext(SQLParser.LiteralContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(SQLParser.FunctionCallContext,0)


        def caseExpression(self):
            return self.getTypedRuleContext(SQLParser.CaseExpressionContext,0)


        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def VARIABLE(self):
            return self.getToken(SQLParser.VARIABLE, 0)

        def LPAREN(self):
            return self.getToken(SQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def selectStatement(self):
            return self.getTypedRuleContext(SQLParser.SelectStatementContext,0)


        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(SQLParser.ExpressionListContext,0)


        def OPERATOR(self):
            return self.getToken(SQLParser.OPERATOR, 0)

        def primary(self):
            return self.getTypedRuleContext(SQLParser.PrimaryContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_primary

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

        localctx = SQLParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_primary)
        try:
            self.state = 514
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 499
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 500
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 501
                self.caseExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 502
                self.identifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 503
                self.match(SQLParser.VARIABLE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 504
                self.match(SQLParser.LPAREN)
                self.state = 508
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 505
                    self.selectStatement()
                    pass

                elif la_ == 2:
                    self.state = 506
                    self.expression()
                    pass

                elif la_ == 3:
                    self.state = 507
                    self.expressionList()
                    pass


                self.state = 510
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 512
                self.match(SQLParser.OPERATOR)
                self.state = 513
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
            return self.getToken(SQLParser.OPERATOR, 0)

        def AND(self):
            return self.getToken(SQLParser.AND, 0)

        def OR(self):
            return self.getToken(SQLParser.OR, 0)

        def IN(self):
            return self.getToken(SQLParser.IN, 0)

        def IS(self):
            return self.getToken(SQLParser.IS, 0)

        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def LIKE(self):
            return self.getToken(SQLParser.LIKE, 0)

        def BETWEEN(self):
            return self.getToken(SQLParser.BETWEEN, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_binaryOp

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

        localctx = SQLParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
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
                return self.getTypedRuleContexts(SQLParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SQLParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.COMMA)
            else:
                return self.getToken(SQLParser.COMMA, i)

        def getRuleIndex(self):
            return SQLParser.RULE_expressionList

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

        localctx = SQLParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.expression()
            self.state = 523
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==266:
                self.state = 519
                self.match(SQLParser.COMMA)
                self.state = 520
                self.expression()
                self.state = 525
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
            return self.getToken(SQLParser.NUMBER, 0)

        def STRING_SINGLE(self):
            return self.getToken(SQLParser.STRING_SINGLE, 0)

        def STRING_DOUBLE(self):
            return self.getToken(SQLParser.STRING_DOUBLE, 0)

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_literal

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

        localctx = SQLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
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
            return self.getToken(SQLParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(SQLParser.BRACKET_IDENTIFIER, 0)

        def STRING_DOUBLE(self):
            return self.getToken(SQLParser.STRING_DOUBLE, 0)

        def keywordAsIdentifier(self):
            return self.getTypedRuleContext(SQLParser.KeywordAsIdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_identifier

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

        localctx = SQLParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_identifier)
        try:
            self.state = 532
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [277]:
                self.enterOuterAlt(localctx, 1)
                self.state = 528
                self.match(SQLParser.IDENTIFIER)
                pass
            elif token in [275]:
                self.enterOuterAlt(localctx, 2)
                self.state = 529
                self.match(SQLParser.BRACKET_IDENTIFIER)
                pass
            elif token in [274]:
                self.enterOuterAlt(localctx, 3)
                self.state = 530
                self.match(SQLParser.STRING_DOUBLE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264]:
                self.enterOuterAlt(localctx, 4)
                self.state = 531
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
            return self.getToken(SQLParser.ADD, 0)

        def ALL(self):
            return self.getToken(SQLParser.ALL, 0)

        def ALTER(self):
            return self.getToken(SQLParser.ALTER, 0)

        def AND(self):
            return self.getToken(SQLParser.AND, 0)

        def ANY(self):
            return self.getToken(SQLParser.ANY, 0)

        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def ASC(self):
            return self.getToken(SQLParser.ASC, 0)

        def AUTHORIZATION(self):
            return self.getToken(SQLParser.AUTHORIZATION, 0)

        def BACKUP(self):
            return self.getToken(SQLParser.BACKUP, 0)

        def BEGIN(self):
            return self.getToken(SQLParser.BEGIN, 0)

        def BETWEEN(self):
            return self.getToken(SQLParser.BETWEEN, 0)

        def BREAK(self):
            return self.getToken(SQLParser.BREAK, 0)

        def BULK(self):
            return self.getToken(SQLParser.BULK, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def CASCADE(self):
            return self.getToken(SQLParser.CASCADE, 0)

        def CASE(self):
            return self.getToken(SQLParser.CASE, 0)

        def CHECK(self):
            return self.getToken(SQLParser.CHECK, 0)

        def CHECKPOINT(self):
            return self.getToken(SQLParser.CHECKPOINT, 0)

        def CLOSE(self):
            return self.getToken(SQLParser.CLOSE, 0)

        def CLUSTERED(self):
            return self.getToken(SQLParser.CLUSTERED, 0)

        def COALESCE(self):
            return self.getToken(SQLParser.COALESCE, 0)

        def COLLATE(self):
            return self.getToken(SQLParser.COLLATE, 0)

        def COLUMN(self):
            return self.getToken(SQLParser.COLUMN, 0)

        def COMMIT(self):
            return self.getToken(SQLParser.COMMIT, 0)

        def COMPUTE(self):
            return self.getToken(SQLParser.COMPUTE, 0)

        def CONSTRAINT(self):
            return self.getToken(SQLParser.CONSTRAINT, 0)

        def CONTAINS(self):
            return self.getToken(SQLParser.CONTAINS, 0)

        def CONTINUE(self):
            return self.getToken(SQLParser.CONTINUE, 0)

        def CONVERT(self):
            return self.getToken(SQLParser.CONVERT, 0)

        def CAST(self):
            return self.getToken(SQLParser.CAST, 0)

        def CREATE(self):
            return self.getToken(SQLParser.CREATE, 0)

        def CROSS(self):
            return self.getToken(SQLParser.CROSS, 0)

        def CURRENT(self):
            return self.getToken(SQLParser.CURRENT, 0)

        def CURRENT_DATE(self):
            return self.getToken(SQLParser.CURRENT_DATE, 0)

        def CURRENT_TIME(self):
            return self.getToken(SQLParser.CURRENT_TIME, 0)

        def CURRENT_TIMESTAMP(self):
            return self.getToken(SQLParser.CURRENT_TIMESTAMP, 0)

        def CURRENT_USER(self):
            return self.getToken(SQLParser.CURRENT_USER, 0)

        def CURSOR(self):
            return self.getToken(SQLParser.CURSOR, 0)

        def DATABASE(self):
            return self.getToken(SQLParser.DATABASE, 0)

        def DBCC(self):
            return self.getToken(SQLParser.DBCC, 0)

        def DEALLOCATE(self):
            return self.getToken(SQLParser.DEALLOCATE, 0)

        def DECLARE(self):
            return self.getToken(SQLParser.DECLARE, 0)

        def DEFAULT(self):
            return self.getToken(SQLParser.DEFAULT, 0)

        def DELETE(self):
            return self.getToken(SQLParser.DELETE, 0)

        def DENY(self):
            return self.getToken(SQLParser.DENY, 0)

        def DESC(self):
            return self.getToken(SQLParser.DESC, 0)

        def DISTINCT(self):
            return self.getToken(SQLParser.DISTINCT, 0)

        def DISTRIBUTED(self):
            return self.getToken(SQLParser.DISTRIBUTED, 0)

        def DOUBLE(self):
            return self.getToken(SQLParser.DOUBLE, 0)

        def DROP(self):
            return self.getToken(SQLParser.DROP, 0)

        def DUMP(self):
            return self.getToken(SQLParser.DUMP, 0)

        def ELSE(self):
            return self.getToken(SQLParser.ELSE, 0)

        def END(self):
            return self.getToken(SQLParser.END, 0)

        def ERRLVL(self):
            return self.getToken(SQLParser.ERRLVL, 0)

        def ESCAPE(self):
            return self.getToken(SQLParser.ESCAPE, 0)

        def EXCEPT(self):
            return self.getToken(SQLParser.EXCEPT, 0)

        def EXEC(self):
            return self.getToken(SQLParser.EXEC, 0)

        def EXECUTE(self):
            return self.getToken(SQLParser.EXECUTE, 0)

        def EXISTS(self):
            return self.getToken(SQLParser.EXISTS, 0)

        def EXIT(self):
            return self.getToken(SQLParser.EXIT, 0)

        def EXTERNAL(self):
            return self.getToken(SQLParser.EXTERNAL, 0)

        def FETCH(self):
            return self.getToken(SQLParser.FETCH, 0)

        def FILE(self):
            return self.getToken(SQLParser.FILE, 0)

        def FILLFACTOR(self):
            return self.getToken(SQLParser.FILLFACTOR, 0)

        def FOR(self):
            return self.getToken(SQLParser.FOR, 0)

        def FOREIGN(self):
            return self.getToken(SQLParser.FOREIGN, 0)

        def FREETEXT(self):
            return self.getToken(SQLParser.FREETEXT, 0)

        def FREETEXTTABLE(self):
            return self.getToken(SQLParser.FREETEXTTABLE, 0)

        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def FULL(self):
            return self.getToken(SQLParser.FULL, 0)

        def FUNCTION(self):
            return self.getToken(SQLParser.FUNCTION, 0)

        def GOTO(self):
            return self.getToken(SQLParser.GOTO, 0)

        def GRANT(self):
            return self.getToken(SQLParser.GRANT, 0)

        def GROUP(self):
            return self.getToken(SQLParser.GROUP, 0)

        def HAVING(self):
            return self.getToken(SQLParser.HAVING, 0)

        def HOLDLOCK(self):
            return self.getToken(SQLParser.HOLDLOCK, 0)

        def IDENTITY(self):
            return self.getToken(SQLParser.IDENTITY, 0)

        def IDENTITY_INSERT(self):
            return self.getToken(SQLParser.IDENTITY_INSERT, 0)

        def IDENTITYCOL(self):
            return self.getToken(SQLParser.IDENTITYCOL, 0)

        def IF(self):
            return self.getToken(SQLParser.IF, 0)

        def IN(self):
            return self.getToken(SQLParser.IN, 0)

        def INDEX(self):
            return self.getToken(SQLParser.INDEX, 0)

        def INNER(self):
            return self.getToken(SQLParser.INNER, 0)

        def INSERT(self):
            return self.getToken(SQLParser.INSERT, 0)

        def INTERSECT(self):
            return self.getToken(SQLParser.INTERSECT, 0)

        def INTO(self):
            return self.getToken(SQLParser.INTO, 0)

        def IS(self):
            return self.getToken(SQLParser.IS, 0)

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def KEY(self):
            return self.getToken(SQLParser.KEY, 0)

        def KILL(self):
            return self.getToken(SQLParser.KILL, 0)

        def LEFT(self):
            return self.getToken(SQLParser.LEFT, 0)

        def LIKE(self):
            return self.getToken(SQLParser.LIKE, 0)

        def LINENO(self):
            return self.getToken(SQLParser.LINENO, 0)

        def LOAD(self):
            return self.getToken(SQLParser.LOAD, 0)

        def MERGE(self):
            return self.getToken(SQLParser.MERGE, 0)

        def NATIONAL(self):
            return self.getToken(SQLParser.NATIONAL, 0)

        def NOCHECK(self):
            return self.getToken(SQLParser.NOCHECK, 0)

        def NONCLUSTERED(self):
            return self.getToken(SQLParser.NONCLUSTERED, 0)

        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def NULLIF(self):
            return self.getToken(SQLParser.NULLIF, 0)

        def OF(self):
            return self.getToken(SQLParser.OF, 0)

        def OFF(self):
            return self.getToken(SQLParser.OFF, 0)

        def OFFSETS(self):
            return self.getToken(SQLParser.OFFSETS, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def OPEN(self):
            return self.getToken(SQLParser.OPEN, 0)

        def OPENDATASOURCE(self):
            return self.getToken(SQLParser.OPENDATASOURCE, 0)

        def OPENQUERY(self):
            return self.getToken(SQLParser.OPENQUERY, 0)

        def OPENROWSET(self):
            return self.getToken(SQLParser.OPENROWSET, 0)

        def OPENXML(self):
            return self.getToken(SQLParser.OPENXML, 0)

        def OPTION(self):
            return self.getToken(SQLParser.OPTION, 0)

        def OR(self):
            return self.getToken(SQLParser.OR, 0)

        def ORDER(self):
            return self.getToken(SQLParser.ORDER, 0)

        def OUTER(self):
            return self.getToken(SQLParser.OUTER, 0)

        def OVER(self):
            return self.getToken(SQLParser.OVER, 0)

        def PERCENT(self):
            return self.getToken(SQLParser.PERCENT, 0)

        def PLAN(self):
            return self.getToken(SQLParser.PLAN, 0)

        def PRECISION(self):
            return self.getToken(SQLParser.PRECISION, 0)

        def PRIMARY(self):
            return self.getToken(SQLParser.PRIMARY, 0)

        def PRINT(self):
            return self.getToken(SQLParser.PRINT, 0)

        def PROC(self):
            return self.getToken(SQLParser.PROC, 0)

        def PROCEDURE(self):
            return self.getToken(SQLParser.PROCEDURE, 0)

        def PUBLIC(self):
            return self.getToken(SQLParser.PUBLIC, 0)

        def RAISERROR(self):
            return self.getToken(SQLParser.RAISERROR, 0)

        def READ(self):
            return self.getToken(SQLParser.READ, 0)

        def READTEXT(self):
            return self.getToken(SQLParser.READTEXT, 0)

        def RECONFIGURE(self):
            return self.getToken(SQLParser.RECONFIGURE, 0)

        def REFERENCES(self):
            return self.getToken(SQLParser.REFERENCES, 0)

        def REPLICATION(self):
            return self.getToken(SQLParser.REPLICATION, 0)

        def RESTORE(self):
            return self.getToken(SQLParser.RESTORE, 0)

        def RESTRICT(self):
            return self.getToken(SQLParser.RESTRICT, 0)

        def RETURN(self):
            return self.getToken(SQLParser.RETURN, 0)

        def REVERT(self):
            return self.getToken(SQLParser.REVERT, 0)

        def REVOKE(self):
            return self.getToken(SQLParser.REVOKE, 0)

        def RIGHT(self):
            return self.getToken(SQLParser.RIGHT, 0)

        def ROLLBACK(self):
            return self.getToken(SQLParser.ROLLBACK, 0)

        def ROWCOUNT(self):
            return self.getToken(SQLParser.ROWCOUNT, 0)

        def ROWGUIDCOL(self):
            return self.getToken(SQLParser.ROWGUIDCOL, 0)

        def RULE(self):
            return self.getToken(SQLParser.RULE, 0)

        def SAVE(self):
            return self.getToken(SQLParser.SAVE, 0)

        def SAVEPOINT(self):
            return self.getToken(SQLParser.SAVEPOINT, 0)

        def SCHEMA(self):
            return self.getToken(SQLParser.SCHEMA, 0)

        def SCHEMA_NAME(self):
            return self.getToken(SQLParser.SCHEMA_NAME, 0)

        def SESSION_USER(self):
            return self.getToken(SQLParser.SESSION_USER, 0)

        def SET(self):
            return self.getToken(SQLParser.SET, 0)

        def SETUSER(self):
            return self.getToken(SQLParser.SETUSER, 0)

        def SHUTDOWN(self):
            return self.getToken(SQLParser.SHUTDOWN, 0)

        def SOME(self):
            return self.getToken(SQLParser.SOME, 0)

        def STATISTICS(self):
            return self.getToken(SQLParser.STATISTICS, 0)

        def SYSTEM_USER(self):
            return self.getToken(SQLParser.SYSTEM_USER, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def TABLESAMPLE(self):
            return self.getToken(SQLParser.TABLESAMPLE, 0)

        def TEXTSIZE(self):
            return self.getToken(SQLParser.TEXTSIZE, 0)

        def THEN(self):
            return self.getToken(SQLParser.THEN, 0)

        def TO(self):
            return self.getToken(SQLParser.TO, 0)

        def TOP(self):
            return self.getToken(SQLParser.TOP, 0)

        def TRAN(self):
            return self.getToken(SQLParser.TRAN, 0)

        def TRANSACTION(self):
            return self.getToken(SQLParser.TRANSACTION, 0)

        def TRIGGER(self):
            return self.getToken(SQLParser.TRIGGER, 0)

        def TRUNCATE(self):
            return self.getToken(SQLParser.TRUNCATE, 0)

        def TSEQUAL(self):
            return self.getToken(SQLParser.TSEQUAL, 0)

        def UNION(self):
            return self.getToken(SQLParser.UNION, 0)

        def UNIQUE(self):
            return self.getToken(SQLParser.UNIQUE, 0)

        def UNPIVOT(self):
            return self.getToken(SQLParser.UNPIVOT, 0)

        def UPDATE(self):
            return self.getToken(SQLParser.UPDATE, 0)

        def UPDATETEXT(self):
            return self.getToken(SQLParser.UPDATETEXT, 0)

        def USE(self):
            return self.getToken(SQLParser.USE, 0)

        def USER(self):
            return self.getToken(SQLParser.USER, 0)

        def VALUES(self):
            return self.getToken(SQLParser.VALUES, 0)

        def VARYING(self):
            return self.getToken(SQLParser.VARYING, 0)

        def VIEW(self):
            return self.getToken(SQLParser.VIEW, 0)

        def WAITFOR(self):
            return self.getToken(SQLParser.WAITFOR, 0)

        def WHEN(self):
            return self.getToken(SQLParser.WHEN, 0)

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def WHILE(self):
            return self.getToken(SQLParser.WHILE, 0)

        def WITH(self):
            return self.getToken(SQLParser.WITH, 0)

        def WRITETEXT(self):
            return self.getToken(SQLParser.WRITETEXT, 0)

        def INT(self):
            return self.getToken(SQLParser.INT, 0)

        def BIGINT(self):
            return self.getToken(SQLParser.BIGINT, 0)

        def SMALLINT(self):
            return self.getToken(SQLParser.SMALLINT, 0)

        def TINYINT(self):
            return self.getToken(SQLParser.TINYINT, 0)

        def BIT(self):
            return self.getToken(SQLParser.BIT, 0)

        def DECIMAL(self):
            return self.getToken(SQLParser.DECIMAL, 0)

        def NUMERIC(self):
            return self.getToken(SQLParser.NUMERIC, 0)

        def FLOAT(self):
            return self.getToken(SQLParser.FLOAT, 0)

        def REAL(self):
            return self.getToken(SQLParser.REAL, 0)

        def MONEY(self):
            return self.getToken(SQLParser.MONEY, 0)

        def SMALLMONEY(self):
            return self.getToken(SQLParser.SMALLMONEY, 0)

        def CHAR(self):
            return self.getToken(SQLParser.CHAR, 0)

        def NCHAR(self):
            return self.getToken(SQLParser.NCHAR, 0)

        def VARCHAR(self):
            return self.getToken(SQLParser.VARCHAR, 0)

        def NVARCHAR(self):
            return self.getToken(SQLParser.NVARCHAR, 0)

        def TEXT(self):
            return self.getToken(SQLParser.TEXT, 0)

        def NTEXT(self):
            return self.getToken(SQLParser.NTEXT, 0)

        def DATE(self):
            return self.getToken(SQLParser.DATE, 0)

        def DATETIME(self):
            return self.getToken(SQLParser.DATETIME, 0)

        def TIME(self):
            return self.getToken(SQLParser.TIME, 0)

        def TIMESTAMP(self):
            return self.getToken(SQLParser.TIMESTAMP, 0)

        def UNIQUEIDENTIFIER(self):
            return self.getToken(SQLParser.UNIQUEIDENTIFIER, 0)

        def SQL_VARIANT(self):
            return self.getToken(SQLParser.SQL_VARIANT, 0)

        def XML(self):
            return self.getToken(SQLParser.XML, 0)

        def COUNT(self):
            return self.getToken(SQLParser.COUNT, 0)

        def MAX(self):
            return self.getToken(SQLParser.MAX, 0)

        def MIN(self):
            return self.getToken(SQLParser.MIN, 0)

        def AVG(self):
            return self.getToken(SQLParser.AVG, 0)

        def SUM(self):
            return self.getToken(SQLParser.SUM, 0)

        def LEN(self):
            return self.getToken(SQLParser.LEN, 0)

        def UPPER(self):
            return self.getToken(SQLParser.UPPER, 0)

        def LOWER(self):
            return self.getToken(SQLParser.LOWER, 0)

        def GETDATE(self):
            return self.getToken(SQLParser.GETDATE, 0)

        def ISNULL(self):
            return self.getToken(SQLParser.ISNULL, 0)

        def SUBSTRING(self):
            return self.getToken(SQLParser.SUBSTRING, 0)

        def DATEADD(self):
            return self.getToken(SQLParser.DATEADD, 0)

        def DATEDIFF(self):
            return self.getToken(SQLParser.DATEDIFF, 0)

        def ROUND(self):
            return self.getToken(SQLParser.ROUND, 0)

        def CEILING(self):
            return self.getToken(SQLParser.CEILING, 0)

        def FLOOR(self):
            return self.getToken(SQLParser.FLOOR, 0)

        def FALSE(self):
            return self.getToken(SQLParser.FALSE, 0)

        def ILIKE(self):
            return self.getToken(SQLParser.ILIKE, 0)

        def LIMIT(self):
            return self.getToken(SQLParser.LIMIT, 0)

        def NATURAL(self):
            return self.getToken(SQLParser.NATURAL, 0)

        def PARTITION(self):
            return self.getToken(SQLParser.PARTITION, 0)

        def OFFSET(self):
            return self.getToken(SQLParser.OFFSET, 0)

        def RETURNING(self):
            return self.getToken(SQLParser.RETURNING, 0)

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def UNNEST(self):
            return self.getToken(SQLParser.UNNEST, 0)

        def WINDOW(self):
            return self.getToken(SQLParser.WINDOW, 0)

        def TEMP(self):
            return self.getToken(SQLParser.TEMP, 0)

        def TEMPORARY(self):
            return self.getToken(SQLParser.TEMPORARY, 0)

        def LOOP(self):
            return self.getToken(SQLParser.LOOP, 0)

        def REPLACE(self):
            return self.getToken(SQLParser.REPLACE, 0)

        def MATERIALIZED(self):
            return self.getToken(SQLParser.MATERIALIZED, 0)

        def FIRST(self):
            return self.getToken(SQLParser.FIRST, 0)

        def TRY(self):
            return self.getToken(SQLParser.TRY, 0)

        def CATCH(self):
            return self.getToken(SQLParser.CATCH, 0)

        def GO(self):
            return self.getToken(SQLParser.GO, 0)

        def QUOTENAME(self):
            return self.getToken(SQLParser.QUOTENAME, 0)

        def ERROR_MESSAGE(self):
            return self.getToken(SQLParser.ERROR_MESSAGE, 0)

        def ERROR_SEVERITY(self):
            return self.getToken(SQLParser.ERROR_SEVERITY, 0)

        def ERROR_STATE(self):
            return self.getToken(SQLParser.ERROR_STATE, 0)

        def OBJECT(self):
            return self.getToken(SQLParser.OBJECT, 0)

        def TYPE(self):
            return self.getToken(SQLParser.TYPE, 0)

        def INFORMATION_SCHEMA(self):
            return self.getToken(SQLParser.INFORMATION_SCHEMA, 0)

        def TABLES(self):
            return self.getToken(SQLParser.TABLES, 0)

        def BASE(self):
            return self.getToken(SQLParser.BASE, 0)

        def COLUMNS(self):
            return self.getToken(SQLParser.COLUMNS, 0)

        def KEYS(self):
            return self.getToken(SQLParser.KEYS, 0)

        def PARENT(self):
            return self.getToken(SQLParser.PARENT, 0)

        def SEQUENCES(self):
            return self.getToken(SQLParser.SEQUENCES, 0)

        def OUTPUT(self):
            return self.getToken(SQLParser.OUTPUT, 0)

        def OPENJSON(self):
            return self.getToken(SQLParser.OPENJSON, 0)

        def SP_EXECUTESQL(self):
            return self.getToken(SQLParser.SP_EXECUTESQL, 0)

        def FOREIGN_KEYS(self):
            return self.getToken(SQLParser.FOREIGN_KEYS, 0)

        def PARENT_OBJECT_ID(self):
            return self.getToken(SQLParser.PARENT_OBJECT_ID, 0)

        def EXECPT(self):
            return self.getToken(SQLParser.EXECPT, 0)

        def OBJECT_ID(self):
            return self.getToken(SQLParser.OBJECT_ID, 0)

        def OBJECT_NAME(self):
            return self.getToken(SQLParser.OBJECT_NAME, 0)

        def OBJECT_SCHEMA_NAME(self):
            return self.getToken(SQLParser.OBJECT_SCHEMA_NAME, 0)

        def TABLE_SCHEMA(self):
            return self.getToken(SQLParser.TABLE_SCHEMA, 0)

        def TABLE_NAME(self):
            return self.getToken(SQLParser.TABLE_NAME, 0)

        def TABLE_TYPE(self):
            return self.getToken(SQLParser.TABLE_TYPE, 0)

        def VERSION(self):
            return self.getToken(SQLParser.VERSION, 0)

        def getRuleIndex(self):
            return SQLParser.RULE_keywordAsIdentifier

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

        localctx = SQLParser.KeywordAsIdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_keywordAsIdentifier)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
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
            return self.getToken(SQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SQLParser.RPAREN, 0)

        def MAX(self):
            return self.getToken(SQLParser.MAX, 0)

        def AVG(self):
            return self.getToken(SQLParser.AVG, 0)

        def identifier(self):
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def expressionList(self):
            return self.getTypedRuleContext(SQLParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_functionCall

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

        localctx = SQLParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 536
                self.match(SQLParser.MAX)
                pass

            elif la_ == 2:
                self.state = 537
                self.match(SQLParser.AVG)
                pass

            elif la_ == 3:
                self.state = 538
                self.identifier()
                pass


            self.state = 541
            self.match(SQLParser.LPAREN)
            self.state = 543
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & -536879106) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & -1) != 0) or ((((_la - 128)) & ~0x3f) == 0 and ((1 << (_la - 128)) & -1) != 0) or ((((_la - 192)) & ~0x3f) == 0 and ((1 << (_la - 192)) & -1) != 0) or ((((_la - 256)) & ~0x3f) == 0 and ((1 << (_la - 256)) & 16650751) != 0):
                self.state = 542
                self.expressionList()


            self.state = 545
            self.match(SQLParser.RPAREN)
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
            return self.getToken(SQLParser.CASE, 0)

        def END(self):
            return self.getToken(SQLParser.END, 0)

        def whenClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SQLParser.WhenClauseContext)
            else:
                return self.getTypedRuleContext(SQLParser.WhenClauseContext,i)


        def elseClause(self):
            return self.getTypedRuleContext(SQLParser.ElseClauseContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_caseExpression

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

        localctx = SQLParser.CaseExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_caseExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(SQLParser.CASE)
            self.state = 549 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 548
                self.whenClause()
                self.state = 551 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==173):
                    break

            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==54:
                self.state = 553
                self.elseClause()


            self.state = 556
            self.match(SQLParser.END)
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
            return self.getToken(SQLParser.WHEN, 0)

        def condition(self):
            return self.getTypedRuleContext(SQLParser.ConditionContext,0)


        def THEN(self):
            return self.getToken(SQLParser.THEN, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_whenClause

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

        localctx = SQLParser.WhenClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_whenClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 558
            self.match(SQLParser.WHEN)
            self.state = 559
            self.condition()
            self.state = 560
            self.match(SQLParser.THEN)
            self.state = 561
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
            return self.getToken(SQLParser.ELSE, 0)

        def expression(self):
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_elseClause

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

        localctx = SQLParser.ElseClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_elseClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 563
            self.match(SQLParser.ELSE)
            self.state = 564
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
            return self.getTypedRuleContext(SQLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_condition

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

        localctx = SQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 566
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
                return self.getTypedRuleContexts(SQLParser.IdentifierContext)
            else:
                return self.getTypedRuleContext(SQLParser.IdentifierContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(SQLParser.DOT)
            else:
                return self.getToken(SQLParser.DOT, i)

        def getRuleIndex(self):
            return SQLParser.RULE_tableName

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

        localctx = SQLParser.TableNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_tableName)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 568
            self.identifier()
            self.state = 573
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==265:
                self.state = 569
                self.match(SQLParser.DOT)
                self.state = 570
                self.identifier()
                self.state = 575
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
            return self.getTypedRuleContext(SQLParser.IdentifierContext,0)


        def getRuleIndex(self):
            return SQLParser.RULE_columnName

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

        localctx = SQLParser.ColumnNameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_columnName)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





