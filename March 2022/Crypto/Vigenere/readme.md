### Vigenere
**Category:** Crypto - **Points:** 100 - **Solves:** ????  
**Description:** Can you decrypt this [message](./cipher.txt/)? Decrypt this message using this key **"CYLAB"**.

**Hint:**
> [https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)  

**Solution:**  
To solve this challenge you need to decode the flag in the [.txt file](./cipher.txt/) with a [Vigenere decode tool](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('CYLAB')&input=cmdub0RWRHtPME5VX1dRM19HMUczTzNUM19BMUFIM1NfY2M4MjI3MmJ9).  
With the [Cyberchef](https://gchq.github.io/CyberChef/#recipe=Vigen%C3%A8re_Decode('CYLAB')&input=cmdub0RWRHtPME5VX1dRM19HMUczTzNUM19BMUFIM1NfY2M4MjI3MmJ9) tool, the decoding task is very easy.  
We just need to write the key and the content in the good places, like that :  
![image](https://user-images.githubusercontent.com/91023285/160176644-3be6690b-5ded-4300-b7df-c788405cd00c.png)


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}
  ```
</details>
