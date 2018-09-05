#/usr/bin/env python3
# huffman decoder
# Usage: decoder.py key input 

import sys
import re

def huffmanDecode (dictionary, text, p):
        res = ""
        while text:
            m = re.match(p, text)
            if m == None:
                break
            res += dictionary[m.group()]+" "
            text = text[len(m.group()):]
        return res

if __name__ == "__main__": 
    huffman_dict = dict()

    # Read huffman key and create dict
    try:
        with open(sys.argv[1]) as key:
            for index, line in enumerate(key):
                if index % 2 is 1:
                    code = line.strip()
                    huffman_dict[code] = word
                elif index % 2 is 0:
                    word = line.strip()
    except (IndexError, IOError) as e:
        print("Cannot open key file!")
        print("Usage: decoder.py key input")
        sys.exit(1)
    key.close()
    
    # Decode input using dict and output decoded text
    try:
        with open(sys.argv[2]) as encoded:
            p = "|".join(huffman_dict) # join keys to regex
            for line in encoded:
                dec = huffmanDecode(huffman_dict, line.strip(), p)
                output = dec.strip()
                print(output.strip('</s>'))
    except (IndexError, IOError) as e:
        print("Cannot open input file!")
        print("Usage: decoder.py key input")
        sys.exit(1)
    encoded.close()

