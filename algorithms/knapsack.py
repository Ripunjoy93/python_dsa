import sys
sys.path.append(".")

from utils.test_utils import evaluate_test_cases

"""
You're in charge of selecting a football (soccer) team from a large pool of players. Each player has a cost, and a rating. You have a limited budget. What is the highest total rating of a team that fits within your budget. Assume that there's no minimum or maximum team size.

General problem statement:

Given n elements, each of which has a weight and a profit, determine the maximum profit that can be obtained by selecting a subset of the elements weighing no more than w.
"""


def max_profit_recursive(capacity, weights, profits, idx=0):
    """
    - We'll write a recursive function that computes max_profit(weights[idx:], profits[idx:], capacity), with idx starting from 0.

    - If weights[idx] > capacity, the current element is cannot be selected, so the maximum profit is the same as max_profit(weights[idx+1:], profits[idx+1:], capacity).

    - Otherwise, there are two possibilities: we either pick weights[idx] or don't. We can recursively compute the maximum

        - A. If we don't pick weights[idx], once again the maximum profit for this case is max_profit(weights[idx+1:], profits[idx+1:], capacity)

        - B. If we pick weights[idx], the maximum profit for this case is profits[idx] + max_profit(weights[idx+1:], profits[idx+1:], capacity - weights[idx]

    - If weights[idx:] is empty, the maximum profit for this case is 0.
    - Time complexity O(2^N)
    """
    if idx == len(weights):
        return 0
    if weights[idx] > capacity:
        return max_profit_recursive(capacity, weights, profits, idx+1)
    else:
        return max(max_profit_recursive(capacity, weights, profits, idx+1),
                   profits[idx] + max_profit_recursive(capacity-weights[idx], weights, profits, idx+1))


def knapsack_memo(capacity, weights, profits):
    """
    Memorization will have complexity of O(M * N)
    """
    memo = {}

    def recurse(idx, remaining):
        key = (idx, remaining)
        if key in memo:
            return memo[key]
        elif idx == len(weights):
            memo[key] = 0
        elif weights[idx] > remaining:
            memo[key] = recurse(idx+1, remaining)
        else:
            memo[key] = max(recurse(idx+1, remaining),
                            profits[idx] + recurse(idx+1, remaining-weights[idx]))
        return memo[key]

    return recurse(0, capacity)


def knapsack_dp(capacity, weights, profits):
    """
    - Create a table of size (n+1) * (capacity+1) consisting of all 0s, where is n is the number of elements. table[i][c] represents the maximum profit that can be obtained using the first i elements if the maximum capacity is c. Here's a visual representation of a filled table (source - geeksforgeeks):
    
    - We'll fill the table row by row and column by column. table[i][c] can be filled using some values in the row above it.

    - If weights[i] > c i.e. if the current element can is larger than capacity, then table[i+1][c] is simply equal to table[i][c] (since there's no way we can pick this element).

    - If weights[i] <= c then we have two choices: to either pick the current element or not to get the value of table[i+1][c]. We can compare the maximum profit for both these options and pick the better one as the value of table[i][c].

        - A. If we don't pick the element with weight weights[i], then once again the maximum profit is table[i][c]

        - B. If we pick the element with weight weights[i], then the maximum profit is profits[i] + table[i][c-weights[i]], since we have used up some capacity.

    Time complexity of the dynamic programming solution is O(N * W)
    """
    n = len(weights)
    results = [[0 for _ in range(capacity+1)] for _ in range(n+1)]

    for idx in range(n):
        for c in range(capacity+1):
            if weights[idx] > c:
                results[idx+1][c] = results[idx][c]
            else:
                results[idx+1][c] = max(results[idx][c],
                                        profits[idx] + results[idx][c-weights[idx]])

    return results[-1][-1]


test_cases = [
    {
    'input': {
        'capacity': 165,
        'weights': [23, 31, 29, 44, 53, 38, 63, 85, 89, 82],
        'profits': [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    },
    'output': 309
},
    {
    'input': {
        'capacity': 3,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 0
},
    {
    'input': {
        'capacity': 4,
        'weights': [4, 5, 1],
        'profits': [1, 2, 3]
    },
    'output': 3
},
    {
    'input': {
        'capacity': 170,
        'weights': [41, 50, 49, 59, 55, 57, 60],
        'profits': [442, 525, 511, 593, 546, 564, 617]
    },
    'output': 1735
},
    {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 6],
        'profits': [1, 2, 3]
    },
    'output': 6
},
    {
    'input': {
        'capacity': 15,
        'weights': [4, 5, 1, 3, 2, 5],
        'profits': [2, 3, 1, 5, 4, 7]
    },
    'output': 19
}
]