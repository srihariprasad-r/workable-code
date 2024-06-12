package src.MultiThreading;

public class MultipleThreadTestClass implements Runnable {
    String name;
    Thread t;

    MultipleThreadTestClass(String threadName) {
        t = new Thread(this, threadName);
    }
    public void run() {
        go();
    }

    public void go() {
        doMore();
    }

    public void doMore(){
        System.out.println("inside doMore method!");
    }
}

class MultipleThreads {
    public static void main(String[] args) {
        MultipleThreadTestClass one = new MultipleThreadTestClass("First");
        MultipleThreadTestClass two = new MultipleThreadTestClass("Second");
        one.t.start();
        two.t.start();

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            System.out.println("Interrupted");
        }

        System.out.println("Completed");
    }
}
