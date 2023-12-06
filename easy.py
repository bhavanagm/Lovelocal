def length_of_last_word(s):
    # Split the string into words by spaces and filter out empty strings
    words = s.split()
    
    # Return the length of the last word
    return len(words[-1])

# Test cases
s1 = "Hello World"
print(length_of_last_word(s1))  # Output: 5

s2 = "   fly me   to   the moon  "
print(length_of_last_word(s2))  # Output: 4

s3 = "luffy is still joyboy"
print(length_of_last_word(s3))  # output:5