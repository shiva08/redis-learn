from settings import redisObject
import sys

# test
if __name__ == '__main__':
    name = sys.argv[1]
    channel = sys.argv[2]
    print 'Welcome to {channel}'.format(**locals())
    print 'Type exit to leave.'
    while True:
        message = raw_input('Enter a message: ')
        if message.lower() == 'exit':
            break
        message = '{name} says: {message}'.format(**locals())
        redisObject.publish(channel, message)