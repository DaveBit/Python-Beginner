def greet_user(first_name, last_name): #parameter
    print(f'Hi there {first_name} {last_name}!')
    print('Welcome aboard')


print("Start")
name = input("What's your name?\n") #argument
surname = input("What's your surname?\n") #argument
greet_user(last_name=surname, first_name=name)
#calc_cost(total=50,shipping=5,discount=0.1)
#positional arguments are ok usually. 
#for numbers, better to use keyword arguments. 
#when using positional and keyword arguments, positional first. 
# greet_user("John", last_name="Smith") this is ok. 
print("Finish") 

#arguments are those we supply to the function. 
#parameters are the placeholders we define in a function for receiving information. 