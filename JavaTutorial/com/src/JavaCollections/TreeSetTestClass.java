package src.JavaCollections;

import java.util.Comparator;
import java.util.TreeSet;

class Employee {
    String name;
    int age;

    Employee (String name, int age) {
        this.name = name;
        this.age = age;
    }

    String getName (Employee e) {
        return e.name;
    }

    int getAge (Employee e) {
        return e.age;
    }
}

class FirstComparator implements Comparator<Employee> {
    @Override
    public int compare(Employee e1, Employee e2) {
        int e1Age = e1.getAge(e1);
        int e2Age = e2.getAge(e2);
        if (e1Age < e2Age) {
            return -1;
        } else if (e1Age > e2Age) {
            return 1;
        }
        return 0;
    }
}

public class TreeSetTestClass {
    public static void main(String[] args) {
        TreeSet<Employee> st = new TreeSet<Employee>(new FirstComparator());
        st.add(new Employee("Albe", 33));
        st.add(new Employee("Albert", 32));

        for (Employee s: st) {
            System.out.println(s.name);
        }
    }
}
