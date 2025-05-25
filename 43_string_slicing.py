x = "python programming"
"""
This script demonstrates various string slicing techniques in Python.
String slicing allows you to extract a portion of a string by specifying a range of indices.
The general syntax for slicing is: string[start:stop:step]
Key slicing examples in this script:
1. `x[7:]` - Extracts the substring starting from index 7 to the end of the string.
2. `x[::-2]` (commented out) - Reverses the string and selects every second character.
3. `x[::1]` (commented out) - Selects the entire string with a step of 1 (default behavior).
4. `x[-11:]` - Extracts the substring starting from the 11th character from the end to the end of the string.
Note:
- Positive indices start from the beginning of the string (0-based indexing).
- Negative indices start from the end of the string (-1 being the last character).
- The `step` parameter determines the interval between characters in the slice.
"""
# print(x[7:])

#print(x[::-2])
print(x[-5:])
print(x[-5:5:-1])
print(x[-5:-5:1])








# print(x[-11:])
