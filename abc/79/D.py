def main():
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    for k in range(10):
        for i in range(10):
            for j in range(10):
                C[i][j] = min(C[i][j], C[i][k] + C[k][j])
    ans = 0
    for h in range(H):
        for a in A[h]:
            if a >= 0:
                ans += C[a][1]
    print(ans)


main()
