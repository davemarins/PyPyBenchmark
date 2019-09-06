from cppyy import cppdef
import time
import json

# 1M operations comparison between C++ and Python
# With small numbers, context switch time is prelevant
# but Python doesn't scale up with big numbers
# Here's an example of string declaration and addition

# Conclusions: Flask as microframework is enough, but when
# you need to do a lot of calculation, C++ is the only way
# Flask listens to requests, meanwhile a C++ programm is running
# in background with a thread pool, some signal is passed through
# OS, the programm does calculations and when exits, Flask
# returns the correct reply to client(s)

# Beware that C++ JSON is a dependency, package management
# in Python is better handled

with open('main.cpp', 'r') as myfile:
	data = myfile.read()
	cppdef(str(data))

if __name__ == "__main__":
	from cppyy.gbl import hello
	from cppyy.gbl import calculate
	from cppyy.gbl import json_out

	start = time.time()
	string = hello(1000000)
	end = time.time()
	print("String output in C++ in " + str(end - start))

	start = time.time()
	json_dump = json_out(1000000);
	end = time.time()
	print("JSON output in C++ in " + str(end - start))

	start = time.time()
	result = calculate(10, 2, 1000000)
	end = time.time()
	print("Addition output in C++ in " + str(end - start))
