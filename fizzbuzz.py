"""
Author: Scott C Gramig
Program: Fizz Buzz Test
"""

print "--------- The Fizz Buzz Test --------"

for x in range (1,101):
	if x % 15 == 0:
		print "%d: FizzBuzz" % x
	elif x % 3 == 0:
		print "%d: Fizz" % x
	elif x % 5 == 0:
		print "%d: Buzz" % x
