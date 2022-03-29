### File types
**Category:** Forensics - **Points:** 100 - **Solves:** ????  
**Description:**  
This file was found among some files marked confidential but my pdf reader cannot read it, maybe yours can.  
You can download the file from [here](./Flag.pdf/)  

**Hint:**  
> Remember that some file types can contain and nest other files

**Solution:**  
To solve this challenge you need to find the flag hidden in a lot of compressed files.  
To do that, we start with a PDF file who hide a shell archive file.  
After some extraction and differents (strange) files, the flag is in ASCII code.  
We just need to convert them in hexadecimal, to find the good file.


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_3c79c5ba}
  ```
</details>

