package com.ashifshadab.basic;

/**
 * In Java 10, a sort of type holder, var, was introduced.
 * The Java Language Specification defines it thus:
 * “var is not a keyword, but an identifier with special meaning
 * as the type of a local variable declaration.”
 * In practical terms, it lets a compiler figure out
 * the nature of the declared variable
 * **/
public class VarIdentifier {
    public static void main(String[] args) {

        var i = 10;

        var a = "Test";

        //var b; compilation error:
        // Cannot infer type: 'var' on variable without initializer

    }
}
