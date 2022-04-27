# SI507 Final Project

## What is this repo about?
Including all the data source cache (1 .json file), texts (2 .txt files) and source codes (9 .py files) of SI 507 final project, which will build a visitor system for University of Michigan. Users could use this system to have optimal path planning of the spots they choose, or to browse the restaurant recommendation in Ann Arbor based on their choice of food category.

No need of API keys for the tour guide system because most of the data have been stored in cache. It will be necessary to apply a Yelp Fusion API for the restaurant recommendation system. If you do not apply a new key, the system will use the default one. Python packages this program uses are requests, json, itertools, sys, collections, and webbrowser. Most are built-in packages.

## What is the data structure of this program?
The data structure is a graph. Each node of the graph represents a destination that user want to visit. Each edge represents the distance of the two locations. The graph will be depicted using the Graph class, which defines some attributes and methods. The attributes include edge list, edge dictionary and edge matrix, and the methods are used to get these three attributes. 

This structure will be stored in the cache file graph.json. To read this file, the ReadFile.py includes some method. One is to read all the file contents, one for reading the corresponding locations, one for getting the size of files, the last one for reading contents line by line. Use the first function is enough.

## How to run the program?
To run the program, just execute the Interface.py. There will be three choice for user: tour guide system, local restaurant recommendation system, or exit.

In the tour guide system, user will choose the destinations from the University of Michigan’s buildings with brief introduction. There are totally 25 destinations but to get results instantaneously it is better to only choose 10 or less destinations. After user choose the point to start, the shortest path and distance will be output. User will have an option to choose whether showing the graph structure or exit this system.

In the local restaurant recommendation system, user could input the sorting requirement, number of results to show, and the food category to search. The results will show the restaurants list. User could choose to see the webpages about each restaurant in the browser or just input other food category to start a new search or exit this system.
