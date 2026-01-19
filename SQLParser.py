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
        4,1,78,576,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,2,55,7,55,1,0,1,0,1,0,1,1,5,1,117,8,1,10,1,12,
        1,120,9,1,1,2,1,2,4,2,124,8,2,11,2,12,2,125,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,3,3,136,8,3,1,4,1,4,3,4,140,8,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,1,6,1,6,1,6,5,6,152,8,6,10,6,12,6,155,9,6,1,7,1,7,1,7,5,
        7,160,8,7,10,7,12,7,163,9,7,1,8,1,8,1,8,1,8,1,8,3,8,170,8,8,1,8,
        3,8,173,8,8,1,9,1,9,1,9,3,9,178,8,9,1,9,1,9,5,9,182,8,9,10,9,12,
        9,185,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,3,10,195,8,10,1,
        10,1,10,1,10,1,10,3,10,201,8,10,1,10,4,10,204,8,10,11,10,12,10,205,
        1,11,1,11,1,11,1,11,1,11,3,11,213,8,11,1,12,1,12,1,12,1,13,1,13,
        1,13,1,13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,230,8,15,
        1,16,1,16,1,16,1,16,3,16,236,8,16,1,16,1,16,3,16,240,8,16,1,16,1,
        16,1,16,3,16,245,8,16,1,16,1,16,3,16,249,8,16,1,16,1,16,1,16,3,16,
        254,8,16,1,17,1,17,1,17,5,17,259,8,17,10,17,12,17,262,9,17,1,18,
        1,18,3,18,266,8,18,1,19,1,19,1,19,5,19,271,8,19,10,19,12,19,274,
        9,19,1,20,1,20,3,20,278,8,20,1,20,3,20,281,8,20,1,20,1,20,3,20,285,
        8,20,3,20,287,8,20,1,21,1,21,5,21,291,8,21,10,21,12,21,294,9,21,
        1,22,3,22,297,8,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,3,23,
        307,8,23,1,23,1,23,3,23,311,8,23,1,23,1,23,3,23,315,8,23,3,23,317,
        8,23,1,24,1,24,3,24,321,8,24,1,24,3,24,324,8,24,1,24,1,24,1,24,1,
        24,3,24,330,8,24,1,24,1,24,3,24,334,8,24,1,25,1,25,3,25,338,8,25,
        1,25,1,25,1,25,1,25,1,25,3,25,345,8,25,1,25,1,25,3,25,349,8,25,1,
        26,1,26,1,26,5,26,354,8,26,10,26,12,26,357,9,26,1,27,1,27,1,27,1,
        27,1,27,1,27,1,27,1,27,1,27,1,27,5,27,369,8,27,10,27,12,27,372,9,
        27,1,28,1,28,1,28,1,28,1,28,1,28,3,28,380,8,28,1,29,1,29,1,29,5,
        29,385,8,29,10,29,12,29,388,9,29,1,30,1,30,1,30,1,30,1,31,1,31,3,
        31,396,8,31,1,31,1,31,1,31,3,31,401,8,31,1,32,1,32,1,32,3,32,406,
        8,32,1,33,1,33,1,33,1,33,1,33,1,33,1,33,1,33,3,33,416,8,33,1,33,
        1,33,1,33,3,33,421,8,33,1,34,1,34,3,34,425,8,34,1,35,1,35,3,35,429,
        8,35,1,36,1,36,1,36,5,36,434,8,36,10,36,12,36,437,9,36,1,36,1,36,
        1,37,1,37,1,37,5,37,444,8,37,10,37,12,37,447,9,37,1,37,1,37,1,37,
        1,37,1,37,5,37,454,8,37,10,37,12,37,457,9,37,1,37,1,37,1,37,1,38,
        1,38,3,38,464,8,38,1,39,1,39,1,39,1,39,1,39,3,39,471,8,39,1,40,1,
        40,1,40,3,40,476,8,40,1,40,1,40,1,40,1,41,1,41,1,41,3,41,484,8,41,
        1,41,3,41,487,8,41,1,42,1,42,1,42,1,42,5,42,493,8,42,10,42,12,42,
        496,9,42,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,1,43,3,43,507,8,
        43,1,43,1,43,1,43,1,43,3,43,513,8,43,1,44,1,44,1,45,1,45,1,45,5,
        45,520,8,45,10,45,12,45,523,9,45,1,46,1,46,1,47,1,47,1,47,3,47,530,
        8,47,1,48,1,48,1,49,1,49,1,49,3,49,537,8,49,1,49,1,49,3,49,541,8,
        49,1,49,1,49,1,50,1,50,4,50,547,8,50,11,50,12,50,548,1,50,3,50,552,
        8,50,1,50,1,50,1,51,1,51,1,51,1,51,1,51,1,52,1,52,1,52,1,53,1,53,
        1,54,1,54,1,54,5,54,569,8,54,10,54,12,54,572,9,54,1,55,1,55,1,55,
        0,0,56,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,
        86,88,90,92,94,96,98,100,102,104,106,108,110,0,6,1,0,67,68,1,0,55,
        56,1,0,47,48,3,0,22,24,39,42,78,78,3,0,38,38,72,73,77,77,4,0,1,26,
        29,33,38,60,67,68,616,0,112,1,0,0,0,2,118,1,0,0,0,4,123,1,0,0,0,
        6,135,1,0,0,0,8,139,1,0,0,0,10,141,1,0,0,0,12,148,1,0,0,0,14,156,
        1,0,0,0,16,169,1,0,0,0,18,174,1,0,0,0,20,203,1,0,0,0,22,207,1,0,
        0,0,24,214,1,0,0,0,26,217,1,0,0,0,28,221,1,0,0,0,30,229,1,0,0,0,
        32,231,1,0,0,0,34,255,1,0,0,0,36,263,1,0,0,0,38,267,1,0,0,0,40,277,
        1,0,0,0,42,288,1,0,0,0,44,296,1,0,0,0,46,316,1,0,0,0,48,333,1,0,
        0,0,50,335,1,0,0,0,52,350,1,0,0,0,54,358,1,0,0,0,56,373,1,0,0,0,
        58,381,1,0,0,0,60,389,1,0,0,0,62,393,1,0,0,0,64,405,1,0,0,0,66,407,
        1,0,0,0,68,424,1,0,0,0,70,428,1,0,0,0,72,430,1,0,0,0,74,440,1,0,
        0,0,76,463,1,0,0,0,78,465,1,0,0,0,80,472,1,0,0,0,82,480,1,0,0,0,
        84,488,1,0,0,0,86,512,1,0,0,0,88,514,1,0,0,0,90,516,1,0,0,0,92,524,
        1,0,0,0,94,529,1,0,0,0,96,531,1,0,0,0,98,536,1,0,0,0,100,544,1,0,
        0,0,102,555,1,0,0,0,104,560,1,0,0,0,106,563,1,0,0,0,108,565,1,0,
        0,0,110,573,1,0,0,0,112,113,3,2,1,0,113,114,5,0,0,1,114,1,1,0,0,
        0,115,117,3,4,2,0,116,115,1,0,0,0,117,120,1,0,0,0,118,116,1,0,0,
        0,118,119,1,0,0,0,119,3,1,0,0,0,120,118,1,0,0,0,121,124,3,6,3,0,
        122,124,5,33,0,0,123,121,1,0,0,0,123,122,1,0,0,0,124,125,1,0,0,0,
        125,123,1,0,0,0,125,126,1,0,0,0,126,5,1,0,0,0,127,136,3,8,4,0,128,
        136,3,30,15,0,129,136,3,64,32,0,130,136,3,76,38,0,131,136,3,82,41,
        0,132,136,3,28,14,0,133,136,3,72,36,0,134,136,5,63,0,0,135,127,1,
        0,0,0,135,128,1,0,0,0,135,129,1,0,0,0,135,130,1,0,0,0,135,131,1,
        0,0,0,135,132,1,0,0,0,135,133,1,0,0,0,135,134,1,0,0,0,136,7,1,0,
        0,0,137,140,3,10,5,0,138,140,3,22,11,0,139,137,1,0,0,0,139,138,1,
        0,0,0,140,9,1,0,0,0,141,142,5,8,0,0,142,143,5,10,0,0,143,144,3,108,
        54,0,144,145,5,64,0,0,145,146,3,12,6,0,146,147,5,65,0,0,147,11,1,
        0,0,0,148,153,3,14,7,0,149,150,5,62,0,0,150,152,3,14,7,0,151,149,
        1,0,0,0,152,155,1,0,0,0,153,151,1,0,0,0,153,154,1,0,0,0,154,13,1,
        0,0,0,155,153,1,0,0,0,156,157,3,110,55,0,157,161,3,16,8,0,158,160,
        3,20,10,0,159,158,1,0,0,0,160,163,1,0,0,0,161,159,1,0,0,0,161,162,
        1,0,0,0,162,15,1,0,0,0,163,161,1,0,0,0,164,170,5,57,0,0,165,170,
        5,58,0,0,166,170,5,59,0,0,167,170,5,60,0,0,168,170,3,94,47,0,169,
        164,1,0,0,0,169,165,1,0,0,0,169,166,1,0,0,0,169,167,1,0,0,0,169,
        168,1,0,0,0,170,172,1,0,0,0,171,173,3,18,9,0,172,171,1,0,0,0,172,
        173,1,0,0,0,173,17,1,0,0,0,174,177,5,64,0,0,175,178,5,77,0,0,176,
        178,3,94,47,0,177,175,1,0,0,0,177,176,1,0,0,0,178,183,1,0,0,0,179,
        180,5,62,0,0,180,182,5,77,0,0,181,179,1,0,0,0,182,185,1,0,0,0,183,
        181,1,0,0,0,183,184,1,0,0,0,184,186,1,0,0,0,185,183,1,0,0,0,186,
        187,5,65,0,0,187,19,1,0,0,0,188,189,5,24,0,0,189,204,5,38,0,0,190,
        204,5,38,0,0,191,192,5,53,0,0,192,194,5,54,0,0,193,195,7,0,0,0,194,
        193,1,0,0,0,194,195,1,0,0,0,195,200,1,0,0,0,196,197,5,64,0,0,197,
        198,3,52,26,0,198,199,5,65,0,0,199,201,1,0,0,0,200,196,1,0,0,0,200,
        201,1,0,0,0,201,204,1,0,0,0,202,204,3,94,47,0,203,188,1,0,0,0,203,
        190,1,0,0,0,203,191,1,0,0,0,203,202,1,0,0,0,204,205,1,0,0,0,205,
        203,1,0,0,0,205,206,1,0,0,0,206,21,1,0,0,0,207,208,5,9,0,0,208,209,
        5,10,0,0,209,212,3,108,54,0,210,213,3,24,12,0,211,213,3,26,13,0,
        212,210,1,0,0,0,212,211,1,0,0,0,213,23,1,0,0,0,214,215,5,12,0,0,
        215,216,3,14,7,0,216,25,1,0,0,0,217,218,5,11,0,0,218,219,7,1,0,0,
        219,220,3,94,47,0,220,27,1,0,0,0,221,222,5,52,0,0,222,223,5,10,0,
        0,223,224,3,108,54,0,224,29,1,0,0,0,225,230,3,32,16,0,226,230,3,
        50,25,0,227,230,3,56,28,0,228,230,3,62,31,0,229,225,1,0,0,0,229,
        226,1,0,0,0,229,227,1,0,0,0,229,228,1,0,0,0,230,31,1,0,0,0,231,232,
        5,1,0,0,232,235,3,38,19,0,233,234,5,2,0,0,234,236,3,42,21,0,235,
        233,1,0,0,0,235,236,1,0,0,0,236,239,1,0,0,0,237,238,5,3,0,0,238,
        240,3,106,53,0,239,237,1,0,0,0,239,240,1,0,0,0,240,244,1,0,0,0,241,
        242,5,45,0,0,242,243,5,44,0,0,243,245,3,90,45,0,244,241,1,0,0,0,
        244,245,1,0,0,0,245,248,1,0,0,0,246,247,5,46,0,0,247,249,3,106,53,
        0,248,246,1,0,0,0,248,249,1,0,0,0,249,253,1,0,0,0,250,251,5,43,0,
        0,251,252,5,44,0,0,252,254,3,34,17,0,253,250,1,0,0,0,253,254,1,0,
        0,0,254,33,1,0,0,0,255,260,3,36,18,0,256,257,5,62,0,0,257,259,3,
        36,18,0,258,256,1,0,0,0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,
        1,0,0,0,261,35,1,0,0,0,262,260,1,0,0,0,263,265,3,84,42,0,264,266,
        7,2,0,0,265,264,1,0,0,0,265,266,1,0,0,0,266,37,1,0,0,0,267,272,3,
        40,20,0,268,269,5,62,0,0,269,271,3,40,20,0,270,268,1,0,0,0,271,274,
        1,0,0,0,272,270,1,0,0,0,272,273,1,0,0,0,273,39,1,0,0,0,274,272,1,
        0,0,0,275,278,5,78,0,0,276,278,3,84,42,0,277,275,1,0,0,0,277,276,
        1,0,0,0,278,286,1,0,0,0,279,281,5,49,0,0,280,279,1,0,0,0,280,281,
        1,0,0,0,281,284,1,0,0,0,282,285,3,110,55,0,283,285,3,92,46,0,284,
        282,1,0,0,0,284,283,1,0,0,0,285,287,1,0,0,0,286,280,1,0,0,0,286,
        287,1,0,0,0,287,41,1,0,0,0,288,292,3,48,24,0,289,291,3,44,22,0,290,
        289,1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,
        43,1,0,0,0,294,292,1,0,0,0,295,297,3,46,23,0,296,295,1,0,0,0,296,
        297,1,0,0,0,297,298,1,0,0,0,298,299,5,15,0,0,299,300,3,48,24,0,300,
        301,5,21,0,0,301,302,3,106,53,0,302,45,1,0,0,0,303,317,5,16,0,0,
        304,306,5,17,0,0,305,307,5,20,0,0,306,305,1,0,0,0,306,307,1,0,0,
        0,307,317,1,0,0,0,308,310,5,18,0,0,309,311,5,20,0,0,310,309,1,0,
        0,0,310,311,1,0,0,0,311,317,1,0,0,0,312,314,5,19,0,0,313,315,5,20,
        0,0,314,313,1,0,0,0,314,315,1,0,0,0,315,317,1,0,0,0,316,303,1,0,
        0,0,316,304,1,0,0,0,316,308,1,0,0,0,316,312,1,0,0,0,317,47,1,0,0,
        0,318,323,3,108,54,0,319,321,5,49,0,0,320,319,1,0,0,0,320,321,1,
        0,0,0,321,322,1,0,0,0,322,324,3,94,47,0,323,320,1,0,0,0,323,324,
        1,0,0,0,324,334,1,0,0,0,325,326,5,64,0,0,326,327,3,32,16,0,327,329,
        5,65,0,0,328,330,5,49,0,0,329,328,1,0,0,0,329,330,1,0,0,0,330,331,
        1,0,0,0,331,332,3,94,47,0,332,334,1,0,0,0,333,318,1,0,0,0,333,325,
        1,0,0,0,334,49,1,0,0,0,335,337,5,4,0,0,336,338,5,5,0,0,337,336,1,
        0,0,0,337,338,1,0,0,0,338,339,1,0,0,0,339,344,3,108,54,0,340,341,
        5,64,0,0,341,342,3,52,26,0,342,343,5,65,0,0,343,345,1,0,0,0,344,
        340,1,0,0,0,344,345,1,0,0,0,345,348,1,0,0,0,346,349,3,54,27,0,347,
        349,3,32,16,0,348,346,1,0,0,0,348,347,1,0,0,0,349,51,1,0,0,0,350,
        355,3,110,55,0,351,352,5,62,0,0,352,354,3,110,55,0,353,351,1,0,0,
        0,354,357,1,0,0,0,355,353,1,0,0,0,355,356,1,0,0,0,356,53,1,0,0,0,
        357,355,1,0,0,0,358,359,5,13,0,0,359,360,5,64,0,0,360,361,3,90,45,
        0,361,362,5,65,0,0,362,370,1,0,0,0,363,364,5,62,0,0,364,365,5,64,
        0,0,365,366,3,90,45,0,366,367,5,65,0,0,367,369,1,0,0,0,368,363,1,
        0,0,0,369,372,1,0,0,0,370,368,1,0,0,0,370,371,1,0,0,0,371,55,1,0,
        0,0,372,370,1,0,0,0,373,374,5,6,0,0,374,375,3,108,54,0,375,376,5,
        14,0,0,376,379,3,58,29,0,377,378,5,3,0,0,378,380,3,106,53,0,379,
        377,1,0,0,0,379,380,1,0,0,0,380,57,1,0,0,0,381,386,3,60,30,0,382,
        383,5,62,0,0,383,385,3,60,30,0,384,382,1,0,0,0,385,388,1,0,0,0,386,
        384,1,0,0,0,386,387,1,0,0,0,387,59,1,0,0,0,388,386,1,0,0,0,389,390,
        3,110,55,0,390,391,5,78,0,0,391,392,3,84,42,0,392,61,1,0,0,0,393,
        395,5,7,0,0,394,396,5,2,0,0,395,394,1,0,0,0,395,396,1,0,0,0,396,
        397,1,0,0,0,397,400,3,108,54,0,398,399,5,3,0,0,399,401,3,106,53,
        0,400,398,1,0,0,0,400,401,1,0,0,0,401,63,1,0,0,0,402,406,3,66,33,
        0,403,406,3,74,37,0,404,406,3,72,36,0,405,402,1,0,0,0,405,403,1,
        0,0,0,405,404,1,0,0,0,406,65,1,0,0,0,407,415,5,26,0,0,408,409,5,
        24,0,0,409,410,5,25,0,0,410,411,5,64,0,0,411,412,3,32,16,0,412,413,
        5,65,0,0,413,416,1,0,0,0,414,416,3,106,53,0,415,408,1,0,0,0,415,
        414,1,0,0,0,415,416,1,0,0,0,416,417,1,0,0,0,417,420,3,68,34,0,418,
        419,5,37,0,0,419,421,3,70,35,0,420,418,1,0,0,0,420,421,1,0,0,0,421,
        67,1,0,0,0,422,425,3,72,36,0,423,425,3,6,3,0,424,422,1,0,0,0,424,
        423,1,0,0,0,425,69,1,0,0,0,426,429,3,72,36,0,427,429,3,6,3,0,428,
        426,1,0,0,0,428,427,1,0,0,0,429,71,1,0,0,0,430,435,5,27,0,0,431,
        434,3,6,3,0,432,434,5,33,0,0,433,431,1,0,0,0,433,432,1,0,0,0,434,
        437,1,0,0,0,435,433,1,0,0,0,435,436,1,0,0,0,436,438,1,0,0,0,437,
        435,1,0,0,0,438,439,5,28,0,0,439,73,1,0,0,0,440,441,5,27,0,0,441,
        445,5,29,0,0,442,444,3,6,3,0,443,442,1,0,0,0,444,447,1,0,0,0,445,
        443,1,0,0,0,445,446,1,0,0,0,446,448,1,0,0,0,447,445,1,0,0,0,448,
        449,5,28,0,0,449,450,5,29,0,0,450,451,5,27,0,0,451,455,5,30,0,0,
        452,454,3,6,3,0,453,452,1,0,0,0,454,457,1,0,0,0,455,453,1,0,0,0,
        455,456,1,0,0,0,456,458,1,0,0,0,457,455,1,0,0,0,458,459,5,28,0,0,
        459,460,5,30,0,0,460,75,1,0,0,0,461,464,3,78,39,0,462,464,3,80,40,
        0,463,461,1,0,0,0,463,462,1,0,0,0,464,77,1,0,0,0,465,466,5,31,0,
        0,466,467,5,75,0,0,467,470,3,16,8,0,468,469,5,78,0,0,469,471,3,84,
        42,0,470,468,1,0,0,0,470,471,1,0,0,0,471,79,1,0,0,0,472,475,5,14,
        0,0,473,476,5,75,0,0,474,476,3,110,55,0,475,473,1,0,0,0,475,474,
        1,0,0,0,476,477,1,0,0,0,477,478,5,78,0,0,478,479,3,84,42,0,479,81,
        1,0,0,0,480,483,5,32,0,0,481,484,3,94,47,0,482,484,5,66,0,0,483,
        481,1,0,0,0,483,482,1,0,0,0,484,486,1,0,0,0,485,487,3,90,45,0,486,
        485,1,0,0,0,486,487,1,0,0,0,487,83,1,0,0,0,488,494,3,86,43,0,489,
        490,3,88,44,0,490,491,3,86,43,0,491,493,1,0,0,0,492,489,1,0,0,0,
        493,496,1,0,0,0,494,492,1,0,0,0,494,495,1,0,0,0,495,85,1,0,0,0,496,
        494,1,0,0,0,497,513,3,92,46,0,498,513,3,98,49,0,499,513,3,100,50,
        0,500,513,3,94,47,0,501,513,5,75,0,0,502,506,5,64,0,0,503,507,3,
        32,16,0,504,507,3,84,42,0,505,507,3,90,45,0,506,503,1,0,0,0,506,
        504,1,0,0,0,506,505,1,0,0,0,507,508,1,0,0,0,508,509,5,65,0,0,509,
        513,1,0,0,0,510,511,5,78,0,0,511,513,3,86,43,0,512,497,1,0,0,0,512,
        498,1,0,0,0,512,499,1,0,0,0,512,500,1,0,0,0,512,501,1,0,0,0,512,
        502,1,0,0,0,512,510,1,0,0,0,513,87,1,0,0,0,514,515,7,3,0,0,515,89,
        1,0,0,0,516,521,3,84,42,0,517,518,5,62,0,0,518,520,3,84,42,0,519,
        517,1,0,0,0,520,523,1,0,0,0,521,519,1,0,0,0,521,522,1,0,0,0,522,
        91,1,0,0,0,523,521,1,0,0,0,524,525,7,4,0,0,525,93,1,0,0,0,526,530,
        5,76,0,0,527,530,5,74,0,0,528,530,3,96,48,0,529,526,1,0,0,0,529,
        527,1,0,0,0,529,528,1,0,0,0,530,95,1,0,0,0,531,532,7,5,0,0,532,97,
        1,0,0,0,533,537,5,50,0,0,534,537,5,51,0,0,535,537,3,94,47,0,536,
        533,1,0,0,0,536,534,1,0,0,0,536,535,1,0,0,0,537,538,1,0,0,0,538,
        540,5,64,0,0,539,541,3,90,45,0,540,539,1,0,0,0,540,541,1,0,0,0,541,
        542,1,0,0,0,542,543,5,65,0,0,543,99,1,0,0,0,544,546,5,34,0,0,545,
        547,3,102,51,0,546,545,1,0,0,0,547,548,1,0,0,0,548,546,1,0,0,0,548,
        549,1,0,0,0,549,551,1,0,0,0,550,552,3,104,52,0,551,550,1,0,0,0,551,
        552,1,0,0,0,552,553,1,0,0,0,553,554,5,28,0,0,554,101,1,0,0,0,555,
        556,5,35,0,0,556,557,3,106,53,0,557,558,5,36,0,0,558,559,3,84,42,
        0,559,103,1,0,0,0,560,561,5,37,0,0,561,562,3,84,42,0,562,105,1,0,
        0,0,563,564,3,84,42,0,564,107,1,0,0,0,565,570,3,94,47,0,566,567,
        5,61,0,0,567,569,3,94,47,0,568,566,1,0,0,0,569,572,1,0,0,0,570,568,
        1,0,0,0,570,571,1,0,0,0,571,109,1,0,0,0,572,570,1,0,0,0,573,574,
        3,94,47,0,574,111,1,0,0,0,72,118,123,125,135,139,153,161,169,172,
        177,183,194,200,203,205,212,229,235,239,244,248,253,260,265,272,
        277,280,284,286,292,296,306,310,314,316,320,323,329,333,337,344,
        348,355,370,379,386,395,400,405,415,420,424,428,433,435,445,455,
        463,470,475,483,486,494,506,512,521,529,536,540,548,551,570
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
                     "<INVALID>", "'.'", "','", "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SELECT", "FROM", "WHERE", "INSERT", 
                      "INTO", "UPDATE", "DELETE", "CREATE", "ALTER", "TABLE", 
                      "DROP", "ADD", "VALUES", "SET", "JOIN", "INNER", "LEFT", 
                      "RIGHT", "FULL", "OUTER", "ON", "AND", "OR", "NOT", 
                      "EXISTS", "IF", "BEGIN", "END", "TRY", "CATCH", "DECLARE", 
                      "EXEC", "GO", "CASE", "WHEN", "THEN", "ELSE", "NULL", 
                      "IN", "IS", "LIKE", "BETWEEN", "ORDER", "BY", "GROUP", 
                      "HAVING", "ASC", "DESC", "AS", "MAX", "AVG", "TRUNCATE", 
                      "PRIMARY", "KEY", "CONSTRAINT", "COLUMN", "INT", "NVARCHAR", 
                      "BIGINT", "DATE", "DOT", "COMMA", "SEMI", "LPAREN", 
                      "RPAREN", "SP_EXECUTESQL", "CLUSTERED", "NONCLUSTERED", 
                      "LINE_COMMENT", "BLOCK_COMMENT", "WS", "STRING_SINGLE", 
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
    SELECT=1
    FROM=2
    WHERE=3
    INSERT=4
    INTO=5
    UPDATE=6
    DELETE=7
    CREATE=8
    ALTER=9
    TABLE=10
    DROP=11
    ADD=12
    VALUES=13
    SET=14
    JOIN=15
    INNER=16
    LEFT=17
    RIGHT=18
    FULL=19
    OUTER=20
    ON=21
    AND=22
    OR=23
    NOT=24
    EXISTS=25
    IF=26
    BEGIN=27
    END=28
    TRY=29
    CATCH=30
    DECLARE=31
    EXEC=32
    GO=33
    CASE=34
    WHEN=35
    THEN=36
    ELSE=37
    NULL=38
    IN=39
    IS=40
    LIKE=41
    BETWEEN=42
    ORDER=43
    BY=44
    GROUP=45
    HAVING=46
    ASC=47
    DESC=48
    AS=49
    MAX=50
    AVG=51
    TRUNCATE=52
    PRIMARY=53
    KEY=54
    CONSTRAINT=55
    COLUMN=56
    INT=57
    NVARCHAR=58
    BIGINT=59
    DATE=60
    DOT=61
    COMMA=62
    SEMI=63
    LPAREN=64
    RPAREN=65
    SP_EXECUTESQL=66
    CLUSTERED=67
    NONCLUSTERED=68
    LINE_COMMENT=69
    BLOCK_COMMENT=70
    WS=71
    STRING_SINGLE=72
    STRING_DOUBLE=73
    BRACKET_IDENTIFIER=74
    VARIABLE=75
    IDENTIFIER=76
    NUMBER=77
    OPERATOR=78

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9218868421993675822) != 0):
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
                    if token in [1, 4, 6, 7, 8, 9, 14, 26, 27, 31, 32, 52, 63]:
                        self.state = 121
                        self.statement()
                        pass
                    elif token in [33]:
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
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.createTableStatement()
                pass
            elif token in [9]:
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
            while _la==62:
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
            if _la==64:
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
            if token in [77]:
                self.state = 175
                self.match(SQLParser.NUMBER)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 74, 76]:
                self.state = 176
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 183
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
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
            self.state = 203 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 203
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
                            if not(_la==67 or _la==68):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()


                        self.state = 200
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==64:
                            self.state = 196
                            self.match(SQLParser.LPAREN)
                            self.state = 197
                            self.columnList()
                            self.state = 198
                            self.match(SQLParser.RPAREN)


                        pass

                    elif la_ == 4:
                        self.state = 202
                        self.identifier()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 205 
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
            self.state = 207
            self.match(SQLParser.ALTER)
            self.state = 208
            self.match(SQLParser.TABLE)
            self.state = 209
            self.tableName()
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 210
                self.addColumnClause()
                pass
            elif token in [11]:
                self.state = 211
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
            self.state = 214
            self.match(SQLParser.ADD)
            self.state = 215
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
            self.state = 217
            self.match(SQLParser.DROP)
            self.state = 218
            _la = self._input.LA(1)
            if not(_la==55 or _la==56):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 219
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
            self.state = 221
            self.match(SQLParser.TRUNCATE)
            self.state = 222
            self.match(SQLParser.TABLE)
            self.state = 223
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
            self.state = 229
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.selectStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.insertStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.updateStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
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
            self.state = 231
            self.match(SQLParser.SELECT)
            self.state = 232
            self.selectList()
            self.state = 235
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 233
                self.match(SQLParser.FROM)
                self.state = 234
                self.tableList()


            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 237
                self.match(SQLParser.WHERE)
                self.state = 238
                self.condition()


            self.state = 244
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 241
                self.match(SQLParser.GROUP)
                self.state = 242
                self.match(SQLParser.BY)
                self.state = 243
                self.expressionList()


            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 246
                self.match(SQLParser.HAVING)
                self.state = 247
                self.condition()


            self.state = 253
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 250
                self.match(SQLParser.ORDER)
                self.state = 251
                self.match(SQLParser.BY)
                self.state = 252
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
            self.state = 255
            self.orderByItem()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 256
                self.match(SQLParser.COMMA)
                self.state = 257
                self.orderByItem()
                self.state = 262
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
            self.state = 263
            self.expression()
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47 or _la==48:
                self.state = 264
                _la = self._input.LA(1)
                if not(_la==47 or _la==48):
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
            self.state = 267
            self.selectItem()
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 268
                self.match(SQLParser.COMMA)
                self.state = 269
                self.selectItem()
                self.state = 274
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
            self.state = 277
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 275
                self.match(SQLParser.OPERATOR)
                pass

            elif la_ == 2:
                self.state = 276
                self.expression()
                pass


            self.state = 286
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 280
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 279
                    self.match(SQLParser.AS)


                self.state = 284
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 282
                    self.columnName()
                    pass

                elif la_ == 2:
                    self.state = 283
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
            self.state = 288
            self.tableRef()
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0):
                self.state = 289
                self.joinClause()
                self.state = 294
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
            self.state = 296
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                self.state = 295
                self.joinType()


            self.state = 298
            self.match(SQLParser.JOIN)
            self.state = 299
            self.tableRef()
            self.state = 300
            self.match(SQLParser.ON)
            self.state = 301
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
            self.state = 316
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 303
                self.match(SQLParser.INNER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 304
                self.match(SQLParser.LEFT)
                self.state = 306
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 305
                    self.match(SQLParser.OUTER)


                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 308
                self.match(SQLParser.RIGHT)
                self.state = 310
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 309
                    self.match(SQLParser.OUTER)


                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.match(SQLParser.FULL)
                self.state = 314
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 313
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
            self.state = 333
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 74, 76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.tableName()
                self.state = 323
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 320
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 319
                        self.match(SQLParser.AS)


                    self.state = 322
                    self.identifier()


                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 2)
                self.state = 325
                self.match(SQLParser.LPAREN)
                self.state = 326
                self.selectStatement()
                self.state = 327
                self.match(SQLParser.RPAREN)

                self.state = 329
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 328
                    self.match(SQLParser.AS)


                self.state = 331
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
            self.state = 335
            self.match(SQLParser.INSERT)
            self.state = 337
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 336
                self.match(SQLParser.INTO)


            self.state = 339
            self.tableName()
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 340
                self.match(SQLParser.LPAREN)
                self.state = 341
                self.columnList()
                self.state = 342
                self.match(SQLParser.RPAREN)


            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 346
                self.insertValues()
                pass
            elif token in [1]:
                self.state = 347
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
            self.state = 350
            self.columnName()
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 351
                self.match(SQLParser.COMMA)
                self.state = 352
                self.columnName()
                self.state = 357
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
            self.state = 358
            self.match(SQLParser.VALUES)

            self.state = 359
            self.match(SQLParser.LPAREN)
            self.state = 360
            self.expressionList()
            self.state = 361
            self.match(SQLParser.RPAREN)
            self.state = 370
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 363
                self.match(SQLParser.COMMA)
                self.state = 364
                self.match(SQLParser.LPAREN)
                self.state = 365
                self.expressionList()
                self.state = 366
                self.match(SQLParser.RPAREN)
                self.state = 372
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
            self.state = 373
            self.match(SQLParser.UPDATE)
            self.state = 374
            self.tableName()
            self.state = 375
            self.match(SQLParser.SET)
            self.state = 376
            self.assignments()
            self.state = 379
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 377
                self.match(SQLParser.WHERE)
                self.state = 378
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
            self.state = 381
            self.assignment()
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 382
                self.match(SQLParser.COMMA)
                self.state = 383
                self.assignment()
                self.state = 388
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
            self.state = 389
            self.columnName()
            self.state = 390
            self.match(SQLParser.OPERATOR)
            self.state = 391
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
            self.state = 393
            self.match(SQLParser.DELETE)
            self.state = 395
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 394
                self.match(SQLParser.FROM)


            self.state = 397
            self.tableName()
            self.state = 400
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 398
                self.match(SQLParser.WHERE)
                self.state = 399
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
            self.state = 405
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 402
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 403
                self.tryCatchStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 404
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
            self.state = 407
            self.match(SQLParser.IF)
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 408
                self.match(SQLParser.NOT)
                self.state = 409
                self.match(SQLParser.EXISTS)
                self.state = 410
                self.match(SQLParser.LPAREN)
                self.state = 411
                self.selectStatement()
                self.state = 412
                self.match(SQLParser.RPAREN)

            elif la_ == 2:
                self.state = 414
                self.condition()


            self.state = 417
            self.thenBlock()
            self.state = 420
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 418
                self.match(SQLParser.ELSE)
                self.state = 419
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
            self.state = 424
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 422
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 423
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
            self.state = 428
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 426
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 427
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
            self.state = 430
            self.match(SQLParser.BEGIN)
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9218868421993675822) != 0):
                self.state = 433
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 4, 6, 7, 8, 9, 14, 26, 27, 31, 32, 52, 63]:
                    self.state = 431
                    self.statement()
                    pass
                elif token in [33]:
                    self.state = 432
                    self.match(SQLParser.GO)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 438
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
            self.state = 440
            self.match(SQLParser.BEGIN)
            self.state = 441
            self.match(SQLParser.TRY)
            self.state = 445
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9218868430583610414) != 0):
                self.state = 442
                self.statement()
                self.state = 447
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 448
            self.match(SQLParser.END)
            self.state = 449
            self.match(SQLParser.TRY)
            self.state = 450
            self.match(SQLParser.BEGIN)
            self.state = 451
            self.match(SQLParser.CATCH)
            self.state = 455
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9218868430583610414) != 0):
                self.state = 452
                self.statement()
                self.state = 457
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 458
            self.match(SQLParser.END)
            self.state = 459
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
            self.state = 463
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 461
                self.declareStatement()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 462
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
            self.state = 465
            self.match(SQLParser.DECLARE)
            self.state = 466
            self.match(SQLParser.VARIABLE)
            self.state = 467
            self.dataType()
            self.state = 470
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 468
                self.match(SQLParser.OPERATOR)
                self.state = 469
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
            self.state = 472
            self.match(SQLParser.SET)
            self.state = 475
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [75]:
                self.state = 473
                self.match(SQLParser.VARIABLE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 74, 76]:
                self.state = 474
                self.columnName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 477
            self.match(SQLParser.OPERATOR)
            self.state = 478
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
            self.state = 480
            self.match(SQLParser.EXEC)
            self.state = 483
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 74, 76]:
                self.state = 481
                self.identifier()
                pass
            elif token in [66]:
                self.state = 482
                self.match(SQLParser.SP_EXECUTESQL)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 486
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 485
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
            self.state = 488
            self.primary()
            self.state = 494
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 489
                    self.binaryOp()
                    self.state = 490
                    self.primary() 
                self.state = 496
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
            self.state = 512
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 497
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 498
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 499
                self.caseExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 500
                self.identifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 501
                self.match(SQLParser.VARIABLE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 502
                self.match(SQLParser.LPAREN)
                self.state = 506
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 503
                    self.selectStatement()
                    pass

                elif la_ == 2:
                    self.state = 504
                    self.expression()
                    pass

                elif la_ == 3:
                    self.state = 505
                    self.expressionList()
                    pass


                self.state = 508
                self.match(SQLParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 510
                self.match(SQLParser.OPERATOR)
                self.state = 511
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
            self.state = 514
            _la = self._input.LA(1)
            if not(((((_la - 22)) & ~0x3f) == 0 and ((1 << (_la - 22)) & 72057594039894023) != 0)):
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
            self.state = 516
            self.expression()
            self.state = 521
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 517
                self.match(SQLParser.COMMA)
                self.state = 518
                self.expression()
                self.state = 523
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
            self.state = 524
            _la = self._input.LA(1)
            if not(((((_la - 38)) & ~0x3f) == 0 and ((1 << (_la - 38)) & 601295421441) != 0)):
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
            self.state = 529
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 526
                self.match(SQLParser.IDENTIFIER)
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 527
                self.match(SQLParser.BRACKET_IDENTIFIER)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68]:
                self.enterOuterAlt(localctx, 3)
                self.state = 528
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

        def SELECT(self):
            return self.getToken(SQLParser.SELECT, 0)

        def FROM(self):
            return self.getToken(SQLParser.FROM, 0)

        def WHERE(self):
            return self.getToken(SQLParser.WHERE, 0)

        def INSERT(self):
            return self.getToken(SQLParser.INSERT, 0)

        def INTO(self):
            return self.getToken(SQLParser.INTO, 0)

        def UPDATE(self):
            return self.getToken(SQLParser.UPDATE, 0)

        def DELETE(self):
            return self.getToken(SQLParser.DELETE, 0)

        def CREATE(self):
            return self.getToken(SQLParser.CREATE, 0)

        def ALTER(self):
            return self.getToken(SQLParser.ALTER, 0)

        def TABLE(self):
            return self.getToken(SQLParser.TABLE, 0)

        def DROP(self):
            return self.getToken(SQLParser.DROP, 0)

        def ADD(self):
            return self.getToken(SQLParser.ADD, 0)

        def VALUES(self):
            return self.getToken(SQLParser.VALUES, 0)

        def SET(self):
            return self.getToken(SQLParser.SET, 0)

        def JOIN(self):
            return self.getToken(SQLParser.JOIN, 0)

        def INNER(self):
            return self.getToken(SQLParser.INNER, 0)

        def LEFT(self):
            return self.getToken(SQLParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(SQLParser.RIGHT, 0)

        def FULL(self):
            return self.getToken(SQLParser.FULL, 0)

        def OUTER(self):
            return self.getToken(SQLParser.OUTER, 0)

        def ON(self):
            return self.getToken(SQLParser.ON, 0)

        def AND(self):
            return self.getToken(SQLParser.AND, 0)

        def OR(self):
            return self.getToken(SQLParser.OR, 0)

        def NOT(self):
            return self.getToken(SQLParser.NOT, 0)

        def EXISTS(self):
            return self.getToken(SQLParser.EXISTS, 0)

        def IF(self):
            return self.getToken(SQLParser.IF, 0)

        def TRY(self):
            return self.getToken(SQLParser.TRY, 0)

        def CATCH(self):
            return self.getToken(SQLParser.CATCH, 0)

        def DECLARE(self):
            return self.getToken(SQLParser.DECLARE, 0)

        def EXEC(self):
            return self.getToken(SQLParser.EXEC, 0)

        def GO(self):
            return self.getToken(SQLParser.GO, 0)

        def NULL(self):
            return self.getToken(SQLParser.NULL, 0)

        def IN(self):
            return self.getToken(SQLParser.IN, 0)

        def IS(self):
            return self.getToken(SQLParser.IS, 0)

        def LIKE(self):
            return self.getToken(SQLParser.LIKE, 0)

        def BETWEEN(self):
            return self.getToken(SQLParser.BETWEEN, 0)

        def ORDER(self):
            return self.getToken(SQLParser.ORDER, 0)

        def BY(self):
            return self.getToken(SQLParser.BY, 0)

        def GROUP(self):
            return self.getToken(SQLParser.GROUP, 0)

        def HAVING(self):
            return self.getToken(SQLParser.HAVING, 0)

        def ASC(self):
            return self.getToken(SQLParser.ASC, 0)

        def DESC(self):
            return self.getToken(SQLParser.DESC, 0)

        def AS(self):
            return self.getToken(SQLParser.AS, 0)

        def INT(self):
            return self.getToken(SQLParser.INT, 0)

        def NVARCHAR(self):
            return self.getToken(SQLParser.NVARCHAR, 0)

        def BIGINT(self):
            return self.getToken(SQLParser.BIGINT, 0)

        def DATE(self):
            return self.getToken(SQLParser.DATE, 0)

        def MAX(self):
            return self.getToken(SQLParser.MAX, 0)

        def AVG(self):
            return self.getToken(SQLParser.AVG, 0)

        def TRUNCATE(self):
            return self.getToken(SQLParser.TRUNCATE, 0)

        def PRIMARY(self):
            return self.getToken(SQLParser.PRIMARY, 0)

        def KEY(self):
            return self.getToken(SQLParser.KEY, 0)

        def CONSTRAINT(self):
            return self.getToken(SQLParser.CONSTRAINT, 0)

        def COLUMN(self):
            return self.getToken(SQLParser.COLUMN, 0)

        def CLUSTERED(self):
            return self.getToken(SQLParser.CLUSTERED, 0)

        def NONCLUSTERED(self):
            return self.getToken(SQLParser.NONCLUSTERED, 0)

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
            self.state = 531
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2305842751113003006) != 0) or _la==67 or _la==68):
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
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 533
                self.match(SQLParser.MAX)
                pass

            elif la_ == 2:
                self.state = 534
                self.match(SQLParser.AVG)
                pass

            elif la_ == 3:
                self.state = 535
                self.identifier()
                pass


            self.state = 538
            self.match(SQLParser.LPAREN)
            self.state = 540
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2305842768292872190) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 32537) != 0):
                self.state = 539
                self.expressionList()


            self.state = 542
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
            self.state = 544
            self.match(SQLParser.CASE)
            self.state = 546 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 545
                self.whenClause()
                self.state = 548 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==35):
                    break

            self.state = 551
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 550
                self.elseClause()


            self.state = 553
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
            self.state = 555
            self.match(SQLParser.WHEN)
            self.state = 556
            self.condition()
            self.state = 557
            self.match(SQLParser.THEN)
            self.state = 558
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
            self.state = 560
            self.match(SQLParser.ELSE)
            self.state = 561
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
            self.state = 563
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
            self.state = 565
            self.identifier()
            self.state = 570
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 566
                self.match(SQLParser.DOT)
                self.state = 567
                self.identifier()
                self.state = 572
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
            self.state = 573
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





