state = "idle"

print("Take care of Biscuit the hamster!")

while True:
    print()

    if state == "idle":
        print("Biscuit is idle.")
        print("Events: play, feed, nap, quit")
        event = input("What do you do?\n")
        event = event.lower()

        if event == "play":
            state = "playing"
        elif event == "feed":
            state = "eating"
        elif event == "nap":
            state = "sleeping"
        elif event == "quit":
            break
        else:
            print("Invalid event!")

    elif state == "playing":
        print("Biscuit is playing on the wheel!")
        print("Events: rest, snack, tired, quit")
        event = input("What do you do?\n")
        event = event.lower()

        if event == "rest":
            state = "idle"
        elif event == "snack":
            state = "eating"
        elif event == "tired":
            state = "sleeping"
        elif event == "quit":
            break
        else:
            print("Invalid event!")

    elif state == "eating":
        print("Biscuit is eating seeds!")
        print("Events: full, play, sleepy, quit")
        event = input("What do you do?\n")
        event = event.lower()

        if event == "full":
            state = "idle"
        elif event == "play":
            state = "playing"
        elif event == "sleepy":
            state = "sleeping"
        elif event == "quit":
            break
        else:
            print("Invalid event!")

    elif state == "sleeping":
        print("Biscuit is sleeping. Zzz...")
        print("Events: wake, food, quit")
        event = input("What do you do?\n")
        event = event.lower()

        if event == "wake":
            state = "idle"
        elif event == "food":
            state = "eating"
        elif event == "quit":
            break
        else:
            print("Invalid event!")

print("Bye!")