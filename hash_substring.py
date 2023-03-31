import numpy as np

def read_input():
    return input().rstrip(), input().rstrip()

def poly_hash(s, p, x):
    hash_value = 0
    for i in reversed(s):
        hash_value = (hash_value * x + ord(i)) % p
    return hash_value

def precompute_hashes(text, len_pattern, p, x):
    len_text = len(text)
    H = np.zeros(len_text - len_pattern + 1, dtype=int)
    S = text[len_text - len_pattern:]
    H[len_text - len_pattern] = poly_hash(S, p, x)

    y = 1
    for i in range(len_pattern):
        y = (y * x) % p

    for i in range(len_text - len_pattern - 1, -1, -1):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + len_pattern])) % p

    return H

def get_occurrences(pattern, text):
    p = 10**9 + 7
    x = np.random.randint(1, p)

    p_hash = poly_hash(pattern, p, x)
    H = precompute_hashes(text, len(pattern), p, x)

    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if p_hash != H[i]:
            continue
        if text[i:i+len(pattern)] == pattern:
            occurrences.append(i)
    return occurrences

def print_occurrences(output):
    print(" ".join(map(str, output)))

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
