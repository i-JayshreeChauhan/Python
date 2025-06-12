def is_valid_regex_manual(pattern):
    invalid_sequences = ["*+", "++", "?+", "**", "+*", "+?", "*?", "??"]

    # Check for known invalid quantifier combinations
    for seq in invalid_sequences:
        if seq in pattern:
            return False

    # Try compiling it to ensure general regex validity
    try:
        import re
        re.compile(pattern)
        return True
    except re.error:
        return False


# Input handling
T = int(input())
for _ in range(T):
    pattern = input()
    print(is_valid_regex_manual(pattern))