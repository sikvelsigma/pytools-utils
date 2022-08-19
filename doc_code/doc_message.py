import sys
sys.path.insert(0, 'src/')

# splice@:msg
from pyuseful.classtools.message import MessageThread

def some_print(msg):
    print(f"some_print: {msg}")

msg = MessageThread(print_func=print)

# will print "some_print: hello"
msg.print("hello")
# wait for all messages to print
msg.join()
# /splice@:msg