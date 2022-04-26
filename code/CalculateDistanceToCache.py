import requests
import json
from ReadFile import ReadLocationFile


def CalculateDistanceToCache(locationFileName, cacheFileName):
    ''' Get the information from two locations in the location file to the cache

    Parameters
    ----------
    locationFileName: string
        the file that contains all the specfic locations of the destinations, should be .txt file
    
    cacheFileName: string
        the cache file that write to, should be .json file

    Returns
    -------
    None
    '''

    locationList = ReadLocationFile(locationFileName)
    apikey = 'OAfDV93FwvvWxqNAzhP2nmemBPnNh'
    basicUrl = 'https://api.distancematrix.ai/maps/api/distancematrix/json?origins='
    fw = open(cacheFileName,"w")

    for i in range(len(locationList)):
        for j in range(i + 1, len(locationList)):
            urlToSearch = basicUrl + str(locationList[i]) + '&destinations=' + str(locationList[j]) + '&key=' + apikey
            response = requests.get(urlToSearch)  # get json object from web api
            json_data = json.loads(response.text)
            dumped_json_cache = json.dumps(json_data)
            fw.write(dumped_json_cache)
            fw.write('\n')

    fw.close()
