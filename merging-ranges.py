"""
To do this, you’ll need to know when any team is having a meeting. In HiCal, a
meeting is stored as tuples ↴ of integers (start_time, end_time). These
integers represent the number of 30-minute blocks past 9:00am.

For example:

    (2, 3) # meeting from 10:00 – 10:30 am
    (6, 9) # meeting from 12:00 – 1:30 pm

Write a function condense_meeting_times() that takes a list of meeting time
ranges and returns a list of condensed ranges.

For example, given:

    [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

your function would return:

    [(0, 1), (3, 8), (9, 12)]

Do not assume the meetings are in order. The meeting times are coming from
multiple teams.

In this case the possibilities for start_time and end_time are bounded by the
number of 30-minute slots in a day. But soon you plan to refactor HiCal to
store times as Unix timestamps (which are big numbers). Write something that's
efficient even when we can't put a nice upper bound on the numbers representing
our time ranges.
"""


def merge_ranges(ranges):
    def overlaps(ro, rt):
        return ro[1] > rt[0]

    sranges = [r for r in sorted(ranges)]

    merged = []
    prev_start, prev_end = sranges[0]
    for curr_start, curr_end in sranges[1:]:
        if curr_start <= prev_end:
            prev_end = max(curr_end, prev_end)
        else:
            merged.append((prev_start, prev_end,))
            prev_start, prev_end = curr_start, curr_end
    merged.append((prev_start, prev_end,))
    return merged


if __name__ == '__main__':
    ranges = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
    assert merge_ranges(ranges) == [(0, 1), (3, 8), (9, 12)]
    print('[+] Tests passed.')
