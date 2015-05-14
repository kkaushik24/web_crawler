import re
import codecs

streamWriter = codecs.lookup('utf-8')[-1]


http_pattern = '^https{0,1}:\/\/'  # match for protocol http and https
relative_pattern = '^\/'  # match for relative url


def sanitize_url(link, base_link):
    """docstring for sanitze_url"""
    link = link.lower()
    try:
        if re.match(http_pattern, link):
            return link
        elif re.match(relative_pattern, link):
            if re.match(r'.*\/$', base_link):
                return base_link+link[1:]
            else:
                return base_link+link
        else:
            return str("http://{0}".format(link))
    except:
        return link


def is_valid_url(link, base_link):
    """docstring for is_valid_url"""
    if link:
        if re.match(http_pattern, link):
            return True
        elif re.match(relative_pattern, link):
            if re.search(link, base_link):
                return False
            else:
                return True
        else:
            return False
    else:
        return False
