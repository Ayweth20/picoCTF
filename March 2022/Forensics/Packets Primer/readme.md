### Packets Primer
**Category:** Forensics - **Points:** 100 - **Solves:** ????  
**Description:** Download the [packet capture](./network-dump.flag.pcap) file and use packet analysis software to find the flag.  
**Hint:**  
> Wireshark, if you can install and use it, is probably the most beginner friendly packet analysis software product.

**Solution:**  
To solve this challenge you need to find the flag in the .pcap datas.  
To find the flag, we just need to search them into all datas with Wireshark.  
So to do that, we need to "Expand All" datas and analyze them.  
After some searches, we can see that there is a "Datas" tab in the 4th packet :  
![image](https://user-images.githubusercontent.com/91023285/160286656-2012ba69-4d91-4362-8b3c-e513be25706b.png)

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{p4ck37_5h4rk_ceccaa7f}
  ```
</details>
