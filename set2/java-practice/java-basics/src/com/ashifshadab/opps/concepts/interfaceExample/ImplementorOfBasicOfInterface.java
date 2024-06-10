package com.ashifshadab.opps.concepts.interfaceExample;
/**
 * The purpose of the default method in an interface is to provide a new method
 * to the classes (that implement this interface) without changing them. But the
 * interface implementation is ignored as soon as a class implements the new
 * method too.
 * **/
public class ImplementorOfBasicOfInterface implements BasicOfInterface{
    @Override
    public void method1() {
        System.out.println(":::::METHOD1:::::");
    }

    @Override
    public String method2(int i) {
        return "METHOD2 "+i;
    }

    public int method3(){
        return 15;
    }

    public static void main(String[] args) {
        ImplementorOfBasicOfInterface iobi = new ImplementorOfBasicOfInterface();
        iobi.method1();
        System.out.println(iobi.method2(5));
        System.out.println(iobi.method3());
        System.out.println(iobi.method4());

    }
}
