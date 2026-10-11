# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

def check(value, limit):
    status = "OVER LIMIT" if value > limit else "OK"
    return status

status = check(87,100)

print(status)

#status was not defined, so i removed it from the def function and defined status