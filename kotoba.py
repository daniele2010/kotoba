from hashlib import sha256
import hashlib
import math
import base64
import gzip

def calculate_list_faces(faces: int) -> tuple:
   base = 2 ** int(math.log(faces, 2))
   throws = math.ceil(math.log(2048, base))
   max_valid = (2048 // (base ** (throws - 1))) - 1
   return (throws, base, max_valid)

def calculate_mnemonics(nwords: int) -> tuple:
   total_bits = nwords * 11
   entropy_bits_length = total_bits * 32 // 33
   checksum_length = total_bits - entropy_bits_length
   return (entropy_bits_length, checksum_length)


def get_word_value(throws: int, base: int, max_valid: int) -> int:
    word_value = 0
    for t in range(throws):
        if t == 0:
            print(f'First throw, valid faces: {list(range(1, max_valid + 2))}')
        else:
            print(f'Valid faces: {list(range(1, base + 1))}')
        throw = int(input(f'Insert throw {t + 1} result: ') or 0) - 1
        if (throw < 0 or throw >= base) or (t == 0 and (throw < 0 or throw > max_valid)):
            raise IndexError
        word_value += throw * base**(throws - t - 1)
    return word_value

def generate_mnemonic(wordlist: list) -> str:
    faces = int(input('Insert the number of faces your thing have:\n') or -1)
    if faces < 2:
        print('Invalid number of faces')
        exit()
    throws, base, max_valid = calculate_list_faces(faces)

    nwords = int(input('Do you want a seed phrase with 12, 15, 18, 21 or 24 words?\n') or -1)
    if nwords not in [12, 15, 18, 21, 24]:
        print('Invalid number of words')
        exit()
    entropy_bits_length, checksum_length = calculate_mnemonics(nwords)

    words = []
    for i in range(nwords):
        while True:
            try:
                word_value = get_word_value(throws, base, max_valid)
                words.append(word_value)
                if i + 1 != nwords:
                    print(f'Word n. {i + 1}: {wordlist[word_value]}\n')
                break
            except IndexError:
                if len(words) > 0:
                    words.pop()
                print('Invalid number, try again!')

    all_words = ''.join([format(word,'011b') for word in words])
    entropy_bits = all_words[:entropy_bits_length]
    checksum_calculated = bin(int(hashlib.sha256(int(entropy_bits,2).to_bytes((len(entropy_bits)+7)//8,'big')).hexdigest(),16))[2:].zfill(256)[:checksum_length]
    last_word = int(all_words[-11:-checksum_length] + checksum_calculated, 2)
    words[-1] = last_word
    print(f'Word n. {nwords}: {wordlist[last_word]}\n')
    mnemonic = ' '.join([wordlist[word] for word in words])
    return mnemonic


wordlist_encoded = "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"
wordlist_compressed = base64.b64decode(wordlist_encoded)
wordlist_str = gzip.decompress(wordlist_compressed).decode('utf-8')
"""
SHA256 english.txt
187db04a869dd9bc7be80d21a86497d692c0db6abd3aa8cb6be5d618ff757fae  english.txt
"""
print(sha256(wordlist_str.encode('utf-8')).hexdigest())

wordlist = wordlist_str.splitlines()
mnemonic = generate_mnemonic(wordlist)
print(f'Mnemonic: {mnemonic}')
