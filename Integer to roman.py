class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        value_map = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        roman_numeral = ""
        num = self.number
        for value, symbol in value_map:
            while num >= value:
                roman_numeral += symbol
                num -= value
        return roman_numeral

number = int(input("Enter an integer: "))
converter = IntegerToRoman(number)
print(f"The Roman numeral for {number} is {converter.to_roman()}")
