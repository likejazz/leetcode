package com.likejazz.leetcode.solution482;

public class Solution {
    public String licenseKeyFormatting(String s, int k) {
        String result = "";
        String[] s_splitted = s.split("-");

        // Combine the splitted string array into single character sequence.
        String s_combined = "";
        for (int i = 0; i < s_splitted.length; i++) {
            s_combined += s_splitted[i];
        }

        // Exception Handling
        if (s_combined.length() == 0)
            return "";

        // Process PREFIX
        int first_part_len = s_combined.length() % k;
        if (first_part_len == 0) {
            first_part_len = k;
        }
        for (int i = 0; i < first_part_len; i++) {
            result += Character.toUpperCase(s_combined.charAt(i));
        }
        if (s_combined.length() > first_part_len)
            result += "-";

        // Process SUFFIX
        for (int i = first_part_len; i < s_combined.length(); i++) {
            if (i != first_part_len && (i - first_part_len) % k == 0) {
                result += "-";
            }
            result += Character.toUpperCase(s_combined.charAt(i));
        }

        return result;
    }
}
