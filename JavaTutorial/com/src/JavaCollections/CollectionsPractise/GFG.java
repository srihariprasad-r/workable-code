package src.JavaCollections.CollectionsPractise;
import java.util.*;

public class GFG {
    public String reverse(int idx, ArrayList<String> ar, ArrayList<String> res) {
        if (idx < 0) {
            return String.join(",", res);
        }
        res.add(ar.get(idx));
        reverse(idx-1, ar, res);

        return String.join(",", res);
    }
    public static void main(String[] args) {
        ArrayList<String> sal = new ArrayList<String>();
        sal.add("One");
        sal.add("Two");
        sal.add("Three");

        for (String c: sal) {
            System.out.println(c);
        }

        String strs[] = new String[sal.size()];
        for (int i = 0; i < sal.size(); i++) {
            strs[i] = sal.get(i);
        }

        for (String s: strs) {
            System.out.println(s);
        }
        ArrayList<String> res = new ArrayList<String>();
        GFG gfg = new GFG();
        System.out.println(gfg.reverse(sal.size()-1, sal, res));
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
        Map<Integer,Integer> mp1 = new HashMap<>();

        for (int i =0; i < list1.length;i++){
            al1.add(list1[i]);
            boolean key = mp1.containsKey(list1[i]);
            if (!key) {
                mp1.put(list1[i], 1);
            } else {
                int ct = mp1.get(list1[i]);
                mp1.put(list1[i], ct + 1);
            }
        };
        System.out.println(al1);
        System.out.println(mp1);

        for (int i =0; i < list2.length;i++){
            boolean key = mp1.containsKey(list2[i]);
            if (key){
                mp1.remove(list2[i]);
            }
        }

        System.out.println(mp1.size());
        //find 3rd largest element
        int[] a = {44,66,99,77,33,22,55};
        ArrayList<Integer> alist = new ArrayList<Integer>(a.length);
        for (int c: a){
            alist.add(c);
        }
        Collections.sort(alist, new Comparator<Integer>() {
            //@Override
            public int compare(Integer e1, Integer e2) {
                if (e1 > e2){
                    return -1;
                } else return 0;
            }
        });
        int k = 3;
        for (int i = 0;i < alist.size();i++){
            if (i == k-1) System.out.print(alist.get(i));
        }
    }
}
