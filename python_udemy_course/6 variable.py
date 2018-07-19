msg=" Hi There "
_msg=" This variable name begins with a '_' "
t1=8
t2=4.182
print(msg)

print(_msg)
t2=7.89
print(msg,_msg," This message is just added ",t1," ",t2)

msg,_msg,t1,t2= "rewrite", "_rewrite_", 10.132, 4
print(msg,_msg," This message is just added ",t1," ",t2)

msg=_msg=t1=t2=" All vars now equal this statement "

print(msg,_msg," This message is just added ",t1," ",t2)

del msg #actually deletes a var

input()