# python3
import collections

def each_window(sequence, m, deque, window):
    for i in range(m):
        while deque and sequence[i] >= deque[-1]:
            deque.pop()    
        deque.append(i)
    
    return deque

def max_sliding_window(sequence, m):
    deque = collections.deque()
    maximums = []

    # first sliding window
    for i in range(m):
        while deque and sequence[i] >= sequence[deque[-1]]:
            deque.pop()    
        deque.append(i)
    maximums.append(sequence[deque[0]])

    for window in range(1, len(sequence) - m + 1):
        # the first element of previous sliding window is removed
        if deque[0] == window - 1:
            deque.popleft()
        
        # the index of the last element of the current window
        last_element = m  + window - 1
        while deque and sequence[last_element] >= sequence[deque[-1]]:
            deque.pop()
        deque.append(last_element)

        maximums.append(sequence[deque[0]])

    return maximums


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    print(*max_sliding_window(input_sequence, window_size))

