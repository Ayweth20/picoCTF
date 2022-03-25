### credstuff
**Category:** Crypto - **Points:** 100 - **Solves:** ????  
**Description:**  
We found a leak of a blackmarket website's login credentials. Can you find the password of the user `cultiris` and successfully decrypt it? Download the leak [here](./leak.tar/).  
The first user in `usernames.txt` corresponds to the first password in `passwords.txt`. The second user corresponds to the second password, and so on.  

**Hint:**
> Maybe other passwords will have hints about the leak? 

**Solution:**  
To solve this challenge you need to find the `cultiris` password and decipher the flag.
In first step, we need to extract the files of the .tar archive. To do that, we can use WinRAR or an [online tool](https://www.ezyzip.com/ouvrir-le-fichier-tar-en-ligne.html).  
So when we extract the files (`usernames.txt` & `passwords.txt`) we can view all datas. To associate the username with his password we can insert these datas in Excel like that :  
![image](https://user-images.githubusercontent.com/91023285/160170924-9de877eb-c06f-464d-826a-676ba44e1cf2.png)  
We need to find the `cultiris` password : `cvpbPGS{P7e1S_54I35_71Z3}`.  
To decipher the flag, we need to use a [ROT-13 tool](https://www.dcode.fr/chiffre-rot-13) and the flag is deciphered automatically.

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{C7r1F_54V35_71M3}
  ```
</details>
