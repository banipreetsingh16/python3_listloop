#decalring an empty list
Names=[]                                                                    #declaring an empty list in which we will store data aferwards.
print("Enter to enter your 10 names below:") 

for x in range(10):                                                         #using for loop of range 10 such that it will take 10 input of names 
    name=input("Enter your name here: ")                                   
    Names.append(name)                                                      #appnending the entered names into the empty list which we created.
   
print("Your names are: ", Names)                                            #printing the list which now stores the names which we entered



