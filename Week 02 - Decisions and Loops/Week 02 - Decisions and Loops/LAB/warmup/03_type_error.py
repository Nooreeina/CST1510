# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = int(input("Value: "))

if value > limit:
    print("OVER")

else:
    print("OK")

#int was missing, so since the value entered by the user is an integer, it cannot be read as a string 