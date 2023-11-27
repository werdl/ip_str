class IpStrException(Exception):
    pass

def __ipv4str(sep: str, inp: list[int]) -> list[str]:
    with open("words.txt", "r") as wordfile:
        ipv4_words=wordfile.read().split("\n")
    return sep.join([ipv4_words[int(n)] for n in inp])
def __ipv6str(sep: str, inp: list[int]) -> list[str]:
    with open("ipv6.txt", "r") as wordfile:
        ipv6_words=wordfile.read().split("\n")
    return sep.join([ipv6_words[int(n, 16)] for n in inp])

def ipstr(inp: list|str) -> list[str]:
    if "[" in str(inp): # list
        if len(inp)==8: # ipv6
            for block in inp:
                if block>65536 or block<0: # overflow
                    return IpStrException(f"Overflow block size - {block}")
            return __ipv6str(":",inp)
        elif len(inp)==4: # ipv4
            for block in inp:
                if block>255 or block<0: # overflow
                    return IpStrException(f"Overflow block size - {block}")
            return __ipv4str(".",inp)
        else:
            raise IpStrException(f"Invalid IP input - {inp}")
    else: # str
        splitted=inp.split(".")
        if len(splitted) not in [4,8]: # not decimal seperated
            splitted=inp.split(":")
            if len(splitted) not in [4,8]: # not colon seperated; error
                raise IpStrException("Incorrect or missing seperator char")
        if len(splitted)==8:
            l_inp=[int(item, 16) for item in splitted]
            for block in l_inp:
                if block>65536 or block<0: # overflow
                    return IpStrException(f"Overflow block size - {block}")
            return __ipv6str(":",splitted)
        elif len(splitted)==4:
            l_inp=[int(item) for item in splitted]
            for block in l_inp:
                if block>255 or block<0: # overflow
                    return IpStrException(f"Overflow block size - {block}")
            return __ipv4str(".",splitted)
        else:
            raise IpStrException(f"Invalid IP input - {inp}")
        
def strip(inp: str) -> str:   
    splitted=inp.split(".")
    if len(splitted) not in [4,8]: # not decimal seperated
        splitted=inp.split(":")
        if len(splitted) not in [4,8]: # not colon seperated; error
            raise IpStrException("Incorrect or missing seperator char")
    if len(splitted)==8: # ipv6
        return str_ipv6(splitted)
    elif len(splitted)==4: # ipv4
        return str_ipv4(splitted)
    else:
        raise IpStrException(f"Invalid ipstr input - {inp}")
     



def str_ipv4(inp: list[str]) -> list[int]:
    with open("words.txt", "r") as wordfile:
        words=wordfile.read().split("\n")
    return ".".join([words.index(val) for val in inp])

def str_ipv6(inp: list[str]) -> list[int]:
    with open("ipv6.txt", "r") as wordfile:
        words=wordfile.read().split("\n")
    return ":".join([hex(words.index(val))[2:].zfill(4) for val in inp])

print(strip(ipstr("2001:0db8:0000:0000:0000:8a2e:0370:7334")))