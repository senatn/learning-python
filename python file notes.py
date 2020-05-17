x = open('sena.txt','w')

x.write('sena tan\nmusa yurt')

x.close()

musa = open('sena.txt')

print(musa.read())

musa.close()

with open('sena.txt', 'r', encoding = 'utf-8') as y:
    print(y.read())

z = open('sena.txt')
print(z.read())

print(z.read())

print(z.seek(0))
print(z.read())
print(z.seek(3))
print(z.tell())

# 'a' dosyanin sonuna ekleme yapmamizi saglar
with open('sena.txt','a') as i:
    i.write('\nsemine tan\nbuse yurt')

# 'r+' okuma ve yazma kipinde
with open('sena.txt','r+') as i:
    j = i.read()
    i.seek(0)
    i.write('balim\n'+j)
    i.seek(0)
    print(i.read())

with open('sena.txt','r+')as s:
    i = s.readlines()  #satirlari okur ve liste olarak dondurur
    i.insert(1,'cay\n')
    s.seek(0)
    s.writelines(i)  #dosyalara liste tipinde veri yazar
    s.seek(0)
    print(s.read())