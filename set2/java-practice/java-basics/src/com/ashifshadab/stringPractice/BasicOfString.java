package com.ashifshadab.stringPractice;

public class BasicOfString {

    /**
     * == operator is used to compare  by reference
     * equals() is used to compare by spelling and case**/
    public static void main(String[] args) {
        String firstString = "abc";
        String secondString = "abc";

        System.out.println("CASE -1");
        System.out.println("Compare String with == "+ (firstString == secondString));
        System.out.println("Compare String with equal methods  " + firstString.equals(secondString));

        System.out.println("CASE -2");
        //When String created by new operator == operator return false
        // because new operator put string object outside the string pool;
        String thirdString = new String("abc");
        System.out.println("Compare String with == "+ (firstString == thirdString));
        System.out.println("Compare String with equal methods  " + firstString.equals(thirdString));

        System.out.println("CASE -3");
        String fourthString = new String("abc");
        System.out.println("Compare String with == "+ (firstString == fourthString.intern()));
        System.out.println("Compare String with equal methods  " + firstString.equals(fourthString));

        String fifthString = """
                Hello Java,
                I Love Java,
                I Like Java """;
        System.out.println(fifthString);
    }
}
