### Fresh Java
**Category:** Reverse - **Points:** 200 - **Solves:** ????  
**Description:** Can you get the flag? Reverse engineer this [Java program](./KeygenMe.class).  

**Hint:**
> Use a decompiler for Java!  

**Solution:**  
To solve this challenge you need to decompile the Java program.  
So to that, I found a [website](https://jdec.app/) who decompile easily the program.  
When the program is decompiled, we can see his content :  
![image](https://user-images.githubusercontent.com/91023285/160241960-c1c90b60-a68f-475e-bbe0-03b38c20025c.png)  
Now the task is to range the datas in ascending order (with `charAt(x)` parameter).  
At the end, the flag is find :  
![image](https://user-images.githubusercontent.com/91023285/160242196-d37f63cc-3c51-4736-a55b-5b4269308528.png)


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{700l1ng_r3qu1r3d_738cac89}
  ```
</details>
