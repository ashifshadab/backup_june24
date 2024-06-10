package com.ashifshadab.stringPractice;

public class StringTextBlock {

    public static void main(String[] args) {

        // Before Java 15 and use \n to break the line:
        String firstString = "<html>\n" + " <body>\n" + " <p>Hello World.</p>\n" + " </body>\n" + "</html>\n";

        System.out.println(firstString);

        /* A new String literal, called a text block, was introduced with Java 15.
        It facilitates the preservation of indents and multiple lines without adding white spaces in quotes.*/
        String secondString = """
                <html>
                    <body>
                        <p>Hello World</p>
                    </body>
                </html>
                """;

        System.out.println(secondString);
    }
}
