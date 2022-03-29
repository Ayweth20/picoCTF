### SideChannel
**Category:** Forensics - **Points:** 400 - **Solves:** ????  
**Description:**  
There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?  
Download the PIN checker program here [pin_checker](./pin_checker/)  
Once you've figured out the PIN (and gotten the checker program to accept it), connect to the master server using `nc saturn.picoctf.net 55824` and provide it the PIN to get your flag.


**Hints:**  
> Read about "timing-based side-channel attacks."  
> Attempting to reverse-engineer or exploit the binary won't help you, you can figure out the PIN just by interacting with it and measuring certain properties about it.  
> Don't run your attacks against the master server, it is secured against them. The PIN code you get from the pin_checker binary is the same as the one for the master server.  

**Solution:**  


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{}
  ```
</details>
