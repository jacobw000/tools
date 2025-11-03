def listCreate():
    # Sets the size of the list
    size = int(input("How big does your list need to be?"))

    
    intList = []
    cont = 0
    
    # Checks the list is not at capacity yet
    while cont < size:
        
        # Allows the user to input numbers to start making the list
        x = int(input("Enter number."))

        # Adds 1 to cont to make sure the user has a correctly sized list
        cont = cont + 1

        # Adds the inputted number to the list
        intList.append(x)

    return intList







