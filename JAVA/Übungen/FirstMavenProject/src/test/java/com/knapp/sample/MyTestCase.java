package com.knapp.sample;

import ArithmeticOperations.ArithmeticOperations;
import ArithmeticOperations.Calculator;
import org.junit.Test;

import static junit.framework.TestCase.assertEquals;


public class MyTestCase {
    @Test
    public void myfirstTest(){
        Calculator calc = new Calculator(4);
        float res = calc.calculate(ArithmeticOperations.ADD, 4.1234f, 5.1234f);
        assertEquals(9.2468f, res);
    }
}