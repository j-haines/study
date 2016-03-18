"""
Write a function to find the rectangular intersection of two given love
rectangles.

As with the example above, love rectangles are always "straight" and never
"diagonal." More rigorously: each side is parallel with either the x-axis or
the y-axis.

They are defined as dictionaries like this:

my_rectangle = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 5,

    # width and height
    'width': 10,
    'height': 4,
}

Your output rectangle should use this format as well.
"""


def rectangular_love(lr, rr):
    def to_coords(rect):
        x = rect['left_x']
        y = rect['bottom_y']
        width = rect['width']
        height = rect['height']

        return ((x, y,), (x + width, y + height),)
    def overlap(l, r):
        lx = max(l[0], r[0])
        rx = min(l[1], r[1])
        return (lx, rx)

    def x_overlap(lr, rr):
        lx = (lr['left_x'], lr['left_x'] + lr['width'])
        rx = (rr['left_x'], rr['left_x'] + rr['width'])
        return overlap(lx, rx)
    def y_overlap(lr, rr):
        ly = (lr['bottom_y'], lr['bottom_y'] + lr['height'])
        ry = (rr['bottom_y'], rr['bottom_y'] + rr['height'])
        return overlap(ly, ry)
    y = y_overlap(lr, rr)
    x = x_overlap(lr, rr)

    left_x = x[0]
    bottom_y = y[0]
    width = x[1] - left_x
    height = y[1] - bottom_y

    if width < 0 or height < 0:
        return {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None
        }

    return {
        'left_x': left_x,
        'bottom_y': bottom_y,
        'width': width,
        'height': height
    }

if __name__ == '__main__':
    lr = {'left_x': 0, 'bottom_y': 0, 'height': 5, 'width': 5}
    rr = {'left_x': 6, 'bottom_y': 6, 'height': 1, 'width': 4}
    rect = {'left_x': None, 'bottom_y': None, 'height': None, 'width': None}
    assert rectangular_love(lr, rr) == rect
    print('[+] Test #1 passed')

    rr = {'left_x': 2, 'bottom_y': 4, 'height': 3, 'width': 3}
    rect = {'left_x': 2, 'bottom_y': 4, 'height': 1, 'width': 3}
    assert rectangular_love(lr, rr) == rect
    print('[+] Test #2 passed')

    rr = {'left_x': 1, 'bottom_y': 1, 'height': 2, 'width': 2}
    rect = rr
    assert rectangular_love(lr, rr) == rect
    print('[+] Test #3 passed')

    rr = {'left_x': 5, 'bottom_y': 0, 'height': 5, 'width': 5}
    rect = {'left_x': 5, 'bottom_y': 0, 'height': 5, 'width': 0}
    assert rectangular_love(lr, rr) == rect
    print('[+] Test #4 passed')
