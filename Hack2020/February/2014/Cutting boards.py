def compute_min_cost(horizontal, vertical, total_cuts):
    i_h, i_v, cost = 0, 0, 0
    for i in xrange(total_cuts):
        if horizontal[i_h] >= vertical[i_v]:
            cost += horizontal[i_h] * (i_v + 1)
            i_h += 1
        else:
            cost += vertical[i_v] * (i_h + 1)
            i_v += 1
        cost %= 1000000007
    return cost

def main():
    T = int(raw_input())
    for t in xrange(T):
        M, N = (int(x) for x in raw_input().split())
        # Add -1 to the end of each list as a sentinel value.
        horizontal = sorted([int(x) for x in raw_input().split()], reverse=True) + [-1]
        vertical = sorted([int(x) for x in raw_input().split()], reverse=True) + [-1]
        print compute_min_cost(horizontal, vertical, M + N - 2)

if __name__ == "__main__":
    main()