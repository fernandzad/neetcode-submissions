class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we create our dp array of size amount + 1 (bc 0 index plus 1)
        dp = [float("inf")] * (amount + 1)
        # it tooks us 0 coins to get 0 amount
        dp[0] = 0

        # Iterate over all the possible coins
        for coin in coins:
            # We start at the position coin since previous values
            # can't be processed bc are smaller than the coin value
            for i in range(coin, amount + 1):
                # Here is the important part:
                # We took between the min and what is calculating
                # which is the current coin minimum minus the previous value calculated
                dp[i] = min(dp[i], 1 + dp[i - coin])
            print(f"coin: {coin}\n dp: {dp}")
        return dp[amount] if dp[amount] != float("inf") else -1
        