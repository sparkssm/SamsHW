from pattern.web import Crawler
from pattern.web import download
from pattern.web import plaintext
from textblob import TextBlob

class Polly(Crawler):
    def visit(self, link, source=None):
        print 'visited:', repr(link.url), 'from:', link.referrer
        html = download(link.url)
        blob = TextBlob(plaintext(html))
        for sentence in blob.sentences:
            print(sentence.sentiment.polarity)

    def fail(self, link):
        print 'failed:', repr(link.url)

p = Polly(links=['http://www.cia.gov/'], delay=1)
while not p.done:
    p.crawl(method=2, cached=False, throttle=1)