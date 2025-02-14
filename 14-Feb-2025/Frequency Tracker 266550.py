# Problem: Frequency Tracker - https://leetcode.com/problems/frequency-tracker/description/

class FrequencyTracker:
    from collections import defaultdict
    def __init__(self):
        self.number_to_frequency = defaultdict(int)
        self.frequency_to_number = defaultdict(set)


    def add(self, number: int) -> None:
        frequency = self.number_to_frequency[number]
        if number in self.frequency_to_number[frequency]:
            self.frequency_to_number[frequency].remove(number)
        self.frequency_to_number[frequency + 1].add(number)
        self.number_to_frequency[number] += 1

    def deleteOne(self, number: int) -> None:
       frequency = self.number_to_frequency[number]
       if frequency:
        self.frequency_to_number[frequency].remove(number)
        self.frequency_to_number[frequency - 1].add(number)
        self.number_to_frequency[number] -= 1

        
    def hasFrequency(self, frequency: int) -> bool:
       if len(self.frequency_to_number[frequency]) == 0:
        return False
       return True 

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)