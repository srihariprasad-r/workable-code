package src.MultiThreading;

public class RunnableTestClass implements Runnable {
    public void run(){
        go();
    }

    public void go(){
        doMore();
    }

    public void doMore(){
        System.out.println("inside doMore method!");
    }

}

class TestRunnable {
    public static void main(String[] args) {
        Runnable rnable = new RunnableTestClass();
        Thread t = new Thread(rnable);
        t.start();
    }
}
