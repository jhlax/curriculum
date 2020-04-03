// LESSON 0


// This is a single line comment
/*
 * This is a multiline comment
 */

 #include <stdio.h>  // you can put a comment AFTER code. But not before.

 /* Unless its one of these types of comments */ #define BUT_DONT_DO_THIS 1  // use this kind of comment instead

 /*
  *  All C programs will be EXECUTABLE if they have a MAIN FUNCTION.
  *
  */

/*

int main() {
    // This is the code body, all of these variables only apply within its SCOPE. Look at function 2 and 3.

    return 0;  // This is the return value of this function. Since this function is INT main() { ... we have
               // an int return value; typing is STATIC and EXPLICIT in C. It is DYNAMIC and DUCK in Python.
               // Do not worry about Python or what these terms mean YET.
}

*/

#define TRUE 1   // defined true as 1
#define FALSE 0  // defined false as 0


int function1() {
    int scoped_variable = 1;  // This variable is available only within the curly braces.

    return TRUE;  // In actual C, true == 1 and false == 0; more in the next lesson. FIXME! define a macro or code
}

int function2() {
    int scoped_variable = 69;        // created and initialized scoped_variable. (one method of passing)

    printf("%d\n", scoped_variable);  // I declared this variable in `function1()`. Compiling will tell us if
                                     // the program is valid. TODO: make this work. multiple ways to make it work.

    return 0;
}

int function3() {
    printf("hello, world\n");

    return 0;
}

/*
 *
 *  Now try to look for mistakes, and mess with variables and statements to make these things work.
 *
 *  Comment out the `main()` function and make your own that runs function 1, prints it's result, then runs function 2
 *  and stores its result, but does not print it. Instead, create a function3 that prints "hello, world". The main
 *  function should then exit.
 *
 *  If you are confused, try looking at the Python code further down when you see Lesson 0.1
 *
 */

int main() {
    int f1 = function1();
    int f2 = function2();  // it is good practice to declare (and usually initialize) your variables at the top of
                           // a function.

    printf("function1: %d\n", f1);

    function3();

    return 0;
}
