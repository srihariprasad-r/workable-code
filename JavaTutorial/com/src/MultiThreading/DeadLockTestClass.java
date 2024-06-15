package src.MultiThreading;

class A {
    synchronized void foo(B b) {
        String name = Thread.currentThread().getName();
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println( name + " calling B last()");
        b.last();
    }

    synchronized void last() {
        System.out.println("Inside A last");
    }
}

class B {
    synchronized void bar(A a) {
        String name = Thread.currentThread().getName();
        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println( name + " calling A last()");
        a.last();
    }

    synchronized void last() {
        System.out.println("Inside B last");
    }
}

class DeadLockTestClass implements Runnable{
    Thread t;

    A a = new A();
    B b = new B();

    DeadLockTestClass(){
        Thread.currentThread().setName("Main Thread");
        t = new Thread(this, "Racing Thread");
    }

    void deadLockStart() {
        t.start();
        a.foo(b);
    }
    public void run () {
        b.bar(a);
    }

    public static void main(String[] args) {
        DeadLockTestClass dl = new DeadLockTestClass();
        dl.deadLockStart();
    }
}
