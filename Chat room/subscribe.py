from settings import redisObject
import sys

if __name__ == '__main__':
    channel = sys.argv[1]
    pubsub = redisObject.pubsub()
    pubsub.subscribe(channel)
    print 'Listening to {channel}'.format(**locals())
    while True:
        for item in pubsub.listen():
            print item['data']