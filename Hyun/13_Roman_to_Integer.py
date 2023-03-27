class Solution:
    def romanToInt(self, s: str) -> int:

        rom2int = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5,
                   "I": 1}

        rom2int_minus = {"CM": -200, "CD": -200, "XC": -20, "XL": -20, "IX": -2, "IV": -2}

        score = 0
        for ch in s:
            score += rom2int[ch]

        for key in rom2int_minus.keys():
            if key in s:
                score += rom2int_minus[key]

        return score