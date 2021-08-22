#Get numbers
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

#Transfer to not numbers
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

#This is the code that actually does it
get1=0
get2=0
for i in range(9):
    for i in range(9):
        count=1
        if len((puzzleIn[get1])[get2])==1:
            for i in range(9):
                if count not in (puzzleIn[get1])[get2]:
                    (main[get1])[get2].append(count)
                count+=1
        get2+=1
    get1+=1
    get2=0




def not_to_actual():
    print('\n\nnot_to_actual:\n')
    #This routes through main, checks if length is 8 (that is, number exists), and outputs missing number (that is, the actual number)
    get1=0
    get2=0
    record=[]
    length=0
    for i in range(9):
        for i in range(9):
            if len((main[get1])[get2])==8:
                count=1
                for i in range(9):
                    if count not in (main[get1])[get2]:
                        record.append(count)
                    count+=1
            else:
                record.append(0)
            get2+=1
        print(record)
        for i in record:
            if i!=0:
                length+=1
        record=[]
        get2=0
        get1+=1
    print('\nLength of not_to_actual:',length)





def get_coords(place):
    use=0
    if place>=0 and place<=2:
        use=0
    elif place>=3 and place<=5:
        use=3
    elif place>=6 and place<=8:
        use=6
    else:
        print('   Error - place is out of range')

    return use





#Printing not_to_actual and the length of it
not_to_actual()

#Printing main and the length of it
print('\n\nmain:\n')
for i in main:
    print(i,'\n')

count=0
for i in main:
    for j in i:
        count+=len(j)

print('\nLength of main:',count)



complete1=0
complete2=1
#Routing through the 9 by 9 sudoku
while complete1 != complete2:
    complete1=complete2

    print('\n*******************************************************************************\n')
    get1=0
    get2=0
    for i in range(9):
        for i in range(9):
    ##        not_to_actual()
            if len((main[get1])[get2])==8:
                count=1
                for i in range(9):
                    if count not in (main[get1])[get2]:
                        #print(count)
                        #At this stage, the actual number has just been outputted and we know the coordinates too

                        #This is the column update
                        use1=0
                        use2=get2
                        variable=count
                        for i in range(9):
                            if len((main[use1])[use2])<8 and variable not in (main[use1])[use2]:
                                (main[use1])[use2].append(variable)
                            use1+=1
                        #End updating the column

                        #This is the row update
                        use1=get1
                        use2=0
                        variable=count
                        for i in range(9):
                            if len((main[use1])[use2])<8 and variable not in (main[use1])[use2]:
                                (main[use1])[use2].append(variable)
                            use2+=1      
                        #End updating the row

                        #This is the 3 by 3 update
                        use1=get_coords(get1)
                        store=get_coords(get2)
                        use2=store
                        variable=count

                        for i in range(3):
                            for i in range(3):
                                if len((main[use1])[use2])<8 and variable not in (main[use1])[use2]:
                                    (main[use1])[use2].append(variable)
                                use2+=1
                            use2=store
                            use1+=1
                        
                        #End updating the 3 by 3
                    count+=1
            get2+=1
        get2=0
        get1+=1


    #This is the: rows - not in times 8, then add all but that one as not numbers
    place1=0

    for i in range(9):
        check=1
        for i in range(9):
            record=0
            store=0
            place2=0
            for i in range(9):
                if check in (main[place1])[place2]:
                    record+=1
                else:
                    store=place2
                place2+=1


            count=1
            if record==8:
                for i in range(9):
                    if count not in (main[place1])[store] and count != check:
                        (main[place1])[store].append(count)
                    count+=1
                    
            check+=1
        place1+=1
    #End the rows not in times 8


    #This is the: columns - not in times 8, then add all but that one as not numbers
    place2=0

    for i in range(9):
        check=1
        for i in range(9):
            record=0
            store=0
            place1=0
            for i in range(9):
                if check in (main[place1])[place2]:
                    record+=1
                else:
                    store=place1
                place1+=1


            count=1
            if record==8:
                for i in range(9):
                    if count not in (main[store])[place2] and count != check:
                        (main[store])[place2].append(count)
                    count+=1

            check+=1
        place2+=1
    #End the columns not in times 8



    #This is the: 3 by 3 - not in times 8, then add all but that one as not numbers
    start_coords=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
        
    location=0
    for i in range(9):
        check=1
        for i in range(9):
            record=0
            store=[]
            
            place1=(start_coords[location])[0]
            place2=(start_coords[location])[1]


            for i in range(3):
                for i in range(3):
                    if check in (main[place1])[place2]:
                        record+=1
                    else:
                        store=[place1,place2]
                    place2+=1
                place2=(start_coords[location])[1]
                place1+=1

                

            count=1
            if record==8:        
                for i in range(9):
                    if count not in (main[store[0]])[store[1]] and count != check:
                        (main[store[0]])[store[1]].append(count)
                    count+=1

            check+=1
        location+=1

    #End the 3 by 3 not in times 8

    

    #Printing not_to_actual and the length of it
    not_to_actual()

    #Printing main and the length of it
    print('\n\nmain:\n')
    for i in main:
        print(i,'\n')

    count=0
    for i in main:
        for j in i:
            count+=len(j)

    print('\nLength of main:',count)
    complete2=count




############################################

































