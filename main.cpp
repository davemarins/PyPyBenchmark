#include <string>
#include <chrono>
#include <iostream>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

std::string hello(int times) {
	auto start = std::chrono::high_resolution_clock::now();
	std::string s;
	for(int i = 0; i < times; i++)
		s = "Hello Euro Python 2019!";
	auto stop = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
	std::cout << "Time duration of string in C++ without context switch: " << duration.count() << " microseconds" << endl;
	return s;
}

int calculate(int a, int b, int times) {
	auto start = std::chrono::high_resolution_clock::now();
	int result = 1;
	for(int i = 0; i < times; i++)
		if(result == 0)
			result = 1;
		else
			result = (a * b) / result;
	auto stop = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
	std::cout << "Time duration of addition in C++ without context switch: " << duration.count() << " microseconds" << endl;
    return result;
}

std::string json_out(int times) {
	auto start = std::chrono::high_resolution_clock::now();
	json j;
	for(int i = 0; i < times; i++) {
		json temp;
		temp["userId"] = 1;
		temp["id"] = 1;
		temp["title"] = "delectus aut autem";
		temp["completed"] = false;
		j = temp;
	}
	auto stop = std::chrono::high_resolution_clock::now();
	auto duration = std::chrono::duration_cast<std::chrono::microseconds>(stop - start);
	std::cout << "Time duration of JSON build in C++ without context switch: " << duration.count() << " microseconds" << endl;
	return j.dump(4); // pretty printing - 4 spaces = 1 tab
}
