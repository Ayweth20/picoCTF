### unpackme.py
**Category:** Reverse - **Points:** 100 - **Solves:** ????  
**Description:** Can you get the flag? Reverse engineer this [Python program](./unpackme.flag.py/)

**Solution:**  

First, when we open the program we can see a "payload" :

"payload = b'gAAAAABiMD04m0Z6CohVV7ozdwHqtgc2__CuAFGG8rWhZBTL0lhfzp-mhu9LYNMnMQMGO-7tEwy3DJ2Y8yjogvzyojFETwN9YEIPXTnO9F1QnkPypWTgjISGve4gcSerJMs694oKcIdKHuVaSxOg1MMNs5k9iPaBIPU7xOKQqCyhnf_f4yUvLdMcer38BqRptocJNvKlyWN8h7ikoWL0zlssxd8OJyPujMz78HZaefvUouvq6LDtPVqRBJFPgSJYf1nHpHKFa1O0zJ6UpTe6ba3PPAxCVXutNg=='"

Then we spot a variable named key_str :
key_str = 'correctstaplecorrectstaplecorrec'

This string is converted to Base64 :
key_base64 = base64.b64encode(key_str.encode())

and we can see that the program creates a Fernet encryption method with key_base64 as the key :
f = Fernet(key_base64)

to decrypt the flag we need to do a Fernet decryption and for this I used [this online tool.](https://asecuritysite.com/encryption/ferdecode)

by entering "Y29ycmVjdHN0YXBsZWNvcnJlY3RzdGFwbGVjb3JyZWM=" as the key (key_str to base64) and our payload we get :
![image](https://user-images.githubusercontent.com/90833446/160919054-2fb42e4b-5981-4292-9169-c48190209f24.png)

And here's our flag !


<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{175_chr157m45_5274ff21}
  ```
</details>
