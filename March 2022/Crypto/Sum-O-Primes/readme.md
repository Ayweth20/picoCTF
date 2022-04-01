### Sum-O-Primes
**Category:** Crypto - **Points:** 400 - **Solves:** ????  
**Description:**  
We have so much faith in RSA we give you not just the product of the primes, but their sum as well!  
- [gen.py](./gen.py/)
- [output.txt](./output.txt/)

**Hint:**
> I love squares :)  

**Solution:**  
In order to understand this challenge, you have to know how to deal with RSA challenges.

To get the flag, we need three particular values : `e`,`p`, `q` and `c`.

In our output.txt, `c` is given as `x` and `n`, which is `p`*`q`.

By reading the python script, we learn that :

`x = p+q`.

`e = 65537`

As we said, our goal is to find `p` and `q`.

We now have two equations with two unknown factors:

- x = p+q
- n = p.q

After some quick maths and a second degree equation, we get 

- p = (-2.x.sqrt(x²-4.n))/2
- q = x-p

Now that we have all variables needed, we can decipher the message using [this site](https://www.dcode.fr/rsa-cipher)

<details>
  <summary>:triangular_flag_on_post: FLAG</summary>

  ```
  picoCTF{}
  ```
</details>
