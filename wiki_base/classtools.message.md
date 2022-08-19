# Summery
- <kbd>class `MessageThread`</kbd>

Making an instance of `MessageThread` launches a separate thread which will output messages using `print_func` function provided on init with method `print`. This is useful if there're multiple threads outputing messages which may result in a disjoined output

# Contains

## MessageThread
```python
from pyuseful.classtools.message import MessageThread

def some_print(msg):
    print(f"some_print: {msg}")

msg = MessageThread(print_func=print)

# will print "some_print: hello"
msg.print("hello")
# wait for all messages to print
msg.join()
```