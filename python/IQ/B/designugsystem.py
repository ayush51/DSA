class UndergroundSystem:

    def __init__(self):
        self.times = {}
        self.checkedin = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedin[id]=(stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startstation, starttime = self.checkedin[id]
        del self.checkedin[id]
        totaltime = t - starttime
        if (startstation, stationName) not in self.times:
            self.times[(startstation, stationName)]=[totaltime,1]
        else:
            self.times[(startstation,stationName)][0] += totaltime
            self.times[(startstation,stationName)][1] += 1
            
    def getAverageTime(self, startstation: str, endstation: str) -> float:
        sumoftime, numoftrips = self.times[startstation,endstation]
        avg = float(sumoftime)/float(numoftrips)
        return avg

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
