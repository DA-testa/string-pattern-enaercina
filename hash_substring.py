import sys

# function to read input from keyboard
def read_input():
    return input().rstrip(), input().rstrip()

# function to read input from file
def read_input_from_file():
    with open("test.txt", "r") as f:
        return f.readline().rstrip(), f.readline().rstrip()

# Rabin Karp's algorithm
def rabin_karp(pattern, text):
    p = 10**9 + 7
    x = 263
    result = []
    p_hash = sum(ord(pattern[i]) * pow(x, i, p) for i in range(len(pattern))) % p
    h = pow(x, len(pattern)-1, p)
    t_hash = sum(ord(text[i]) * pow(x, i, p) for i in range(len(pattern))) % p
    for i in range(len(text) - len(pattern) + 1):
        if p_hash == t_hash:
            if pattern == text[i:i+len(pattern)]:
                result.append(i)
        if i < len(text) - len(pattern):
            t_hash = (t_hash - ord(text[i]) * h) % p
            t_hash = (t_hash * x + ord(text[i+len(pattern)])) % p
            t_hash = (t_hash + p) % p
    return result

# function to print output
def print_output(result):
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    if sys.argv[1] == 'I':
        pattern, text = read_input()
    else:
        pattern, text = read_input_from_file()
    result = rabin_karp(pattern, text)
    print_output(result)
