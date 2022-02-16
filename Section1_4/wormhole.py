"""
ID: wangyan27
LANG: PYTHON3
PROG: wormhole
"""

fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')

N = int( fin.readline())
holes = []
for _ in range(N):
    [x,y] = list( map(int, fin.readline().split() ))
    holes.append([x,y])
holes.sort(key = lambda _: _[0])

def All_Pairings(holes):
    if len(holes) == 2:
        return [ [ holes  ] ]

    all_pairings = []
    for i in range(1, len(holes)):
        rest = [_ for _ in holes if ( _ != holes[0] and _ != holes[i] ) ]
        pairings = All_Pairings( rest  )
        for pair in pairings:
            pair.append( [ holes[0], holes[i] ] )
            all_pairings.append( pair )

    return all_pairings

def Partner_Hole(hole, configuration):
    for pair in configuration:
        if hole == pair[0]:
            partner = pair[1]

        elif hole == pair[1]:
            partner = pair[0]

    return partner

def Find_Loop(hole, route, config):
    route.append(hole)
    partner = Partner_Hole(hole, config)
    
    for next_hole in holes:
        if next_hole[0] > partner[0] and next_hole[1] == partner[1]:
            if next_hole in route:
                return True
            else:
                return Find_Loop(next_hole, route, config)
    return False

all_pairings = All_Pairings(holes)

valid_config = 0
for configuration in all_pairings:
    for start_hole in holes:
        route = []
        if Find_Loop(hole = start_hole, route = route, config= configuration):
            valid_config += 1
            break

        
fout.write(str(valid_config)+ "\n")
fout.close()     