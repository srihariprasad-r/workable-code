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

        //convert array to ArrayList
        int[] ac;
        ac = new int[5];
        ac[0] = 2;
        ac[1] = 3;
        ac[2] = 4;
        ac[3] = 5;
        ac[4] = 8;

        List<Integer> al = new ArrayList<Integer>();
        for (int el: ac){
            al.add(el);
        }

        System.out.println(al);
        //compare arraylist
        int[] list1 = {1,2,3,4};
        int[] list2 = {4,2,3,1};

        List<Integer> al1 = new ArrayList<Integer>();
        Map<Integer,Integer> mp = new HashMap<>();

        for (int i =0; i < list1.length;i++){
            al1.add(list1[i]);
            mp.add()
        }
        System.out.println(al1);

        List<Integer> al2 = new ArrayList<Integer>();

        for (int i =0; i < list2.length;i++){
            al2.add(list2[i]);
        }
        System.out.println(al2);

        boolean eq = al1.equals(al2);


        System.out.println(eq);
    }
}
