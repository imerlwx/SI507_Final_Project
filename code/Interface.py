from Restaurant import Restaurant
from yelpapi import YelpAPI
import webbrowser
from FindShortestPath import FindShortestPath
from ReadFile import GetSizeOfFile, ReadDestinationFile
from Graph import Graph

yelp_api = YelpAPI('A5eJ8VgQCSTyvS4T8klmR7N4xwZA6Vayb5AMRPbfsI2nRuJB1ZqRwQJWfmraTOev7tLgApMtrF-uMr5P90MRvlTL2fxG1Ocsg_7MywgJUgX3BZV8TXz44W3xSb5UYnYx')

def RestaurantOutput(restaurant_list):
    '''output the info
    
    Given the restaurant objects list output the info of each object

    Parameters:
    ---------- 
    restaurant_list: object lists

    Returns
    -------
    print each object's info()
    
    '''

    for i in range(len(restaurant_list)):
        
        # print each result with a number, starting at 1 and going up at the beginning of the line.
        print(f"{i + 1}: ", restaurant_list[i].info(), "\n") 

def RestaurantInterface(userInput="exit", location='ann arbor, mi'):
    '''interactive search interface
    
    Given the user's choice, fetch data from the local restaurant or exit.

    Parameters:
    ---------- 
    userInput: string
        the choice of user, could be a term, or the index that user is interested in or exit

    Returns
    -------
    print interactive search interface
    
    '''
    
    if userInput != "exit":

        response = yelp_api.search_query(term=userInput, location=location, sort_by='distance', limit=10)
        json_data = response['businesses']
        
        restaurant_list = []

        # store each kind of media objects respectively 
        for i in range(len(json_data)):
            restaurant_list.append(Restaurant(dict=json_data[i]))
        
        RestaurantOutput(restaurant_list)

        print("Enter a number for more info, or another search term, or exit: ")
        userInput = input()
        # If user enters a number within the range of number of results returned, program can launch preview using webbrowser module.
        while (userInput.isdigit() and int(userInput) <= len(restaurant_list)):
            webbrowser.open(restaurant_list[int(userInput) - 1].url)

            print("\n", "Launching", "\n", f"{restaurant_list[int(userInput) - 1].url}", "\n", "in web browser", "\n")
            
            print("Enter a number for more info, or another search term, or exit: ")
            userInput = input()
        
        # If user enters something else except "exit", it should be treated as a search term, 
        # and another query would be run and results based on the search term would be displayed.
        if (userInput != "exit"):
            RestaurantInterface(userInput)
        else:
            print("Thanks for using the restaurant recommendation system! ")

    # User is able to quit the program at any time by entering “exit”.       
    else:
        print("Thanks for using the restaurant recommendation system! ")

def DestinationInput(destinationList, totalDestinationFile):
    '''interactive destination input interface
    
    Given the user's choices, conclude them into a destination list

    Parameters:
    ---------- 
    destinationList: list
        the user's choice of where to visit

    totalDestinationFile: filename
        all the destinations user could choose from

    Returns
    -------
    destinationList: list
        the user's choice of where to visit
    
    '''
    
    userInput = input('Enter a destination to travel, or "end" to end: ')

    if userInput != 'end':
        
        # if the user input is in the options, set it into the destination list
        if (int(userInput) - 1) in range(GetSizeOfFile(totalDestinationFile)):   
            if int(userInput) in destinationList: # if already in the list, prompt for input again
                print('This place has been chosen, please enter again ')
                DestinationInput(destinationList, totalDestinationFile)
            else:
                destinationList.append(int(userInput))
                DestinationInput(destinationList, totalDestinationFile)
        else: 
            print('Invalid number, please enter again ')
            DestinationInput(destinationList, totalDestinationFile)

    else:
        print('Here is your destination list: ', destinationList)
        return destinationList

def TourGuideInterface():
    '''interactive tour guide interface
    
    based on the user's choice, output the shortest path and length

    Parameters:
    ---------- 
    None

    Returns
    -------
    print the shortest path and the path length
    
    '''
    
    ReadDestinationFile('totalDestinations.txt')
    print('\n')
    destinationList = []
    DestinationInput(destinationList, 'totalDestinations.txt')

    if destinationList == []:
        print('Sorry for that. Please come later for more interesting spots!')
        return
    elif len(destinationList) == 1:
        print("Too few destinations! ")
        return

    graph = Graph(destinationList, 'totalDistanceCache.json', 'totalLocations.txt')

    startLoc = input('Please enter your start location: ')
    
    minPath, shortestLength = FindShortestPath(graph, int(startLoc))

    print('The shortest path is', destinationList[minPath[0]], end = ' ')
    for i in range(1, len(minPath)):
        print('--->', destinationList[minPath[i]], end = ' ')
    print('. The length of this path is', shortestLength / 1000, 'km')
    print('Thanks for using the tour guide system! ')

def userInterface(): 
    '''total interface
    
    User could choose the function that want to perform

    Parameters:
    ---------- 
    None

    Returns
    -------
    Output based on the choice
    
    '''
    
    print('Welcome to our tour guide system!')
    print('Please choose the function you want: ', '\n', '1. Campus Tour Guide', '\n', '2. Restaurant Recommendation', '\n', '3. Exit')
    userInput = input()
    
    if userInput == '1':
        TourGuideInterface()
        userInterface()
    elif userInput == '2':
        print('Enter a food category to search, or "exit" to quit: ')
        category = input()
        RestaurantInterface(category)
        userInterface()
    elif userInput == '3':
        print('\n', 'Bye!', '\n')
        return
    else:
        print('Please input between 1, 2, 3')

if __name__ == "__main__":
    
    userInterface()
    pass