# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def get_maximum_value(dataset):
    nums, ops = [], []
    for char in range(len(dataset)):
        if char % 2 == 0:
            nums.append(int(dataset[char]))
        else:
            ops.append(dataset[char])

    min_matrix = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    max_matrix = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    for i in range(len(nums)):
        min_matrix[i][i] = nums[i]
        max_matrix[i][i] = nums[i]

    for diff in range(1, len(nums)):
        for i in range(len(nums)-diff):
            j = i + diff
            solutions = []
            for k in range(i, j):
                op = ops[k]
                min_first, max_first = min_matrix[i][k], max_matrix[i][k]
                min_second, max_second = min_matrix[k+1][j], max_matrix[k+1][j]
                for a in [min_first, max_first]:
                    for b in [min_second, max_second]:
                        solutions.append(evalt(a, b, op))
            min_matrix[i][j] = min(solutions)
            max_matrix[i][j] = max(solutions)

    return max_matrix[0][-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))


