import json

def OpenCache(CACHE_FILENAME, index):
    ''' opens the cache file if it exists and loads the JSON into
    the FIB_CACHE dictionary.

    if the cache file doesn't exist, creates a new cache dictionary
    
    Parameters
    ----------
    None

    Returns
    -------
    The opened cache
    '''
    try:
        cache_file = open(CACHE_FILENAME, 'r')
        cache_contents = cache_file.read()
        cacheList = list(cache_contents.split('\n'))
        cache_dict = json.loads(cacheList[index])
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict
