# Problem: Gas Station - https://leetcode.com/problems/gas-station/

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Initialize the length of the gas and cost lists
        num_stations = len(gas)
      
        # Initialize pointers for traversing the gas stations
        start_index = end_index = num_stations - 1
      
        # Initialize counter for stations visited and total balance of gas
        stations_visited = total_gas_balance = 0
      
        # Loop until all stations have been visited
        while stations_visited < num_stations:
            # Update the total balance by adding current gas and subtracting current cost
            total_gas_balance += gas[end_index] - cost[end_index]
          
            # Increment the number of stations visited
            stations_visited += 1
          
            # Move to the next station, wrapping around if necessary
            end_index = (end_index + 1) % num_stations
          
            # While the total balance is negative and we haven't visited all stations
            # move the start index backwards and adjust the balance.
            while total_gas_balance < 0 and stations_visited < num_stations:
                # Move the start index to the previous station
                start_index = (start_index - 1 + num_stations) % num_stations
              
                # Update the total balance by adding gas and subtracting cost at the new start
                total_gas_balance += gas[start_index] - cost[start_index]
              
                # Increment the number of stations visited
                stations_visited += 1
      
        # If the total balance is negative, return -1 indicating the circuit cannot be completed,
        # otherwise return the start index
        return -1 if total_gas_balance < 0 else start_index
        