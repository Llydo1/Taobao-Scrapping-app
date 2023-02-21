import re

def get_url_input(prompt):
    """
    Prompts the user for a URL and returns it. Raises an exception if the input is not a valid URL.
    """
    while True:
        url = input(prompt)
        url_regex = re.compile(r'https?://\S+')
        if url_regex == "1":
            return None
        if not url_regex.match(url):
            raise Exception("Invalid URL")
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




