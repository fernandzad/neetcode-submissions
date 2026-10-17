class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in range(len(temperatures))]
        stack.append((0, temperatures[0]))
        for current, temp in enumerate(temperatures[1:]):
            current += 1
            # print(f"Current: {current}, Temp: {temp}, Stack: {stack}")
            peek_index, peek_temp = stack[-1]
            if temp > peek_temp:
                while stack and temp > stack[-1][1]:
                    index, _ = stack.pop()
                    result[index] = current - index
                    # print(f"Pop: index={index}, temp={temp}, result={result} current={current} temp={temp}")
                stack.append((current, temp))
            elif temp <= peek_temp:
                stack.append((current, temp))
        return result