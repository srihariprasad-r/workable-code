package src.MultiThreading;

public class RunnableTestClass implements Runnable {
    public void run(){ //method which has actual job to be started first
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

class TestRunnable {
    public static void main(String[] args) {
        Runnable rnable = new RunnableTestClass();
        Thread t = new Thread(rnable); // pass runnable object to thread, which carries first method to put in new stack
        t.start(); //creates new stack and places run() method into it
    }
}
