# Signal Handling in Python

Signal handling in Python allows programs to respond to specific signals sent by the operating system. These signals, like interruptions or terminations, are often used to control or manage running processes. Signals help you build programs that can:

- Gracefully exit when an interrupt (like pressing CTRL+C) is received.
- Pause and resume based on specific conditions.
- Clean up resources when exiting due to unexpected events.

Python's signal module provides the functionality for managing these signals. The two primary concepts here are signals and handlers.

In this section, we’ll explore how to handle signals, create interrupt-safe programs, and control program behavior based on specific signals.

## Key Concepts

- **Signals**: What they are and why they’re used (e.g., `SIGINT`, `SIGTERM`).
- **Signal Handling**: How to use Python’s `signal` module to manage and respond to signals.
- **Graceful Shutdowns**: Ensuring proper closure of resources during program interruptions.
- **Interrupt-Safe Programs**: Using signals to pause or save program progress.

## Key Signals in Python
Here are some commonly used signals:

- **SIGINT**: Sent when you press CTRL+C. Used to interrupt a process.
- **SIGTERM**: Sent to terminate a process. Unlike SIGINT, this is a standard way for processes to end.
- **SIGHUP**: Sent when the controlling terminal is closed or a configuration reload is required.
- **SIGUSR1** and **SIGUSR2**: Custom signals for user-defined purposes.

## Interview Questions

1. **Basics of Signal Handling**
   - **Q1**: How would you implement a program that gracefully stops processing when the user presses `CTRL+C`? Why might this be useful?
   - **Q2**: Explain the difference between `SIGINT` and `SIGTERM` signals. How would you handle each in Python?

2. **Advanced Signal Management**
   - **Q3**: How would you use signals in a multithreaded Python application?
   - **Q4**: Describe a scenario where handling `SIGHUP` or `SIGUSR1` might be helpful for a server process.

## Exercises

1. **Graceful Shutdown with SIGINT**
   - Create a program that starts a timer and counts every second. When `CTRL+C` (SIGINT) is pressed, it should print the total elapsed time before exiting.

2. **Handling Long-Running Processes**
   - Write a Python script that simulates a long-running data processing job. Use signals to allow the program to save its progress and exit gracefully when interrupted.

3. **Custom Signal Handlers**
   - Create a program that listens for `SIGUSR1` and prints "Received custom signal" when detected. Use `kill` command in another terminal to send `SIGUSR1` and observe the program’s response.

4. **Advanced Signal Processing**
   - Implement a Python program that performs file processing. It should automatically pause on receiving `SIGTSTP` and resume on `SIGCONT` signals, allowing manual control over execution.

## Code Samples

For sample solutions and code references, check the [code_samples](code_samples/) folder in this directory.

---

## Additional Resources

- [Python’s `signal` Module](https://docs.python.org/3/library/signal.html)
- [Graceful Shutdowns with Signals](https://realpython.com/python-signal-handling/)

Master these questions and exercises to confidently manage signal handling in Python and build resilient applications.
