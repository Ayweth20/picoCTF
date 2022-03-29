### Enhance!
**Category:** Forensics - **Points:** 400 - **Solves:** ????  
**Description:**  
SOS, someone is torrenting on our network.  
One of your colleagues has been using torrent to download some files on the company’s network. Can you identify the file(s) that were downloaded?  
The file name will be the flag, like `picoCTF{filename}`. [Captured traffic](.//).

**Hints:**  
> Download and open the file with a packet analyzer like [Wireshark](https://www.wireshark.org/).
> You may want to enable BitTorrent protocol (BT-DHT, etc.) on Wireshark. Analyze -> Enabled Protocols
> Try to understand peers, leechers and seeds. [Article](https://www.techworm.net/2017/03/seeds-peers-leechers-torrents-language.html)
> The file name ends with `.iso`

**Solution:**  


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{}
  ```
</details>
