import re
import random
import numpy

DATA = [] # json list: [{x: [0.97714 0.77051 0.54517 0.72295], y: -1}, ...]

TEST_NUMS = 2000
W = None

def sign(value):
    return 1 if value > 0 else -1

def parse_data():
    with open("./hw1_15_train.dat", "r") as fin:
        for line in fin.readlines():
            l = re.split('[ ]*', line)
            yt = float(l.pop().strip())
            xt = [float(xi) for xi in l]
            xt = numpy.array(xt)

            DATA.append({
                "x": xt,
                "y": yt
            })

def run_test():
    is_first_time_update = True
    updated_num = 0

    random.shuffle(DATA)

    for data in DATA:
        if (is_first_time_update):
            is_first_time_update = False
            W = data["x"]
        if (sign(numpy.dot(W, data["x"])) != data["y"]):
            updated_num += 1
            # Correct mistake
            W = W + 0.5 * data["y"] * data["x"]
    return updated_num

if __name__=='__main__':
    sum_update_num = 0

    parse_data()
    for i in xrange(TEST_NUMS):
        print "RUM {0}".format(i)
        sum_update_num += run_test()
    print '\nAVG: {avg}'.format(avg=(sum_update_num / TEST_NUMS))
