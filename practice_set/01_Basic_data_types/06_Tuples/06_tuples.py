
import hashlib

if __name__ == "__main__":
   
   n = int(input())            # Read number of elements
   integer_list = map(int, input().split())
   t = tuple(integer_list)

    
   # Convert tuple to bytes and hash using SHA-256 (or any stable hash)
   h = hashlib.sha256(str(t).encode()).hexdigest()
   print(h)