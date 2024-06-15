package src.MultiThreading;

class Q {
    int n;

    int get() {
        System.out.println("Get :" + n);
        return this.n;
    }

    void put(int n) {
        System.out.println("Put :" + n);
        this.n = n;
    }
}

class Producer extends Q implements Runnable {
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

class Consumer extends Q implements Runnable {
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

        synchronized (p) {
            p.t.start();
        }
        p.t.join();

        synchronized (c){
            c.t.start();
        }
        c.t.join();

    }

}
