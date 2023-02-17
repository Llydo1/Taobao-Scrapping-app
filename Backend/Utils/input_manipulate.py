import re

def get_url_input(prompt):
    """
    Prompts the user for a URL and returns it. Raises an exception if the input is not a valid URL.
    """
    url = input(prompt)
    url_regex = re.compile(r'https?://\S+')
    if not url_regex.match(url):
        raise Exception("Invalid URL")
    return url
