state = "coding"

while True:
    if state == "coding":
        print("You are coding!")

        while True:
            print("How are you feeling?")
            feeling = input()
            feeling = feeling.lower()

            if feeling == "tired" or feeling == "hungry" or feeling == "full" or feeling == "awake":
                if feeling == "tired":
                    state = "sleeping"
                elif feeling == "hungry":
                    state = "eating"
                else:
                    state = "coding"
                break
            else:
                print("Invalid! Type tired, hungry, full, or awake")

    elif state == "eating":
        print("You are eating!")

        while True:
            print("How are you feeling?")
            feeling = input()
            feeling = feeling.lower()

            if feeling == "tired" or feeling == "hungry" or feeling == "full" or feeling == "awake":
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "full":
                    state = "coding"
                else:
                    state = "sleeping"
                break
            else:
                print("Invalid! Type tired, hungry, full, or awake")

    elif state == "sleeping":
        print("You are sleeping!")

        while True:
            print("How are you feeling?")
            feeling = input()
            feeling = feeling.lower()

            if feeling == "tired" or feeling == "hungry" or feeling == "full" or feeling == "awake":
                if feeling == "hungry":
                    state = "eating"
                elif feeling == "awake":
                    state = "coding"
                else:
                    state = "sleeping"
                break
            else:
                print("Invalid! Type tired, hungry, full, or awake")

