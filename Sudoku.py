
# function to output name of variable and what the variable is
def pri(var_name, str_var_name):
    
    print(f"\n\n   {str_var_name} ...")
    print(var_name)


# the initial numbers that we start with
puzzleIn=[
    [[],[],[],  [1],[],[],  [],[],[]],
    [[],[],[2],  [],[9],[6],  [],[],[]],
    [[],[8],[5],  [],[],[3],  [],[],[]],

    [[],[],[],  [],[],[],  [7],[3],[]],
    [[5],[7],[1],  [3],[],[],  [],[4],[]],
    [[],[6],[3],  [],[8],[],  [],[],[1]],

    [[1],[],[],  [9],[3],[],  [4],[6],[]],
    [[2],[],[],  [8],[5],[],  [1],[],[]],
    [[],[9],[8],  [],[1],[],  [],[],[]]
    ]

# main will be populated with numbers that are not the solution (like the inverse of PuzzleIn)
main=[
    [[],[],[],  [],[],[],  [],[],[]],
    [[],[],[],  [],[],[],  [],[],[]],
    [[],[],[],  [],[],[],  [],[],[]],

    [[],[],[],  [],[],[],  [],[],[]],
    [[],[],[],  [],[],[],  [],[],[]],
    [[],[],[],  [],[],[],  [],[],[]],

    [[],[],[],  [],[],[],  [],[],[]],
    [[],[],[],  [],[],[],  [],[],[]],
    [[],[],[],  [],[],[],  [],[],[]]
    ]


# outputting each row of main
##print("\n\n Outputting each row of main ...\n")
##for row in main:
##    print(row)
##    print()


# make main be the inverse of PuzzleIn
for row in range(9):
    for column in range(9):
        if len((puzzleIn[row])[column]) == 1:
            for number in range(1, 10):
                if number not in (puzzleIn[row])[column]:
                    (main[row])[column].append(number)


# outputting each row of main
##print("\n\n Outputting each row of main ...\n")
##for row in main:
##    print(row)
##    print()


# this function goes through the 81 elements in main and checks if the length of each of the 81 places is 8 (that is, number exists)
    # and outputs the missing number (that is, the solution for that space)
def not_to_actual():
    print('\n\nnot_to_actual:\n')

    # initialise variable which holds how many numbers we have solved
    length=0
    
    for row in range(9):
        # initiliase an array which will stay one dimensional and is used per row
        record=[]
        for column in range(9):
            
            if len((main[row])[column]) == 8: # if this is true that means we have found a solution for this space
                for number in range(1, 10):
                    if number not in (main[row])[column]:
                        record.append(number)
                        
            else:
                record.append(0) # record will have a 0 if the solution for one of the 81 spaces has not been found yet
            
        print(record)

        # how many numbers have we solved?
        for i in record:
            if i!=0:
                length+=1

    print('\nHow many of the 81 spaces have we found a number for:', length)


# this function accepts an argument called place
    # it outputs 0, 3 or 6 depending on where in this segmentation 'place' is
def get_coords(place):
    if place>=0 and place<=2:
        use=0
    elif place>=3 and place<=5:
        use=3
    elif place>=6 and place<=8:
        use=6
    else:
        print('   Error - place is out of range')

    return use


# Calling not_to_actual function
##not_to_actual()


###Printing main and the length of it
##print('\n\nmain:\n')
##for i in main:
##    print(i,'\n')
##
##count=0
##for i in main:
##    for j in i:
##        count+=len(j)
##
##print('\nLength of main:',count)


complete1=0
complete2=1
# main code
while complete1 != complete2: # if the number of solutions doesn't increase then the code stops
    complete1=complete2

    print('\n*******************************************************************************\n')

    # look through all 81 spaces of 'main'
        # if one of them has 8 numbers which can't exist in that space then the odd one out is the solution for that space and is the variable 'number'
        # this 'number' needs to be put in the row, column and '3 by 3 box' that the space is in because if 'number' is the solution to the current place it can't
        # be the solution to the nearby spaces.
    for row in range(9):
        for column in range(9):

            if len((main[row])[column])==8: # if this is true then we have found the solution for this space
                for number in range(1, 10):
                    if number not in (main[get1])[get2]: # if this is true then 'number' is the solution for this space

                        # Make all the spaces in the same column as the current location have 'number' added to them (if 'number' doesn't already exist)
                        for sub_row in range(9): # sub_row will go from 0 through 8
                            if len(main[sub_row][column]) < 8 and number not in main[sub_row][column]:
                                main[sub_row][column].append(number)
                        # sub_row and sub_column are not needed anymore


                        # Make all the spaces in the same row as the current location have 'number' added to them (if 'number' doesn't already exist)
                        for sub_column in range(9): # sub_column will go from 0 through 8
                            if len(main[row][sub_column]) < 8 and number not in main[row][sub_column]:
                                main[row][sub_column].append(number)
                        # sub_row and sub_column are not needed anymore


                        # Make all the spaces in the same 3 by 3 box as the current location have 'number' added to them (if 'number' doesn't already exist)
                        row_start = get_coords(row)
                        column_start = get_coords(column)

                        for sub_row in range(row_start, row_start + 3):
                            for sub_column in range(column_start, column_start + 3):
                                if len(main[sub_row][sub_column]) < 8 and number not in main[sub_row][sub_column]:
                                    main[sub_row][sub_column].append(number)
                        # sub_row and sub_column are not needed anymore
                                    

                        break # break out of the 'for number in range(1, 10)' bcos we have found what the solution for this space is
    # row, column and number are note needed anymore


    # if a row, column or '3 by 3 box' has 8 spaces which all "can't have a certain number" then the space which is the odd one out is where the number needs to go

    '''
    # putting the solution into main if any of the rows can't have a number anywhere but one space
    '''
    for sub_row in range(9):
        
        for number in range(1, 10):
            num_of_appearances = 0

            for sub_column in range(9):
                if number in main[sub_row][sub_column]:
                    num_of_appearances += 1
                else: # if 'number' is not in the space then this space is where the 'number' is the solution for (as long as num_of_appearances == 8)
                    solution_column = sub_column


            if num_of_appearances == 8: # if this is true then the row we are in has enough information to output the solution to a space in this row corresponding to
                    # solution_column
                for one_to_nine in range(1, 10):
                    if one_to_nine not in main[sub_row][solution_column] and one_to_nine != number: # the space which 'number' is a solution to needs to have all the
                            # the numbers from 1 through 9 in it apart from 'number'
                        main[sub_row][solution_column].append(one_to_nine)


    '''
    # putting the solution into main if any of the columns can't have a number anywhere but one space
    '''
    for sub_column in range(9):
        
        for number in range(1, 10):
            num_of_appearances = 0

            for sub_row in range(9):
                if number in main[sub_row][sub_column]:
                    num_of_appearances += 1
                else: # if 'number' is not in the space then this space is where the 'number' is the solution for (as long as num_of_appearances == 8)
                    solution_row = sub_row


            if num_of_appearances == 8: # if this is true then the column we are in has enough information to output the solution to a space in this column
                    # corresponding to solution_row
                for one_to_nine in range(1, 10):
                    if one_to_nine not in main[solution_row][sub_column] and one_to_nine != number: # the space which 'number' is a solution to needs to have all the
                            # the numbers from 1 through 9 in it apart from 'number'
                        main[solution_row][sub_column].append(one_to_nine)


    '''
    # putting the solution into main if any of the '3 by 3 boxes' can't have a number anywhere but one space
    '''
    start_coords=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
    
    for start_location in start_coords:
        for number in range(1, 10):
            num_of_appearances = 0

            row_start = start_location[0]
            column_start = start_location[1]


            for sub_row in range(row_start, row_start + 3):
                for sub_column in range(column_start, column_start + 3):
                    if number in main[sub_row][sub_column]:
                        num_of_appearances += 1
                    else:
                        solution_location = [sub_row, sub_column]

                
            if num_of_appearances == 8:        
                for one_to_nine in range(1, 10):
                    if one_to_nine not in main[solution_location[0]][solution_location[1]] and one_to_nine != number:
                        main[solution_location[0]][solution_location[1]].append(one_to_nine)


    # Calling the not_to_actual function
    not_to_actual()

    #Printing main and the length of it
##    print('\n\nmain:\n')
##    for i in main:
##        print(i,'\n')

    count=0
    for i in main:
        for j in i:
            count+=len(j)

    print('\nNumber of numbers solved:',count)
    complete2=count




############################################

































'''
