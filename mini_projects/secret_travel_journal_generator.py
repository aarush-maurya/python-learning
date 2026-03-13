import random


def menu():
    print(f"{'='*30}")
    print(f"1.Create an encrypted journal")
    print(f"2.Decrypt a journal")
    print(f"3.Exit")
    print(f"{'='*30}")


def create_travel_journal():
    trip_names = []
    destinations = []
    costs = []
    list_of_participants = []
    name = input(f"Enter your name : ")
    while True:
        num_of_trips = input(f"Enter the number of trips : ")
        try:
            num_of_trips = int(num_of_trips)
            if num_of_trips > 0:
                break
            else:
                print(f"Must be a positive integer")
        except ValueError:
            print(f"Invalid Input, please enter a positive integer")
    trip_numbers = list(range(1, num_of_trips + 1))
    for i in range(num_of_trips):
        participants = []
        trip = input(f"Enter the trip #{i+1} name :  ")
        trip_names.append(trip.strip())
        destination = input(f"Enter the destination of the trip #{i+1} : ")
        destinations.append(destination)
        while True:
            cost = input(f"Enter the cost of trip #{i+1} : ")
            try:
                cost = float(cost)
                if cost < 0:
                    print(f"Can't be a negative number")
                else:
                    break
            except ValueError:
                print(f"Invalid Input, please enter a number")
        costs.append(cost)
        j = 1
        while True:
            participant = input(
                f"Enter the name of the participant #{j} for trip #{i+1}('q' to stop) : "
            )
            if participant.strip().lower() == "q":
                break
            else:
                participants.append(participant)
            j += 1
        participants = list(map(lambda x: x.strip().capitalize(), participants))
        list_of_participants.append(participants)

    cost_of_all_trips = sum(costs)
    print(cost_of_all_trips)
    discount = 0
    is_discount = input(f"Do you want to apply a discount? (y/N) : ")
    if is_discount.strip().lower() == "y":
        while True:
            discount = input(
                f"Enter the discount percent(e.g : enter '10' for 10% discount) : "
            )
            try:
                discount = int(discount)
                if discount < 1 or discount > 100:
                    print(f"the discount percent must be between 1 to 100")
                else:
                    discount /= 100
                    break
            except ValueError:
                print(f"The discount percent must be a positive integer")

    cost_of_all_trips -= discount * cost_of_all_trips
    journal_string = f"USER: {name}"
    for i, trip, destination, cost, participants in zip(
        trip_numbers, trip_names, destinations, costs, list_of_participants
    ):
        participants_string = ", ".join(participants)
        journal_string += f"\nTRIP #{i} NAME: {trip}\nDESTINATION: {destination}\nCOST: {cost}\nPARTICIPANTS: {participants_string}\n\n"
    journal_string += f"TOTAL COST : {round(cost_of_all_trips, 2)}"

    return journal_string


def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return "Shift must be an integer value."

    if shift < 1 or shift > 25:
        return "Shift must be an integer between 1 and 25."

    characters = "abcdefghijklmnopqrstuvwxyz1234567890"

    if not encrypt:
        shift = -shift

    shifted_characters = characters[shift:] + characters[:shift]
    translation_table = str.maketrans(
        characters + characters.upper(), shifted_characters + shifted_characters.upper()
    )
    encrypted_text = text.translate(translation_table)
    return encrypted_text


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)


def create_key():
    num = random.randint(1, 25)
    return num


while True:
    menu()
    while True:
        mode = input(f"Enter the mode (1 - 3) : ")
        try:
            mode = int(mode)
            if mode < 1 or mode > 3:
                print(f"must be from 1,2 or 3")
            else:
                break
        except ValueError:
            print(f"Invalid Input, must be a positive integer")
    if mode == 1:
        journal = create_travel_journal()
        key = create_key()
        encrypted_journal = encrypt(journal, key)
        print(
            f"Here is the encrypted jounral:\n\n{encrypted_journal}\nKEY : {key}\nIMPORTANT : YOU WILL ONLY BE ABLE TO DECRYPT THIS WITH YOUR KEY"
        )
    elif mode == 2:
        encrypted_journal = input(f"Paste your encrypted journal : ")
        while True:
            key = input(f"Enter the key associated with the journal : ")
            try:
                key = int(key)
                if key < 26 and key > 0:
                    break
                else:
                    print(f"The key must be between 1 to 25")
            except ValueError:
                print(f"Invalid Input, please enter a positive integer")
        journal = decrypt(encrypted_journal, key)
        print(f"\n{journal}")
    elif mode == 3:
        break
