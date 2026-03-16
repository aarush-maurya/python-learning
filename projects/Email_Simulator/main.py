#this is the first multi modular project made by me. Learned at freecodecamp.org
from Classes.User import User

# you cn modify this main function to try out the other features :)
def main():
    aarush = User("Aarush")
    anay = User("Anay")

    aarush.send_email(anay, "Hello", "Hi Anay, just saying hello!")
    anay.send_email(aarush, "Hello", "Hi Aarush, hope you are fine.")
    anay.check_inbox()
    anay.read_email(1)
    anay.delete_email(1)
    anay.check_inbox()


if __name__ == "__main__":
    main()
