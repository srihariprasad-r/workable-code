package com.src.JavaCollections;

import java.util.*;
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

        }
    }
