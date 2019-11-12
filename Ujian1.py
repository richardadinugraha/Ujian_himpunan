'''Soal 1
A = himpunan (set) bilangan genap antara 1 dan 20.
B = himpunan (set) bilangan ganjil antara 1 dan 20.
C = himpunan (set) bilangan negatif lebih dari -10.
D = himpunan (set) bilangan prima antara 1 dan 20.
E = himpunan (set) bilangan komposit antara 1 dan 20.
'''
'''Bilangan genap & ganjil'''

alist = []
blist = []
for a in range(1,20):
    if a % 2==0:
        alist.append(a) 
    elif a%2!=0:
        blist.append(a)

'''bilangan negatif lebih dari -10'''
clist=(range(-10,0))
'''bilangan prima'''
def prima1(num):
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               return False
               break
       else:
           return True
D = set (filter(prima1,range (20)))
'''bilangan komposit'''
elist=[]
for a in range(2,20):
    if a not in D:
        elist.append(a)

A = set(alist)
B = set(blist)
C = set(clist)
D = set (filter(prima1,range (20)))
E = set (elist)

'''Jawaban:
a. A ∪ B ∪ C ∪ D ∪ E
b. (A ∩ B) ∪ (D ∩ E)
c. (A ∪ B) ∩ (D ∪ E)
d. (A ∪ B) - (D ∪ E)
e. (A ∪ B ∪ C) - (A ∩ E)
'''
print ('a.jawab:'); print (A|B|C|D|E)
print ('b.jawab:');print ((A&B)|(D&E))
print ('c.jawab:');print ((A|B) & (D|E))
print ('d.jawab:');print ((A|B)-(D|E))
print ('e.jawab:');print ((A|B|C)-(A&E))

