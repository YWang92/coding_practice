"""
ID: wangyan27
LANG: PYTHON3
PROG: milk2
"""


fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')

number_famers= int( fin.readline().strip() )
farmer_times = []
for _ in range(number_famers):
    farmer_times.append( [int(_) for _ in fin.readline().split()] )

# sort farmers by their starting times
farmer_times.sort(key = lambda x:x[0])

interval_start, interval_end = farmer_times[0][0], farmer_times[0][1]
longest_continuous, longest_idle = interval_end - interval_start, 0

for farmer in range(1, number_famers):
    farmer_start, farmer_end = farmer_times[farmer][0], farmer_times[farmer][1]
 
    if farmer_start > interval_end:
        longest_idle = max( [farmer_start - interval_end, longest_idle] )
        interval_start, interval_end = farmer_start, farmer_end
    
    elif farmer_end > interval_end:
        interval_end = farmer_end
    
    longest_continuous = max( [interval_end - interval_start, longest_continuous] )
    

        
fout.write(str(longest_continuous) + " " + str(longest_idle) + '\n')
fout.close()
