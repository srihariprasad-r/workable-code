package src.JavaCollections.CollectionsPractise;
import java.util.*;

public class GFG {
    public static void main(String[] args) {
        //[3, 5, 18, 4, 6]
        List<Integer> l = new ArrayList<Integer>();
        l.add(3);
        l.add(5);
        l.add(18);
        l.add(4);
        l.add(6);

        int mnValue = Collections.min(l);
        System.out.println(mnValue);

        int mnLoop = Integer.MAX_VALUE;
        for(int i = 0; i < l.size(); i++) {
            if (l.get(i) < mnLoop) {
                mnLoop = l.get(i);
            }
        };
        System.out.println(mnLoop);

        List<Integer> newList = new ArrayList<Integer>();
        newList.add(10);
        newList.add(20);
        newList.add(30);
        newList.add(1);
        newList.add(2);

        // remove element based on for loop with listIterator
        int idx = 0;
        for (ListIterator<Integer> liter = newList.listIterator(); liter.hasNext();) {
            int num = liter.next();
            if (idx == 2) liter.remove();
            idx++;
        }

        for (Integer el: newList) {
            System.out.println(el);
        }
    }
}
