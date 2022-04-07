# Uses python3
import sys

# def get_majority_element(a, left, right):
#     if right == left + 1:
#         return a[0]
        
#     mid = (right - left)//2
#     left_majority = get_majority_element(a[left, mid], left, mid)
#     right_majority = get_majority_element(a[mid, right], mid, right)
#     if left_majority == right_majority:
#         return left_majority
#     else:
#         left_count = sum([_ for _ in a[left, mid] if _ == left_majority])
#         right_count = sum([_ for _ in a[mid, right] if _ == right_majority])

#         return left_majority if left_count >= right_count else right_majority


def get_majority_element(a, left, right):
    counter = {}
    for i in a:
        try:
            counter[i] += 1
        except KeyError:
            counter[i] = 1
    
    if max(counter.values()) > len(a)/2:
        return 1
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
