# Writeup inverse magik

You are given a file `garden_blekk` and an image file `eureka.jpg`. and some hints.

**Hints**
* you might want to find the offset of the corrupted data(s) :u

#### Solution

First, identify the file type. you can try any tool, perhaps `exiftool` or `file`, etc. By Opening file in Hex editor, we can see part of the header says `IHDR`. this implies the file is an image file. moreover it's PNG.

But even after changing the extension to `.png`, we are unable to open the file. check the hex again and compare the header hex value to png *magic number*. turns out the header is broken. change it till it matches the magic number `89 50 4E 47 0D 0A 1A 0A`.

we are now able to open the file. it shows nothing but "noiseful" graphic.
this usually means, some data on png `iDAT` is invalid or has been tampered. if you recall, the description mentioned `the power of XOR` this means we ought to do bitwise operation. then again, we don't know which data (byte offset) that has been tampered.

Now, we are given another file `eureka.jpg`, it is an image with a text inside saying "try checking \_ until \_". ok, this might indicate the byte offset, but how do we get the blank value there? If we analyze the file using binwalk we can see that it's actually an image with a hidden file inside it, Aha! now we can extract the txt file using binwalk. the txt says `202 -- 205` changing to hex we get ` 0xCA  0xCD`

those value are valid bit offset, but this tells us nothing about the original data. again, recalling to the description, `XOR`-ing any to 0 means nothing as `any XOR 0` will result that "any", so it's gotta be `XOR 1` which is the same as inverting bits. we can now see the connection. all we have to do is `XOR 1` all the bits from the given offset range above.

Huwala! we can now see the picture. it is a photo of garden. we can see the part of the flag `COMPFEST14`, but not the rest. we are stuck here, not much we can do. this leads us to a condition where we have to "play" with the image itself using photo editor, such as photoshop. after playing around, by changing the image's lightness, we get the flag. 

> COMPFEST14{welcome_2_the_mag1k_klubzz}
