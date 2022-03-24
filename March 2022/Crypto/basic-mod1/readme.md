### basic-mod1
**Category:** Crypto - **Points:** 100 - **Solves:** ????  
**Description:**  
We found this weird message being passed around on the servers, we think we have a working decrpytion scheme. Download the message [here](./March%202022/Crypto/basic-mod1/message.txt/).  
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.  
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

**Hint:**
> Do you know what mod 37 means?
> `mod 37` means modulo 37. It gives the remainder of a number after being divided by 37.  

**Solution:**  
To solve this challenge you need to decipher the flag in the [.txt file](./March%202022/Crypto/basic-mod1/message.txt/).  
In the chall description, it's explained how to decipher the file content. `0-25` is for the alphabet, `26-35` is for decimal (0 to 10) and `36` is for the underscore (`_`)  
In the .txt file, there are many numbers greater than 36.  
So we need to calculate the good values with a modulo 37. To do that I wrote a [python script](./March%202022/Crypto/basic-mod1/decipher.py/) who calculate automatically the good values and give the flag.  
You can try this python code or try to find the flag manually.

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{R0UND_N_R0UND_79C18FB3}
  ```
</details>

