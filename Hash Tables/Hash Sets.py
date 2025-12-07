s = set()
print(s)

# Add value - O(1)
s.add(1)
s.add(2)
s.add(3)
s.add(1)
s.add(7)
print(s)

# Remove values - O(1)
s.remove(3)
print(s)

# Search for a value - O(1)
if 1 in s:
    print(True)

# Constructing a set from a string - O(S), S is length on string
string = "aaaaabbbbcccddeeee"
strs = set(string)
print(strs)
