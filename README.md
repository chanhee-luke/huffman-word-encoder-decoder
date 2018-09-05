# Word-level Huffman encoder/decoder
Luke Song

# Overview
Encodes text file into a word-level huffman coding. Key file is also produced from the encoder.
Decoder decodes a huffman coded bitstream from the key file.

# Usage
    gcc encoder.c -o encoder
    ./encoder input_text output_name key_text_name
    python decoder.py key_text encoded_text
