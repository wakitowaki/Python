matrix = [[1,2,2],
          [2,2,1],
          [1,2,2]]

count_winner = [0,0,0,0]

def Test(vect):
    for i in range(len(vect)):
        vect[i] = 8

def Check4(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            #temp[j]=matrix[i][j]
            if (matrix[i][j]==matrix[i][j+1]==matrix[i][j+2]):
                print "winner on column",j
            else:
                print "niente"

def Check5(matrix,ticks):
    count_a=0
    count_b=0
    count_c=0
    count_d=0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j]==1:
                count_a += 1
                if count_a == 3:
                    print "winner P1 row",i+1
            elif matrix[i][j]==2:
                count_b += 1
                if count_b == 3:
                    print "winner P2 row",i+1
            if matrix[j][i]==1:
                count_c += 1
                if count_c==3:
                    print "winner P1 column",i+1
            elif matrix[j][i]==2:
                count_d += 1
                if count_d==3:
                    print "winner P2 column",i+1
        count_a=0
        count_b=0
        count_c=0
        counr_d=0
        
    
        
            

def CheckWinner(matrix):
    try:
        for i in range(len(matrix)):
                  if (matrix[i][0]==matrix[i][1]==matrix[i][2]):
                      print "winner on line",i+1
                  elif (matrix[0][i]==matrix[1][i]==matrix[2][i]):
                      print "winner on column",i+1
                    

    except:
                  print "error"



#CheckWinner(matrix)
#Check4(matrix)                 
Check5(matrix,3)
vect = [1,2,3]
print vect
print type(vect)
Test(vect)
print vect
