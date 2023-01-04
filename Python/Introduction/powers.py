'''Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers i < n, print . i^2'''

if __name__ == '__main__':
    n = int(input())
    if n>0:
        m = 0
        while(n>m):
            print(str(m**2))
            m+=1