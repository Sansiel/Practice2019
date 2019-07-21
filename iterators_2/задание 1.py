
#FizzBuzz

for n in range(1, 101):
     if (n%3==0)&(n%5==0):
          print("FizzBuzz")
     elif (n%3==0):
          print("Fizz")
     elif (n%5==0):
          print("Bazz")
     else:
          print(n)

#Ключ-значение

l = {'RPG': 'Black_Desert','Shooter': 'Warframe','Strategy': 'Civilization',}
print ({v:k for k, v in l.items()})

#Дубликаты
source_vocebulary = {1,1,2,2,2,3,3,4,5,5}
generate_vocebulary = set(source_vocebulary)
print(generate_vocebulary)