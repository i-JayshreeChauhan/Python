
"""

A set A is a strict superset of set B if:

    -Every element of B is in A, and
    -A has at least one element not in B

"""


A = set(input().split())
n = int(input())

is_strict_superset = True

for _ in range(n):
    other_set = set(input().split())
    if not (A > other_set):  # A must be a strict superset
        is_strict_superset = False
        break

print(is_strict_superset)