import re

def generate_hashtag(s):
    return "".join("#" + "".join(s.strip().title().split())) if len("".join("#" + "".join(s.strip().title().split()))) <= 140 and len("".join("#" + "".join(s.strip().title().split()))) > 1 else False

#--------------------------------------------------------------------------------------------------------------

def parse_int(string):
    ONES = {'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight': 8,'nine': 9,'ten': 10,'eleven': 11,'twelve': 12,'thirteen': 13,
            'fourteen': 14,'fifteen': 15,'sixteen': 16,'seventeen': 17,'eighteen': 18,'nineteen': 19,'twenty': 20,'thirty': 30,'forty': 40,'fifty': 50,
            'sixty': 60,'seventy': 70,'eighty': 80,'ninety': 90,
              }
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES[token])
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)
#--------------------------------------------------------------------------------------------------------------

def make_readable(seconds):
    years = 0
    days = seconds // 86400
    hours  = (seconds % 86400) // 3600
    minuts = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{str(days).zfill(2)}:{str(hours).zfill(2)}:{str(minuts).zfill(2)}:{str(seconds).zfill(2)}"
#--------------------------------------------------------------------------------------------------------------
def format_duration(seconds):
    if seconds == 0:
        return "now"

    time_units = [
        ("year", "years", seconds // 31536000),
        ("day", "days", (seconds % 31536000) // 86400),
        ("hour", "hours", (seconds % 86400) // 3600),
        ("minute", "minutes", (seconds % 3600) // 60),
        ("second", "seconds", seconds % 60),
    ]

    result = []
    for unit, plural_unit, conversion in time_units:
        value = conversion
        if value:
            result.append(f"{value} {plural_unit if value > 1 else unit}")
            seconds = value

    if len(result) >= 2:
        result[-1] = "and " + result[-1]
        for i in range(0, len(result) - 2):
            result[i] = result[i] + ","

    return " ".join(result[::1])
#--------------------------------------------------------------------------------------------------------------




print()
