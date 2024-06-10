package src.JavaStreams;

public class DishExample {
    private String name;
    private boolean vegetarian;
    private float calories;
    private String type;

    public DishExample (String name, boolean vegetarian, float calories, String type) {
        this.name = name;
        this.vegetarian = vegetarian;
        this.calories = calories;
        this.type = type;
    }

    public float getCalories() {
        return this.calories;
    }

    public String getName() {
        return this.name;
    }

    public boolean getOption() {
        return this.vegetarian;
    }

    public String getType() {
        return this.type;
    }
}
