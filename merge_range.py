"""
Write a function condense_meeting_times() that takes a list of meeting time 
ranges and returns a list of condensed ranges.

For example, given:

    - [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

    - [(0, 1), (3, 8), (9, 12)]
"""

def merge_range(seq):
    sorted_seq = sorted(seq)

    flat = []
    end = None
    start = None
    for idx, period in enumerate(sorted_seq):
        if start is None:
            start = period[0]
            end = period[1]
        elif end >= period[0]:
            end = max(period[1], end)
        else:
            flat.append((start, end,))
            start = period[0]
            end = period[1]
        
        if idx + 1 == len(seq):
            flat.append((start, end,))

    return flat


if __name__ == '__main__':
    seq = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    assert merge_range(seq) == [(0, 1), (3, 8), (9, 12)]
    print('[+] Test #1 passed')

    seq = [(1, 2), (2, 3)]
    assert merge_range(seq) == [(1, 3),]
    print('[+] Test #2 passed')

    seq = [(1, 5), (2, 3)]
    assert merge_range(seq) == [(1, 5),]
    print('[+] Test #3 passed')

    seq = [(1, 10), (2, 6), (3, 5), (7, 9)]
    assert merge_range(seq) == [(1, 10),]
    print('[+] Test #4 passed')
