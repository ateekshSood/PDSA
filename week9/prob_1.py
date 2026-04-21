def constructWord(word , wordList , memo = None):
    
    if memo == None:
        memo = {}
        
    if word in memo:
        return memo[word]
        
    if word == "":
        return [[]]
    
    total_ways = []
    
    for prefix in wordList:
        
        if word[:len(prefix)] == prefix:
            
            suffix = word[len(prefix):]
            
            suffix_ways = constructWord(suffix , wordList , memo)
            
            for way in suffix_ways:
                
                total_ways.append([prefix] + way)
    
    
    memo[word] = total_ways 
    
    return memo[word]
            
        
    