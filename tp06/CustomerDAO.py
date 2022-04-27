




from itertools import tee
from Customer import Customer


class CustomerDAO:

    def __init__(self,filename=""):
        self.filename = filename
        self.reload()

    def reload(self):
        self.file = open(self.filename)
        next(self.file)
    
    def find_all(self):
        self.reload()
        for line in self.file:
            l = line.strip().split(',')
            c = Customer(*l)
            yield c

    def find_done(self):
        self.reload()
        for line in self.file:
            l = line.strip().split(',')
            if l[-1] == 'true':
                c = Customer(*l)
                yield c



    def __del__(self):
        self.file.close()
