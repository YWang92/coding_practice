"""
ID: wangyan27
LANG: PYTHON3
PROG: transform
"""


fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')


number_patterns = int( fin.readline().strip() )

before_pattern = []
for _ in range(1, number_patterns + 1):
    pattern = [_ for _ in fin.readline().strip()]
    before_pattern.append( pattern )
print(before_pattern)

after_pattern = []
for _ in range(number_patterns + 1, 2*number_patterns + 1 ):
    pattern = [_ for _ in fin.readline().strip()]
    after_pattern.append( pattern )

def rotation_90(pattern):
    after_pattern = [ [0]*number_patterns for _ in range(number_patterns) ]
    for i in range(number_patterns):
        for j in range(number_patterns):
            # for i, 0->2, 1->1, 2->0
            after_pattern[j][abs(i-number_patterns+1)] = pattern[i][j]
    
    return after_pattern

def rotation(pattern, n):
    if n != 0:
        for _ in range(1, n+1):
            pattern = rotation_90(pattern)
    return pattern

def reflection(pattern, ref = 1):
    after_pattern = [ [0]*number_patterns for _ in range(number_patterns) ]
    if ref == 0:
        after_pattern = pattern

    elif ref == 1:
        for i in range(number_patterns):
            for j in range(number_patterns):
                after_pattern[i][j] = pattern[i][-(j+1)]
            
    return after_pattern


def transformations(before_pattern):
    transformation_types = []
    for ref in [0, 1]:
        for n in range(4):
            changed_pattern = rotation( reflection(before_pattern, ref),   n )
            if changed_pattern == after_pattern:
                number_transform = n + ref

                if ref == 0 and n == 0:
                    transformation_types.append(6)
                elif ref == 1 and n == 0:
                    transformation_types.append(4)
                elif ref == 0 and n != 0:
                    transformation_types.append(n)
                elif ref == 1 and n != 0:
                    transformation_types.append(5)
    if len(transformation_types) == 0:
        return 7
    else:
        return min(transformation_types)
 

transform_type = transformations(before_pattern)

fout.write(str(transform_type) + '\n')
fout.close()