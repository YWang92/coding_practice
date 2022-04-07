# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d
    n_refill, curr_stop = 0, 0
    n = len(stops)
    limit = m
    while limit < d:
        if curr_stop >= n or stops[curr_stop] > limit:
            return -1
        while curr_stop < n-1 and stops[curr_stop + 1] <= limit:
            curr_stop += 1
        n_refill += 1
        limit = stops[curr_stop] + m
        curr_stop += 1

    return n_refill






if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
