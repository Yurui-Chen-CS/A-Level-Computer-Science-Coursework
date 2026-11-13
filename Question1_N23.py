def IterativeVowels(Value):
    Total=0
    LengthString=len(Value)
    for i in range(LengthString):
        FirstCharacter=Value[i]
        if FirstCharacter in'aeiou':
            Total+=1
    return Total

result=IterativeVowels("house")
print(result)

def RecursiveVowels(Value):
    if len(Value) == 0:
        return 0
    else:
        FirstCharacter = Value[0]
        if FirstCharacter in'aeiou':
            return 1 + RecursiveVowels(Value[1:])
        else:
            return RecursiveVowels(Value[1:])

def main():
    print(IterativeVowels("house"))
    print(RecursiveVowels("imagine"))

main()               