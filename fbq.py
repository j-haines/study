import time
import random
import string

# Consider a string of length 3 to 500,000. Write a program to calculate the
# lexicographically smallest and largest substrings. The substrings must start
# and end with a vowel, and the second character must be a consonant.

def fbq(seq):
    def is_vowel(char):
        return char in 'aeiouy'

    in_subsequence = False

    longest_seq = ''
    shortest_seq = seq

    # Index of the start of the current subsequence
    curr_seq_idx = 0
    last_vowel_idx = 0

    idx = 0
    last_char = chr(ord('a') - 1)
    curr_subsequence = ''
    while idx < len(seq):
        char = seq[idx]

        if is_vowel(char):
            last_vowel_idx = idx
        elif is_vowel(last_char):
            # Last char was a vowel and current char is a consonant
            curr_seq_idx = curr_seq_idx if in_subsequence else last_vowel_idx
            in_subsequence = True

        # Current sequence has been broken
        if char < last_char and in_subsequence:
            in_subsequence = False
            last_char = seq[curr_seq_idx + 1]
            idx = curr_seq_idx + 2
            continue

        # Current sequence is potentially complete
        if in_subsequence and is_vowel(char):
            curr_subsequence = seq[curr_seq_idx:idx + 1]

            if len(curr_subsequence) > len(longest_seq):
                longest_seq = curr_subsequence

            if len(curr_subsequence) < len(shortest_seq):
                shortest_seq = curr_subsequence

        last_char = char
        idx += 1
    return (longest_seq, shortest_seq)


if __name__ == '__main__':

    seq = 'abeeeeeer'
    assert fbq(seq) == ('abeeeeee', 'abe')
    print('[+] Test #1 passed.')

    seq = 'adefghryujgcvbbthgg'
    assert fbq(seq) == ('adefghry', 'ade')
    print('[+] Test #2 passed.')

    seq = 'qrytabbbbbbbbefibbbbbbb'
    assert fbq(seq) == ('abbbbbbbbefi', 'efi')
    print('[+] Test #3 passed.')
