"""Repeatedly collect user input until 'Stop' is entered, echoing each entry."""


def collect_inputs() -> None:
    """Prompt the user for text inputs and echo them back until 'Stop' is entered."""
    print("Enter text (type 'Stop' to exit):")
    while True:
        reply = input("Enter text: ")
        if reply.strip().lower() == "stop":
            print("Goodbye!")
            break
        print(reply)


if __name__ == "__main__":
    collect_inputs()
