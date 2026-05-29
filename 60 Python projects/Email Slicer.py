"""Extract the username and domain from an email address."""


def slice_email(email: str) -> None:
    """Parse an email and print the username and domain."""
    try:
        at_index = email.index("@")
        username = email[:at_index]
        domain_name = email[at_index + 1:]

        # Validate that the domain contains a dot
        if "." not in domain_name:
            print("Error: invalid email format (domain missing dot).")
            return

        print(f"Your username is '{username.upper()}' and your domain is '{domain_name.upper()}'")
    except ValueError:
        print("Error: invalid email address (missing '@' symbol).")


if __name__ == '__main__':
    user_email = input("Enter your email: ").strip()
    slice_email(user_email)
