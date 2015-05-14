import requests
import BeautifulSoup
import utils
import codecs

streamWriter = codecs.lookup('utf-8')[-1]


def generate_links(link, base_link):
    """docstring for generate_links"""
    a_url_list = []
    try:
        response = requests.get(link)
        # BeautifulSoup generate DOM tree for html document
        # for searching and manuplation of dom document
        dom_tree = BeautifulSoup.BeautifulSoup(response.text)
        a_element_list = dom_tree.fetch('a')  # a elements in html doc
        for a_element in a_element_list:
            a_url = a_element.get('href')
            if utils.is_valid_url(a_url, base_link):
                a_url_list.append(utils.sanitize_url(a_url, base_link))
    except:
        return a_url_list
    return a_url_list
