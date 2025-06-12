# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
Student = namedtuple('Student', input().split())
print(f"{sum(int(Student(*input().split()).MARKS) for _ in range(n)) / n:.2f}")
        
    
