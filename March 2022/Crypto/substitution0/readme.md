### substitution0
**Category:** Crypto - **Points:** 100 - **Solves:** ????  
**Description:**  
A message has come in but it seems to be all scrambled. Luckily it seems to have the key at the beginning. Can you crack this substitution cipher?  
Download the message [here](./message.txt/).  

**Hint:**
> Try a frequency attack. An online tool might help.  

**Solution:**  


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{}
  ```
</details>

At first sight of our message.txt, we can guess 3 different parts : 

The first one is `EKSZJTCMXOQUDYLFABGPHNRVIW` . After a brief analysis, we notice that this string is an **alphabet **: there is 26 characters, all different.

The second part is an unreadable text, that has the structure of a real text, but the letters are obviously the wrong one.

The last one contains the flag wrapper `fxslSPT{5HK5717H710Y_3N0UH710Y_59533E2J}`. We'll keep it until the end.



As we know this challenge is about substitution, a little search (https://en.wikipedia.org/wiki/Substitution_cipher), makes us understand what the alphabet in the first part is about : each letter of our English alphabet is replaced by another of our new alphabet.

Explanation : 

- English alphabet : `ABCDEFGHIJKLMNOPQRSTUVWXYZ`
- Our given alphabet : `EKSZJTCMXOQUDYLFABGPHNRVIW`

For each letter in the message written in our given alphabet, it will be replaced by it's index in the english alphabet. Every `e` will be `a`, every `k` will be `b`.....



We can easily do it letter by letter using a paper, but it'll be faster using a program.

We therefore made one, check it !

