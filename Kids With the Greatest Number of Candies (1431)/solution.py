from typing import List


class Solution:
    def kids_with_candies(self, candies: List[int], extra_candies: int) -> List[bool]:
        result = []
        for index in range(len(candies)):
            rest = candies[:index] + candies[index+1:]   
            sorted_list = sorted(rest, reverse=True)
            new_max = candies[index] + extra_candies
            result.append(new_max >= sorted_list[0])

        return result

candies = [2, 3, 5, 1, 3]
extra_candies = 3
print(Solution.kids_with_candies(Solution, candies, extra_candies))
