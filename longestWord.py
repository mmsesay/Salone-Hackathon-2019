#!/usr/bin/python3

wordPack = ["hello", "worlds", "hi", "bye"]

# for word in wordPack:

#     if word[word] :
#         max(word)

m=max(map(len,wordPack))
print([x for x in wordPack if len(x) == m])

# print(max(wordPack, key=len))