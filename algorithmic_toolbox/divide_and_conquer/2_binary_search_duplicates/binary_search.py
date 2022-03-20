# python3


def binary_search(keys, query):
    low, high = 0, len(keys)-1
    while low <= high:
        mid = low + (high - low)//2
        if keys[mid] == query:
            index = mid
            high = mid - 1      
        elif keys[mid] > query:
            high = mid - 1
        else:
            low = mid + 1
    try:
        return index
    except NameError:
        return -1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
