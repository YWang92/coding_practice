# Uses python3
import sys

def optimal_sequence(n):
    path_list = [[]]  #  store the optimal sequences 
    
    for i in range(1, n+1):
        path = path_list[i-1] + [i]
        if i % 2 == 0 and len(path_list[i//2] + [i]) <= len(path):
            path = path_list[i//2] + [i]
        if i % 3 == 0 and len(path_list[i//3] + [i]) <= len(path):
            path = path_list[i//3] + [i]
        
        path_list.append(path)
    
    return path
                


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')