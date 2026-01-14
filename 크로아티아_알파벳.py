cro_list="c=,c-,dz=,d-,lj,nj,s=,z=".split(',')
cro = input()


for i in (cro_list):
    cro = cro.replace(i, '*')


print(len(cro))