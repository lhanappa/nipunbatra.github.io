1. Write a simple hello world program which uses multiple threads, each displaying its unique number/id. Run this program multiple times to show that the ordering between different threads can be different on different runs.

**Bonus** Use `pstree`, `ps`, `top` to dig more information about these threads. You may need to add some delays in the code to be able to see the results of these commands.

2. Extend the above program to use `join` to ensure a specific thread ordering.

**Bonus** Use `pstree`, `ps`, `top` along with watch to see how more threads are getting created.

3. Write a multi-threaded program which shares a variable count across multiple threads. Increment the variable in each thread for a given number of times in a loop. Use `objtool` to disassemble the code and find the critical section.

4. Write a multi-threaded program with 2 threads to add the numbers in a large array. The first thread adds the first half elements, the second thread adds the second half elements. Also, write a non-threaded program to compute the result. Do you get the same answer? Do the two threads operate on the same shared data? Use `objtool` to disassemble the code and find out more.

**Bonus** Vary the number of threads and compute time v/s number of threads. Vary the size of the array now to see if more threads means more performance.

5. Use load-store to implement a basic version of a lock. See Book 28.6. Re-run question 3 now with the lock before the critical section and unlocking after the critical section. Run the program and confirm that this lock still does not solve the issue of mutual exclusion. Use `objtool` to disassemble the code and find the critical section.

**Bonus** Compute the time spent spinning on the CPU waiting for the other thread to release the lock.

6. Use pthread mutex to write a fully correct working version of Question 3. Use `objtool` to disassemble the code and find out more.

7. Questions 1-5 from the textbook Chapter 27 (Threads API).

**Bonus** Study multi-processing and multi-threading in Python. Use `pool` to parallelize image processing on a large batch of images. Do some simple operation like batch convert from colour to grayscale. 
