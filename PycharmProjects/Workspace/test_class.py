


matrix = [[1,0,1],
          [2,0,2],
          [1,2,2]]

class Board:
    def __init__(self):
        self.dimension=int(raw_input("Dimension of the board: "))
        self.matrix=self.CompMatrix(self.dimension)

    def __str__(self):
         a = '\n'.join(['| ' + str(row).strip('[]').replace(',',' | ')+' |' for row in self.matrix])
         return a

    def StampaTest(self,matrix):
        a =str([n for row in matrix for n in row]).replace(',',' |').strip('[]')
        return a

    def StampaTest2(self,matrix):
        return '\n'.join(['| ' + str(row).strip('[]').replace(',',' | ')+' |' for row in matrix])

    def CompMatrix(self,dimension):
        matrix = [[int(raw_input("insert element " + str(n))) for n in range(self.dimension)] for i in range(self.dimension)]
        return matrix




if __name__ == '__main__':
    #P=Board(matrix)
    P=Board()
    print P
    print type(P)
    #print '\n'
    #print '| ' + P.StampaTest(matrix) + ' |'
    #print P.StampaTest2(matrix)
    #print type(P.StampaTest2(matrix))


    
