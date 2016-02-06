from pattern.web import Twitter

t = Twitter()
i = None
for j in range(3):
    for tweet in t.search('hotdogs', start=i, count=30):
        print tweet.id
        print tweet.name
        print tweet.text
        print