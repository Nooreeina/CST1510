"""
RECORD CHECK  -  my version
===========================

Name  : Nooree Bhugloo
Lane  : Cyber
Date  : 18.10.2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Bring back check_record(value, limit) and print_report(...) from Week 3
#    (copy them, or rewrite them - either is fine). check_record returns
#    difference, percent and status. print_report does all of the printing,
#    nothing outside it should contain a print() of its own. Give each a
#    one-line docstring.

# your function(s) go here

def status_of(percent):
    """this function checks the status of the report"""
    if percent >=100:
        return "OVER LIMIT"

    elif percent >= 90:
        return "WARNING"

    else:
        return "OK"

def check_report(value, limit):
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


# ====================================================================== STORE
# 2. Get your records into a list of dicts, each shaped like:
#        {"label": ..., "value": ..., "limit": ...}
#
#    Threshold : write the list directly in the code - at least 3 records.
#    Typical   : instead, write a function load_records(path) that reads
#                label,value,limit lines from a file and returns the list.
#                Make your own data file, one record per line.
#    Excellent : also write the results out to a new file (one line per
#                record: label, status), as well as printing them.

records = [
    {"label": "N-001", "value": 50,  "limit": 100},
    {"label": "N-002", "value": 12, "limit": 100},
    {"label": "N-003", "value": 90, "limit": 100},
]



# =============================================================== PROCESS + OUTPUT
# 3. Loop over records. For each one, call check_record and print_report.


for report in records:

    label = report["label"]
    value = report["value"]
    limit = report["limit"]

    difference, percent = check_report(value, limit)
    status = status_of(percent)

    print_report(label, value, limit, difference, percent, status )
#
#    Excellent : also keep a running count of how many were OVER LIMIT, and
#                print that once, after the loop ends.

# your loop goes here


# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it and check every record's numbers are correct by hand
#    [ ] If you are loading from a file, check what happens when the file
#        does not exist - write the error down
#    [ ] Check every function still does one job
