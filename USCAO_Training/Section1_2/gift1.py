"""
ID: wangyan27
LANG: PYTHON3
TASK: gift1
"""


fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')


input_lines = fin.readlines()

NP = int( input_lines[0] )
record = {}
for i in range(NP):
    record[ input_lines[i+1].strip() ] = 0

count = NP+1
for i in range(NP):
    giver_name = input_lines[count].strip()

    [money, group_num] = [ int(x) for x in input_lines[count+1].split() ]
    if group_num != 0:
        record[giver_name] -= (money - money % group_num )
        
        receiver_money = money // group_num
        for receiver_count in range(group_num):
            receiver_name = input_lines[count + 2 + receiver_count].strip()
            record[receiver_name] += receiver_money
    
    count += group_num + 2

for i in record:
    fout.write(str(i) + " " + str(record[i]) + "\n"    )
fout.close()