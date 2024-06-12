package src.MultiThreading;

public class ThreadTestClass extends Thread {
    String name;
    ThreadTestClass(String threadName) {
        super(threadName);
    }

    public void run(){
        go();
    }

    public void go(){
        try {
            Thread.sleep(5000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        doMore();
    }

    public void doMore(){
        System.out.println("inside doMore method!");
    }
}

class TestThread {
    public static void main(String[] args) {
        Thread t = new ThreadTestClass("One");
        t.start();
    }
}