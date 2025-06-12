
def custom_sort(s):
    return ''.join(sorted(s, key=lambda c: (
        c.isdigit(),           # digits after letters
        c.isupper(),           # uppercase after lowercase
        int(c) % 2 == 0 if c.isdigit() else False,  # even after odd for digits
        c                      # natural order
    )))

s = input()
print(custom_sort(s))
