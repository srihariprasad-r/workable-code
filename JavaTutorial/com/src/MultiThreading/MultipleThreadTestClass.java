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

        try {
//            Thread.sleep(2000); // sleep does not have meaningful wait/interruption
            one.t.start();
            System.out.println("First thread is processing!");
            one.t.join();
            System.out.println("First thread is done!");
            two.t.start();  //starts second thread
            System.out.println("Second thread is processing!");
            two.t.join();
            System.out.println("Second thread is done!");
        } catch (InterruptedException e) {
            System.out.println("Interrupted");
        }

        System.out.println("Completed");
    }
}
