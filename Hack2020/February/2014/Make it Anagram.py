import string

def get_frequency_count(S):
    freq = dict(((letter, 0) for letter in string.lowercase))
    for letter in S:
        freq[letter] += 1
    return freq

def main():
    freqA = get_frequency_count(raw_input())
    freqB = get_frequency_count(raw_input())
    deletions = 0
    for letter in string.lowercase:
        deletions += abs(freqA[letter] - freqB[letter])
    print deletions

if __name__ == "__main__":
    main()