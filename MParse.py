import sys
import string

try:
    InputFile = str(sys.argv[1]) #First is script name

    with open(InputFile, "r") as File:
        InputWords = File.read()

    if InputWords == []: raise Exception
except Exception as E:
    print("Empty or non-existent input")
    InputFile = "a.mp"

#InputWords = """integral _a dt = _v
#integral _v dt = _s = _x"""

InputLines = InputWords.splitlines(False)
InputWords = []
for i in InputLines:
    for e in i.split(): InputWords.append(e)
    InputWords.append("\n")

#print(InputWords)

# Check keywords
INTEGRAL = '\u222B'
#VECTOR_A = '\U0001D400'
VECTOR_CONSTANT = 119743
PHI = '\u03D5'
THETA = '\u03B8'
RHO = '\u03C1'
OMEGA = '\u03C9'
#print(INTEGRAL + " x^2 dx = 1/3 x^3 + C")
#print("A")
#print(chr(ord("V")+VECTOR_CONSTANT))


#Substitutions
OutputWords = ""

for Word in InputWords:
    Word = Word.replace('theta', THETA)
    Word = Word.replace('phi', PHI)
    Word = Word.replace('rho', RHO)
    Word = Word.replace('omega', OMEGA)
    Word = Word.replace('integral', INTEGRAL)
    Word = Word.replace('int', INTEGRAL)

    for Letter in list(string.ascii_lowercase):
        Word = Word.replace('_'+Letter, chr(ord(Letter.upper())+VECTOR_CONSTANT))
        Word = Word.replace('_' + Letter.upper(), chr(ord(Letter.upper()) + VECTOR_CONSTANT))

    if ("\n" not in Word) and (Word != INTEGRAL):
        OutputWords += Word + " "
    else: OutputWords += Word

print(OutputWords)
