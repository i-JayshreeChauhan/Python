N , X  = map(int, input().split())    # N = number of students , X = number of subjects
l = [] 

for _ in range(X):
    l.append(list(map(float,input().split())))




tot = list(zip(*l))

for i in tot:
    print(f"{sum(i) / float(X):.1f}" )



