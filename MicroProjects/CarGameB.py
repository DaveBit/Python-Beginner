command = ""
started = False
# while command != "quit":
# we could also use the above while statement but the below is more efficient since the conditions does not have to be checked on every iteration. 
while True:
    command = input("> ").lower()
    
    if command == "start":
        
        if started:
            print("CAR ALREADY STARTED!")
        else:
            started = True
            print ("Car started...")

    elif command == "stop":   
        if not started:
            print("CAR ALREADY STOPPED!")
        else:
            started = False
            print("Car Stopped.")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to quit
        """)
    elif command == "quit":
        print("See you later!")
        break
    else: 
        print("Sorry, I don't understand that!")