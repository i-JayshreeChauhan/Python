
m_set = set()
n_set = set()

M = int(input())

m_set = input().split()
m_set = set(map(int,m_set))


N = int(input())

n_set = input().split()
n_set = set(map(int,n_set))

a = m_set.difference(n_set)
b = n_set.difference(m_set)

c = a.union(b)
c = list(c)
c.sort()

for i in c:
    print(i)
