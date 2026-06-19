package com.example;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class CalcTest {
    @Test
    void testAdd() {
        assertEquals(5, Calc.add(2, 3));
    }
}
