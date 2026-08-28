class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int maxCount = 0;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            count = nums[i] == 1 ? count + 1 : 0;
            maxCount = Math.max(maxCount, count);
        }
        return maxCount;
    }
}