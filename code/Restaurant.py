'''
This file will define a restaurant object which will contain a restaurant's attributes

'''

class Restaurant:
    '''
    
    This function is to find the shortest path given the Graph object and start location

    Parameters:
    ---------- 
    dict: dict
        a dictionary that contains all the information about a restaurant

    Returns
    -------
    name, categories, phoneNumber, location, rating, url: string
        the information about the restaurant

    info: function
        will print the information about this restaurant
    
    '''

    def __init__(self, dict):
        self.name = dict['name']
        self.categories = dict['categories'][0]['title']
        self.phoneNumber = dict['display_phone']
        self.location = dict['location']['display_address']
        self.rating = dict['rating']
        self.url = dict['url']

    def info(self):
        return str(self.name) + " about " + str(self.categories) + " (" + str(self.rating) + ")"