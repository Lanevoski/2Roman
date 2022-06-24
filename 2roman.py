## RYAN AKERS 2022
import sys

symbols = ['I','V','X','L','C','D','M']

def getSymbol(offset):
    if offset <= 6:
        return symbols[offset]
    else:
        q = offset // 6
        p = (offset % 6)
        return symbols[p] + '\''*q

def convertSingle(digit,offset):
    if digit <= 3:
        return (getSymbol(offset)*digit)
    elif digit == 4:
        return (getSymbol(offset) + getSymbol(offset+1))
    elif digit <= 8:
        return (getSymbol(offset+1) + getSymbol(offset)*(digit-5))
    elif digit == 9:
        return (getSymbol(offset) + getSymbol(offset+2))
    print(digit,offset)

def toRoman(number):
    offset = 0
    final = ""
    while number > 0:
        final = convertSingle(number%10,offset) + final
        number //= 10 
        offset += 2
    return (final)

def main():
    if len(sys.argv) < 2:
        print("Usage: {} [int]".format(sys.argv[0]))
    else:
        num = int(sys.argv[1])
        print(toRoman(num))

if __name__ == "__main__":
    main()
