# Assignment No. 1 – CLO1 Student Support Rule Engine

## Program Description

The Student Support Rule Engine is a command-line Python program that validates student information and assigns a support-priority category based on attendance, assignment average, and missed submissions. It then displays an advisory message for the student.

## Support-Priority Rules

1. **High priority**

   * Attendance is below 60%, **OR**
   * Missed submissions are 4 or more.

2. **Moderate priority**

   * Attendance is below 75%, **OR**
   * Assignment average is below 60%, **OR**
   * Missed submissions are 2 or more.

3. **Routine monitoring**

   * If none of the above conditions are met.

## Submitted Files

### `support_engine.py`

Contains the main program and functions for:

* Reading and validating floating-point input.
* Reading and validating integer input.
* Classifying the student's support priority.
* Generating the advisory message.
* Running the program through the `main()` function.

### `test_support_engine.py`

Contains assertions to test the support-priority rules using normal and boundary cases.

### `README.md`

Contains the assignment description, support rules, file descriptions, run commands, test command, and known limitations.

## How to Run the Program

Open the `Assignment_01` folder in the terminal and run:

```bash
uv run python support_engine.py
```

## How to Run the Tests

Run:

```bash
uv run python test_support_engine.py
```

If all assertions pass, the program displays:

```text
All tests passed successfully.
```

## Known Limitations

1. The program uses fixed support-priority rules and does not learn or adapt from student data.
2. The program only considers three student indicators: attendance, assignment average, and missed submissions.
3. The program does not permanently store student records or previous results.
4. The program is command-line based and does not provide a graphical user interface.
