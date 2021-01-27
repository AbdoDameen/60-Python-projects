import random
password_length=int(input("enter the length of the password"))
characters="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password="".join(random.sample(characters,password_length))
print(password)
