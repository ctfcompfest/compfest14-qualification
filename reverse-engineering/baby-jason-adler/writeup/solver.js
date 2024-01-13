enc="DàİŶƻȎɢʓˇ͂ͶϚцҫԝռןهٺ۝݀޳ߣࡐࢵऔॅসਗ੽઱ତ୛ீల಑ೈര൤ිัດ໦༩ཊཫ࿊࿺ာၠ႐ჶᄧᅘᆻሞቓዐD×ųȐʦ̱ωѰӵ՚؉ڸݐࣱࠠৈઙ୛దುൗฝ໳ྖဳᄅᇉ቙ዽᏏᒔᔮᗕᙿ᜛៲ᣃᥙ᧸᪔ᬶᰃ᳅ᵺḏṳẵἵῄ…₌⃰ↆ∝≿⌓⏙⑱┣"
enc1 = enc.slice(0, enc.length/2)
string1 = ""
for (let i = 0; i < enc1.length; i++){
	!i?string1+=String.fromCharCode(enc1[i].charCodeAt(0)-1):string1+=String.fromCharCode(enc1[i].charCodeAt(0) - enc1[i-1].charCodeAt(0));
}
console.log(string1)