"""
ID: wangyan27
LANG: PYTHON3
PROG: friday
"""


fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

month_days_list = [ 
    [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
    [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
]

outputs = [0]*7

starting_year = 1900
number_year = int( fin.readline().strip() )

accumulated_days = 0
for i in range(number_year):
    year = starting_year + i
    if i % 100 == 0:
        if year % 400 == 0:
            leap = 1
        else:
            leap = 0
    else:
        if year % 4 == 0:
            leap = 1
        else:
            leap = 0

    month_days = month_days_list[leap]

    for j in range( len(month_days) ):
        week_day_count = ( sum(month_days[0:j]) + 13  + accumulated_days) % 7 -1
        outputs[week_day_count] += 1
    accumulated_days += sum(month_days)

outputs = outputs[5:7] + outputs[:5]

for i in range(len(outputs)):
    if i != len(outputs)-1:
        fout.write(str(outputs[i]) + ' ')
    else:
        fout.write(str(outputs[i]) + '\n')
fout.close()
