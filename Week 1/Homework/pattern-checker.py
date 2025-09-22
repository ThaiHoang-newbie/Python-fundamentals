def checkPattern(pattern, text) -> bool:
    words = text.split()
    if len(pattern) != len(words): return False

    p2t, t2p = {}, {}
    for c, w in zip(pattern, words):
        if c in p2t:
            if p2t[c] != w: return False
        else:
            p2t[c] = w

        if w in t2p:
            if t2p[w] != c: return False
        else:
            t2p[w] = c
    return True

    
print(checkPattern('aabb', 'cat cat dog dog')) #true
print(checkPattern('aabb', 'rat rat pig pig')) #true
print(checkPattern('aabb', 'cat cat dog')) #false
print(checkPattern('aabb', 'cat dog dog dog')) #false