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
        4,1,78,571,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,46,
        7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,52,
        2,53,7,53,2,54,7,54,1,0,5,0,112,8,0,10,0,12,0,115,9,0,1,1,1,1,4,
        1,119,8,1,11,1,12,1,120,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,131,
        8,2,1,3,1,3,3,3,135,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        5,5,147,8,5,10,5,12,5,150,9,5,1,6,1,6,1,6,5,6,155,8,6,10,6,12,6,
        158,9,6,1,7,1,7,1,7,1,7,1,7,3,7,165,8,7,1,7,3,7,168,8,7,1,8,1,8,
        1,8,3,8,173,8,8,1,8,1,8,5,8,177,8,8,10,8,12,8,180,9,8,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,3,9,190,8,9,1,9,1,9,1,9,1,9,3,9,196,8,9,1,
        9,4,9,199,8,9,11,9,12,9,200,1,10,1,10,1,10,1,10,1,10,3,10,208,8,
        10,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,
        14,1,14,1,14,3,14,225,8,14,1,15,1,15,1,15,1,15,3,15,231,8,15,1,15,
        1,15,3,15,235,8,15,1,15,1,15,1,15,3,15,240,8,15,1,15,1,15,3,15,244,
        8,15,1,15,1,15,1,15,3,15,249,8,15,1,16,1,16,1,16,5,16,254,8,16,10,
        16,12,16,257,9,16,1,17,1,17,3,17,261,8,17,1,18,1,18,1,18,5,18,266,
        8,18,10,18,12,18,269,9,18,1,19,1,19,3,19,273,8,19,1,19,3,19,276,
        8,19,1,19,1,19,3,19,280,8,19,3,19,282,8,19,1,20,1,20,5,20,286,8,
        20,10,20,12,20,289,9,20,1,21,3,21,292,8,21,1,21,1,21,1,21,1,21,1,
        21,1,22,1,22,1,22,3,22,302,8,22,1,22,1,22,3,22,306,8,22,1,22,1,22,
        3,22,310,8,22,3,22,312,8,22,1,23,1,23,3,23,316,8,23,1,23,3,23,319,
        8,23,1,23,1,23,1,23,1,23,3,23,325,8,23,1,23,1,23,3,23,329,8,23,1,
        24,1,24,3,24,333,8,24,1,24,1,24,1,24,1,24,1,24,3,24,340,8,24,1,24,
        1,24,3,24,344,8,24,1,25,1,25,1,25,5,25,349,8,25,10,25,12,25,352,
        9,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,5,26,364,
        8,26,10,26,12,26,367,9,26,1,27,1,27,1,27,1,27,1,27,1,27,3,27,375,
        8,27,1,28,1,28,1,28,5,28,380,8,28,10,28,12,28,383,9,28,1,29,1,29,
        1,29,1,29,1,30,1,30,3,30,391,8,30,1,30,1,30,1,30,3,30,396,8,30,1,
        31,1,31,1,31,3,31,401,8,31,1,32,1,32,1,32,1,32,1,32,1,32,1,32,1,
        32,3,32,411,8,32,1,32,1,32,1,32,3,32,416,8,32,1,33,1,33,3,33,420,
        8,33,1,34,1,34,3,34,424,8,34,1,35,1,35,1,35,5,35,429,8,35,10,35,
        12,35,432,9,35,1,35,1,35,1,36,1,36,1,36,5,36,439,8,36,10,36,12,36,
        442,9,36,1,36,1,36,1,36,1,36,1,36,5,36,449,8,36,10,36,12,36,452,
        9,36,1,36,1,36,1,36,1,37,1,37,3,37,459,8,37,1,38,1,38,1,38,1,38,
        1,38,3,38,466,8,38,1,39,1,39,1,39,3,39,471,8,39,1,39,1,39,1,39,1,
        40,1,40,1,40,3,40,479,8,40,1,40,3,40,482,8,40,1,41,1,41,1,41,1,41,
        5,41,488,8,41,10,41,12,41,491,9,41,1,42,1,42,1,42,1,42,1,42,1,42,
        1,42,1,42,1,42,3,42,502,8,42,1,42,1,42,1,42,1,42,3,42,508,8,42,1,
        43,1,43,1,44,1,44,1,44,5,44,515,8,44,10,44,12,44,518,9,44,1,45,1,
        45,1,46,1,46,1,46,3,46,525,8,46,1,47,1,47,1,48,1,48,1,48,3,48,532,
        8,48,1,48,1,48,3,48,536,8,48,1,48,1,48,1,49,1,49,4,49,542,8,49,11,
        49,12,49,543,1,49,3,49,547,8,49,1,49,1,49,1,50,1,50,1,50,1,50,1,
        50,1,51,1,51,1,51,1,52,1,52,1,53,1,53,1,53,5,53,564,8,53,10,53,12,
        53,567,9,53,1,54,1,54,1,54,0,0,55,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,66,
        68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,104,106,
        108,0,6,1,0,67,68,1,0,55,56,1,0,47,48,3,0,22,24,39,42,78,78,3,0,
        38,38,72,73,77,77,4,0,1,26,29,33,38,60,67,68,612,0,113,1,0,0,0,2,
        118,1,0,0,0,4,130,1,0,0,0,6,134,1,0,0,0,8,136,1,0,0,0,10,143,1,0,
        0,0,12,151,1,0,0,0,14,164,1,0,0,0,16,169,1,0,0,0,18,198,1,0,0,0,
        20,202,1,0,0,0,22,209,1,0,0,0,24,212,1,0,0,0,26,216,1,0,0,0,28,224,
        1,0,0,0,30,226,1,0,0,0,32,250,1,0,0,0,34,258,1,0,0,0,36,262,1,0,
        0,0,38,272,1,0,0,0,40,283,1,0,0,0,42,291,1,0,0,0,44,311,1,0,0,0,
        46,328,1,0,0,0,48,330,1,0,0,0,50,345,1,0,0,0,52,353,1,0,0,0,54,368,
        1,0,0,0,56,376,1,0,0,0,58,384,1,0,0,0,60,388,1,0,0,0,62,400,1,0,
        0,0,64,402,1,0,0,0,66,419,1,0,0,0,68,423,1,0,0,0,70,425,1,0,0,0,
        72,435,1,0,0,0,74,458,1,0,0,0,76,460,1,0,0,0,78,467,1,0,0,0,80,475,
        1,0,0,0,82,483,1,0,0,0,84,507,1,0,0,0,86,509,1,0,0,0,88,511,1,0,
        0,0,90,519,1,0,0,0,92,524,1,0,0,0,94,526,1,0,0,0,96,531,1,0,0,0,
        98,539,1,0,0,0,100,550,1,0,0,0,102,555,1,0,0,0,104,558,1,0,0,0,106,
        560,1,0,0,0,108,568,1,0,0,0,110,112,3,2,1,0,111,110,1,0,0,0,112,
        115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,1,1,0,0,0,115,113,
        1,0,0,0,116,119,3,4,2,0,117,119,5,33,0,0,118,116,1,0,0,0,118,117,
        1,0,0,0,119,120,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,3,1,
        0,0,0,122,131,3,6,3,0,123,131,3,28,14,0,124,131,3,62,31,0,125,131,
        3,74,37,0,126,131,3,80,40,0,127,131,3,26,13,0,128,131,3,70,35,0,
        129,131,5,63,0,0,130,122,1,0,0,0,130,123,1,0,0,0,130,124,1,0,0,0,
        130,125,1,0,0,0,130,126,1,0,0,0,130,127,1,0,0,0,130,128,1,0,0,0,
        130,129,1,0,0,0,131,5,1,0,0,0,132,135,3,8,4,0,133,135,3,20,10,0,
        134,132,1,0,0,0,134,133,1,0,0,0,135,7,1,0,0,0,136,137,5,8,0,0,137,
        138,5,10,0,0,138,139,3,106,53,0,139,140,5,64,0,0,140,141,3,10,5,
        0,141,142,5,65,0,0,142,9,1,0,0,0,143,148,3,12,6,0,144,145,5,62,0,
        0,145,147,3,12,6,0,146,144,1,0,0,0,147,150,1,0,0,0,148,146,1,0,0,
        0,148,149,1,0,0,0,149,11,1,0,0,0,150,148,1,0,0,0,151,152,3,108,54,
        0,152,156,3,14,7,0,153,155,3,18,9,0,154,153,1,0,0,0,155,158,1,0,
        0,0,156,154,1,0,0,0,156,157,1,0,0,0,157,13,1,0,0,0,158,156,1,0,0,
        0,159,165,5,57,0,0,160,165,5,58,0,0,161,165,5,59,0,0,162,165,5,60,
        0,0,163,165,3,92,46,0,164,159,1,0,0,0,164,160,1,0,0,0,164,161,1,
        0,0,0,164,162,1,0,0,0,164,163,1,0,0,0,165,167,1,0,0,0,166,168,3,
        16,8,0,167,166,1,0,0,0,167,168,1,0,0,0,168,15,1,0,0,0,169,172,5,
        64,0,0,170,173,5,77,0,0,171,173,3,92,46,0,172,170,1,0,0,0,172,171,
        1,0,0,0,173,178,1,0,0,0,174,175,5,62,0,0,175,177,5,77,0,0,176,174,
        1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,181,
        1,0,0,0,180,178,1,0,0,0,181,182,5,65,0,0,182,17,1,0,0,0,183,184,
        5,24,0,0,184,199,5,38,0,0,185,199,5,38,0,0,186,187,5,53,0,0,187,
        189,5,54,0,0,188,190,7,0,0,0,189,188,1,0,0,0,189,190,1,0,0,0,190,
        195,1,0,0,0,191,192,5,64,0,0,192,193,3,50,25,0,193,194,5,65,0,0,
        194,196,1,0,0,0,195,191,1,0,0,0,195,196,1,0,0,0,196,199,1,0,0,0,
        197,199,3,92,46,0,198,183,1,0,0,0,198,185,1,0,0,0,198,186,1,0,0,
        0,198,197,1,0,0,0,199,200,1,0,0,0,200,198,1,0,0,0,200,201,1,0,0,
        0,201,19,1,0,0,0,202,203,5,9,0,0,203,204,5,10,0,0,204,207,3,106,
        53,0,205,208,3,22,11,0,206,208,3,24,12,0,207,205,1,0,0,0,207,206,
        1,0,0,0,208,21,1,0,0,0,209,210,5,12,0,0,210,211,3,12,6,0,211,23,
        1,0,0,0,212,213,5,11,0,0,213,214,7,1,0,0,214,215,3,92,46,0,215,25,
        1,0,0,0,216,217,5,52,0,0,217,218,5,10,0,0,218,219,3,106,53,0,219,
        27,1,0,0,0,220,225,3,30,15,0,221,225,3,48,24,0,222,225,3,54,27,0,
        223,225,3,60,30,0,224,220,1,0,0,0,224,221,1,0,0,0,224,222,1,0,0,
        0,224,223,1,0,0,0,225,29,1,0,0,0,226,227,5,1,0,0,227,230,3,36,18,
        0,228,229,5,2,0,0,229,231,3,40,20,0,230,228,1,0,0,0,230,231,1,0,
        0,0,231,234,1,0,0,0,232,233,5,3,0,0,233,235,3,104,52,0,234,232,1,
        0,0,0,234,235,1,0,0,0,235,239,1,0,0,0,236,237,5,45,0,0,237,238,5,
        44,0,0,238,240,3,88,44,0,239,236,1,0,0,0,239,240,1,0,0,0,240,243,
        1,0,0,0,241,242,5,46,0,0,242,244,3,104,52,0,243,241,1,0,0,0,243,
        244,1,0,0,0,244,248,1,0,0,0,245,246,5,43,0,0,246,247,5,44,0,0,247,
        249,3,32,16,0,248,245,1,0,0,0,248,249,1,0,0,0,249,31,1,0,0,0,250,
        255,3,34,17,0,251,252,5,62,0,0,252,254,3,34,17,0,253,251,1,0,0,0,
        254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,33,1,0,0,0,257,
        255,1,0,0,0,258,260,3,82,41,0,259,261,7,2,0,0,260,259,1,0,0,0,260,
        261,1,0,0,0,261,35,1,0,0,0,262,267,3,38,19,0,263,264,5,62,0,0,264,
        266,3,38,19,0,265,263,1,0,0,0,266,269,1,0,0,0,267,265,1,0,0,0,267,
        268,1,0,0,0,268,37,1,0,0,0,269,267,1,0,0,0,270,273,5,78,0,0,271,
        273,3,82,41,0,272,270,1,0,0,0,272,271,1,0,0,0,273,281,1,0,0,0,274,
        276,5,49,0,0,275,274,1,0,0,0,275,276,1,0,0,0,276,279,1,0,0,0,277,
        280,3,108,54,0,278,280,3,90,45,0,279,277,1,0,0,0,279,278,1,0,0,0,
        280,282,1,0,0,0,281,275,1,0,0,0,281,282,1,0,0,0,282,39,1,0,0,0,283,
        287,3,46,23,0,284,286,3,42,21,0,285,284,1,0,0,0,286,289,1,0,0,0,
        287,285,1,0,0,0,287,288,1,0,0,0,288,41,1,0,0,0,289,287,1,0,0,0,290,
        292,3,44,22,0,291,290,1,0,0,0,291,292,1,0,0,0,292,293,1,0,0,0,293,
        294,5,15,0,0,294,295,3,46,23,0,295,296,5,21,0,0,296,297,3,104,52,
        0,297,43,1,0,0,0,298,312,5,16,0,0,299,301,5,17,0,0,300,302,5,20,
        0,0,301,300,1,0,0,0,301,302,1,0,0,0,302,312,1,0,0,0,303,305,5,18,
        0,0,304,306,5,20,0,0,305,304,1,0,0,0,305,306,1,0,0,0,306,312,1,0,
        0,0,307,309,5,19,0,0,308,310,5,20,0,0,309,308,1,0,0,0,309,310,1,
        0,0,0,310,312,1,0,0,0,311,298,1,0,0,0,311,299,1,0,0,0,311,303,1,
        0,0,0,311,307,1,0,0,0,312,45,1,0,0,0,313,318,3,106,53,0,314,316,
        5,49,0,0,315,314,1,0,0,0,315,316,1,0,0,0,316,317,1,0,0,0,317,319,
        3,92,46,0,318,315,1,0,0,0,318,319,1,0,0,0,319,329,1,0,0,0,320,321,
        5,64,0,0,321,322,3,30,15,0,322,324,5,65,0,0,323,325,5,49,0,0,324,
        323,1,0,0,0,324,325,1,0,0,0,325,326,1,0,0,0,326,327,3,92,46,0,327,
        329,1,0,0,0,328,313,1,0,0,0,328,320,1,0,0,0,329,47,1,0,0,0,330,332,
        5,4,0,0,331,333,5,5,0,0,332,331,1,0,0,0,332,333,1,0,0,0,333,334,
        1,0,0,0,334,339,3,106,53,0,335,336,5,64,0,0,336,337,3,50,25,0,337,
        338,5,65,0,0,338,340,1,0,0,0,339,335,1,0,0,0,339,340,1,0,0,0,340,
        343,1,0,0,0,341,344,3,52,26,0,342,344,3,30,15,0,343,341,1,0,0,0,
        343,342,1,0,0,0,344,49,1,0,0,0,345,350,3,108,54,0,346,347,5,62,0,
        0,347,349,3,108,54,0,348,346,1,0,0,0,349,352,1,0,0,0,350,348,1,0,
        0,0,350,351,1,0,0,0,351,51,1,0,0,0,352,350,1,0,0,0,353,354,5,13,
        0,0,354,355,5,64,0,0,355,356,3,88,44,0,356,357,5,65,0,0,357,365,
        1,0,0,0,358,359,5,62,0,0,359,360,5,64,0,0,360,361,3,88,44,0,361,
        362,5,65,0,0,362,364,1,0,0,0,363,358,1,0,0,0,364,367,1,0,0,0,365,
        363,1,0,0,0,365,366,1,0,0,0,366,53,1,0,0,0,367,365,1,0,0,0,368,369,
        5,6,0,0,369,370,3,106,53,0,370,371,5,14,0,0,371,374,3,56,28,0,372,
        373,5,3,0,0,373,375,3,104,52,0,374,372,1,0,0,0,374,375,1,0,0,0,375,
        55,1,0,0,0,376,381,3,58,29,0,377,378,5,62,0,0,378,380,3,58,29,0,
        379,377,1,0,0,0,380,383,1,0,0,0,381,379,1,0,0,0,381,382,1,0,0,0,
        382,57,1,0,0,0,383,381,1,0,0,0,384,385,3,108,54,0,385,386,5,78,0,
        0,386,387,3,82,41,0,387,59,1,0,0,0,388,390,5,7,0,0,389,391,5,2,0,
        0,390,389,1,0,0,0,390,391,1,0,0,0,391,392,1,0,0,0,392,395,3,106,
        53,0,393,394,5,3,0,0,394,396,3,104,52,0,395,393,1,0,0,0,395,396,
        1,0,0,0,396,61,1,0,0,0,397,401,3,64,32,0,398,401,3,72,36,0,399,401,
        3,70,35,0,400,397,1,0,0,0,400,398,1,0,0,0,400,399,1,0,0,0,401,63,
        1,0,0,0,402,410,5,26,0,0,403,404,5,24,0,0,404,405,5,25,0,0,405,406,
        5,64,0,0,406,407,3,30,15,0,407,408,5,65,0,0,408,411,1,0,0,0,409,
        411,3,104,52,0,410,403,1,0,0,0,410,409,1,0,0,0,410,411,1,0,0,0,411,
        412,1,0,0,0,412,415,3,66,33,0,413,414,5,37,0,0,414,416,3,68,34,0,
        415,413,1,0,0,0,415,416,1,0,0,0,416,65,1,0,0,0,417,420,3,70,35,0,
        418,420,3,4,2,0,419,417,1,0,0,0,419,418,1,0,0,0,420,67,1,0,0,0,421,
        424,3,70,35,0,422,424,3,4,2,0,423,421,1,0,0,0,423,422,1,0,0,0,424,
        69,1,0,0,0,425,430,5,27,0,0,426,429,3,4,2,0,427,429,5,33,0,0,428,
        426,1,0,0,0,428,427,1,0,0,0,429,432,1,0,0,0,430,428,1,0,0,0,430,
        431,1,0,0,0,431,433,1,0,0,0,432,430,1,0,0,0,433,434,5,28,0,0,434,
        71,1,0,0,0,435,436,5,27,0,0,436,440,5,29,0,0,437,439,3,4,2,0,438,
        437,1,0,0,0,439,442,1,0,0,0,440,438,1,0,0,0,440,441,1,0,0,0,441,
        443,1,0,0,0,442,440,1,0,0,0,443,444,5,28,0,0,444,445,5,29,0,0,445,
        446,5,27,0,0,446,450,5,30,0,0,447,449,3,4,2,0,448,447,1,0,0,0,449,
        452,1,0,0,0,450,448,1,0,0,0,450,451,1,0,0,0,451,453,1,0,0,0,452,
        450,1,0,0,0,453,454,5,28,0,0,454,455,5,30,0,0,455,73,1,0,0,0,456,
        459,3,76,38,0,457,459,3,78,39,0,458,456,1,0,0,0,458,457,1,0,0,0,
        459,75,1,0,0,0,460,461,5,31,0,0,461,462,5,75,0,0,462,465,3,14,7,
        0,463,464,5,78,0,0,464,466,3,82,41,0,465,463,1,0,0,0,465,466,1,0,
        0,0,466,77,1,0,0,0,467,470,5,14,0,0,468,471,5,75,0,0,469,471,3,108,
        54,0,470,468,1,0,0,0,470,469,1,0,0,0,471,472,1,0,0,0,472,473,5,78,
        0,0,473,474,3,82,41,0,474,79,1,0,0,0,475,478,5,32,0,0,476,479,3,
        92,46,0,477,479,5,66,0,0,478,476,1,0,0,0,478,477,1,0,0,0,479,481,
        1,0,0,0,480,482,3,88,44,0,481,480,1,0,0,0,481,482,1,0,0,0,482,81,
        1,0,0,0,483,489,3,84,42,0,484,485,3,86,43,0,485,486,3,84,42,0,486,
        488,1,0,0,0,487,484,1,0,0,0,488,491,1,0,0,0,489,487,1,0,0,0,489,
        490,1,0,0,0,490,83,1,0,0,0,491,489,1,0,0,0,492,508,3,90,45,0,493,
        508,3,96,48,0,494,508,3,98,49,0,495,508,3,92,46,0,496,508,5,75,0,
        0,497,501,5,64,0,0,498,502,3,30,15,0,499,502,3,82,41,0,500,502,3,
        88,44,0,501,498,1,0,0,0,501,499,1,0,0,0,501,500,1,0,0,0,502,503,
        1,0,0,0,503,504,5,65,0,0,504,508,1,0,0,0,505,506,5,78,0,0,506,508,
        3,84,42,0,507,492,1,0,0,0,507,493,1,0,0,0,507,494,1,0,0,0,507,495,
        1,0,0,0,507,496,1,0,0,0,507,497,1,0,0,0,507,505,1,0,0,0,508,85,1,
        0,0,0,509,510,7,3,0,0,510,87,1,0,0,0,511,516,3,82,41,0,512,513,5,
        62,0,0,513,515,3,82,41,0,514,512,1,0,0,0,515,518,1,0,0,0,516,514,
        1,0,0,0,516,517,1,0,0,0,517,89,1,0,0,0,518,516,1,0,0,0,519,520,7,
        4,0,0,520,91,1,0,0,0,521,525,5,76,0,0,522,525,5,74,0,0,523,525,3,
        94,47,0,524,521,1,0,0,0,524,522,1,0,0,0,524,523,1,0,0,0,525,93,1,
        0,0,0,526,527,7,5,0,0,527,95,1,0,0,0,528,532,5,50,0,0,529,532,5,
        51,0,0,530,532,3,92,46,0,531,528,1,0,0,0,531,529,1,0,0,0,531,530,
        1,0,0,0,532,533,1,0,0,0,533,535,5,64,0,0,534,536,3,88,44,0,535,534,
        1,0,0,0,535,536,1,0,0,0,536,537,1,0,0,0,537,538,5,65,0,0,538,97,
        1,0,0,0,539,541,5,34,0,0,540,542,3,100,50,0,541,540,1,0,0,0,542,
        543,1,0,0,0,543,541,1,0,0,0,543,544,1,0,0,0,544,546,1,0,0,0,545,
        547,3,102,51,0,546,545,1,0,0,0,546,547,1,0,0,0,547,548,1,0,0,0,548,
        549,5,28,0,0,549,99,1,0,0,0,550,551,5,35,0,0,551,552,3,104,52,0,
        552,553,5,36,0,0,553,554,3,82,41,0,554,101,1,0,0,0,555,556,5,37,
        0,0,556,557,3,82,41,0,557,103,1,0,0,0,558,559,3,82,41,0,559,105,
        1,0,0,0,560,565,3,92,46,0,561,562,5,61,0,0,562,564,3,92,46,0,563,
        561,1,0,0,0,564,567,1,0,0,0,565,563,1,0,0,0,565,566,1,0,0,0,566,
        107,1,0,0,0,567,565,1,0,0,0,568,569,3,92,46,0,569,109,1,0,0,0,72,
        113,118,120,130,134,148,156,164,167,172,178,189,195,198,200,207,
        224,230,234,239,243,248,255,260,267,272,275,279,281,287,291,301,
        305,309,311,315,318,324,328,332,339,343,350,365,374,381,390,395,
        400,410,415,419,423,428,430,440,450,458,465,470,478,481,489,501,
        507,516,524,531,535,543,546,565
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9218868421993675822) != 0):
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
                    if token in [1, 4, 6, 7, 8, 9, 14, 26, 27, 31, 32, 52, 63]:
                        self.state = 116
                        self.statement()
                        pass
                    elif token in [33]:
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
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 132
                self.createTableStatement()
                pass
            elif token in [9]:
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
            while _la==62:
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
            if _la==64:
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
            if token in [77]:
                self.state = 170
                self.match(StatementParser.NUMBER)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 74, 76]:
                self.state = 171
                self.identifier()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
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
            self.state = 198 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 198
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
                            if not(_la==67 or _la==68):
                                self._errHandler.recoverInline(self)
                            else:
                                self._errHandler.reportMatch(self)
                                self.consume()


                        self.state = 195
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==64:
                            self.state = 191
                            self.match(StatementParser.LPAREN)
                            self.state = 192
                            self.columnList()
                            self.state = 193
                            self.match(StatementParser.RPAREN)


                        pass

                    elif la_ == 4:
                        self.state = 197
                        self.identifier()
                        pass



                else:
                    raise NoViableAltException(self)
                self.state = 200 
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
            self.state = 202
            self.match(StatementParser.ALTER)
            self.state = 203
            self.match(StatementParser.TABLE)
            self.state = 204
            self.tableName()
            self.state = 207
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.state = 205
                self.addColumnClause()
                pass
            elif token in [11]:
                self.state = 206
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
            self.state = 209
            self.match(StatementParser.ADD)
            self.state = 210
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
            self.state = 212
            self.match(StatementParser.DROP)
            self.state = 213
            _la = self._input.LA(1)
            if not(_la==55 or _la==56):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 214
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
            self.state = 216
            self.match(StatementParser.TRUNCATE)
            self.state = 217
            self.match(StatementParser.TABLE)
            self.state = 218
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
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.selectStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 221
                self.insertStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 222
                self.updateStatement()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 223
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
            self.state = 226
            self.match(StatementParser.SELECT)
            self.state = 227
            self.selectList()
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 228
                self.match(StatementParser.FROM)
                self.state = 229
                self.tableList()


            self.state = 234
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 232
                self.match(StatementParser.WHERE)
                self.state = 233
                self.condition()


            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==45:
                self.state = 236
                self.match(StatementParser.GROUP)
                self.state = 237
                self.match(StatementParser.BY)
                self.state = 238
                self.expressionList()


            self.state = 243
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 241
                self.match(StatementParser.HAVING)
                self.state = 242
                self.condition()


            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 245
                self.match(StatementParser.ORDER)
                self.state = 246
                self.match(StatementParser.BY)
                self.state = 247
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
            self.state = 250
            self.orderByItem()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 251
                self.match(StatementParser.COMMA)
                self.state = 252
                self.orderByItem()
                self.state = 257
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
            self.state = 258
            self.expression()
            self.state = 260
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==47 or _la==48:
                self.state = 259
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
            self.state = 262
            self.selectItem()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 263
                self.match(StatementParser.COMMA)
                self.state = 264
                self.selectItem()
                self.state = 269
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
            self.state = 272
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 270
                self.match(StatementParser.OPERATOR)
                pass

            elif la_ == 2:
                self.state = 271
                self.expression()
                pass


            self.state = 281
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 275
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
                if la_ == 1:
                    self.state = 274
                    self.match(StatementParser.AS)


                self.state = 279
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                if la_ == 1:
                    self.state = 277
                    self.columnName()
                    pass

                elif la_ == 2:
                    self.state = 278
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
            self.state = 283
            self.tableRef()
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0):
                self.state = 284
                self.joinClause()
                self.state = 289
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
            self.state = 291
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0):
                self.state = 290
                self.joinType()


            self.state = 293
            self.match(StatementParser.JOIN)
            self.state = 294
            self.tableRef()
            self.state = 295
            self.match(StatementParser.ON)
            self.state = 296
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
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.match(StatementParser.INNER)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.match(StatementParser.LEFT)
                self.state = 301
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 300
                    self.match(StatementParser.OUTER)


                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 303
                self.match(StatementParser.RIGHT)
                self.state = 305
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 304
                    self.match(StatementParser.OUTER)


                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 4)
                self.state = 307
                self.match(StatementParser.FULL)
                self.state = 309
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==20:
                    self.state = 308
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
            self.state = 328
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 74, 76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 313
                self.tableName()
                self.state = 318
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
                if la_ == 1:
                    self.state = 315
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
                    if la_ == 1:
                        self.state = 314
                        self.match(StatementParser.AS)


                    self.state = 317
                    self.identifier()


                pass
            elif token in [64]:
                self.enterOuterAlt(localctx, 2)
                self.state = 320
                self.match(StatementParser.LPAREN)
                self.state = 321
                self.selectStatement()
                self.state = 322
                self.match(StatementParser.RPAREN)

                self.state = 324
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                if la_ == 1:
                    self.state = 323
                    self.match(StatementParser.AS)


                self.state = 326
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
            self.state = 330
            self.match(StatementParser.INSERT)
            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 331
                self.match(StatementParser.INTO)


            self.state = 334
            self.tableName()
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==64:
                self.state = 335
                self.match(StatementParser.LPAREN)
                self.state = 336
                self.columnList()
                self.state = 337
                self.match(StatementParser.RPAREN)


            self.state = 343
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.state = 341
                self.insertValues()
                pass
            elif token in [1]:
                self.state = 342
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
            self.state = 345
            self.columnName()
            self.state = 350
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 346
                self.match(StatementParser.COMMA)
                self.state = 347
                self.columnName()
                self.state = 352
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
            self.state = 353
            self.match(StatementParser.VALUES)

            self.state = 354
            self.match(StatementParser.LPAREN)
            self.state = 355
            self.expressionList()
            self.state = 356
            self.match(StatementParser.RPAREN)
            self.state = 365
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 358
                self.match(StatementParser.COMMA)
                self.state = 359
                self.match(StatementParser.LPAREN)
                self.state = 360
                self.expressionList()
                self.state = 361
                self.match(StatementParser.RPAREN)
                self.state = 367
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
            self.state = 368
            self.match(StatementParser.UPDATE)
            self.state = 369
            self.tableName()
            self.state = 370
            self.match(StatementParser.SET)
            self.state = 371
            self.assignments()
            self.state = 374
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 372
                self.match(StatementParser.WHERE)
                self.state = 373
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
            self.state = 376
            self.assignment()
            self.state = 381
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 377
                self.match(StatementParser.COMMA)
                self.state = 378
                self.assignment()
                self.state = 383
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
            self.state = 384
            self.columnName()
            self.state = 385
            self.match(StatementParser.OPERATOR)
            self.state = 386
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
            self.state = 388
            self.match(StatementParser.DELETE)
            self.state = 390
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 389
                self.match(StatementParser.FROM)


            self.state = 392
            self.tableName()
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==3:
                self.state = 393
                self.match(StatementParser.WHERE)
                self.state = 394
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
            self.state = 400
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.ifStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.tryCatchStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
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
            self.state = 402
            self.match(StatementParser.IF)
            self.state = 410
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.state = 403
                self.match(StatementParser.NOT)
                self.state = 404
                self.match(StatementParser.EXISTS)
                self.state = 405
                self.match(StatementParser.LPAREN)
                self.state = 406
                self.selectStatement()
                self.state = 407
                self.match(StatementParser.RPAREN)

            elif la_ == 2:
                self.state = 409
                self.condition()


            self.state = 412
            self.thenBlock()
            self.state = 415
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 413
                self.match(StatementParser.ELSE)
                self.state = 414
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
            self.state = 419
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 417
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 418
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
            self.state = 423
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 421
                self.blockStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 422
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
            self.state = 425
            self.match(StatementParser.BEGIN)
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9218868421993675822) != 0):
                self.state = 428
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1, 4, 6, 7, 8, 9, 14, 26, 27, 31, 32, 52, 63]:
                    self.state = 426
                    self.statement()
                    pass
                elif token in [33]:
                    self.state = 427
                    self.match(StatementParser.GO)
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 432
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 433
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
            self.state = 435
            self.match(StatementParser.BEGIN)
            self.state = 436
            self.match(StatementParser.TRY)
            self.state = 440
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9218868430583610414) != 0):
                self.state = 437
                self.statement()
                self.state = 442
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 443
            self.match(StatementParser.END)
            self.state = 444
            self.match(StatementParser.TRY)
            self.state = 445
            self.match(StatementParser.BEGIN)
            self.state = 446
            self.match(StatementParser.CATCH)
            self.state = 450
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -9218868430583610414) != 0):
                self.state = 447
                self.statement()
                self.state = 452
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 453
            self.match(StatementParser.END)
            self.state = 454
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
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.declareStatement()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 457
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
            self.state = 460
            self.match(StatementParser.DECLARE)
            self.state = 461
            self.match(StatementParser.VARIABLE)
            self.state = 462
            self.dataType()
            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==78:
                self.state = 463
                self.match(StatementParser.OPERATOR)
                self.state = 464
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
            self.state = 467
            self.match(StatementParser.SET)
            self.state = 470
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [75]:
                self.state = 468
                self.match(StatementParser.VARIABLE)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 74, 76]:
                self.state = 469
                self.columnName()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 472
            self.match(StatementParser.OPERATOR)
            self.state = 473
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
            self.state = 475
            self.match(StatementParser.EXEC)
            self.state = 478
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68, 74, 76]:
                self.state = 476
                self.identifier()
                pass
            elif token in [66]:
                self.state = 477
                self.match(StatementParser.SP_EXECUTESQL)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 481
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 480
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
            self.state = 483
            self.primary()
            self.state = 489
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 484
                    self.binaryOp()
                    self.state = 485
                    self.primary() 
                self.state = 491
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
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 492
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 493
                self.functionCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 494
                self.caseExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 495
                self.identifier()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 496
                self.match(StatementParser.VARIABLE)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 497
                self.match(StatementParser.LPAREN)
                self.state = 501
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 498
                    self.selectStatement()
                    pass

                elif la_ == 2:
                    self.state = 499
                    self.expression()
                    pass

                elif la_ == 3:
                    self.state = 500
                    self.expressionList()
                    pass


                self.state = 503
                self.match(StatementParser.RPAREN)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 505
                self.match(StatementParser.OPERATOR)
                self.state = 506
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
            self.state = 509
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
            self.state = 511
            self.expression()
            self.state = 516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==62:
                self.state = 512
                self.match(StatementParser.COMMA)
                self.state = 513
                self.expression()
                self.state = 518
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
            self.state = 519
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
            return self.getToken(StatementParser.IDENTIFIER, 0)

        def BRACKET_IDENTIFIER(self):
            return self.getToken(StatementParser.BRACKET_IDENTIFIER, 0)

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
            self.state = 524
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [76]:
                self.enterOuterAlt(localctx, 1)
                self.state = 521
                self.match(StatementParser.IDENTIFIER)
                pass
            elif token in [74]:
                self.enterOuterAlt(localctx, 2)
                self.state = 522
                self.match(StatementParser.BRACKET_IDENTIFIER)
                pass
            elif token in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 29, 30, 31, 32, 33, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 67, 68]:
                self.enterOuterAlt(localctx, 3)
                self.state = 523
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
            return self.getToken(StatementParser.SELECT, 0)

        def FROM(self):
            return self.getToken(StatementParser.FROM, 0)

        def WHERE(self):
            return self.getToken(StatementParser.WHERE, 0)

        def INSERT(self):
            return self.getToken(StatementParser.INSERT, 0)

        def INTO(self):
            return self.getToken(StatementParser.INTO, 0)

        def UPDATE(self):
            return self.getToken(StatementParser.UPDATE, 0)

        def DELETE(self):
            return self.getToken(StatementParser.DELETE, 0)

        def CREATE(self):
            return self.getToken(StatementParser.CREATE, 0)

        def ALTER(self):
            return self.getToken(StatementParser.ALTER, 0)

        def TABLE(self):
            return self.getToken(StatementParser.TABLE, 0)

        def DROP(self):
            return self.getToken(StatementParser.DROP, 0)

        def ADD(self):
            return self.getToken(StatementParser.ADD, 0)

        def VALUES(self):
            return self.getToken(StatementParser.VALUES, 0)

        def SET(self):
            return self.getToken(StatementParser.SET, 0)

        def JOIN(self):
            return self.getToken(StatementParser.JOIN, 0)

        def INNER(self):
            return self.getToken(StatementParser.INNER, 0)

        def LEFT(self):
            return self.getToken(StatementParser.LEFT, 0)

        def RIGHT(self):
            return self.getToken(StatementParser.RIGHT, 0)

        def FULL(self):
            return self.getToken(StatementParser.FULL, 0)

        def OUTER(self):
            return self.getToken(StatementParser.OUTER, 0)

        def ON(self):
            return self.getToken(StatementParser.ON, 0)

        def AND(self):
            return self.getToken(StatementParser.AND, 0)

        def OR(self):
            return self.getToken(StatementParser.OR, 0)

        def NOT(self):
            return self.getToken(StatementParser.NOT, 0)

        def EXISTS(self):
            return self.getToken(StatementParser.EXISTS, 0)

        def IF(self):
            return self.getToken(StatementParser.IF, 0)

        def TRY(self):
            return self.getToken(StatementParser.TRY, 0)

        def CATCH(self):
            return self.getToken(StatementParser.CATCH, 0)

        def DECLARE(self):
            return self.getToken(StatementParser.DECLARE, 0)

        def EXEC(self):
            return self.getToken(StatementParser.EXEC, 0)

        def GO(self):
            return self.getToken(StatementParser.GO, 0)

        def NULL(self):
            return self.getToken(StatementParser.NULL, 0)

        def IN(self):
            return self.getToken(StatementParser.IN, 0)

        def IS(self):
            return self.getToken(StatementParser.IS, 0)

        def LIKE(self):
            return self.getToken(StatementParser.LIKE, 0)

        def BETWEEN(self):
            return self.getToken(StatementParser.BETWEEN, 0)

        def ORDER(self):
            return self.getToken(StatementParser.ORDER, 0)

        def BY(self):
            return self.getToken(StatementParser.BY, 0)

        def GROUP(self):
            return self.getToken(StatementParser.GROUP, 0)

        def HAVING(self):
            return self.getToken(StatementParser.HAVING, 0)

        def ASC(self):
            return self.getToken(StatementParser.ASC, 0)

        def DESC(self):
            return self.getToken(StatementParser.DESC, 0)

        def AS(self):
            return self.getToken(StatementParser.AS, 0)

        def INT(self):
            return self.getToken(StatementParser.INT, 0)

        def NVARCHAR(self):
            return self.getToken(StatementParser.NVARCHAR, 0)

        def BIGINT(self):
            return self.getToken(StatementParser.BIGINT, 0)

        def DATE(self):
            return self.getToken(StatementParser.DATE, 0)

        def MAX(self):
            return self.getToken(StatementParser.MAX, 0)

        def AVG(self):
            return self.getToken(StatementParser.AVG, 0)

        def TRUNCATE(self):
            return self.getToken(StatementParser.TRUNCATE, 0)

        def PRIMARY(self):
            return self.getToken(StatementParser.PRIMARY, 0)

        def KEY(self):
            return self.getToken(StatementParser.KEY, 0)

        def CONSTRAINT(self):
            return self.getToken(StatementParser.CONSTRAINT, 0)

        def COLUMN(self):
            return self.getToken(StatementParser.COLUMN, 0)

        def CLUSTERED(self):
            return self.getToken(StatementParser.CLUSTERED, 0)

        def NONCLUSTERED(self):
            return self.getToken(StatementParser.NONCLUSTERED, 0)

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
            self.state = 526
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
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 528
                self.match(StatementParser.MAX)
                pass

            elif la_ == 2:
                self.state = 529
                self.match(StatementParser.AVG)
                pass

            elif la_ == 3:
                self.state = 530
                self.identifier()
                pass


            self.state = 533
            self.match(StatementParser.LPAREN)
            self.state = 535
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2305842768292872190) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 32537) != 0):
                self.state = 534
                self.expressionList()


            self.state = 537
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
            self.state = 539
            self.match(StatementParser.CASE)
            self.state = 541 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 540
                self.whenClause()
                self.state = 543 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==35):
                    break

            self.state = 546
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 545
                self.elseClause()


            self.state = 548
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
            self.state = 550
            self.match(StatementParser.WHEN)
            self.state = 551
            self.condition()
            self.state = 552
            self.match(StatementParser.THEN)
            self.state = 553
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
            self.state = 555
            self.match(StatementParser.ELSE)
            self.state = 556
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
            self.state = 558
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
            self.state = 560
            self.identifier()
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==61:
                self.state = 561
                self.match(StatementParser.DOT)
                self.state = 562
                self.identifier()
                self.state = 567
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
            self.state = 568
            self.identifier()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





