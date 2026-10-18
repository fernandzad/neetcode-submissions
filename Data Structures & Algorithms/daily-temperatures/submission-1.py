class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # pair of (index, temperature)
        result = [0 for _ in range(len(temperatures))]
        stack.append((0, temperatures[0])) # stack the first temperature

        for current, temp in enumerate(temperatures[1:]):
            current += 1
            # peek_index, peek_temp = stack[-1] pair of (index, temperature)
            if temp > stack[-1][1]:
                while stack and temp > stack[-1][1]:
                    pop_index, _ = stack.pop()
                    result[pop_index] = current - pop_index

                stack.append((current, temp))
            elif temp <= stack[-1][1]:
                stack.append((current, temp))
        return result