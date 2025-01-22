def RomanToInt(roman_str):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    result_int = 0
    
    for i in range(len(roman_str) - 1):
        if roman[roman_str[i]] < roman[roman_str[i + 1]]:
            result_int -= roman[roman_str[i]]
        else:
            result_int += roman[roman_str[i]]
            
    return result_int + roman[roman_str[-1]]

# Get input from user
roman = input('Input Roman Numeral: ')
print("Integer equivalent:", RomanToInt(roman))