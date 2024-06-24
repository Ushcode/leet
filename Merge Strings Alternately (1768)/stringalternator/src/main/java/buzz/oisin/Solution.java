package buzz.oisin;

public class Solution {
    public static String mergeAlternately(String word1, String word2) {
        int shorter = Math.min(word1.length(), word2.length());
        
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < shorter; i++) {
            result.append(word1.charAt(i));
            result.append(word2.charAt(i));
        }
        result.append(word1.substring(shorter));
        result.append(word2.substring(shorter));

        return result.toString();
    }

    public static void main(String[] args) {
        System.out.println(Solution.mergeAlternately(args[0], args[1]));
    }
}