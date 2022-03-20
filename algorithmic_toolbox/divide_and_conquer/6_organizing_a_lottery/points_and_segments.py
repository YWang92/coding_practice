# Uses python3
from multiprocessing import Event
from os import stat
import sys
import collections

Event = collections.namedtuple("Event", ['coordinate', 'type', "index"])

        
def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)

    events = []
    for i in range(len(starts)):
        events.append(Event(starts[i], 0, i))
        events.append(Event(ends[i], 2, i))
    for i in range(len(points)):
        events.append(Event(points[i], 1, i))
    
    # event.type are set as 0,1,2. So that the list events is sorted
    # in the priority of start, point and end respectively !!!!
    events = sorted(events)
    number_of_segments = 0
    for event in events:
        if event.type == 0:
            number_of_segments += 1
        elif event.type == 2:
            number_of_segments -= 1
        elif event.type == 1:
            cnt[event.index] = number_of_segments

    return cnt



# from bisect import bisect_left, bisect_right

# def fast_count_segments(starts, ends, points):
#     starts, ends = sorted(starts), sorted(ends)
#     count = [len(starts)] * len(points)
#     for index, point in enumerate(points):
#         count[index] -= bisect_left(ends, point)
#         count[index] -= len(starts) - bisect_right(starts, point)
#     return count


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
