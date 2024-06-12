package src.MultiThreading;

public class SynchronizedTestClass implements Runnable{
    String msg;
    Thread t;
    someClass sObj;

    SynchronizedTestClass(someClass c, String message) {
        sObj = c;
        msg = message;
        t = new Thread(this);
    }

    public void run() {
        //Output:
        //[ Hello
        //]
        //[ Bye
        //]
        //[ Synchronized
        //]
        synchronized (sObj) {  //synchronised objRef
            sObj.callMethod(msg);
        }

    }
}

class someClass{
    void callMethod (String msg) {
        System.out.println("[ " + msg);
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("]");
    }
}

class createThreadInstances {
    public static void main(String[] args) {
        someClass c1 = new someClass();
        SynchronizedTestClass obj1 = new SynchronizedTestClass(c1, "Hello");
        SynchronizedTestClass obj2 = new SynchronizedTestClass(c1, "Synchronized");
        SynchronizedTestClass obj3 = new SynchronizedTestClass(c1, "Bye");

        obj1.t.start();
        obj2.t.start();
        obj3.t.start();

        try {
            obj1.t.join();
            obj2.t.join();
            obj3.t.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }


}