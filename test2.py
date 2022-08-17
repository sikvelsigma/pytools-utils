from src.pyuseful.classtools.message import MessageThread

msg = MessageThread(print_func=print)
msg.print("hi")
msg.print("hi")
msg.join()
msg.print("hi")
msg.print("hi")
msg.join()