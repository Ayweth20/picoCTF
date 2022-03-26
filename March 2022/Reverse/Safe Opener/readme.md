### Safe Opener
**Category:** Reverse - **Points:** 100 - **Solves:** ????  
**Description:** Can you open this safe? I forgot the key to my safe but this [program](./SafeOpener.java/) is supposed to help me with retrieving the lost key. Can you help me unlock my safe?  
Put the password you recover into the picoCTF flag format like: `picoCTF{password}`

**Solution:**  
To solve this challenge you need to find the key.  
If we analyze the source code of the Java program, we can see there is a line `String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";` who contain interesting infos.  
![image](https://user-images.githubusercontent.com/91023285/160233700-c283c5ab-f9ad-469b-a4dc-9dfacf3efdc9.png)  
We supposed that the key was encoded in Base64, so we go on a [Base64 decode](https://www.base64decode.org/) and the password is convert instantly.  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
  ```
</details>
