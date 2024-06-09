package src.JavaCollections;

import java.util.*;

public class ReverseListClass<String> {
    private List<String> list;

    public ReverseListClass(List<String> arr) {
        this.list = arr;
    }

    public Iterator<String> iterator() {

        ListIterator<String> it = this.list.listIterator(this.list.size());

        return new Iterator<String>() {
            @Override
            public boolean hasNext() {
                return it.hasPrevious();
            }

            @Override
            public String next() {
                return it.previous();
            }
        };

    }
}
