#-------------------------------
# Tile Coding Lab - Programming Assignment 2
# Author: Brad Harrison
# Date: November 18th 2014
#-------------------------------
numTilings = 8

def tilecode(in1, in2, array):
  for i in range(0, numTilings):
	  calculatedOffset = i *(0.6/numTilings)
	  tempIn1 = int((in1+calculatedOffset)/0.6)
	  tempIn2 = int((in2+calculatedOffset)/0.6)

	  upDirection = 11*tempIn2
	  rightDirection = 1*tempIn1
	  tileNumber = upDirection+rightDirection
	  startTile = i *121
	  array[i] = startTile+tileNumber



def printTileCoderIndices(in1,in2):
    tileIndices = [-1]*numTilings
    tilecode(in1,in2,tileIndices)
    print('Tile indices for input (',in1,',',in2,') are : ', tileIndices)

'''
printTileCoderIndices(0.3,5)
printTileCoderIndices(2.4,3.3)
printTileCoderIndices(4.2,1.1)
printTileCoderIndices(5.9, 0.7)
printTileCoderIndices(0.1,0.1)
 
'''
printTileCoderIndices(0.1,0.1)
printTileCoderIndices(4.0,2.0)
printTileCoderIndices(5.99,5.99)
printTileCoderIndices(4.0,2.1)
'''
	 
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
