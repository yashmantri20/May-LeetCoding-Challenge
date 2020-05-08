'''You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Example 1:

Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:

Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 
Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.'''



class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        length = len(coordinates)
        if length <= 2:
            count = True
        else:
            x1,y1 = coordinates[0]
            x2,y2 = coordinates[1]
            if x2-x1 == 0 or y2-y1 == 0:
                    slope = 0
            else:
                    slope = (y2-y1)/(x2-x1)

            for i in range(1,length-1):
                x1,y1 = coordinates[i]
                x2,y2 = coordinates[i+1]
                if x2-x1 == 0 or y2-y1 == 0:
                    s = 0
                else:
                    s = (y2-y1)/(x2-x1)

                if s == slope:
                    count = True
                else:
                    count = False
                    break
        return count