"""
Curriculum - Comp Sci in Python and C
=====================================

Section 1
---------

I will use Python as a *pseudocode* primarily, with C being the actual language of learning
for at least a few lessons. Learning types, functions, arrays, pointers, then the compiler
as a tool is first. Mixed in throughout we will look at control flow. This is considerably
the most important part, because making decisions based on inputs is huge. How do you choose
between doing something or not? How do you check if something is true or false? Neither?

Section 2
---------

Then we look into the terminal while also writing some simple C programs (again, Python will
be the pseudocode to show the programs in simpler and more abstract terms.) This is when we
will slowly integrate the lessons learned initially into more useful shell programs you can
actually use that has some sort of use. These programs are going to be basic, but hopefully
you come up with them--if not I will try to come up with them (once you start thinking in
code you will start coming up with them.)

Section 3
---------

At a given point we will look at object oriented programming. We will now write in C as our
pseudocode to then write in Python, noticing the differences between two equally similar and
dissimilar languages. We don't have to *implement* the OO programming in C, but I want to see
the control flow and understanding of what an object *is* built up. Transitioning to object-
oriented should be a "oh fuck ahahhaha ok I get it, wow this is so much easier" moment.

Section 4
---------

We will then look at certain algorithms. Searches, sorts, filters. Also, we will look at
very common forms of objects and patterns that allow you to write programs with much less
programming and "boilerplate." Boilerplate is you creating a bunch of code just to use it as
your foundational types and methods... this is reinventing the wheel much of the time. I
still encourage it for now, and we will use existing libraries along with making our own
clones of the boilerplate (like Linux copied Unix) for a few things.

Section 5
---------

We will then start looking at some code with applications. Things that are useful or specific
in nature and really map out or problems and solutions. At this point I think you should have
a fine understanding of both C and Python. Both paradigms should be relatively natural, and
knowing their differences will make you able to learn essentially *any other language with
ease.*

Section 6
---------

At this point were on fire. We will probably work on automation, and focus on Linux, scripting
and then start to look at servers and structured languages like HTML and JSON.

Section Extra Credit
--------------------

At another point, we will begin looking at databases, and working with them. We will try to
keep code well-documented, backed up, and well-written...

After this we look at different libraries and nail the coffin on becoming a self-sufficient
programmer.
"""

current_lesson = 0


#
# Section 1
#

def lesson0():
    """

    Lesson 0

        The main function of a C program, written in Python as pseudocode. This is a very simple
        program, and will print "hello, world", and exit.

        See `lesson0.c`, then complete the program in C.

    """
    pass


def main() -> int:  # main is a function that returns an int type
    print("hello, world")  # print "hello, world" to stdout
    return 0  # return 0 (which is universal for being no error in execution)


# Lesson 0.1

TRUE = 1  # define


def function1() -> int:
    scoped_variable: int = 1
    return TRUE


def function2() -> int:
    scoped_variable: int = 69
    print(scoped_variable)
    return 0


def function3() -> int:
    print("hello, world")
    return 0


def main0() -> int:  # forget the trailing 0
    f1: int = function1()
    print("function1: %d" % f1)
    f2: int = function2()
    function3()
    return 0

# End of Lesson 0.1


if __name__ == "__main__":
    if current_lesson == 0:
        main0()
