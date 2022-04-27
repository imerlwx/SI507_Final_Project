def FindIndex(locationA_index, locationB_index, totalDestinationNum):
    '''
    This function is to find the index of the two locations in the cache

    Parameters:
    ---------- 
    locationA_index, locationB_index: int
        the location's index in the destination list
    
    totalDestinationNum: int
        number of total destinations

    Returns
    -------
    index: int
        the index of this two locations in the cache
    
    '''

    if locationA_index > locationB_index:
        temp = locationA_index
        locationA_index = locationB_index
        locationB_index = temp
    
    if locationB_index > totalDestinationNum - 1:
        return
    elif locationB_index == locationA_index:
        return

    index = 0
    for i in range(locationA_index):
        index += (totalDestinationNum - i - 1)
    
    index = index + locationB_index - locationA_index - 1
    
    return index