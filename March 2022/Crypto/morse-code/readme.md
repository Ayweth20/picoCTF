### morse-code
**Category:** Crypto - **Points:** 100 - **Solves:** ????  
**Description:**  
Morse code is well known. Can you decrypt this? Download the file [here](./morse_chal.wav/).  
Wrap your answer with picoCTF{}, put underscores in place of pauses, and use **all lowercase**.  

**Hint:**
> Audacity is a really good program to analyze morse code audio.  

**Solution:**  
To solve this challenge you need to decode the morse code.  
In the hint, the organizers recommand to use Audacity. But I don't know how to decode morse with Audacity...  
So I found a webapp who decode our morse file : [morsecode.world](https://morsecode.world/international/decoder/audio-decoder-adaptive.html)  
We just need to upload our file and the flag is decode after about 5 seconds :  
![image](https://user-images.githubusercontent.com/91023285/160433116-386b60ca-a6a5-4cd6-83ff-5d23c41f505b.png)  
Now we have the flag in uppercase but the website want them in lowercase.

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{wh47_h47h_90d_w20u9h7}
  ```
</details>

