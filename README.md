# Assignment 04: Loop exercises


**Due: Thursday 03/05 by Midnight**

*Note: Homework Assignment 4 should be completed individually.*

# Objective
You will complete three functions with loops that accomplish 3 specific tasks. In addition, you need to fill out two functions of your own design.

This homework has no "theme", it's just three different exercises and two self-designed functions.

For this homework you need to complete four tasks:

  1. Fill out the `check_text` function.
  2. Fill out the `check_greater` function.
  3. Fill out the `get_special_numbers` function.
  4. Design and fill out the `my_for_loop` function as well as the `my_while_loop` function.

So you understand what we are shooting for, an example run looks like this:
```
Give me a sentence: No secret word here
Try again
Give me a sentence: using the word Dog
You used the word "dog" or the word "Dog"!
Give me a first integer: 2
Give me a second integer: 2
Try again
Give me a first integer: 3
Give me a second integer: 5
Second is Greater
Done
3
9
21
27
33
39
Give me a string: hello
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel
Choose one option: a, b, or c: a
Choose one option: a, b, or c: d
try again
Choose one option: a, b, or c: b
Goodbye
The End
```

You only need to complete the functions. The `main` is provided for you and it takes care of all the printouts except the success or error messages we require you to print (more on that below).

You need to add the DocStrings below every function as well as small but informative comments explaining your logic.

# A Note on passing the tests

Any tests are very strict with respect to the format of requested prompts and printouts so pay attention to exactly what is requested and replicate it as exactly as possible.


# Theory reminders

## The keyword `break`

If you use the keyword `break` inside a loop, this will immediately terminate the loop and the execution will continue in the step immediately following the loop (if there is one).


## The keyword `continue`

If you use the keyword `continue` inside a loop, this will immediately jump to the next iteration of the loop, skipping anything not executed so far in the body of the loop and jumping to the top again. If inside a for loop, this will mean jumping to the next iteration (and the next iterator value).

## The global variable `secret_word`

The variable `secret_word` is declred at the top and outside any function. This makes it a member of the **global context** and visible to all functions.

  * This variable is initialized with the provided word "food" but can be set to any secret word. Testing coes not depend on any particular word, so feel free to change it for testing.


## Task 1: check_text

### define the function

The objective of this function is to read read text from the user and then check three conditions.

  * If the user inputs text that uses the secret word `secret_word`, then the function should print out the following message: `You used the secret word!`. Note that the message shown is what should appear on the terminal, it's not necessarily how you construct the string that you print.
  * If the user inputs text that uses the word `dog` or the word `Dog`, then the function should print out the following message: `You used the word "dog" or the word "Dog"!`. Note that the message shown is what should appear on the terminal, it's not necessarily how you construct the string that you print. In particular, you will need to print double quotes inside a string, which will require that you escape them using this notation: `\"` every time you wish to place them inside a string.
  * If the user inputs text that does not use the secret word or the words `dog` or `Dog`, it should print the message `Try again` and it should run the whole body of the loop again. This is shown in the example output shown above.

### Notes:

This function does not need input parameters and does not return anything.
Also, you do not need to do input checking. If the user inputs a bad input (like a float instead of an int), that's on them. In this homework, just concentrate on the stated objectives.

## Task 2: check_greater

### define the function

The purpose of check_greater function is to get two integers from te user (you decide what prompts to use), and compare them. There are three cases of what can happen:

  * If the first integer is greater than the second, your function should print `First is Greater`.
  * If the second integer is greater than the first, your function should print `Second is Greater`.
  * If the integers are equal, your function should print `Try again` and repeat the body of the loop. This is shown in the example output shown above.

### Notes:

This function does not need input parameters and does not return anything.
Also, you do not need to do input checking. If the user inputs a bad input (like a float instead of an int), that's on them. In this homework, just concentrate on the stated objectives.


## Task 3: get_special_numbers

### define the function

The purpose of get_special_numbers function is to use a for loop to examine each and every number between 1 and 40 and either print it (each in its own line) or skip it, depending on three criteria.

  * If the number is even, it should be discarded
  * If the number is not a mltiple of 3, it should be discarded.
  * If the number is a multiple of 5, it should be discarded.
  * Otherwise, you should print the value (as an integer)

### Notes:

This function does not need input parameters and does not return anything.
Also, you do not need to do input checking. If the user inputs a bad input (like a float instead of an int), that's on them. In this homework, just concentrate on the stated objectives.

## Task 4: my_for_loop and my_while_loop functions

These are self-desig functions that take no inputs.

### my_for_loop

The function has to ask for a string from the user. If the string length (use the `len` function) is not in the range [2,5] (between 2 and 5 inclusive), or if the string has spaces, then the function should immediately return.
If the word is of a valid length, then the function should print one of the following things:
  * if the letter is a vowel, it should print: `"letter <let> is a vowel"` (where `<let>` is the letter in question)
  * if the letter is a consonant, it should print: `"letter <let> is a consonant"` (where `<let>` is the letter in question)

### my_while_loop
The function should offer the user three choices, where the user needs to input one of three letters: `a`, `b`, or `c`.
  * if the user selects `a`, the menu should repeat.
  * if the user selects `b`, the function should print `"Goodbye"` and return.
  * if the user selects `c`, the program should exit immediately.
  * if any other letter is selected, the loop should print `"try again"` and the menu should repeat.

# Output Examples


## A: Secret word used, first number greater, "hello", a, d, b

```
Give me a sentence: I love food
You used the secret word!
Give me a first integer: 4
Give me a second integer: 3
First is Greater
Done
3
9
21
27
33
39
Give me a string: hello
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel
Choose one option: a, b, or c: a
Choose one option: a, b, or c: d
try again
Choose one option: a, b, or c: b
Goodbye
The End
```

### B: word `dog` used, second number greater, "hello", a, d, b

```
Give me a sentence: my dog is better than yours
You used the word "dog" or the word "Dog"!
Give me a first integer: 2
Give me a second integer: 7
Second is Greater
Done
3
9
21
27
33
39
Give me a string: hello
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel
Choose one option: a, b, or c: a
Choose one option: a, b, or c: d
try again
Choose one option: a, b, or c: b
Goodbye
The End
```

### C: word `Dog` used, first number greater, "hello", a, d, b

```
Give me a sentence: Dogma is a so-so movie
You used the word "dog" or the word "Dog"!
Give me a first integer: 7
Give me a second integer: 1
First is Greater
Done
3
9
21
27
33
39
Give me a string: hello
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel
Choose one option: a, b, or c: a
Choose one option: a, b, or c: d
try again
Choose one option: a, b, or c: b
Goodbye
The End
```

### D: Try again first, then `Dog`, then numbers equal (twice), Second greater, "hello", a, d, b

```
Give me a sentence: no secret words here
Try again
Give me a sentence: Yak is a Dog with capital D
You used the word "dog" or the word "Dog"!
Give me a first integer: 3
Give me a second integer: 3
Try again
Give me a first integer: 4
Give me a second integer: 4
Try again
Give me a first integer: 5
Give me a second integer: 8
Second is Greater
Done
3
9
21
27
33
39
Give me a string: hello
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel
Choose one option: a, b, or c: a
Choose one option: a, b, or c: d
try again
Choose one option: a, b, or c: b
Goodbye
The End
```

### E: word `Dog` used, first number greater, "hi there"

```
Give me a sentence: Dogma is a so-so movie
You used the word "dog" or the word "Dog"!
Give me a first integer: 7
Give me a second integer: 1
First is Greater
Done
3
9
21
27
33
39
Give me a string: hi there
```

### F: word `Dog` used, first number greater, "hello", a, d, c

```
Give me a sentence: Dogma is a so-so movie
You used the word "dog" or the word "Dog"!
Give me a first integer: 7
Give me a second integer: 1
First is Greater
Done
3
9
21
27
33
39
Give me a string: hello
h is a consonant
e is a vowel
l is a consonant
l is a consonant
o is a vowel
Choose one option: a, b, or c: a
Choose one option: a, b, or c: d
try again
Choose one option: a, b, or c: c
```

# Grading


## Grading criteria:

### General
The submission:

  * **IMPORTANT**: If your code does not compile, you get 0% of your grade so make sure you run your code often (to avoid syntax or runtime errors) and you always have it in a "running" state, even if it does not get the desired results.
  * Your grade will be the percentage of tests you pass.
  * You have any imports on the top, you added Docstrings (or -5%),
  * You added a few small but informative comments (or -5%)

  ### Operations

  The program:

    * Passes all 14 tests (or lose ~7% per missed test).

  Note: before submitting, you should check all the boxes that you actually completed like this:

    - [x] this is a checked box

  The submission (check boxes after you complete each step):

    - [ ] you added your name to the top comments of the python file
    - [ ] runs without syntax errors (or -50%)
    - [ ] adds a few small but informative comments (or -5%)
    - [ ] adds docstrings to each function (or -5%)
    - [ ] Passes all tests (or lose points per missed test). If you do not pass all tests, do not check this box
    - [ ] You checked the correct boxes

## Submitting

Submit to your GitHub repositories before the due date/time.
