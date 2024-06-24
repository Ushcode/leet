class Solution:

    def gcd_of_strings(self, str1: str, str2: str) -> str:
        lengths = [len(str1),len(str2)]
        result = str1[0]
        i = 1
        if str1[0] == str2[0]:
            while i < min(lengths):
                divisors = [lengths[0] // len(result), lengths[1] // len(result)]
                if (result * divisors[0] == str1) and (result * divisors[1] == str2):
                    break
                result += str1[i]
                i += 1
        else:
            result = ""
        return result

print(Solution.gcd_of_strings(Solution, "Leet", "Code"))
