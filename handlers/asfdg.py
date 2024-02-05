from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        prefix_sum = [0] * (len(temperatures) + 1)
        ans = []

        for i in range(1, len(temperatures) + 1):
            prefix_sum[i] = prefix_sum[i-1] + temperatures[i-1]

        for i in range(1, len(temperatures)):
            ans.append(prefix_sum[i-1]+temperatures[i]-prefix_sum[i])

        return prefix_sum, ans


x = Solution
temps = [30,60,90]

print(x.dailyTemperatures(x, temps))