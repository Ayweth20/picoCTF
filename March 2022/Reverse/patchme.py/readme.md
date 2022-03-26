### patchme.py
**Category:** Reverse - **Points:** 100 - **Solves:** ????  
**Description:** Can you get the flag? Run this [Python program](./patchme.flag.py/) in the same directory as this [encrypted flag](./flag.txt.enc/).  

**Solution:**  
To solve this challenge you need to find the good password to decode the encrypted file.  
In first step we analyze the python program to see how he work and what he's doing.  
So we can see that the user need to enter a password to decode the file :  
![image](https://user-images.githubusercontent.com/91023285/160236910-77c6c5c1-576a-46fc-8f58-bebe971c8783.png)  
The password is visible in the script so it's very easy to bypass them : `ak98-=90adfjhgj321sleuth9000`  
When the password is send, the script decode the file and send the flag :  
![image](https://user-images.githubusercontent.com/91023285/160236997-5e5af8e5-06c1-42ca-b6a9-b46400848b14.png)


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{p47ch1ng_l1f3_h4ck_c4a4688b}
  ```
</details>
