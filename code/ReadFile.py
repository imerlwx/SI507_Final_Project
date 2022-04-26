# some functions about read files

def ReadFileAll(filename):
    '''
    This function will read all the contents in the file and output it

    Parameters:
    ---------- 
    filename: string
        the file's name

    Returns
    -------
    print all the destinations line by line
    
    '''
    # Using readlines()
    file = open(filename, 'r')
    Lines = file.readlines()

    for line in Lines:
        print(line)
    
    file.close()

def ReadLocationFile(locationFile):
    '''
    This function will read the location file and return a location list

    Parameters:
    ---------- 
    locationFile: string
        the file that contains all the locations

    Returns
    -------
    locationList: list
        a list that contain all the locations

    '''
    # Using readlines()
    file = open(locationFile, 'r')
    file_contents = file.read()
    locationList = list(file_contents.split('\n'))
    file.close()

    return locationList

def GetSizeOfFile(FILENAME):
    '''
    This function will read the location file and return a location list

    Parameters:
    ---------- 
    FILENAME: string
        any .txt file

    Returns
    -------
    lengthOfFile: int
        the number of lines in the file
    
    '''
    with open(FILENAME, 'r') as fp:
        lengthOfFile = len(fp.readlines())

    return lengthOfFile

def ReadFileLineByLine(filename, index):
    '''
    This function will read a file line by line

    Parameters:
    ---------- 
    filename: string
        the file's name

    Returns
    -------
    print the file contents line by line
    
    '''
    file = open(filename, 'r')
    Lines = file.readlines()

    print(Lines[index])

    file.close()