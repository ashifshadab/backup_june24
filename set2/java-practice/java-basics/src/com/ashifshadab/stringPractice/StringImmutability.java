package com.ashifshadab.stringPractice;
/**
 * Since all String literals can be shared,
 * the JVM authors make sure that,
 * once stored, a String variable cannot be changed.
 * This helps not only avoid the problem of concurrent modification of the same value
 * from different places of the code but also prevents unauthorized modification of a String value,
 * which often represents a username or password.**/

public class StringImmutability {

    public static void main(String[] args) {

        String str = "abc";
        str = str + "def";
        System.out.println(str);

        str = str + new String("123");
        System.out.println(str);

        System.out.println("Validation of String Immutability");
        String str1 = "xyz";
        String r1 = str1;
        str1 = str1 + "lmn";
        String r2 = str1;
        System.out.println(r1 == r2);
        System.out.println(r1.equals(r2));
        System.out.println("str1 = " + str1);
        System.out.println("r1 = " + r1);
        System.out.println("r2 = " + r2);
    }
}
