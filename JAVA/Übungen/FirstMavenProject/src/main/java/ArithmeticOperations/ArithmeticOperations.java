package ArithmeticOperations;

public enum ArithmeticOperations {
    ADD{
        @Override
        public float calc(float a, float b) {
            return a + b;
        }
    },
    SUB{
        @Override
        public float calc(float a, float b) {
            return a - b;
        }
    },
    MULTI{
        @Override
        public float calc(float a, float b) {
            return a * b;
        }
    },
    DIV{
        @Override
        public float calc(float a, float b) throws ArithmeticException {
            if( b == 0){
                throw  new ArithmeticException("Division durch 0 nicht defiiniert!");
            }
            return a / b;
        }
    };


    public abstract float calc(float a, float b);
}
