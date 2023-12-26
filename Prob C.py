# Recursive function to modify a string based on its length
def f(s):
    n = len(s)
    
    # If the length is odd, return the original string
    if n % 2 == 1:
        return s
    
    # Divide the string into two halves and recursively call f on each half
    left = f(s[:n // 2])
    right = f(s[n // 2:])
    
    # Combine the modified left and right halves based on lexicographical order
    if left < right:
        return left + right
    return right + left

# Function to check if two strings are equivalent after modification
def equivalentStrings(s1, s2):
    # Compare the modified strings using function f
    if f(s1) == f(s2):
        return "YES"
    return "NO"

# Input two strings
s1 = input().strip()
s2 = input().strip()

# Call the equivalentStrings function and print the result
print(equivalentStrings(s1, s2))
