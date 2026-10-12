s="How arE yOu"
vowels="aeiou"
result=[]
for ch in s:
    ch=ch.lower()
    if ch in vowels:
       result.append(ch)
              
print(result)        