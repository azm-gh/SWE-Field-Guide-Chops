"""
LeetCode 1143: Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
"""


# Intuition: DP on two sequences. If chars match, LCS extends by 1:
# dp[i][j] = 1 + dp[i-1][j-1]. Otherwise, skip one char from either sequence:
# dp[i][j] = max(dp[i-1][j], dp[i][j-1]). The 2D table builds bottom-up.


def longest_common_subsequence_recursive_naive(text1: str, text2: str) -> int:
    # Time: O(2^(n+m)) — two recursive branches with overlapping subproblems
    # Space: O(n+m) — recursion stack depth
    def lcs(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + lcs(i + 1, j + 1)
        return max(lcs(i + 1, j), lcs(i, j + 1))
    return lcs(0, 0)


def longest_common_subsequence_dp_optimized(text1: str, text2: str) -> int:
    # Time: O(m*n) — fill 2D DP table
    # Space: O(m*n) — 2D DP table
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]
