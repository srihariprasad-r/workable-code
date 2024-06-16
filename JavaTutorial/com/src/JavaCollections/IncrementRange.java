package src.JavaCollections;

import java.util.Iterator;

public class IncrementRange implements Iterable<Integer>  {
    int start;
    int end;

    IncrementRange(int a, int b) {
        this.start = a;
        this.end = b;
    }

    @Override
    public Iterator<Integer> iterator () {
        return new Iterator<Integer>() {
            @Override
            public boolean hasNext () {
                return start <= end;
            }

            @Override
            public Integer next () {
                return start++;
            }
        };
    }
}
