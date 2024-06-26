"""class py_solution:
    def int_to_Roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num


print(py_solution().int_to_Roman(2))
print(py_solution().int_to_Roman(4000))"""

class py_solution:
    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]: # 1.ci index 0.cı index den böyükdürsə
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]] # 2 * menası: (int_val += rom_val[s[i]] - rom_val[s[i - 1]])   (5-1=4)   (int_val += rom_val[s[i]]) (4+1=5)   hesablama sehf olur.
            else:
                int_val += rom_val[s[i]]
        return int_val

print(py_solution().roman_to_int('IV')) # index 0,1
print(py_solution().roman_to_int('V')) # index 0
print(py_solution().roman_to_int('VII')) # index 0,1,2