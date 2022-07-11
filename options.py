import time

options = (["", "Option 1", "Option 2", "Option 3"])

for number in range(1,4):
    print(number, ": " + options[1])

for x in options:
    print(x)
a = input('Enter your option:')
time.sleep(0.25)
if a == ("1"):
    print("You picked", options[1])
elif a == ("2"):
    print("You picked", options[2])
elif a == ("3"):
    print("You picked", options[3])
else:
    print("Not an option")
