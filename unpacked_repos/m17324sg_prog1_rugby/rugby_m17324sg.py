import sys
with open(sys.argv[1], 'r') as f:
    contents = f.read()


team1 = 'T1'
team2 = 'T2'


a = contents[0] + contents[1]
b = contents[3] + contents[4]
c = contents[6] + contents[7]
d = contents[9] + contents[10]
e = contents[12] + contents[13]

team_list = [a, b, c, d, e]





score_type = [contents[2], contents[5], contents[8], contents[11], contents[14]]



def scoreCalc():
      team1_score = 0
      team2_score = 0
      team1_temp = 0
      team2_temp = 0

      if a == 'T1':
            if score_type[0] == 't':
                  team1_score = 5
                  team1_temp += team1_score
            elif score_type[0] == 'p':
                  team1_score = 3
                  team1_temp += team1_score
            elif score_type[0] == 'd':
                  team1_score =3
                  team1_temp += team1_score
            elif score_type[0] == 'c':
                  team1_score = 2
                  team1_temp += team1_score
      if a == 'T2':
            if score_type[0] == 't':
                  team2_score = 5
                  team2_temp += team2_score
            elif score_type[0] == 'p':
                  team2_score = 3
                  team2_temp += team2_score
            elif score_type[0] == 'd':
                  team2_score =3
                  team2_temp += team2_score
            elif score_type[0] == 'c':
                  team2_score = 2
                  team2_temp += team2_score
      if b == 'T1':
            if score_type[1] == 't':
                  team1_score = 5
                  team1_temp += team1_score
            elif score_type[1] == 'p':
                  team1_score = 3
                  team1_temp += team1_score
            elif score_type[1] == 'd':
                  team1_score =3
                  team1_temp += team1_score
            elif score_type[1] == 'c':
                  team1_score = 2
                  team1_temp += team1_score
      if b == 'T2':
            if score_type[1] == 't':
                  team2_score = 5
                  team2_temp += team2_score
            elif score_type[1] == 'p':
                  team2_score = 3
                  team2_temp += team2_score
            elif score_type[1] == 'd':
                  team2_score =3
                  team2_temp += team2_score
            elif score_type[1] == 'c':
                  team2_score = 2
                  team2_temp += team2_score
      if c == 'T1':
            if score_type[2] == 't':
                  team1_score = 5
                  team1_temp += team1_score
            elif score_type[2] == 'p':
                  team1_score = 3
                  team1_temp += team1_score
            elif score_type[2] == 'd':
                  team1_score =3
                  team1_temp += team1_score
            elif score_type[2] == 'c':
                  team1_score = 2
                  team1_temp += team1_score
      if c == 'T2':
            if score_type[2] == 't':
                  team2_score = 5
                  team2_temp += team2_score
            elif score_type[2] == 'p':
                  team2_score = 3
                  team2_temp += team2_score
            elif score_type[2] == 'd':
                  team2_score =3
                  team2_temp += team2_score
            elif score_type[2] == 'c':
                  team2_score = 2
                  team2_temp += team2_score
      if d == 'T1':
            if score_type[3] == 't':
                  team1_score += 5
                  team1_temp += team1_score
            elif score_type[3] == 'p':
                  team1_score = 3
                  team1_temp += team1_score
            elif score_type[3] == 'd':
                  team1_score =3
                  team1_temp += team1_score
            elif score_type[3] == 'c':
                  team1_score = 2
                  team1_temp += team1_score
      if d == 'T2':
            if score_type[3] == 't':
                  team2_score = 5
                  team2_temp += team2_score
            elif score_type[3] == 'p':
                  team2_score = 3
                  team2_temp += team2_score
            elif score_type[3] == 'd':
                  team2_score =3
                  team2_temp += team2_score
            elif score_type[3] == 'c':
                  team2_score = 2
                  team2_temp += team2_score
      if e == 'T1':
            if score_type[4] == 't':
                  team1_score = 5
                  team1_temp += team1_score
            elif score_type[4] == 'p':
                  team1_score = 3
                  team1_temp += team1_score
            elif score_type[4] == 'd':
                  team1_score =3
                  team1_temp += team1_score
            elif score_type[4] == 'c':
                  team1_score = 2
                  team1_temp += team1_score
      if e == 'T2':
            if score_type[4] == 't':
                  team2_score = 5
                  team2_temp += team2_score
            elif score_type[4] == 'p':
                  team2_score = 3
                  team2_temp += team2_score
            elif score_type[4] == 'd':
                  team2_score =3
                  team2_temp += team2_score
            elif score_type[4] == 'c':
                  team2_score = 2
                  team2_temp += team2_score
      team1 = team1_temp
      team2 = team2_temp
      with open(sys.argv[2], 'w') as o:
            o.write(str(team1) + ':' + str(team2))


scoreCalc()





