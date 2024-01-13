def compress(fname_in, fname_out):
    with open(fname_in, 'rb') as fin:
        _input = list(map(chr, fin.read()))

    d = {chr(i): i for i in range(256)}

    i = 256
    buffer = ""
    compressed = []
    for c in _input:
        buffer += c
        if buffer not in d:
            compressed.append(d[buffer[:-1]])
            d[buffer] = i
            buffer = c
            i += 1
    else:
        compressed.append(d[buffer])

    with open(fname_out, 'wb') as fout:
        for c in compressed:
            fout.write(c.to_bytes(2, 'big'))

def decompress(fname_in, fname_out):
    with open(fname_in, 'rb') as fin:
        compressed = fin.read()
        compressed = [int.from_bytes(compressed[i:i+2], 'big') for i in range(0, len(compressed), 2)]

    d = {i:bytes([i]) for i in range(256)}

    dict_index = 256
    buffer, decompressed = b"", b""
    for i in compressed:
        if i not in d:
            d[i] = buffer + bytes([buffer[0]])

        if buffer != b"":
            d[dict_index] = buffer + bytes([d[i][0]])
            dict_index += 1

        decompressed += d[i]
        buffer = d[i]
        
    with open(fname_out, 'wb') as fout:
        fout.write(bytes(decompressed))