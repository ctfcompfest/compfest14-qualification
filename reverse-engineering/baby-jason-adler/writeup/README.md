# Writeup baby JaSon adler


we are given a file in which we can see a line of code. you can easily determined that it is a JS code (even the chall name hints it). it's a typical one-liner code with some unnecessary operations (like the modulo). the code is actually an adler32 checksum algorithm [(see more)](https://en.wikipedia.org/wiki/Adler-32).

basically, all you need to do is reverse adler32 the first half of the encrypted text. the rest doesn't matter.

__here's my script__

```javascript
enc="DàİŶƻȎɢʓˇ͂ͶϚцҫԝռןهٺ۝݀޳ߣࡐࢵऔॅসਗ੽઱ତ୛ீల಑ೈര൤ිัດ໦༩ཊཫ࿊࿺ာၠ႐ჶᄧᅘᆻሞቓዐD×ųȐʦ̱ωѰӵ՚؉ڸݐࣱࠠৈઙ୛దುൗฝ໳ྖဳᄅᇉ቙ዽᏏᒔᔮᗕᙿ᜛៲ᣃᥙ᧸᪔ᬶᰃ᳅ᵺḏṳẵἵῄ…₌⃰ↆ∝≿⌓⏙⑱┣"
enc1 = enc.slice(0, enc.length/2)
string1 = ""
for (let i = 0; i < enc1.length; i++){
	!i?string1+=String.fromCharCode(enc1[i].charCodeAt(0)-1):string1+=String.fromCharCode(enc1[i].charCodeAt(0) - enc1[i-1].charCodeAt(0));
}
console.log(string1) // COMPFEST14{4dler_ch3ccs0me_1s_f4s7er_7h4n_cRC!!_0240f11cc5}
```