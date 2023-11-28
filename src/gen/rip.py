import random
with open("in.txt", "r") as infile:
    words=infile.read().split("\n")
    random.shuffle(words)
    words=["zero"]+words
    words=[word for word in words if len(word)<=4 and len(word)>2]
with open("words.txt", "w") as outfile:
    outfile.write('\n'.join(words))
    
with open("ipv6_words.txt", "r") as infile:
    words=infile.read().split("\n")
    random.shuffle(words)
    words=["zero"]+words
    words=[word.lower() for word in words if len(word)<=8 and len(word)>2 and all(ord(char) < 128 for char in word) and all(char not in ['"', "'"] for char in word)]
    
with open("ipv6.txt", "w") as outfile:
    outfile.write('\n'.join(words))