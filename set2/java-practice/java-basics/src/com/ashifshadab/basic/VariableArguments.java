package com.ashifshadab.basic;
/**
 * Variable Arguments (Varargs) in Java is a method that takes a variable number of arguments.
 * Variable Arguments in Java simplifies the creation of methods
 * that need to take a variable number of arguments.
 * Variable Arguments (Varargs) in Java is a method that takes a variable number of arguments.
 * Variable Arguments in Java simplifies the creation of methods
 * that need to take a variable number of arguments.
 *
 * Vararg Methods can also be overloaded, but overloading may lead to ambiguity.
 * Before JDK 5, variable length arguments could be handled in two ways:
 * One was using overloading, other was using array argument.
 * There can be only one variable argument in a method.
 * Variable argument (Varargs) must be the last argument.
 * **/
public class VariableArguments {
    public static void main(String[] args) {
        fun("Ashif");
        fun("Ashif","Shadab");
        fun("Ashif","Shadab","Raj");
    }

    public static void fun(String ... arr){
        System.out.println("Number of arguments: " + arr.length);
        for (String i : arr)
            System.out.print(i + " ");
        System.out.println("");
    }
}
