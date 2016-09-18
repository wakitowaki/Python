
import numpy
import matplotlib.pylab as mp

def DrawBoard(size,matrix):
    mp.figure()
    tb=mp.table(cellText=matrix, loc=(0,0), cellLoc='center')
    
        
        
def BuildMatrix(size):
    a = numpy.zeros((size,size))
    return a


if __name__ == "__main__":
    size=input("Grandezza della board (numero intero)")
    matrix = BuildMatrix(size)
    #print matrix
    DrawBoard(size,matrix)
