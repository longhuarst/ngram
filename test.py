#coding=utf-8

import ngram


str1 = "hello i am a chinese"

str2 = "hello i am a english"





print(ngram.NGram.compare("hello world", "nihao world",N=2))




lst_str1 = str1.split(" ");


print("lst_str1.len = %d"%len(lst_str1))
print(lst_str1)


lst_str2 = str2.split(" ");


print("lst_str2.len = %d"%len(lst_str2))
print(lst_str2)

N = min(len(lst_str1),len(lst_str2))



print("N=min(len(lst_str1),len(lst_str2)) = %d"%N)

if N > 0 :
    print("N>0")

    #开始组词
    #根据N组词




else :
    print("N<=0")