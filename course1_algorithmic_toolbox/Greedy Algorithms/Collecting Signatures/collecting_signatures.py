# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    segments = sorted(segments, key=lambda x: x.start)
    n_points = 0
    output_points = []
    segment = segments[0]
    start, end = segment.start, segment.end
    for i in range(1, len(segments)):
        segment = segments[i]
        if segment.start > end:
            n_points += 1
            output_points.append(end)
            start, end = segment.start, segment.end
        elif segment.end < end:
            end = segment.end
    n_points += 1
    output_points.append(end)
    return output_points





if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
