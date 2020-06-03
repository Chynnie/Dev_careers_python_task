import numpy as np

# Data for each continent
n_america = {
    'countries': ['USA', 'Canada', 'mexico'],
    'total_cases': [1746311, 87519, 78023],
    'active cases': [1153939, 34590, 15043],
    'discharged': [490256, 46164, 54383],
    'death': [102116, 6765, 8597]
}

europe = {
    'countries': ['Russia', 'Spain', 'Italy'],
    'total_cases': [379051, 283849, 231139],
    'active cases': [223916, 59773, 50996],
    'discharged': [150993, 196958, 147101],
    'death': [4142, 27118, 33072]
}

s_america = {
            'countries': ['Brazil', 'Peru', 'Chile'],
            'total_cases': [414661, 134905, 82289],
            'active cases': [222317, 75753, 47908],
            'discharged': [166647, 56169, 33540],
            'death': [25697, 3983, 841]
}

asia = {
            'countries': ['China', 'India', 'Japan'],
            'total_cases': [82995, 159054, 16651],
            'active cases': [73, 86584, 1829],
            'discharged': [78288, 67929, 13973],
            'death': [4634, 4541, 858]
}

africa = {
            'countries': ['Nigeria', 'Egypt', 'Ghana'],
            'total_cases': [8733, 19666, 7303],
            'active cases': [5978, 13645, 4857],
            'discharged': [2501, 5205, 2412],
            'death': [254, 816, 34]
}

# A function to print the details of each continent
def details(continents,continent_number):
    print('\n')
    while True:
        choice = input("Do you want to see Further details? (y/n): ")
        try:
            if choice=='y':
                data_for_selected_case = []
                for i in continents[continent_number]:
                    data_for_selected_case.append(continents[continent_number][i])

                name = ['Country','Total Cases','Active cases','Discharged Cases','Death']

                # Looping through the Data for selected case and naming
                y = 0
                while y < 3:
                    z = 0
                    for i in data_for_selected_case :
                        print(str(name[z]) + "----" + str(i[y]))
                        z = z + 1
                    y = y + 1
                    print("\n")
                break
            elif choice=='n':
                end_restart()
            else:
                print("Error--Wrong input, choose (y/n)")

        except ValueError:
            print("Error--Enter a Single digit number")
    end_restart()


# A function to restart or end the program
def end_restart():
    try:
        choice=int(input("Enter (1) to restart or (2) to End the Program: "))
        if choice==1:
            program()
        elif choice ==2:
            exit()
        else:
            print("Wrong Input")
            end_restart()
    except ValueError:
        print("Error--Entered the wrong Value")
        end_restart()



# The main program
def program():
    continents = [africa, asia, europe, n_america, s_america]
    continent_string = ['Africa', 'Asia', 'Europe', 'North America', 'South America']

    print("Here are the continents:")
    print(" 1) Africa \n 2) Asia \n 3) Europe \n 4) North America \n 5) South_america")
    print('\n')

    while True:
        try:
            # Collect number from the user
            continent_number = int(
                input("Enter the Number for the Continent Above you will like to check or Enter 0 to exit: "))

            # condition to exit the program
            if continent_number == 0:
                exit()

            # Updates the continent index because ir starts from 0
            continent_number = continent_number - 1

            # Prints out the continent details
            print('\n')
            print(f"----Here is the statistics for {continent_string[continent_number]}----")
            print("Sum : " + str(np.sum(continents[continent_number]['total_cases'])))
            print("Minimum : " + str(np.min(continents[continent_number]['total_cases'])))
            print("Max : " + str(np.max(continents[continent_number]['total_cases'])))
            print("Mean : " + str(np.mean(continents[continent_number]['total_cases'])))


            # Redirect to get further details
            details(continents,continent_number)
            break
        except IndexError:
            print("Error--Enter a number from 1 to 5")
        except ValueError:
            print("Error--Enter a Single digit number")

# Run the program function
program()