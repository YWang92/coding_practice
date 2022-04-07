import sys

def get_number_of_inversions(a, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, left, ave)
    number_of_inversions += get_number_of_inversions(a, ave, right)
    #write your code here
    a1, a2 = a[left:ave], a[ave:right]
    b = []
    while a1 and a2:
        if a1[0] > a2[0]:
            b.append(a1[0])
            a1.pop(0)
            number_of_inversions += len(a2)
        else:
            b.append(a2[0])
            a2.pop(0)
    b += (a1 + a2)
    a[left:right] = b
    
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    print(get_number_of_inversions(a, 0, len(a)))
