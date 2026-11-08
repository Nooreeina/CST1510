"""
RECORD CHECK  -  my version
===========================

Name  : Bhugloo Nooree
Lane  : Cyber
Date  : 08/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

# =================================================================== FUNCTIONS
# 1. Write parse_line(raw_line) that cleans and parses one raw, messy line
#    into a dict. Handle inconsistent spacing and case - that is the whole
#    point of this week.
#
#    Typical and above: also write status_of(...), shaped for your lane
#    (e.g. OVER LIMIT / WARNING / OK, or FLAGGED / OK). Give both a
#    one-line docstring.

# your function(s) go here

def parse_line(raw_line):
    """clean one raw line and return as dict"""

    raw_line = raw_line.strip().lower() #remove spaces

    src, attempts, result = raw_line.split(",")

    return {
        "src": src.split("=")[1].strip(),
        "attempts": int(attempts.split("=")[1].strip()),
        "result": (result.split("=")[1].strip()),
    }


#return the status as percentage

def status_of(attempts, result):
    """Return status."""


    if result == "failed" and attempts >= 10:
        return "FLAGGED"
    else:
        return "OK"


# ====================================================================== INPUT
# 2. Your raw, messy records - at least 5, deliberately varied in spacing
#    and case. Match the shape to your lane:
#
#    AI / Data Science : "  Survey_2026 , rating=4 , age=23  "
#    Cyber Security     : "SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED"
#    IT                  : "  Srv-01 , used=87 , total=100  "
#
#    Excellent: save these lines to a file and load them with open() /
#    a for loop over the file, instead of writing them directly here.



raw_records = ["SRC=10.0.0.5,ATTEMPTS=12,RESULT=FAILED",
    "  src = 192.168.1.20 , attempts = 3 , result = success  ",
    "SRC=172.16.0.9 ,ATTEMPTS=25, RESULT=Failed",
    "   Src=10.0.0.77,attempts=1,result=SUCCESS",
    "SRC = 8.8.4.4 , ATTEMPTS = 9 , RESULT = FAILED   ",
    "src=203.0.113.4,Attempts=40,Result=failed"]   


# =============================================================== PROCESS + OUTPUT
# 3. Parse and report on every record.
#
#    Threshold : parse each record, print the cleaned dict.
#    Typical   : also call status_of(...) for each, print it alongside.
#    Excellent : print a one-line summary at the end - how many records,
#                how many flagged.

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record["attempts"], record["result"])

    print(record, "-", status)



# ==========================================================================
# 4. Before you finish:
#
#    [ ] Run it against at least 5 genuinely messy raw records
#    [ ] Run it with a value that will not convert to a number - write the
#        error down
#    [ ] Check every function does one job, with a docstring
