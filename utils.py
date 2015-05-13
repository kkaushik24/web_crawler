import re

http_pattern = '^https{0,1}:\/\/'  # match for protocol http and https
relative_pattern = '^\/'  # match for relative url


def sanitize_url(link, base_link):
    """docstring for sanitze_url"""

    if re.match(http_pattern, link):
        return link
    elif re.match(relative_pattern, link):
        return base_link+link
    else:
        return str("http://{0}".format(link))


def is_valid_url(link):
    """docstring for is_valid_url"""

    if re.match(http_pattern, link):
        return True
    elif re.match(relative_pattern, link):
        return True
    else:
        return False
