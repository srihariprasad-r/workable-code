package src.JavaCollections;

import java.util.*;

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
        st.add(new Employee("Albe", 38));
        st.add(new Employee("Clbe", 32));
        st.add(new Employee("Brad", 26));

        for (Employee s: st) {
            System.out.println(s.name);
        }

        NavigableSet<Employee> stn = st.descendingSet();

        Iterator<Employee> sil = stn.iterator();

        while (sil.hasNext()) {
            System.out.println(sil.next().age);
        }

        System.out.println(st.pollLast().age);
        System.out.println("-----------");
        SortedSet<Employee> row = st.headSet(new Employee("Dlbe", 40));

        Iterator<Employee> silrow = row.iterator();

        while (silrow.hasNext()) {
            System.out.println(silrow.next().age);
        }

    }
}
