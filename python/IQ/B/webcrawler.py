# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
#class HtmlParser(object):
#    def getUrls(self, url):
#        """
#        :type url: str
#        :rtype List[str]
#        """


class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        #hostName = startUrl.split("/")[2];
        
        q = collections.deque()
        q.append(startUrl)
        visit = set()
        res = [startUrl]
        visit.add(startUrl)
        
        while q:
            for _ in range(len(q)):
                parent_url = q.popleft()
                parent_domain = parent_url.split("/")[2]

                for child_url in htmlParser.getUrls(parent_url):
                    ''' child_url in visit:
                        continue
                    if child_url.split("/")[2] != parent_domain:
                        continue'''
                    if child_url not in visit and child_url.split("/")[2] == parent_domain:
                        res.append(child_url)
                        visit.add(child_url)
                        q.append(child_url)
                    else:
                        continue

        return res
            
        
         
