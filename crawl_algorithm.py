import process_data

'''
url_dict structure
url_dict :{
    url:{
            repeat_count:number of times url being repeated,
            number_of_links:total number of links from this url
        }
}
'''


class Crawl(object):
    """docstring for Crawl"""
    def __init__(self, link, link_to_fetch):
        super(Crawl, self).__init__()
        self.url_dict = {}
        self.link_to_fetch = link_to_fetch
        self.base_link = link
        self.depth_first_search(link)

    def depth_first_search(self, link):

        """docstring for depth_first_search"""

        if link in self.url_dict.keys():
            self.url_dict[link]['repeat_count'] = self.url_dict[
                    link]['repeat_count']+1
            print link+"\t" + str(self.url_dict[link]['repeat_count'])+"\t" + \
                str(self.url_dict[link]['number_of_links'])
        else:
            url_links = process_data.generate_links(link, self.base_link)
            print link+"\t"+'0'+"\t"+str(len(url_links))

            self.url_dict.update({link: {'repeat_count': 0,
                                 'number_of_links': len(url_links)}})

            for url in url_links:
                if self.link_to_fetch > 0:
                    self.link_to_fetch = self.link_to_fetch - 1
                    self.depth_first_search(url)
