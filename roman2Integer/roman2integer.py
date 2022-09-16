class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
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
