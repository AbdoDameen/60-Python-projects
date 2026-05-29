import random


def main():
    """Generate a random story from predefined word lists."""
    when = ["A few years ago", "Yesterday", "Last Night", "A long time ago", "On 20th Jan"]
    who = ["a rabbit", "an elephant", "a mouse", "a dog", "a cat"]
    name = ["Abdo", "Jesse", "Adam", "Jack", "Greg"]
    residence = ["Sydney", "Melbourne", "Brisbane", "Tasmania", "Perth"]
    went = ["the Shop", "College", "School", "Party", "Work"]
    happened = [
        "made good friends",
        "ate a banana",
        "found a secret door",
        "solved a case",
        "wrote a book",
    ]

    # Build and print the story
    story = (
        f"{random.choice(when)}, "
        f"{random.choice(who)} that lived in "
        f"{random.choice(residence)}, went to "
        f"{random.choice(went)} and "
        f"{random.choice(happened)}"
    )
    print(story)


if __name__ == '__main__':
    main()
