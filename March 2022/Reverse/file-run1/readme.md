### file-run1
**Category:** Reverse - **Points:** 100 - **Solves:** ????  
**Description:** A program has been provided to you, what happens if you try to run it on the command line? Download the program [here](./run).

**Hint:**
> To run the program at all, you must make it executable (i.e. `$ chmod +x run`)  
> Try running it by adding a '.' in front of the path to the file (i.e. `$ ./run`)  

**Solution:**  
To solve this challenge you need to reverse the program to find the flag.  
The file haven't extension, so we try to find the filetype with the `file` command :  
![image](https://user-images.githubusercontent.com/91023285/160232922-71415d0b-e997-414e-ae99-d7d52d88662b.png)  
Ok, it's an *ELF 64-bit LSB pie executable* file.  
Now we can try the second command (who I use very often) for reverse : `strings` :  
![image](https://user-images.githubusercontent.com/91023285/160233062-8aa1153b-be35-40ea-9e46-c9cc094a4a09.png)  
And here the flag is displayed in the differents strings.

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{U51N6_Y0Ur_F1r57_F113_9bc52b6b}
  ```
</details>
