email=input("Enter your Email: ").strip()
username=email[:email.index("@")]
domain_name=email[email.index("@")+1:]
User_Name=username.upper()
Domain_Name=domain_name.upper()
format_=(f"Your user name is '{User_Name}' and your domain is '{Domain_Name}'")
print(format_)
