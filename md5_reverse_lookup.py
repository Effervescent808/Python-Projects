import hashlib

def Exit():
    print("Wrong Password")
    exit(0)

print("Password 1 is: dc647eb65e6711e155375218212b3964")
pass1 = input("Password 1: ")

if hashlib.sha256(pass1.encode()).hexdigest() == "e7cf3ef4f17c3999a94f2c6f612e8a888e5b1026878e4e19398b23bd38ec221a":
    print("Password 2 is: 25f9e794323b453885f5181f1b624d0b")
    pass2=input("Password 2: ")
    if hashlib.sha256(pass2.encode()).hexdigest() == "15e2b0d3c33891ebb0f1ef609ec419420c20e320ce94c65fbc8c3312448eb225":
        print("Password 3 is: d8578edf8458ce06fbc5bb76a58c5ca4")
        pass3=input("Password 3: ")
        if hashlib.sha256(pass3.encode()).hexdigest() == "65e84be33532fb784c48129675f9eff3a682b27168c0ea744b2cf58ee02337c5":
            print("Here is your flag: <WExFul>")
        else:
            Exit()
    else:
        Exit()
else:
    Exit()

