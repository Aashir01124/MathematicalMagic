while 1:
    def RomanToInt(romanNum):
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        
        for i in range(0, len(romanNum) - 1):
            if (roman[romanNum[i]] < roman[romanNum[i+1]]):
                result  -= roman[romanNum[i]]
            else:
                result += roman[romanNum[i]]
        return result + roman[romanNum[-1]]

    romanInp = input("Input roman numeral: ")
    print("Integer equivalent to roman numeral is ",RomanToInt(romanInp))