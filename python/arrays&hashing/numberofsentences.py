def noofsentences(wordSet,sentence):
    hashmap = {}
    
    for w in wordSet:
        word = tuple(sorted(w))
        hashmap[word] = hashmap.get(word,0) + 1
    result = [1] * len(sentence)
    for i in range(len(sentence)):
        for w in sentence[i].split():
            key = tuple(sorted(w))
            if key in hashmap:
                result[i] *= hashmap[key]
    return result
        

