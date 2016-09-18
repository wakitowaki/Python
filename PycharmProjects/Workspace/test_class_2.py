

class Board:
    def __init__(self):
        self.dimension=int(raw_input("Dimension of the board: "))
        self.matrix=self.CompMatrix(self.dimension)

    def __str__(self):
         a = '\n'.join(['| ' + str(row).strip('[]').replace(',',' | ')+' |' for row in self.matrix])
         return a

    def CompMatrix(self,dimension):
        matrix = [[int(raw_input("insert element " + str(n) + ' ' + str(i))) for n in range(self.dimension)] for i in range(self.dimension)]
        return matrix




if __name__ == '__main__':
    P=Board()
    print P
    #print type(P)



    
