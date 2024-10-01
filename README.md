[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/U2uaA5Md)
# CS151 PROGRAMMING ASSIGNMENT #1
 
* ### DESIGN DUE: 09/25/24 
  * ### Grade:  MRN 
* ### FINAL DUE: 10/09/24
  * ### Grade:  EMRN
* #### Three weeks: Because we have test in between

## I. PROBLEM:

You are creating a text adventure game!  In this game, the user gives input that affects the path of the story. You must create a game that meets the requirements in the specification below.

## II. PURPOSE OF THE ASSIGNMENT

The purpose of this assignment is to give you:  
1. Practice with input & output  
2. The opportunity to use decision-making  
3. A chance to be creative

## III. REQUIREMENTS ANALYSIS 

The first stage in your programming assignment is the requirements analysis stage.  You need to make sure you understand the below requirements for what needs to be included in your story’s decision making:

1. Your adventure game must have at least one decision for each of the following types:  
    1. Make a decision based on the value of an integer.  
    2. Make a decision based on the value of a float.  
    3. Make a decision based on the value of a string.  
2. Your adventure game must have a path with at least 2 decisions on it (e.g. I am given the option of choosing A or B. I make choice A which then lets me decide between X and Y; but if I choose B I do not get to choose between X and Y, but instead do something else).   
3. Your adventure game must have at least 1 choice that has at least 3 possible directions (for example, when they enter a number the game takes a different path if their number is <5, between 5 and 10, or > 10).  
4. Your adventure game must use at least 3 different boolean operators throughout the story.  
5. Your adventure game must have a decision where it gives the user at least two specific inputs to choose from, and does something different based on which value they input (e.g. "enter 'green', 'red', or 'yellow'").
6. Your adventure game must use something the user input in part of the output at least once (e.g., asking for their name and then outputting their name every time you address them).
7. Your study must ask for at least three user inputs, but likely you'll need more than that.

The game must make sense and have an actual story to it. It needs to be understandable. Consider that your professor will be reading the entire story.

Your game should also not just use the exact examples used above, or used in the example below.

### An Example Game

Please watch the [youtube video showing an example game](http://www.youtube.com/watch?v=x0Ksedq3Z5k). It does not show all of the requirements from above, but does demonstrate a number of them. If you are having trouble understanding what is being asked of you in this assignment, be sure to watch the video, then ask for clarification if you still have questions.

## IV. DESIGN

The second stage is to design your solution based on the requirements:

1. Write out your algorithm, including input, output, decisions, and calculations.  
    1. Be sure to indent and properly number to show when a decision is nested inside another decision.  
    2. If you have story elements that are used in multiple paths, you can label them as "story part 1," "story part 2," etc., and then reference them by that name the next time it’s used, instead of writing it all out again. However you must give your full story as part of your design. Don’t write your entire algorithm by just saying "story part X."
2. Double check that you included all of the requirements

If you are having trouble coming up with a story, think about a book or movie you enjoyed. Be inspired by its story line or characters and come up with something original.

### DESIGN SUBMISSION: 9/25/24

 * Write you design on the `Initial_design.docx` using Word and save it.
 * Push and commit from PyCharm

Your algorithm should follow the requirements of an algorithm, contain all of the requirements, and include your entire story. Everything should be planned out. **There should not be any code.**

## V. PROGRAMMING REQUIREMENTS

After your design is complete and correct, it's time to start programming and then testing:

1. Fix design issues: If there were issues with your design, either not meeting requirements or in the format, fix that before you start writing your code.
2. Implementation: Write your program following the requirements and based on your design.  
    1. Follow good usability/HCI principles in your input and output (for instance, make it clear the type of input you are asking for).  
    2. Remember to state the purpose of the program.  
3. Testing: Make sure it works correctly; give it sample input, and check that the output is correct.  
    1. Create test cases where each test case is a separate path through your program. You do not need to put the full output in the test case, just make it clear what part of the output is there.  Note that if you have a particularly large program that results in a large number of control paths, you only need to list 10 test cases. If you have fewer than 10 paths through your program, then you should list one test case for each path.
    2. Test that you can get through each path correctly by running your code using the output. If it doesn’t give the expected output, find the error and fix it. 

## VII. ASSIGNMENT REMINDERS

Follow the programming assignment requirements document for comments, formatting, etc.

## VIII. FINAL SUBMISSION due 10/9
### What to Submit in GitHub:

1. Completed `main.py` file  
2. `Initial_design.docx`
3. `Final_design.docx`
4. An Excel file with your test cases.  
    - Edit the `test_cases.xlsx` file with Excel software 
    - If it can open then ok. Otherwise
      - Right click on `test_cases.xlsx` -> Open In -> Associated Application
5. `Reflection.docx` -> Reflection of the assignment


**As a reminder, reflections count toward your participation grade.**

Type the Reflection INSIDE the respective Word file and addressing the following questions:

 - Objective:
   - What were you supposed to learn/accomplish?

 - Procedure:
   - What steps were followed and what techniques did you use to solve the problem?
   - What were the Key concepts explored?

 - Results:
   - Did your results match what you expected to get? 
   - Did you try using various test cases, or extreme test cases?
  
 - Reflection:
   - What challenges did you encounter? 
   - How did you follow the first 3 rules of programming?
   - Did you overcome them, and how? 
   - Any key takeaways? 
   - Do you think you learned what you were supposed to learn for this lab? 
   - What was it like working by yourself?
   
***Remember to commit and push your GitHub project.***