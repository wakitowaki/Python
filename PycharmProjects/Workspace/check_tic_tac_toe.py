matrix = [[1,2,2,2],
          [1,1,2,2],
          [2,2,1,1],
          [2,1,2,2]]

count_winner = [0,0,0,0,0,0,0,0]

def CleanList(vect):
    for i in range(len(vect)):
        vect[i] = 0

def CheckDiagonalWin(matrix, count_winner,ticks):
    for i in range(len(matrix)):
        #print matrix[i][i], " ", matrix[i][len(matrix) -1 -i] FOR DEBUG
        if matrix[i][i]==1:
            count_winner[4] +=1
            if count_winner[4] == ticks:
                print "winner P1 diagonal 1"
        elif matrix[i][i]==2:
            count_winner[5] +=1
            if count_winner[5] == ticks:
                print "winner P2 diagonal 1"
        if matrix[i][len(matrix) -1 -i]==1:
            count_winner[6] += 1
            if count_winner[6] == ticks:
                print "winner P1 diagonal 2"
        elif matrix[i][len(matrix) -1 -i] == 2:
            count_winner[7] += 1
            if count_winner[7] == ticks:
                print "winner P2 diagonal 2"
    CleanList(count_winner)

def Check5(matrix,ticks,count_winner):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==1:
                count_winner[0] += 1
                if count_winner[0] == ticks:
                    print "winner P1 row",i+1
            elif matrix[i][j]==2:
                count_winner[1] += 1
                if count_winner[1] == ticks:
                    print "winner P2 row",i+1
            if matrix[j][i]==1:
                count_winner[2] += 1
                if count_winner[2]==ticks:
                    print "winner P1 column",i+1
            elif matrix[j][i]==2:
                count_winner[3] += 1
                if count_winner[3]==ticks:
                    print "winner P2 column",i+1
        CleanList(count_winner)
    CheckDiagonalWin(matrix,count_winner,ticks)
        

               
Check5(matrix,4,count_winner)


