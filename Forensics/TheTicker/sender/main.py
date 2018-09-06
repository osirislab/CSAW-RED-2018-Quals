import csv
import random
import requests
import copy
import time

class FakeFile:
    def __init__(self, filename):
        self.name = filename 
        self.contents = ""

    def write(self,contents):
        self.contents += contents

    def __repr__(self):
        return self.contents

def gen_csv(rows, cols, possible_headers):
    out = FakeFile("{}by{}.csv".format(rows, cols))
    
    pos = copy.deepcopy(possible_headers)
    contents = []
    headers = []
    
    for i in range(cols):
        header = random.choice(pos)
        pos.pop(pos.index(header))
        headers.append(header)
    
    contents.append(tuple(headers))

    for i in range(rows):
        x = []
        for j in range(cols):
           x.append(random.random() * (10**random.randint(0, 6)))
        contents.append(tuple(x))

    w = csv.writer(out)
    for c in contents:
        w.writerow(c)
    return out

def send_csv(csv, url):
    p = requests.post(url, data=str(csv))


if __name__ == "__main__":
    headers = open("headers", 'r').read().split()
    for i in range(random.randint(15,260)):
        if len(headers) > 0:
            fake = gen_csv(random.randint(10,340), random.randint(1, len(headers)), headers)
            send_csv(fake, "http://yeet.stream:5000/")
            print("Sent csv number {}".format(i))
        time.sleep(random.randint(0,14))
