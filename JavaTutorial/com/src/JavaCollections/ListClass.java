package com.src.JavaCollections;

import java.util.*;
import src.JavaCollections.ReverseListClass;

public class ListClass {
    public static void main(String[] args) {
        List<String> arr = new ArrayList<String>();
        arr.add("One");
        arr.add("Two");

        //for loop
        for (int i = 0; i < arr.size(); i++) {
            System.out.println(arr.get(i));
        }

        //Iterable
        Iterator<String> iterator = arr.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }

        //Reverse list through custom class
        ReverseListClass<String> rls = new ReverseListClass<String>(arr);

        Iterator<String> ril = rls.iterator();
            while (ril.hasNext()){
                System.out.println(ril.next());
            }

        }
    }
