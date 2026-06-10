class Solution {
    public String mergeAlternately(String word1, String word2) {
        int len1 = word1.length(), len2 = word2.length();
        int i = 0, j = 0;
        String result = "";
        while(i != len1 && j != len2){
            result = result + word1.charAt(i) + word2.charAt(j);
            i++;
            j++;
        }
        while(i < len1){
            result = result + word1.charAt(i);
            i++;
        }
        while(j < len2){
            result = result + word2.charAt(j);
            j++;
        }
        return result;
    }
}