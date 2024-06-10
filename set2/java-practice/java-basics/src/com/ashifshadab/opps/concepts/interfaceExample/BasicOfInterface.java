package com.ashifshadab.opps.concepts.interfaceExample;

/**
 * what is the difference between an interface and a class?
 * One principal difference  is
 *      – an interface cannot be instantiated; only a class can be instantiated.
 * Another difference is
 *      - a non-static method implemented inside an interface is declared default or private.
 *      By contrast, a default declaration is not available for the class methods.
 *      - Also, fields in an interface are implicitly public, static, and final.
 *      By contrast, class properties and methods are not static or final by default.
 *      The implicit (default) access modifier of a class itself, its fields, methods,
 *      and constructors are package-private, which means it is visible only within its own package.
 *
 * If there are several default methods in an interface, it is possible to create private methods
 * accessible only by the default methods of the interface. They can be used to contain
 * common functionality, instead of repeating it in every default method.
 *
 * The private methods cannot be accessed from outside the interface.
 *
 * Since Java 8, all the fields declared in an interface are implicitly public, static, and final
 * constants. That is why an interface is a preferred location for the constants. You do not
 * need to add public static final to their declarations.
 * **/
public interface BasicOfInterface {

    void method1();
    String method2(int i);
    default int method3(){
        return 42;
    }

    default int method4(){
        return getNumber() + 22;
    }
    private int getNumber(){
        return 42;
    }

}
