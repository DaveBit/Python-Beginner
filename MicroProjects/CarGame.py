command = ""
countStart = -1
countStop = -1
# while command != "quit":
# we could also use the above while statement but the below is more efficient since the conditions does not have to be checked on every iteration. 
while True:
    command = input("> ").lower()
    
    if command == "start":
        countStart+=1
        countStop = -1
        if countStart == 0:
            print("Car started...")
        elif countStart == 1:
            print("Car already started")
        else:
            print("CAR ALREADY STARTED!")
    elif command == "stop":
        countStop +=1
        countStart = -1
        if countStop == 0:
            print("Car Stopped.")
        elif countStop == 1:
            print("Car already stopped")
        else:
            print("CAR ALREADY STOPPED!")
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