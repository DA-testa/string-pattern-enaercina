def read_input():
    # Input reading function
    return input().rstrip(), input().rstrip()


def print_occurrences(output):
    # Output printing function
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # Rabin-Karp algorithm implementation to find all occurrences of a pattern in a text
    result = []
    p = 10**9 + 7  # prime number for hashing
    x = 263  # base number for hashing

    # Hash the pattern and the first window of the text
    p_hash = 0
    t_hash = 0
    x_pow = 1
    for i in range(len(pattern)):
        p_hash = (p_hash + ord(pattern[i]) * x_pow) % p
        t_hash = (t_hash + ord(text[i]) * x_pow) % p
        x_pow = (x_pow * x) % p

    # Compare the hash of the pattern and the hash of the current window in the text
    for i in range(len(text) - len(pattern) + 1):
        if p_hash == t_hash:
            if text[i:i+len(pattern)] == pattern:
                result.append(i)

        # Calculate the hash of the next window in the text
        if i < len(text) - len(pattern):
            t_hash = (x * (t_hash - ord(text[i]) * x_pow) + ord(text[i+len(pattern)])) % p
            if t_hash < 0:
                t_hash += p
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
