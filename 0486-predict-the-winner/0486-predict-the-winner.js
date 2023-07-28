/**
 * @param {number[]} nums
 * @return {boolean}
 */
var PredictTheWinner = function(nums) {
    const n = nums.length;
    // Create a 2D array filled with zeros
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    
    // Base case: the score difference when there's only one number
    for (let i = 0; i < n; i++) {
        dp[i][i] = nums[i];
    }
    
    // Calculate the score difference for remaining subarrays
    for (let len = 1; len < n; len++) {
        for (let i = 0; i < n - len; i++) {
            const j = i + len;
            dp[i][j] = Math.max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1]);
        }
    }
    
    // If the score difference at the end is non-negative, Player 1 can win
    return dp[0][n - 1] >= 0;
};
