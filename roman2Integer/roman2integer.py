class Solution(object):
    def romanToIntNaive(self, s):
        """
        :type s: str
        :rtype: int
        Naive implementation faster than 50% of submissions and using less space than 50% of submissions
        """
        sum = 0
        index = 0

        while (index < len(s)):
            if (s[index] == "I"):
                if (index + 1 < len(s)):
                    if (s[index + 1] == "V"):
                        sum = sum + 4
                        index = index + 2
                    elif (s[index + 1] == "X"):
                        sum = sum + 9
                        index = index + 2
                    else:
                        sum = sum + 1
                        index = index + 1
                else:
                    sum = sum + 1
                    index = index + 1

            elif (s[index] == "X"):
                if (index + 1 < len(s)):
                    if (s[index + 1] == "L"):
                        sum = sum + 40
                        index = index + 2
                    elif (s[index + 1] == "C"):
                        sum = sum + 90
                        index = index + 2
                    else:
                        sum = sum + 10
                        index = index + 1
                else:
                    sum = sum + 10
                    index = index + 1
            elif (s[index] == "C"):
                if (index + 1 < len(s)):
                    if (s[index + 1] == "D"):
                        sum = sum + 400
                        index = index + 2
                    elif (s[index + 1] == "M"):
                        sum = sum + 900
                        index = index + 2
                    else:
                        sum = sum + 100
                        index = index + 1
                else:
                    sum = sum + 100
                    index = index + 1
            elif (s[index] == "V"):
                sum = sum + 5
                index = index + 1
            elif (s[index] == "L"):
                sum = sum + 50
                index = index + 1
            elif (s[index] == "D"):
                sum = sum + 500
                index = index + 1
            elif (s[index] == "M"):
                sum = sum + 1000
                index = index + 1
            else:
                print("UNEXPECTED INPUT!")

        print(sum)

    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        Optimized implementation faster than 96% of submissions and using less space than 57% of submissions
        """

        i = 0
        sum = 0

        values_Long = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }

        values_Short = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        while (i < len(s)):
            if (s[i:i+2] in values_Long):
                sum = sum + values_Long[s[i:i+2]]
                i = i + 2
            else:
                sum = sum + values_Short[s[i]]
                i = i + 1

        return sum


if __name__ == "__main__":
    Solver = Solution()

    print(Solver.romanToInt("MCMXCIV"))
