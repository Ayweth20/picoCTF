### rail-fence
**Category:** Crypto - **Points:** 100 - **Solves:** ????  
**Description:**  
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). 
Here is one such [cipher encrypted](./message.txt/) using the rail fence with 4 rails. Can you decrypt it?  
Put the decoded message in the picoCTF flag format, `picoCTF{decoded_message}`.

**Hint:**
> Once you've understood how the cipher works, it's best to draw it out yourself on paper.  

**Solution:**  
To solve this challenge you need to decipher the [.txt content file](./message.txt/).  
In the chall description, there is a [link](https://en.wikipedia.org/wiki/Rail_fence_cipher) who explain how to decipher the file content.  
So we can try to decipher by hand or use this website : [dcode - Rail Fence](https://www.dcode.fr/chiffre-rail-fence)  
We need to configure the options like that and the flag is deciphered automatically :  
![image](https://user-images.githubusercontent.com/91023285/160381060-dd09d9ee-515d-40d4-8ee9-21cab0bdd7ec.png)  


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}
  ```
</details>
