### basic-mod2
**Category:** Crypto - **Points:** 100 - **Solves:** ????  
**Description:**  
A new modular challenge! Download the message [here](./March%202022/Crypto/basic-mod2/message.txt/).  
Take each number mod 41 and find the modular inverse for the result. Then map to the following character set: 1-26 are the alphabet, 27-36 are the decimal digits, and 37 is an underscore.  
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})  

**Hint:**
> Do you know what the modular inverse is?
> The inverse modulo z of x is the number, y that when multiplied by x is 1 modulo z
> It's recommended to use a tool to find the modular inverses  

**Solution:**  
To solve this challenge you need to decipher the flag in the [.txt file](./March%202022/Crypto/basic-mod2/message.txt/).  
In the chall description, it's explained how to decipher the file content. `1-26` is for the alphabet, `27-36` is for decimal (0 to 10) and `37` is for the underscore (`_`)  
In the .txt file, there are many numbers greater than 37.  
So we need to calculate the good values with a modulo 41 and reverse modulo. To do that I wrote a [python script](./March%202022/Crypto/basic-mod2/decipher.py/) who calculate automatically the good values and give the flag.  
You can try this python code or try to find the flag manually.

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{1NV3R53LY_H4RD_C680BDC1}
  ```
</details>
