# Control Statements

Control statements decide:

Which statement executes
How many times loop runs

### Types:

1. Conditional statements
2. Looping statements
3. Jump statements

## 1. Conditional Statements
### a) if Statement

Executes block only if condition is true.

if(age >= 18) {
    System.out.println("Adult");
}
### b) if-else Statement
if(age >= 18) {
    System.out.println("Adult");
}
else {
    System.out.println("Minor");
}
### c) Nested if

if inside another if.

if(age >= 18) {
    if(age < 60) {
        System.out.println("Adult");
    }
}
### d) switch Statement

Used when multiple choices exist.

switch(day) {
    case 1:
        System.out.println("Monday");
        break;

    default:
        System.out.println("Invalid");
}
## 2. Looping Statements

Loops repeat code.

### a) for Loop

Best when number of iterations is known.

for(int i = 1; i <= 5; i++) {
    System.out.println(i);
}
Structure

for(initialization; condition; update)

### b) while Loop

Condition checked first.

while(i <= 5) {
    System.out.println(i);
    i++;
}
### c) do-while Loop

Runs at least once.

do {
    System.out.println(i);
    i++;
}
while(i <= 5);
## 3. Jump Statements
break

Stops loop immediately.

break;
continue

Skips current iteration.

continue;
## Comments in Java

Comments improve readability.

Single-line Comment
// This is comment
Multi-line Comment
/*
Multi-line
comment
*/

# Programs
## Addition Program
class Add {
    public static void main(String[] args) {

        int a = 10;
        int b = 20;

        int sum = a + b;

        System.out.println(sum);
    }
}


## Even Odd Program
int num = 10;

if(num % 2 == 0) {
    System.out.println("Even");
}
else {
    System.out.println("Odd");
}


## Largest Number Program
int a = 10;
int b = 20;

if(a > b) {
    System.out.println(a);
}
else {
    System.out.println(b);
}