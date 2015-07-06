def censor(text, word):
    txt_list = text.split(word)
    new_list = [c + '*'*len(word) for c in txt_list]
    return ''.join(new_list)[:-len(word)]
    
    
    

test = censor('this hack is wack hack.', 'hack')
print(test)
    
