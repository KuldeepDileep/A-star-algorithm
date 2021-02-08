# Jumping Frog problem and route planning with A* algorithm

## Jumping Frogs: 
The puzzle involves seven rocks and six frogs. See Fig. 1. The seven rocks are laid out in a horizontal line and numbered left to right. The six frogs are evenly divided into a green trio and a brown trio. The green frogs sit on Rocks 1, 2, and 3, facing right. The brown frogs sit on Rocks 5, 6, and 7, facing left. Rock 4 is vacant. The challenge is to transpose the trios, jumping the green frogs to Rocks 5, 6, and 7 and the brown frogs to Rocks 1, 2, and 3. Their movement is restricted. A frog can only jump forward, either hopping to a vacant rock one place ahead (cost =1) or leaping over its neighbor frog to a vacant rock two places ahead (cost = 2).

## Route Planning:
You are planning a trip to Northern areas of Pakistan. There are several cities that you want to visit in a limited time and hence looking for the best route for them. Your program will take the following CSV files as inputs:
* cities.csv - list of cities under consideration
* connection.csv - the road network mentioning the cities that are connected to each other with their respective distances
* heuristics.csv - aerial distance of every two cities

Given a starting and a destination city, you have to find the shortest path between these two cities using A* algorithm. Develop your search agent that takes a Search Problem and return its solution using A* algorithm. The same implementation should be used to solve both problems given in part (a).

