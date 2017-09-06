def printmsg(msg):
    def printer():
        print(msg)
    return printer

def printmsg2(msg):
    def printer():
        print(msg)
    return printer()

another = printmsg("hi")

another()

printmsg("hihi")