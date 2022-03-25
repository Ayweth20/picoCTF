### transposition-trial
**Category:** Crypto - **Points:** 100 - **Solves:** ????  
**Description:**  
Our data got corrupted on the way here. Luckily, nothing got replaced, but every block of 3 got scrambled around! The first word seems to be three letters long, maybe you can use that to recover the rest of the message.  
Download the corrupted message [here](./transposition-trial/message.txt/).

**Hint:**
> Split the message up into blocks of 3 and see how the first block is scrambled  

**Solution:**  
To solve this challenge you need to rearrange the [.txt file](./March%202022/Crypto/transposition-trial/message.txt/) content.  
Like is say in the hint, we need to split the message into blocks of 3 characters.  
So to do that, I wrote a [python script](./March%202022/Crypto/transposition-trial/script.py/) who split and rearrange the content to find the flag.  

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{7R4N5P051N6_15_3XP3N51V3_56E6924A}
  ```
</details>
