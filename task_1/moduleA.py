class SomeClass(object):
    def __init__(self):
        print("I'm initialized!")

    @staticmethod
    def work(some_attr):
        print(f"I'm worked with {some_attr}")
