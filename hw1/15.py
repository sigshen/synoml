import re
import numpy

ITERATION = 0
CORRECT_NUM = 0
W = None

def sign(value):
    return 1 if value > 0 else -1

if __name__=='__main__':

    with open("./hw1_15_train.dat", "r") as fin:
        for line in fin.readlines():
            ITERATION += 1

            # Parsing
            l = re.split('[ ]*', line)
            yt = float(l.pop().strip())
            xt = [float(xi) for xi in l]
            xt = numpy.array(xt)

            if (ITERATION is 1):
                W = xt
            if (sign(numpy.dot(W, xt)) != yt):
                CORRECT_NUM += 1
                # Correct mistake
                W = W + yt * xt

        print W
        print CORRECT_NUM
