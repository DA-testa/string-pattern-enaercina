import sys

def read_input():
    choice = input().strip()
    if choice == 'I':
        pattern = input().strip()
        text = input().strip()
    elif choice == 'F':
        with open('tests/1.in') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def hash(s, prime, multiplier):
    h = 0
    for c in reversed(s):
        h = (h * multiplier + ord(c)) % prime
    return h

def precompute_hashes(T, P, p, x):
    n, m = len(T), len(P)
    H = [None] * (n - m + 1)
    S = T[n - m:]
    H[n - m] = hash(S, p, x)
    y = 1
    for i in range(1, m + 1):
        y = (y * x) % p
    for i in range(n - m - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(T[i]) - y * ord(T[i + m])) % p
    return H

def get_occurrences(pattern, text):
    prime = 10**9 + 7
    multiplier = 263
    p_hash = hash(pattern, prime, multiplier)
    H = precompute_hashes(text, pattern, prime, multiplier)
    return [i for i in range(len(text) - len(pattern) + 1) if p_hash == H[i] and text[i:i+len(pattern)] == pattern]

if __name__ == '__main__':
    pattern, text = read_input()
    occurrences = get_occurrences(pattern, text)
    print_occurrences(occurrences)
