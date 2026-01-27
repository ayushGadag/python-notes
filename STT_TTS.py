def greet(func):
    def heloo():

        print("hi")
        func()
        print("txn")
    return heloo
@greet
def mine():
    print("ayush")
mine()    