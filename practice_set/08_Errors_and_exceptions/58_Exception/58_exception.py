# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())

for i in range(N):
    try:
        a,b = map(int,input().split())

        result = a//b
        print(result)
        
    except Exception as e:
        print(f"Error Code: {e}")
