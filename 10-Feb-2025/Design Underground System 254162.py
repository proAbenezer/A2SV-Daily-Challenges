# Problem: Design Underground System - https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {} # Id -> stationName, time
        self.totalMap = {} # (start, end) -> total time, count
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInMap[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.checkInMap[id]

        route = (startStation, stationName)

        if route not in self.totalMap:
            self.totalMap[route] = [0, 0]

        self.totalMap[route][0] += t - startTime
        self.totalMap[route][1] += 1
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, count = self.totalMap[(startStation, endStation)]
        return totalTime / count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)