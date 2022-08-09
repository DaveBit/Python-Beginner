def greet_user(first_name, last_name): #parameter
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
name = input("What's your name?\n") #argument
surname = input("What's your surname?\n") #argument
greet_user(name, surname)
print("Finish") 

#arguments are those we supply to the function. 
#parameters are the placeholders we define in a function for receiving information. 