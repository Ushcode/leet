import math


class Solution:

    def gcd_of_strings(self, str1: str, str2: str) -> str:
        lengths = [len(str1), len(str2)]
        result = str1[0]
        i = 1
        if str1 == str2:
            return str1
        if (
            (str1.startswith(str2) or str2.startswith(str1))
            and str1.replace(str2, "") in str2
            and str2.replace(str1, "") in str1
        ):
            while i < min(lengths):
                divisors = [lengths[0] // len(result), lengths[1] // len(result)]
                print(divisors)
                if (
                    (result * divisors[0] == str1)
                    and (result * divisors[1] == str2)
                    and math.gcd(divisors[0], divisors[1]) == 1
                ):
                    break
                result += str1[i]
                i += 1
        else:
            result = ""
        return result


str1 = "AABBAABBAA"
str2 = "AABB"


print(Solution.gcd_of_strings(Solution, str1, str2))
