d = {"greg" : 1, "dave" : 2, "amy" : 3}
print(d)

# Add key:value pair - O(1)
d["vin"] = 5
print(d)

# Search for a key in dict - O(1)
if "amy" in d:
    print(True)
    
# Get corresponding value for a key - O(1)
print(d["amy"])

# Loop through key:value pairs in a dict
for key, val in d.items():
    print(f"{key} : {val}")
    
# DefaultDict
from collections import defaultdict, Counter

default = defaultdict(int)

print(default[2])
print(default[3])

string = "aaAaabbbbcccddeeee"
counter = Counter(string)
print(counter)
