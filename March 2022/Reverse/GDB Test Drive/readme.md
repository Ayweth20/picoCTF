### GDB Test Drive
**Category:** Reverse - **Points:** 100 - **Solves:** ????  
**Description:** Can you get the flag? Download this [binary](./gdbme).  
Here's the test drive instructions:
```
$ chmod +x gdbme
$ gdb gdbme
(gdb) layout asm
(gdb) break *(main+99)
(gdb) run
(gdb) jump *(main+104)
```

**Solution:**  
To solve this challenge you need to find the flag.  
This chall is very easy, because we just need to execute the given commands...  
So at the last command, the flag is return in our terminal :  
![image](https://user-images.githubusercontent.com/91023285/160236202-e1786696-35d4-4157-910f-fd1a857a3843.png)


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{d3bugg3r_dr1v3_197c378a}
  ```
</details>
