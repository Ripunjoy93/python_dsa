"""
Problem statement:

A cafeteria table consists of a row of N seats, numbered from 1 to N from left to right. Social distancing guidelines require that every diner be seated such that K seats to their left and K seats to their right (or all the remaining seats to that side if there are fewer than K) remain empty.

There are currently M diners seated at the table, the i-th of whom is in seat S_i. No two diners are sitting in the same seat, and the social distancing guidelines are satisfied.

Determine the maximum number of additional diners who can potentially sit at the table without social distancing guidelines being violated for any new or existing diners, assuming that the existing diners cannot move and that the additional diners will cooperate to maximize how many of them can sit down.

Please take care to write a solution which runs within the time limit.

Constraints
1 ≤ N ≤1 0^15
1 ≤ K ≤ N
1 ≤ M ≤ 500,000
M ≤ N
1 ≤ S_i ≤ N

Sample test case #1
N = 10
K = 1
M = 2
S = [2, 6]
Expected Return Value = 3

Sample test case #2
N = 15
K = 2
M = 3
S = [11, 6, 14]
Expected Return Value = 1

In the first case, the cafeteria table has N = 10N=10 seats, with two diners currently at seats 22 and 66 respectively. The table initially looks as follows, with brackets covering the K = 1K=1 seat to the left and right of each existing diner that may not be taken.
  1 2 3 4 5 6 7 8 9 10
  [   ]   [   ]
Three additional diners may sit at seats 44, 88, and 1010 without violating the social distancing guidelines.
In the second case, only 11 additional diner is able to join the table, by sitting in any of the first 33 seats.
"""

from typing import List
import math

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  current_position = 1
  count = 0
  # sort it in ascending order
  S.sort()
  # There is a possibility of adding the last seat so
  S.append(N+K+1) # K+1 should be the addition if we want a gap of K
  
  for s in S:
    # calculate how many seats available
    seats = s - K - current_position
    if seats > 0:
      # check how many people seats can be occupied by social distancing norms
      count += math.ceil(seats/(K+1))
    # outside if: make the current position by increasing social distancing gap
    current_position = s + K + 1
    
  return count
