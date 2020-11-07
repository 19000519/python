command = ""
started = False
stopped = False
while True :
    command = input("> ").lower()
    if command == "start" :
        if started :
            print("car is already started")
        else:
            started = True
            print("car started... ready to go")
    elif command == "stop" :
        if not started:
            print("car is already stopped ")
        else:
            print("car stopped")
    elif command == "quit" :
        break
    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit 
        """)
    else :
        print("hey sorry i don't understand that")