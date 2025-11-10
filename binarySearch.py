
def search(nlist):

    search_term = int(input("Which number are you searching for?"))
    # Initializing found to be able to become True if data item is found
    found = False

    # First pointer at first position
    first = 0

    # Last pointer at last position
    last = len(nlist)-1

    # Checks if found is False and first isn't larger/equal to last
    # Either of these conditions being met means the search would be over
    while (found == False and first <= last):

        # Creates midpointer at mid value of list
        mid = (first+last)//2

        # Checks if the search term is the mid pointer
        if (search_term == nlist[mid]):

            # Ends the search because found is no longer False
            found = True

        # Checks if the search term is larger than the mid pointer
        if (search_term > nlist[mid]):

            # Makes the search continue searching the upper half of the list
            first = mid + 1

        # Checks if the search term is lower than the mid pointer
        elif (search_term < nlist[mid]):

            # Makes the search continue searching the lower half of the list
            last = mid - 1


    # Output statement on whether the item has been found or not
    if (found):
        print("The data item has been found.")
    else:
        print ("The data item has not been found.")
