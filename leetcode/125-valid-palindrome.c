/* 125-valid-palindrome.c
 *
 * Copyright (C) 2019 Sang-Kil Park <likejazz@gmail.com>
 * All rights reserved.
 *
 * This software may be modified and distributed under the terms
 * of the BSD license.  See the LICENSE file for details.
 */
bool isPalindrome(char *s) {
    int bias_left = 0;
    int bias_right = 1;

    int str_len = strlen(s);
    for (int i = 0; i < str_len; i++) {
        // Consider only alphanumeric chars from left side.
        while (!isalnum(s[i + bias_left])) {
            bias_left++;
            // Return true if only empty string remain.
            if (i + bias_left == str_len)
                return true;
        }
        // Consider only alphanumeric chars from right side.
        while (!isalnum(s[str_len - i - bias_right])) {
            bias_right++;
        }

        // Break when left pivot goes over right pivot.
        if (i + bias_left >= str_len - i - bias_right)
            break;
        // Check whether or not is palindrome.
        if (tolower(s[i + bias_left]) != tolower(s[str_len - i - bias_right]))
            return false;
    }
    return true;
}
