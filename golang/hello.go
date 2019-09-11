package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"time"
)

const Times = 1000000

func makeTimestamp() int64 {
	return time.Now().UnixNano() / int64(time.Millisecond)
}

type MyMessage struct {
	userID    int64
	id        int64
	title     string
	completed bool
}

func main() {

	http.HandleFunc("/string", func(w http.ResponseWriter, r *http.Request) {
		tempString := "Hello Euro Python 2019!"
		timeStart := makeTimestamp()
		for i := 0; i < Times; i++ {
			tempString = "Hello Euro Python 2019!"
		}
		timeEnd := makeTimestamp()
		elapsedTime := timeEnd - timeStart
		fmt.Fprintf(w, "String output of %s in golang in %d ms\n", tempString, elapsedTime)
	})

	http.HandleFunc("/json/encode", func(w http.ResponseWriter, r *http.Request) {
		m := MyMessage{1, 1, "delectus aut autem", false}
		b, err := json.Marshal(m)
		timeStart := makeTimestamp()
		for i := 0; i < Times; i++ {
			b, err = json.Marshal(m)
			if err != nil {
				fmt.Fprintf(w, "Something went wrong, here's the error:\n")
				fmt.Fprintf(w, err.Error())
			}
		}
		result := string(b)
		timeEnd := makeTimestamp()
		elapsedTime := timeEnd - timeStart
		fmt.Fprintf(w, "JSON encode in golang in %d ms\n", elapsedTime)
		fmt.Fprintf(w, result)
	})

	http.HandleFunc("/json/decode", func(w http.ResponseWriter, r *http.Request) {
		m := MyMessage{1, 1, "delectus aut autem", false}
		b, err := json.Marshal(m)
		var newMessage MyMessage
		errUnmarshal := json.Unmarshal(b, &newMessage)
		if err != nil {
			fmt.Fprintf(w, "Something went wrong, here's the error:\n")
			fmt.Fprintf(w, err.Error())
		}
		timeStart := makeTimestamp()
		for i := 0; i < Times; i++ {
			errUnmarshal = json.Unmarshal(b, &newMessage)
			if errUnmarshal != nil {
				fmt.Fprintf(w, "Something went wrong, here's the error:\n")
				fmt.Fprintf(w, err.Error())
			}
		}
		timeEnd := makeTimestamp()
		elapsedTime := timeEnd - timeStart
		fmt.Fprintf(w, "JSON decode in golang in %d ms\n", elapsedTime)
	})

	http.HandleFunc("/calculation", func(w http.ResponseWriter, r *http.Request) {
		result := 1
		timeStart := makeTimestamp()
		for i := 0; i < Times; i++ {
			if result == 0 {
				result = 1
			} else {
				result = (10 * 2) / result
			}
		}
		timeEnd := makeTimestamp()
		elapsedTime := timeEnd - timeStart
		fmt.Fprintf(w, "Calculation output in golang in %d ms\n", elapsedTime)
	})

	http.ListenAndServe(":8080", nil)
}
