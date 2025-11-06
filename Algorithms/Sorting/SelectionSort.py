mylist = [1,5,3,4,2,0,-10]

def SelectionSort(mylist):
    for i in range (len(mylist)-1):                                 #Initiates Outerloop
        indexval = i                                                #Set 'i' to another variable to make it easier for value swap
        for j in range (i+1,len(mylist)):                           #Create an inner loop to compare all values of list with current value of i
            if mylist[j] < mylist[indexval]:                        #Check if the value is less than index value
                indexval = j                                        #if true reassign the indexval, to prepare for swapping
        mylist[i], mylist[indexval] = mylist[indexval], mylist[i]   #Swap the values of indexval with value of 'i' 
    return mylist                                                   #Once all the iteration are done, return the modified list

s = SelectionSort(mylist)
print(s)