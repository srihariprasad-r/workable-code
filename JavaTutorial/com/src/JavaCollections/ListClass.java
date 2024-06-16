package src.JavaCollections;

import java.util.*;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import src.JavaCollections.ReverseListClass;

public class ListClass {
    public static void main(String[] args) {
        List<String> arr = new ArrayList<String>();
        arr.add("Seven");
        arr.add("One");
        arr.add("Two");
        arr.add("Three");

        System.out.println(arr.indexOf("Three")); //0
        System.out.println(arr.lastIndexOf("Three")); //3

        System.out.println(arr.containsAll(List.of("Three","Four"))); //false (all values should be in list1

        System.out.println(arr.addAll(List.of("Five", "Six")));

        //for loop
        for (int i = 0; i < arr.size(); i++) {
            System.out.println("for loop: " + " " + arr.get(i));
        }

        //Iterable
        Iterator<String> iterator = arr.iterator();
        while(iterator.hasNext()){
            System.out.println("iterator: " + " " + iterator.next());
        }

        //Reverse list through custom class
        ReverseListClass<String> rls = new ReverseListClass<String>(arr);

        Iterator<String> ril = rls.iterator();
        while (ril.hasNext()){
                System.out.println("reversed: " + " " + ril.next());
        }

        System.out.println("---------addAll()----------");
        arr.addAll(List.of("four", "five", "six"));
        System.out.println(arr);

        System.out.println("--------copyOf()---------");
        List<String> newArr = List.copyOf(arr);
        System.out.println(newArr);

        System.out.println("--------indexOf()---------");
        System.out.println(arr.indexOf("Five"));

        String s1 = arr.get(4).toLowerCase();
        System.out.println(arr.lastIndexOf(s1));
        //find all occurrence of string Five
        List<String> el = arr.stream().filter(i -> i.equalsIgnoreCase("Five")).collect(Collectors.toList());
        System.out.println(el); //[Five, five]
        System.out.println("--------sort collection based on alphabetical order(first lowercase & then upper case)---------");
        Collections.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String s, String t1) {
                for ( int i = 0; i < s.length(); i++ ) {
                    boolean slessThant1 = s.charAt(i) < t1.charAt(i);
                    boolean sGreaterThant1 = s.charAt(i) > t1.charAt(i);
                    if ((s.charAt(i) > 64 && s.charAt(i) < 91) || (t1.charAt(i) > 97 && t1.charAt(i) < 122)) {
                        if (slessThant1) {
                            return -1;
                        }
                        if (sGreaterThant1) {
                            return 1;
                        }
                    } else {
                        if (slessThant1) {
                            return 1;
                        }
                        if (sGreaterThant1) {
                            return -1;
                        }
                    }
                }
                return 0;
                //
            }
        });

        System.out.println(arr);
        System.out.println("--------remove arraylist elements based on condition using iterator---------");
        List<Integer> nums = IntStream.range(1,20).boxed().collect(Collectors.toList());
        Iterator<Integer> lnums = nums.iterator();

        while (lnums.hasNext()){
            int it = lnums.next();
            if ((it % 2 == 0)) {
                lnums.remove();
            }
        }

        System.out.println(nums);
        // removeIf Predicate
        nums.removeIf(i -> i % 2 == 0);
        System.out.println("--------Range Iterator custom class---------");
        IncrementRange ir = new IncrementRange(1, 4);
        Iterator<Integer> il = ir.iterator();

        while (il.hasNext()) {
            System.out.println(il.next());
        }

        }
    }
