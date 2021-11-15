###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # initialize result list

    # weight ordered cows:
    woc = {k: v for k, v in sorted(cows.items(), key=lambda item: item[1], reverse = True)}

    # create a list of cows
    cow_list = []
    for cow in woc:
        cow_list.append(cow)

    # initialize result
    result = []

    # iterate through all the cows
    while (len(cow_list) > 0):

        tw = 0
        trip = []
        update_cow_list = []

        for cow in cow_list:

            if(tw + woc[cow] <= limit):

                tw += woc[cow]
                trip.append(cow)
            else:
                update_cow_list.append(cow)
                
        cow_list = update_cow_list
        result.append(trip)

    return result


# Problem 2
def brute_force_cow_transport(cows, limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    # start the number of trips as the number of cows. That is, one cow per trip.
    ltrip = len(cows)

    # iterate thourgh partitions
    for partition in get_partitions(cows):

        # define partition weight
        tp = 0

        # iterate thourgh trips
        for trip in partition:
            
            # check trip weighted
            tw = 0
            for cow in trip:
                tw += cows[cow]

            tp = max(tp, tw)

        # check if conditions are met
        if(tp <= limit and len(partition) <= ltrip):

            # update the number of trips
            ltrip = len(partition)

            # update result
            result = partition
    
    return result




        
# Problem 3
def compare_cow_transport_algorithms(cows, limit = 100):
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greedy_cow_transport(cows, limit)
    end = time.time()
    greedy_time = end - start
    print("Greedy Algorithm Time: " + str(greedy_time) + " seconds")

    start = time.time()
    brute_force_cow_transport(cows, limit)
    end = time.time()
    brute_time = end - start
    print("Brute Force Algorithm Time: " + str(brute_time) + " seconds")


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

cows = load_cows("ps1_cow_data.txt")
limit=100
compare_cow_transport_algorithms(cows, limit)


