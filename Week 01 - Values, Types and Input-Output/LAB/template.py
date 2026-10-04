"""
RECORD CHECK  -  my version
===========================

Name  :  NOOREE BHUGLOO
Lane  :  IT
Date  :  26.09.26

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# ==================================================================== INPUT
# 1. Ask the user for your three values.
#
#    - the first is TEXT      (a name, a hostname, an IP)  -> no conversion needed
#    - the second is a NUMBER (use float(), not int())
#    - the third  is a NUMBER (use float(), not int())
#
#    Remember: input() always gives back text.

#label = ""      # : replace with an input() call
#first = 0.0     # : replace with an input() call, converted
#second = 0.0    # : replace with an input() call, converted


label = input("Enter a label: ")
first = float(input("Enter the first number: "))
second = float(input("Enter the second number: "))

# ================================================================== PROCESS
# 2. Work out what you were NOT given.       [Typical and above]
#
#    - difference : how far the first is from the second
#    - percent    : the first as a percentage of the second
#
#    Do not type the answers. Calculate them.

#quest:
#difference = 0.0   # 
#percent = 0.0      # 

difference = first - second
percent = (first / second) * 100
print("first value entered: ", first)
print("second value entered: ", second)
print("difference: ", difference)
print("percent: ", percent)

# =================================================================== OUTPUT
# 3. Print the report.
#
#    Threshold : print the three values you were given, inside a border
#    Typical   : add difference and percent, 2 decimal places, right-aligned
#    Excellent : difference always shows its sign, plus one line of your own
#
#    Useful:   f"{value:>10.2f}"    right-aligned, 2 decimal places
#              f"{value:>+10.2f}"   the same, but always shows the sign

#quest
#print()
#print("=" * 34)
#print(f"  RECORD CHECK  -  {label}")
#print("=" * 34)

# : your report lines go here
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
difference = first - second
percent = (first / second) * 100
print("first value entered: ",  f"{first:>10.2f}")
print("second value entered: ", f"{second:>10.2f}")
print("difference: ",           f"{difference:>10.2f}")
print("percent: ",              f"{percent:>10.2f}" + "%")
print("=" * 34)


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it three times with different numbers
#    [ ] Run it with a total of 0 and write the error in your journal
#    [ ] Check every variable name says what it holds
#    [ ] Show it to the person next to you
