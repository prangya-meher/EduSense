# Introduction to Java
## What is Java?

Java is a high-level, object-oriented, secure, and platform-independent programming language used for developing different types of applications.

It was developed to make programming easier, safer, and portable across different operating systems.

Java is widely used because:

It is easy to learn
It supports Object-Oriented Programming (OOP)
It can run on multiple platforms
It has strong security and memory management

Java programs are used in:

Web applications
Android applications
Banking software
Desktop software
Enterprise systems
Cloud-based applications

Why Java Became Popular

Before Java, many programming languages were platform dependent.

### Example:

A program written for Windows could not directly run on Linux.

Java solved this problem using:

Bytecode
JVM (Java Virtual Machine)

This allowed Java programs to run on any operating system.

This concept is called:

“Write Once, Run Anywhere”

# History of Java

Java was developed by:
James Gosling and his team at Sun Microsystems in 1995.

Initially, Java was called:

Oak

Later renamed:

Java

In 2010, Oracle Corporation acquired Sun Microsystems and became the owner of Java.

# Structure of Java Program

### Example:

class Hello {
    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
Detailed Explanation
class Hello

Defines a class named:

Hello

Java programs are organized inside classes.

public

Access modifier.

### Means:

Accessible everywhere.
static

Static means:

Method belongs to class itself.

No object required.

void

Means:

Method returns nothing.
main()

Entry point of Java program.

Execution starts from:

main()
String[] args

Stores command-line arguments.

System.out.println()

Used to print output on screen.

Breakdown:

System → predefined class
out → output stream
println() → prints line

Input and Output in Java
Output
System.out.println("Hello");
Input using Scanner
import java.util.Scanner;

class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int age = sc.nextInt();

        System.out.println(age);
    }
}
Explanation
import java.util.Scanner

Imports Scanner class.

Scanner sc

Creates Scanner object.

System.in

Takes input from keyboard.

nextInt()

Reads integer value.

# Type Casting
What is Type Casting?

Converting one data type into another.

## a) Widening Casting

Automatic conversion.

Small datatype → large datatype

Example:

int num = 10;
double d = num;

No data loss.

## b) Narrowing Casting

Manual conversion.

Large datatype → small datatype

Example:

double d = 10.5;
int num = (int)d;

Possible data loss.