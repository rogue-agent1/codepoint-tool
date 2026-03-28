#!/usr/bin/env python3
"""Unicode codepoint explorer — lookup, search, block info."""
import sys, unicodedata
BLOCKS=[(0x0000,0x007F,"Basic Latin"),(0x0080,0x00FF,"Latin-1 Supplement"),(0x0100,0x017F,"Latin Extended-A"),(0x0370,0x03FF,"Greek and Coptic"),(0x0400,0x04FF,"Cyrillic"),(0x0530,0x058F,"Armenian"),(0x0600,0x06FF,"Arabic"),(0x2000,0x206F,"General Punctuation"),(0x2200,0x22FF,"Mathematical Operators"),(0x2600,0x26FF,"Miscellaneous Symbols"),(0x2700,0x27BF,"Dingbats"),(0x1F600,0x1F64F,"Emoticons"),(0x1F300,0x1F5FF,"Misc Symbols and Pictographs")]
def block_of(cp):
    for lo,hi,name in BLOCKS:
        if lo<=cp<=hi: return name
    return "Unknown"
def info(char):
    cp=ord(char)
    try: name=unicodedata.name(char)
    except: name="<unnamed>"
    print(f"  Char: {char}  U+{cp:04X}  {name}")
    print(f"  Category: {unicodedata.category(char)}  Block: {block_of(cp)}")
    print(f"  UTF-8: {char.encode('utf-8').hex(' ')}  UTF-16: {char.encode('utf-16-be').hex(' ')}")
def cli():
    if len(sys.argv)<2: print("Usage: codepoint <char|U+XXXX|search QUERY>"); sys.exit(1)
    arg=sys.argv[1]
    if arg=="search":
        q=" ".join(sys.argv[2:]).upper(); found=0
        for cp in range(0x110000):
            try:
                c=chr(cp); n=unicodedata.name(c)
                if q in n: print(f"  {c}  U+{cp:04X}  {n}"); found+=1
                if found>=20: break
            except: pass
    elif arg.startswith("U+") or arg.startswith("u+"): info(chr(int(arg[2:],16)))
    else: [info(c) for c in arg]
if __name__=="__main__": cli()
