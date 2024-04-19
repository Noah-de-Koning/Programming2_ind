# Write your code here
import re

def correct_dates(string):
    match = re.sub(r'(\d+)/(\d+)/(\d+)', r'\2/\1/\3', string)

    return match