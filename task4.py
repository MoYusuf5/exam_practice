password = input("please enter your password")

def length(password):
    if len(password) < 5:
        print("Your Password is Too Short")
    elif len(password) >= 5 and len(password) <= 20:
        print("Your Password is an acceptable length")
    elif len(password) > 20:
        print("your password is too long and may be forgotten")
    else:
        print("something went wrong")

length(password)