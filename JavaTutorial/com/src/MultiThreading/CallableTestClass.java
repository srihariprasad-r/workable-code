package src.MultiThreading;

import java.util.Collection;
import java.util.ConcurrentModificationException;
import java.util.List;
import java.util.concurrent.*;

public class CallableTestClass implements Callable<String> {
    @Override
    public String call() {
        try {
            Thread.sleep(100);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("result after 10 seconds");
        return "Result has come!";
    }
}

class CallableClass {
    public static void main(String[] args) throws InterruptedException, ExecutionException {
        ExecutorService es = Executors.newSingleThreadExecutor();
        Future<String> result = es.submit(new CallableTestClass());

        try {
            System.out.println("Future has received response: " + result.get());
        } finally {   // need to force shutdown as daemon was up after receiving response
            es.shutdown();
        }
    }
}
