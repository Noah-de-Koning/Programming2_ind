# Write your code here
import re

def parse_link(string):
    match = re.fullmatch(r'<a href="(.+)">(.+)</a>', string)

    if match:
        caption = match.group(2)
        link = match.group(1)
        return (caption, link)
    else:
        return None