# Problem: Walking Robot Simulation - https://leetcode.com/problems/walking-robot-simulation/description/?envType=problem-list-v2&envId=array

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        directions =[[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0
        res = 0 
        obstacles = {tuple(o) for o in obstacles}
        for command in commands:
            if command == -1:
                d  = (d + 1) % 4
            elif command == -2:
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]
                for step in range(command):
                    if(x + dx, y + dy) in obstacles:
                        break
                    x, y = (x + dx), (y + dy)
            res = max(res, x**2 + y**2)
        return res
        