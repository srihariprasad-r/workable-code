package src.MultiThreading;

class Q {
    int n;
    boolean valueSet;

    synchronized int get() {
        while (!valueSet) {
            try{
                System.out.println("Inside get: " + valueSet);
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        valueSet = false;
        System.out.println("Get :" + n);
        notify();
        return this.n;
    }

    synchronized void put(int n) {
        while (valueSet) {
            try {
                System.out.println("Inside put: " + valueSet);
                wait();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
        valueSet = true;
        System.out.println("Put :" + n);
        this.n = n;
        notify();
    }
}

class Producer implements Runnable {
    Q q;
    Thread t;
    Producer(Q q) {
        this.q = q;
        t = new Thread(this, "Producer");
    }

    public void run () {
        int i = 0;

        while (true) {
            q.put(i++);
        }
    }
}

class Consumer implements Runnable {
    Q q;
    Thread t;
    Consumer(Q q) {
        this.q = q;
        t = new Thread(this, "Consumer");
    }

    public void run () {
        while (true) {
            q.get();
        }
    }
}

public class ProducerConsumerTestClass {
    public static void main(String[] args) throws InterruptedException {
        Q q = new Q();
        Producer p = new Producer(q);
        Consumer c = new Consumer(q);
        p.t.start();
        c.t.start();

    }

}
