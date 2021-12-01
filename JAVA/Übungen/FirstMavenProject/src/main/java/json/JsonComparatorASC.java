package json;

import json.objects.ValueObject;

import java.util.Comparator;

public class JsonComparatorASC implements Comparator<ValueObject> {
    /**
     * Compares the name attribute of two instances of the ValueObject and returns the
     * difference between the names in alphabetical order
     * @param o1 First instance of the Value object
     * @param o2 Second instance of the Value object
     * @return int: The gap between the the names in alphabetical order
     */
    @Override
    public int compare(ValueObject o1, ValueObject o2) {
        return o1.getName().compareTo(o2.getName());
    }
}
