from functools import reduce
from operator import and_
test_list = ["434", "823", "98", "74"]
print("The original list is : " + str(test_list))
res = reduce(and_, (string.isdigit() for string in test_list))
print("Are all strings digits ? : " + str(res))
#This code is contributed by Jyothi pinjala.
