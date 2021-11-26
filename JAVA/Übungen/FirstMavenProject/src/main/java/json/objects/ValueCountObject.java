package json.objects;

public class ValueCountObject {
    private ValueObject[] value;
    private int count;

    //-------------------------------------------------Getter/Setter--------------------------------------------------------
    public ValueObject[] getValue() {
        return value;
    }

    public void setValue(ValueObject[] value) {
        this.value = value;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }
}
