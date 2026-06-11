# JDK, JRE and JVM

This is one of the most important concepts in Java.

## a) JVM (Java Virtual Machine)
### What is JVM?

JVM is a virtual machine that runs Java bytecode.

It acts like a bridge between:

Bytecode
Operating system

Without JVM:

Java programs cannot run.
Functions of JVM
### 1.Executes Bytecode

JVM reads .class files and executes them.

### 2.Converts Bytecode into Machine Code

Every operating system has different machine code.

JVM converts bytecode according to the operating system.

### 3. Provides Platform Independence

Because every OS has its own JVM:

Same bytecode works everywhere.
### 4. Memory Management

JVM manages memory automatically.

### 5. Garbage Collection

Unused objects are automatically removed from memory.

JVM Architecture

Main parts:

Class Loader
Method Area
Heap Area
Stack Area
Execution Engine

## b) JRE (Java Runtime Environment)
### What is JRE?

JRE provides everything required to RUN Java programs.

It contains:

JVM
Libraries
Supporting files
Purpose of JRE

If a user only wants to RUN Java applications:

JRE is enough.

No compiler is included.

## c) JDK (Java Development Kit)
### What is JDK?

JDK is used to DEVELOP Java applications.

It contains:

JRE
Compiler
Debugging tools
Development tools
Main Tools in JDK
Tool	Purpose
javac	Compiles Java code
java	Runs program
javadoc	Creates documentation
debugger	Finds errors

## Relationship Between JDK, JRE and JVM

JDK⊃JRE⊃JVM

Meaning:

JDK contains JRE
JRE contains JVM