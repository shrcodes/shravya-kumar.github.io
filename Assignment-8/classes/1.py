#Write a python class to convert an integer into a roman numeral and viceversa

class RomanNumeralConverter:
    def __init__(self):
        self.roman_numerals = {1000: 'M',900: 'CM',500: 'D',400: 'CD',100: 'C',90: 'XC',50: 'L',40: 'XL',10: 'X',9: 'IX',5: 'V',4: 'IV',1: 'I'
}
    
    def int_to_roman(self, num):
        roman_numeral = ''
        for value, numeral in self.roman_numerals.items():
            while num >= value:
                roman_numeral += numeral
                num -= value
        return roman_numeral
    def roman_to_int(self, roman_numeral):
        result = 0
        for value, numeral in reversed(list(self.roman_numerals.items())):
            while roman_numeral.startswith(numeral):
                result += value
                roman_numeral = roman_numeral[len(numeral):]
        return result
n = 23
print(RomanNumeralConverter().int_to_roman(n))
roman='X'
print(RomanNumeralConverter().roman_to_int(roman))
