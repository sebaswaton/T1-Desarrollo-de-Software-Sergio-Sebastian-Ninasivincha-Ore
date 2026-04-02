from collections import defaultdict
import sys

def solve():
    data = sys.stdin.read().split()

    if not data:
        return

    N = int(data[0])
    M = int(data[1])
    S = int(data[2])

    idx = 3
    terminal_to_partner = {}

    for _ in range(M):
        p = int(data[idx])
        t = int(data[idx + 1])
        terminal_to_partner[t] = p
        idx += 2

    partner_clients = [defaultdict(int) for _ in range(N + 1)]

    for _ in range(S):
        c = int(data[idx])
        t = int(data[idx + 1])
        idx += 2

        if t in terminal_to_partner:
            partner = terminal_to_partner[t]
            partner_clients[partner][c] += 1

    for partner in range(1, N + 1):
        if not partner_clients[partner]:
            print(partner, -1)
        else:
            best_client = -1
            best_count = -1

            for client, count in partner_clients[partner].items():
                if count > best_count or (count == best_count and client < best_client):
                    best_count = count
                    best_client = client

            print(partner, best_client)

if __name__ == "__main__":
    solve()