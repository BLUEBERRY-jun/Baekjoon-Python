# cro_list="c=,c-,dz=,d-,lj,nj,s=,z=".split(',')
# cro = input()

# for i in (cro_list):
#     cro = cro.replace(i, '*') #크로아티아 알파벳을 * 로 바꾼다 
    
# print(len(cro))


x = input()
y = ["c=", "c-","dz=","d-","lj", "nj", "s=", "z="]

for i in y:
    x = x.replace(i,"*")

print(len(x))