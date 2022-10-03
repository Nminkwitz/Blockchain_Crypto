zeros = ['\x00' for i in range(5) ]
print(zeros)

zeros2 = [ 5*i for i in range(5) ] # saying I want zeros to be the list of 5 * i where i is each of the #'s in this range 0 - 5
print(zeros2)

zeros3 = [ 5*i for i in range(5) if i > 2]
print(zeros3)

zeros4 = [ '\x7a' for i in range(5) ]
print(zeros4)
print(",".join(zeros4))
print("".join(zeros4))

import random
random.randint(8,24)
