import json

def OpenCache(cacheFileName, index):
    ''' opens the cache file if it exists and loads the JSON into
    the FIB_CACHE dictionary.

    if the cache file doesn't exist, creates a new cache dictionary
    
    Parameters
    ----------
    cacheFileName: string
        the file name of the cache
    
    index: int
        the index of line in the cache file

    Returns
    -------
    The cache line of index
    '''
    try:
        cache_file = open(cacheFileName, 'r')
        cache_contents = cache_file.read()
        cacheList = list(cache_contents.split('\n'))
        cache_dict = json.loads(cacheList[index])
        cache_file.close()
    except:
        cache_dict = {}
    return cache_dict
