### Bbbbloat
**Category:** Reverse - **Points:** 300 - **Solves:** ????  
**Description:** Can you get the flag? Reverse engineer this [binary](./bbbbloat/).

**Solution:**  

So like any reverse chall I start by using the "file" command on the binary which tells us that this is an ELF 64 bit executable :
![image](https://user-images.githubusercontent.com/90833446/160920659-6cc56edc-df90-46ba-b586-cfdab37264c2.png)

But the binary is stripped so any attempts to use gdb on it were unsuccessful.

I then executed the binary to see what it was doing exactly and was prompted by this :
![image](https://user-images.githubusercontent.com/90833446/160921157-4ecfa74d-599c-4873-ac2c-37cebf031530.png)

So we are looking for it's favorite number...

I booted up IDA and went straight to the .main of the binary and found something interesting right away : 
![image](https://user-images.githubusercontent.com/90833446/160921394-f253cecc-5fbd-4492-b46b-7e024e9c03a5.png)

On this last line I highlighted we can see that the bianry compares the input to "86187h" which is equal to "549255"

So I guess we got it's favorite number then, let's try it out!

![image](https://user-images.githubusercontent.com/91023285/161246322-0b830d5a-454d-4332-b776-61c721135544.png)

And here's our flag !

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{cu7_7h3_bl047_36dd316a}
  ```
</details>
