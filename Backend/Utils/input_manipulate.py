import re
from urllib.parse import urlparse



def get_url_input(prompt):
    while True:
        url = input(prompt)
        if not url:
            break
        if not re.match(r"^https?://\S+", url):
            print("Invalid URL. Please enter a valid URL starting with http:// or https://.")
        else:
            return url
        
def get_id_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("ID cannot be blank.")
            continue
        if not user_input.isdigit():
            print("ID must be a number.")
            continue
        if len(user_input.strip("0123456789")) > 0:
            print("ID can only contain numbers.")
            continue
        return int(user_input)




