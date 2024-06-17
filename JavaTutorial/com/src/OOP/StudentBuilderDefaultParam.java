package src.OOP;

class Student {
    private String _name = "";
    private int _age = 99;
    private String _motto = "";

    Student (String name, int age, String motto) {
        this._name = name;
        this._age = age;
        this._motto = motto;
    }

    Student (String name) {
        this._name = name;
    }

    Student (int age) {
        this._age = age;
    }

    public String toString() {
        return "name: " + this._name + "\t age is:" + _age;
    }
}

class StudentBuilder {
    private String _name;
    private int _age = 14;      // this has a default
    private String _motto = ""; // most students don't have one

    public Student buildStudent()
    {
        return new Student(_name, _age, _motto);
    }

    public Student name(String _name)
    {
        this._name = _name;
        return new Student(_name);
    }

    public Student age(int _age)
    {
        this._age = _age;
        return new Student(_age);
    }

    public StudentBuilder motto(String _motto)
    {
        this._motto = _motto;
        return this;
    }
}

public class StudentBuilderDefaultParam {
    public static void main(String[] args) {
        Student s1 = new StudentBuilder().name("Eli");
        System.out.println(s1.toString());
        Student s2 = new StudentBuilder().age(34);
        System.out.println(s2.toString());
    }
}
