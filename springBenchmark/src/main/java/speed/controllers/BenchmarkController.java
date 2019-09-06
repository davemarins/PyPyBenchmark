package speed.controllers;

import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class BenchmarkController {

    private final int iterations = 1000000;

    @GetMapping("/string")
    public String stringBenchmark() {
        long start = System.nanoTime();
        for(int i = 0; i < this.iterations; i++) {
            String result = "Hello Euro Python 2019!";
        }
        long end = System.nanoTime();
        return "String output in Spring 5 Java 8 in " + (end - start)/1000000 + "ms";
    }

    @GetMapping("/json/marshal")
    public String jsonMarshaller() {
        long start = System.nanoTime();
        for(int i = 0; i < this.iterations; i++) {
            JSONObject obj = new JSONObject();
            obj.put("userID", 1);
            obj.put("id", 1);
            obj.put("title", "delectus aut aute");
            obj.put("completed", true);
        }
        long end = System.nanoTime();
        return "JSON marshalling in Spring 5 Java 8 in " + (end - start)/1000000 + "ms";
    }

    @GetMapping("/json/unmarshal")
    public String jsonUnmarshaller() {
        JSONObject obj = new JSONObject();
        obj.put("userID", 1);
        obj.put("id", 1);
        obj.put("title", "delectus aut aute");
        obj.put("completed", true);
        String jsonString = obj.toJSONString();
        JSONParser parser = new JSONParser();
        long start = System.nanoTime();
        for(int i = 0; i < this.iterations; i++) {
            try {
                Object result = parser.parse(jsonString);
            } catch (Exception e) {
                return "Something went wrong";
            }
        }
        long end = System.nanoTime();
        return "JSON unmarshalling in Spring 5 Java 8 in " + (end - start)/1000000 +"ms";
    }


    @GetMapping("/calculation")
    public String calculation() {
        int result = 1;
        long start = System.nanoTime();
        for(int i = 0; i < this.iterations; i++) {
            if(result == 0)
                result = 1;
            else
                result = (10*2)/result;
        }
        long end = System.nanoTime();
        return "Calculation in Spring 5 Java 8 in " + (end - start)/1000000 + "ms";
    }

}
