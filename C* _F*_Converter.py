temp = input ("The current weather outside is: ")
conv = input ("C -> F or F -> C? Type either C or F: ").lower

a = (str(temp)).lower  # a = temperature converted into a str
b = (str(conv)).lower  # b = either Celcius or Farenheight converted into a str

if b == "c":
    print ((temp * 9/5)+32)
elif b == "f":
    print ((temp - 32) * 5/9)
else:
    print ("pls specify more accuratly")


