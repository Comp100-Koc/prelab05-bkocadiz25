def longest_palindromic_substring(s):
    """
    Given a string find the longest palindromic substring
    """
    longest = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            part = s[i:j]
            if part == part[::-1] and len(part) > len(longest) and len(part) > 1:
                longest = part

    return longest