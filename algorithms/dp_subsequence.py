import sys
sys.path.append(".")

from utils.test_utils import evaluate_test_cases

"""
Write a function to find the length of the longest common subsequence between two sequences. E.g. Given the strings "serendipitous" and "precipitation", the longest common subsequence is "reipito" and its length is 7.

A "sequence" is a group of items with a deterministic ordering. Lists, tuples and ranges are some common sequence types in Python.

A "subsequence" is a sequence obtained by deleting zero or more elements from another sequence. For example, "edpt" is a subsequence of "serendipitous".

- General case (string)
- General case (list)
- No common subsequence
- One is a subsequence of the other
- One sequence is empty
- Both sequences are empty
- Multiple subsequences with same length
        - “abcdef” and “badcfe”
"""


def lcq_recursive(seq1, seq2, idx1=0, idx2=0):
    """
    The number of unique paths from root to leaf. The length of each path is m+n and at each level there are 2 choices.
    Based on the above can you infer that the time complexity is O(2^(m+n))
    """
    # Check if either of the sequences is exhausted
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0

    # Check if the current characters are equal
    if seq1[idx1] == seq2[idx2]:
        return 1 + lcq_recursive(seq1, seq2, idx1+1, idx2+1)
    # Skip one element from each sequence
    else:
        return max(lcq_recursive(seq1, seq2, idx1+1, idx2),
                   lcq_recursive(seq1, seq2, idx1, idx2+1))
        

def lcq_memoized(seq1, seq2):
    """
    Memorization bought the complexity down. It's equal to unique memorization combination
    Time complexity O(M * N)
    """
    memo = {}

    def recurse(idx1, idx2):
        key = idx1, idx2

        if key in memo:
            return memo[key]

        if idx1 == len(seq1) or idx2 == len(seq2):
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            memo[key] = max(recurse(idx1+1, idx2),
                            recurse(idx1, idx2+1))
        return memo[key]

    return recurse(0, 0)


def lcq_dp(seq1, seq2):
    """
    - Create a table of size (n1+1) * (n2+1) initialized with 0s, where n1 and n2 are the lengths of the sequences. table[i][j] represents the longest common subsequence of seq1[:i] and seq2[:j]. Here's what the table looks like (source: Kevin Mavani, Medium).
    - seq1[i] and seq2[j] are equal, then table[i+1][j+1] = 1 + table[i][j]
    - f seq1[i] and seq2[j] are not equal, then table[i+1][j+1] = max(table[i][j+1], table[i+1][j])
    Time complexity of the dynamic programming approach is O(M * N)
    """
    n1, n2 = len(seq1), len(seq2)
    results = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    for idx1 in range(n1):
        for idx2 in range(n2):
            if seq1[idx1] == seq2[idx2]:
                results[idx1+1][idx2+1] = 1 + results[idx1][idx2]
            else:
                results[idx1+1][idx2 + 1] = max(results[idx1][idx2+1], results[idx1+1][idx2])
    return results[-1][-1]


test_cases = [
    {
    'input': {
        'seq1': 'serendipitous',
        'seq2': 'precipitation'
    },
    'output': 7
},
    {
    'input': {
        'seq1': [1, 3, 5, 6, 7, 2, 5, 2, 3],
        'seq2': [6, 2, 4, 7, 1, 5, 6, 2, 3]
    },
    'output': 5
},
    {
    'input': {
        'seq1': 'longest',
        'seq2': 'stone'
    },
    'output': 3
},
    {
    'input': {
        'seq1': 'asdfwevad',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
},
    {
    'input': {
        'seq1': 'dense',
        'seq2': 'condensed'
    },
    'output': 5
},
    {
    'input': {
        'seq1': '',
        'seq2': 'opkpoiklklj'
    },
    'output': 0
},
    {
    'input': {
        'seq1': '',
        'seq2': ''
    },
    'output': 0
},
    {
    'input': {
        'seq1': 'abcdef',
        'seq2': 'badcfe'
    },
    'output': 3
}
]

