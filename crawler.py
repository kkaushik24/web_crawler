import utils
import crawl_algorithm
import codecs

streamWriter = codecs.lookup('utf-8')[-1]

URL = utils.sanitize_url(raw_input('enter the url :'), '')
MAX_LINK_TO_FETCH = input('enter the maximum number of links to crawl :')
print "URL\tREPEAT-COUNT\tNUMBER-OF-LINKS"
print "\t(numbe of times url repeated)\t(number of links in url web page)"

crawl_algorithm.Crawl(URL, MAX_LINK_TO_FETCH)
