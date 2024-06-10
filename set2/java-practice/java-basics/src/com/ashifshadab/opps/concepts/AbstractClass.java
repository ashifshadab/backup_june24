package com.ashifshadab.opps.concepts;

/**
 * An abstract class may be a regular class that we do not want to be instantiated,
 * or it may be a class that contains (or inherits) abstract methods.

 * In many respects, an abstract class is very similar to an interface. It forces every child
 * class that extends it to implement the abstract methods. Otherwise, the child cannot be
 * instantiated and has to be declared abstract itself.

 * However, a few principal differences between an interface and abstract class
 * make each of them useful in different situations:
 *          • An abstract class can have a constructor, while an interface cannot.
 *          • An abstract class can have a state, while an interface cannot.
 *          • The fields of an abstract class can be public, private, or protected, static
 *              or not, and final or not, while, in an interface, fields are always public,
 *              static, and final.
 *          • The methods in an abstract class can be public, private, or protected, while
 *              the interface methods can be public or private only.
 *          • If the class you would like to amend extends another class already, you cannot use
 *              an abstract class, but you can implement an interface because a class can extend
 *              only one other class but can implement multiple interfaces.
 * **/
public abstract class AbstractClass {

}
