def shortestPalindrome(s):
    if not s:
        return ""

    # Function to check if a string is a palindrome
    def is_palindrome(string):
        return string == string[::-1]

    for i in range(len(s), 0, -1):
        # Check if the substring s[:i] is a palindrome
        if is_palindrome(s[:i]):
            # Reverse the remaining part of the string and append it to the beginning
            return s[i:][::-1] + s

    return ""  # Return an empty string if no palindrome found

# Test cases
s1 = "aacecaaa"
print(shortestPalindrome(s1))  # Output: "aaacecaaa"

s2 = "abcd"
print(shortestPalindrome(s2))  # Output: "dcbabcd"