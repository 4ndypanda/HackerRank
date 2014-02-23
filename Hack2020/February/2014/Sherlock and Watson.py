def main():
    N, K, Q = [int(x) for x in raw_input().split()]
    A = [int(x) for x in raw_input().split()]
    for i in xrange(Q):
        x = int(raw_input())
        print A[(x - K % N + N) % N]

if __name__ == "__main__":
    main()