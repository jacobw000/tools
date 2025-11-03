def linSearch(intList):
    # Variable created to be checked if number is in list later on
    found = False
    pos = 0
    # Asks for the number to search for
    search = int(input("Enter the number you are searching for."))

    # Loop through each item in the list
    for x in range(len(intList)):

        # Keeps track of how many items have been searched
        pos = pos + 1

        # Checks if the item is the number that is being searched for
        if (search == intList[x]):
            found = True
            break


        
    # Check if the number is in the list or not and give an output
    if (found == True):
        print ("Found number at position:", pos)

    else:
        print ("Not found number.")
        
