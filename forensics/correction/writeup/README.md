# Writeup c0rR3cT10n

__by twoface__


given a png file. but you can't open it. after analyzing using hex editor, the header is wrong. 
change it to correct pNG header.

![bin-string image](https://i.imgur.com/oyDdn7v.png)

now you can see the picture. but it is only picture with black and white pixel. the correct conclusion is that,
the picture is a binary-string picture. which means black represents 0 and white represents 1. now you have
to decode the image to binary string. you can use script or any tools, but the easiest way is using this web 
https://www.dcode.fr/binary-image to decode. 

after you decode , you got bunches of binary strings. you can't manually slice them and decode them to ascii using
some web service, that's absurd (there are so many lol). the logical way is to use script to decode it. 
now copy all of those bin string to a txt file, and write a script to decode it.


__my script__ 

![bin to string script](https://i.imgur.com/Ubap27Q.png)

huwala! the bin strings are decoded to ascii encoded string. if you see clearly, near the end of the strings, you can find a url! it'll redirect you to a google drive on which you can download particular jpg file. but it seems you can't open it, can you?

![output](https://i.imgur.com/eJvddP8.png)

again, analyze the file. you notice that it has iHDR chunk, this implies the file is PNG not jpg. fix the magic bytes. Unfortunately, even after you've fixed it, it still won't open. hmm.... 

Now analyze even further, if you see the content of iHDR chunk, you'll notice something peculiar. the dimensions are set to 0 which is an invalid value. ha! this is the root of the problem. FYI, PNG uses CRC on each chunk as checksum to verify the chunk's integrity. if there are changes on the respective chunk, means that when you open the file, it will throw an "error" (or notice that the file is corrupted, i'd rather say) because the CRC doesn't match.

you now know how the CRC works. you can't manually and randomly try arbitrarily value for the dimension, 
again, that's absurd. you may find tool or script or you can even make your own to bruteforce finding the right dimension which corresponds to the correct CRC value.


__my script__ (inspired by someone on google, sorry i forget who it was).

![crc-bruteforce script](https://i.imgur.com/m0U3Isr.png)

*one might inquire, from which i got this calculation. basically, what the script does is it take the IHDR chunk (without the dimension and CRC bytes) and bruteforcing the possible dimension value which matches the CRC. recall that the picture is widescreen (16:9) and the max resolution is full hd (1920x1080).  also there are 2 possiblity for the orientation (portrait or landscape), though it doesn't matter. you can try which one works.*

After that, the script will give you the correct width or height `954` (depends on your script). in my case the width is `954` and to find the height, you'll only need to do quick math `(954 // 9) * 16` which evaluates to `1696`. Now you got the dimension value `954x1696`, change the file's dimension to the correct one.

voila! you can now open the picture.

the picture shows a pitch black sky with moon on the middle. hmm, now what? you can try using `strings` command to check any hidden printable char, etc. but in the end, you gotta play with color correction. simply use photo editor, and change the brightness. You can see the flag written in red.

![flag](https://i.imgur.com/1SC76B0.png)

**Flag**
> COMPFEST14{hHhH_th0u_4re_c0Rr3ct!_634af16261}