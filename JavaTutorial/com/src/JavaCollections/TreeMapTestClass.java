package src.JavaCollections;

import java.util.ListIterator;
import java.util.Map;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.Comparator;

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


class FirstComparatorTest implements Comparator<Integer> {
    public int compare(Integer s1, Integer s2) {
        if (s1 < s2) {
            return -1;
        } else if (s1 > s2) {
            return 1;
        }
        return 0;
    }
}

public class TreeMapTestClass {
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

        //use custom comparator to sort keys : comparator is only for key!
        TreeMap<Integer, Student> rts = new TreeMap<Integer, Student>(new FirstComparatorTest());
        rts.put(21, new Student(11, "ABC", "Some random address"));
        rts.put(20, new Student(21, "ABC", "Galaxy"));

        System.out.println(rts);
    }
}
