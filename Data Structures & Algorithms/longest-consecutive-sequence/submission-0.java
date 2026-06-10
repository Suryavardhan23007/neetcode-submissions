class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<>();
        for(int num: nums){
            set.add(num);
        }
        int maxCount = 0;
        for(int num: set){
            if(set.contains(num-1)){
                continue;
            }
            int seqCount = 1;
            int temp = num;
            while(set.contains(temp+1)){
                seqCount += 1;
                temp += 1;
            }
            maxCount = Math.max(maxCount, seqCount);
        }
        return maxCount;
    }
}
