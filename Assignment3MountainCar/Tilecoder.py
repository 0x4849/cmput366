#-------------------------------
# MountainCar Lab - Programming Assignment 3
# Author: Brad Harrison
# Date: November 28th 2014
#-------------------------------
numTilings = 4
tilesPerTiling = 9*9
gridLevel = 8

numTiles = numTilings*tilesPerTiling

def tilecode(position,velocity,array):
    position = position + 1.2 
    velocity = velocity + 0.07

    for i in range (0, numTilings):
        xoffset = i * (1.7/8) / numTilings
        yoffset = i * (0.14/8) / numTilings 
        
        tempPosition = int((position + xoffset)/(1.7/8))
        tempVelocity = int((velocity + yoffset)/(0.14/8))
    
        upDirection = 9 * tempVelocity
        rightDirection = 1 * tempPosition
        
        tileNumber = upDirection + rightDirection
        startTile = i * 81
        array[i] = startTile + tileNumber


def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)


'''
printTileCoderIndices(-1.2,-0.07)
printTileCoderIndices(0.5, 0.07)

printTileCoderIndices(0.3,5)
printTileCoderIndices(2.4,3.3)
printTileCoderIndices(4.2,1.1)
printTileCoderIndices(5.9, 0.7)
printTileCoderIndices(0.1,0.1)
 

printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)


	 
0.3,5 ;

tile indices for input (0.3,5 ) are : [8, 129, 250, 371, 503, 624, 746, 867]
tile indices for 2.4, 3.3 ; 49, 170, 291, 412, 534, 655, 776, 897
tile indices for 4.2, 1.1:
78, 199, 321, 442, 563, 684, 805, 926

tile indices for 5.9 and 0.7 :
100, 221, 353, 474, 595, 716, 837, 959

tile indices for 0.1 and 0.1;
0, 121, 242, 363, 484, 605, 726, 859
'''
