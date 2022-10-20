# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def findShips(topRight, bottomLeft):
            if topRight.x < bottomLeft.x or topRight.y < bottomLeft.y:
                return 0
            
            elif topRight.x == bottomLeft.x and topRight.y == bottomLeft.y:
                return int(sea.hasShips(topRight, bottomLeft))
            
            if not sea.hasShips(topRight, bottomLeft):
                return 0
            
            
            
            midX = (topRight.x + bottomLeft.x)//2
            midY = (topRight.y + bottomLeft.y)//2
            mid = Point(midX, midY)
            
            topLeftQ = findShips(Point(mid.x, topRight.y), Point(bottomLeft.x,mid.y+1))
            topRightQ = findShips(topRight, Point(mid.x+1,mid.y+1))
            bottomRightQ = findShips(Point(topRight.x,mid.y), Point(mid.x + 1, bottomLeft.y))
            bottomLeftQ = findShips(Point(mid.x, mid.y), bottomLeft)
        
            return topLeftQ + bottomRightQ + topRightQ + bottomLeftQ
        return findShips(topRight, bottomLeft)
            
        
        
        class Solution:
    def countShips(self, sea: 'Sea', tR: 'Point', bL: 'Point') -> int:
        def findShips(tR, bL):
            if tR.x < bL.x or tR.y < bL.y:
                return 0
            elif  tR.x == bL.x or tR.y == bL.y:
                return int(sea.hasShips(tR,bL))
            
            if not sea.hasShips(tR, bL):
                return 0
            
            midX = (tR.x + bL.x)//2
            midY = (tR.y + bL.y)//2
            mid = Point(midX, midY)
            
            topLeftQ = findShips(Point(mid.x, tR.y), Point(bL.x, mid.y+1))
            topRightQ = findShips(tR, Point(mid.x+1, mid.y+1))
            bottomLeftQ = findShips(Point(mid.x,mid.y), bL)
            bottomRightQ = findShips(Point(tR.x,mid.y), Point(mid.x+1, bL.y))
            
            return topLeftQ + topRightQ + bottomLeftQ + bottomRightQ
        return findShips(tR, bL)
            
    
        
    
        
