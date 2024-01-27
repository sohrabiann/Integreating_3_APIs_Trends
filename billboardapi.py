import billboard


def billboardAPI():
    chart = billboard.ChartData('hot-100')

    list = []
    x = chart.__len__()
    #Set current value to 0, to begin parsing the individual entries on Billboard
    current = 0
    #Empty list to store all billboard values
    new_data = []
    #For the range of 100 (Or as determined by the user), append the data from the billboard charts to a list format (Artist/Song Name for simplicity) 
    for current in range(x):
        raw_data = [(chart[current].artist + ' AND ' + chart[current].title)]
        for data in raw_data:
            new_data.append(str(data))
        current = current + 1
    return(new_data)

#to run overall function
#billboardAPI()
