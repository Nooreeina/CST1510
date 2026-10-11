"""
RECORD CHECK  -  my version
===========================

Name  : Nooree Bhugloo
Lane  : Cyber
Date  : 08.10.26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



# =================================================================== FUNCTIONS
# 1. Write a function called status_of(percent) that returns "OVER LIMIT"
#    (100% or more), "WARNING" (90% or more), or "OK" (anything else).




#    Typical and above: also write check(value, limit) that returns the
#    difference and the percentage as two values - do not print anything
#    inside it, only calculate and return.




#    Excellent: also write print_report(label, value, limit, difference,
#    percent, status) that does ALL of the printing below - nothing outside
#    it should contain a print() of its own.


#Give each function a one-line docstring saying what it does.

#your function(s) go here

def status_of(percent):
    """this function checks the status of the report"""
    if percent >=100:
        return "OVER LIMIT"

    elif percent >= 90:
        return "WARNING"

    else:
        return "OK"

def check(value, limit):
    """this function calculate the difference and percent"""
    difference = limit - value
    percent = ((value / limit) * 100)

    return difference, percent



def print_report(label, value, limit, difference, percent, status):
    """this function print the report"""

    print("label: ", label)
    print("value: ", value)
    print("limit: ", limit)
    print("difference: ", difference)
    print("percent: ", percent)
    print("status: ", status)



# ==================================================================== INPUT
# 2. Ask for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())

#label = ""      # replace with an input() call
#value = 0.0     # replace with an input() call, converted
#limit = 0.0     # replace with an input() call, converted
while True:
    label = input("enter the source IP (or type 'quit' to stop): ")
    if label == "quit":
        print("exited from status check")
        break

    value = float(input("Fail logins: "))
    limit = float(input("Total attempts: "))


# ================================================================== PROCESS
# 3. Work out the difference, the percentage, and the status.
#
#    Threshold : call status_of() to get the status. Work out the
#                difference and percentage inline, not in a function.
#    Typical   : call check() to get the difference and percentage instead.

#difference = 0.0   # replace with your code
#percent = 0.0       # replace with your code
#status = ""          # replace with your code
    difference = limit - value
    percent = (value / limit) * 100 

    status = status_of(percent)
    difference, percent = check(value, limit)


# =================================================================== OUTPUT
# 4. Print the report.
#
#    Threshold : the three values you were given, plus status, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : call print_report() instead of printing directly here, and
#                wrap sections 2-4 in a loop so you can check as many records
#                as you like in one run - type "quit" as the label to stop.
#                Keep count of how many came back OVER LIMIT and print that
#                once, after the loop ends.

    print()
    print("=" * 34)
    print(f"     RECORD CHECK  -  {label}")
    print("=" * 34)

# your report lines go here

    print(f"Failed logins   :{value:>10.2f}")
    print(f"Total attempts  :{limit:>10.2f}")
    print(f"Attempts left   :{difference:>10.2f}")
    print(f"percent         :{percent:>10.2f} %")
    print(f"status          :{status:>10}")




    print("=" * 34)


# ==========================================================================
# 5. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and note the error (do not fix it yet)
#    [ ] Check every function does one job - if a function both calculates
#        and prints, split it
