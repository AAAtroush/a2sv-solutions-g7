t = int(input())

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()
    for i in range(n-1):
        if(abs(a[i] - a[i+1]) >= 2):
            print("NO")
            return
        
    print("YES")
    return


for tc in range(0, t):
    solve()
