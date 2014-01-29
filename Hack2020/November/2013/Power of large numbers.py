def modpow(a, b, c):
    result = 1
    b_bin = bin(b)[2:]
    for i in reversed(b_bin):
        if i == '1':
            result = result * a % c
        a = a ** 2 % c
    return result

def main():
    C = 10 ** 9 + 7
    T = int(raw_input())
    for t in range(T):
        A, B = (long(x) for x in raw_input().split())
        A %= C
        print modpow(A, B, C)

if __name__ == "__main__":
    main()