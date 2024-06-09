package com.src.JavaCollections;

import java.util.*;

public class ListClass {
    public static void main(String[] args) {
        List<String> arr = new ArrayList<String>();
        arr.add("1");
        arr.add("2");

        for (int i = 0; i < arr.size(); i++) {
            System.out.println(arr.get(i));
        }

        Iterator<String> iterator = arr.iterator();
        while(iterator.hasNext()){
            System.out.println(iterator.next());
        }
    }
}
