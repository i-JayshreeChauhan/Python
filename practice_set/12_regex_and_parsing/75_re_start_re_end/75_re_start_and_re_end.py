import re

s = input()
substr = input()

# Use lookahead to find overlapping matches
pattern = f"(?=({re.escape(substr)}))"

matches = re.finditer(pattern, s)

found = 0


for match in matches:
    found=1
    start = match.start()
    end = start + len(substr) - 1
    print((start, end))

if found == 0:
    print("(-1, -1)")