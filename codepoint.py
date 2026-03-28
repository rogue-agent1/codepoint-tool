#!/usr/bin/env python3
"""codepoint - Unicode codepoint lookup and character info."""
import sys, unicodedata

def char_info(c):
    cp = ord(c)
    try: name = unicodedata.name(c)
    except: name = '<unknown>'
    cat = unicodedata.category(c)
    return {'char': c, 'codepoint': f'U+{cp:04X}', 'decimal': cp, 'hex': hex(cp),
            'name': name, 'category': cat, 'utf8': c.encode('utf-8').hex(' ')}

def main():
    args = sys.argv[1:]
    if not args or '-h' in args:
        print("Usage:\n  codepoint.py CHAR [...]\n  codepoint.py U+1F600\n  codepoint.py --string TEXT"); return
    if args[0] == '--string':
        for c in ' '.join(args[1:]):
            info = char_info(c)
            print(f"  {info['char']}  {info['codepoint']}  {info['name']}")
        return
    for a in args:
        if a.startswith('U+') or a.startswith('u+'):
            c = chr(int(a[2:], 16))
        elif a.startswith('0x'):
            c = chr(int(a, 16))
        elif len(a) == 1:
            c = a
        else:
            for ch in a:
                info = char_info(ch)
                print(f"  {info['char']}  {info['codepoint']}  {info['name']}")
            continue
        info = char_info(c)
        print(f"  Character: {info['char']}")
        print(f"  Codepoint: {info['codepoint']} ({info['decimal']})")
        print(f"  Name:      {info['name']}")
        print(f"  Category:  {info['category']}")
        print(f"  UTF-8:     {info['utf8']}")

if __name__ == '__main__': main()
