# 这个函数用来找到一串字符当中频率最高的字母，排除标点符号，且不区分大小写同意返回小写结果。
def mwl(string):
    char_list = []
    count = {}
    candidate = []
    
    if len(string) <= 10000:
        string = string.lower()
        
        for s in string:
            if s.isalpha():
                char_list.append(s)
        collection = set(char_list)

        for unique in collection:
            num = char_list.count(unique)
            count.update({unique: num})
        num_list = list(count.values())
        value = max(num_list)
 
        for key in list(count.keys()):
            if count[key] == value:
                candidate.append(key)
        candidate.sort()
        return candidate[0]
    
    else:
        return 'The input string is too long.'
                
        
test = 'AAAccc'
a = mwl(test)
print(a)

# 以下时最佳答案
'''
import string
​
def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
'''
