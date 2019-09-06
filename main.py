import time
import json
# import numpy as np
from flask import Flask
from werkzeug.serving import run_simple

app = Flask(__name__)

# 1M operations comparison between C++ and Python
# With small numbers, context switch time is prelevant
# but Python doesn't scale up with big numbers
# Here's an example of string declaration and addition

# Conclusions: Flask as microframework is enough, but when
# you need to do a lot of calculation, a good JIT is needed
# instead of interpreting all python scripts
# PyPy is used in this case and results are very close (
# sometimes even better) to C++, but in order to exploit JIT
# you need the JIT with all requirements installed twice

# Performance-wise the use of JIT with Python is very beneficial,
# but compared to Maven it's much more storage instensive and a
# complete build will take much more time in a CI/CD environment

@app.route('/', methods=["GET"])
def alive():
    return 'I\'m alive!'

@app.route("/string", methods=["GET"])
def stringBenchmark():
	start = time.time()
	for count in range(1, 1000000):
		string = "Hello Euro Python 2019!"
	end = time.time()
	return "String output in python in " + str((end - start)*1000) + " ms"

@app.route("/json/dumps", methods=["GET"])
def jsonDumpsBenchmark():
	start = time.time()
	data = {}
	for count in range(1, 1000000):
		temp = {
			'userID': 1,
			'id': 1,
			'title': 'delectus aut autem',
			'completed': False
		}
		data = json.dumps(temp)
	end = time.time()
	return "JSON dumps in python in " + str((end - start)*1000) + " ms"

@app.route("/json/loads", methods=["GET"])
def jsonLoadsBenchmark():
	temp = {
		'userID': 1,
		'id': 1,
		'title': 'delectus aut autem',
		'completed': False
	}
	data = json.dumps(temp)
	start = time.time()
	for count in range(1, 1000000):
		new_temp = json.loads(data)
	end = time.time()
	return "JSON loads in python in " + str((end - start)*1000) + " ms"

@app.route("/calculation", methods=["GET"])
def calculationBenchmark():
	start = time.time()
	result = 1
	for count in range(1, 1000000):
		if result == 0:
			result = 1
		else:
			result = (10 * 2) / result
	end = time.time()
	return "Calculation output in python in " + str((end - start)*1000) + " ms"

"""
@app.route("/numpy", methods=["GET"])
def numpyBenchmark():
	start = time.time()
	for count in range(1, 1000000):
		a = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
		b = np.array([[9, 8, 7],[6, 5, 4],[3, 2, 1]])
		c = np.matmul(a, b)
	end = time.time()
	return "Numpy output in python in " + str(end - start)
"""

if __name__ == '__main__':
    run_simple('localhost', 5000, app)
