package src.JavaCollections;

import java.util.ListIterator;
import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;

class Student {
    int num;
    String name;
    String address;

    Student() {}

    Student (int a, String b, String c ) {
        this.num = a;
        this.name = b;
        this.address = c;
    }

    static String getAddress(Student s) {
        return s.address;
    }
}

public class TreeMapTestClass extends Student {
    public static void main(String[] args) {
        TreeMap<Integer, Student> ts = new TreeMap<>();
        //default comparator
        ts.put(1, new Student(1, "ABC", "Some random address"));
        ts.put(2, new Student(2, "ABC", "Galaxy"));

        //Use Map.Entry Interface to get key and value of each map entry
        for (Map.Entry<Integer, Student> s: ts.entrySet()) {
            Student s1 = s.getValue();
            System.out.println(Student.getAddress(s1));
        }

        // fetch keys and get value of key
        System.out.println(ts.get(ts.keySet().toArray()[0]));
    }
}
