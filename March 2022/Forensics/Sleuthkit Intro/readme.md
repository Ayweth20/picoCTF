### Sleuthkit Intro
**Category:** Forensics - **Points:** 100 - **Solves:** ????  
**Description:**  
Download the [disk image](./disk.img.gz) and use `mmls` on it to find the size of the Linux partition.  
Connect to the remote checker service (`nc saturn.picoctf.net 52279`) to check your answer and get the flag.  
Note: if you are using the webshell, download and extract the disk image into `/tmp` not your home directory.

**Solution:**  
To solve this challenge you need to find the image disk size to get the flag.  
In first step, we need to extract the disk image from the .gz archive (with winRAR because there is an error if we try in command line...)  
So after extract the file, we can do a `mmls disk.img` and view the size of the Linux partition :  
![image](https://user-images.githubusercontent.com/91023285/160288647-10ced5b9-a2f3-4452-8a12-5b11da776d6b.png)  
Now we have the size value, we can send them to checker service who send back the flag :  
![image](https://user-images.githubusercontent.com/91023285/160288734-28c97a87-b955-45cc-88ee-09840b3768a0.png)

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{mm15_f7w!}
  ```
</details>
