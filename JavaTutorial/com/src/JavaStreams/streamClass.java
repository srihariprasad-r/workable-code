package src.JavaStreams;

import java.util.*;
import java.util.stream.Stream;
import src.JavaStreams.DishExample;

public class streamClass {
    public static void main(String[] args) {
        List<String> songs = List.of("item1", "item2", "item3");
        Stream<String> st = songs.stream();
        st.forEach(System.out::println); //cannot be used again

        List<DishExample> menu = Arrays.asList(
                new DishExample("pork", false, 800, "MEAT"),
                new DishExample("beef", false, 700, "MEAT"),
                new DishExample("chicken", false, 400, "MEAT"),
                        new DishExample("french fries", true, 530, "OTHER"),
                        new DishExample("rice", true, 350, "OTHER"),
                        new DishExample("season fruit", true, 120, "OTHER"),
                        new DishExample("pizza", true, 550, "OTHER"),
                        new DishExample("prawns", false, 300, "FISH"),
                        new DishExample("salmon", false, 450, "FISH") );

        menu.stream().map(DishExample::getName).forEach(System.out::println);
    }
}
