def read_input():
    # Read two lines of input: the pattern and the text
    pattern = input().rstrip()
    text = input().rstrip()
    return pattern, text

def print_occurrences(output):
    # Print the positions of occurrences
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # Define constants for the Rabin-Karp algorithm
    p = 31
    m = 10**9 + 9
    # Calculate the hash of the pattern and the first substring of the text
    pattern_hash = 0
    substring_hash = 0
    p_power = 1
    for i in range(len(pattern)):
        pattern_hash = (pattern_hash + (ord(pattern[i]) - ord('a') + 1) * p_power) % m
        substring_hash = (substring_hash + (ord(text[i]) - ord('a') + 1) * p_power) % m
        p_power = (p_power * p) % m
    # Slide the window over the text and compare hash values
    occurrences = []
    for i in range(len(text) - len(pattern) + 1):
        if pattern_hash == substring_hash:
            if pattern == text[i:i+len(pattern)]:
                occurrences.append(i)
        if i < len(text) - len(pattern):
            substring_hash = (substring_hash - (ord(text[i]) - ord('a') + 1) * p_power) % m
            substring_hash = (substring_hash * p + (ord(text[i+len(pattern)]) - ord('a') + 1)) % m
            substring_hash = (substring_hash + m) % m
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
