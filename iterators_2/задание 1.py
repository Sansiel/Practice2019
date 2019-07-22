
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

source_vocebulary = [7,4,1,1, 8, 8]
generate_vocebulary = set(source_vocebulary)
print(generate_vocebulary)

#Дубликаты. С сохранением порядка. В задании нигде не было про сохранение порядка, и без сохранения строчек меньше.

source_vocebulary = [7,4,1,1, 8, 8]
generate_vocebulary=[]
for value in source_vocebulary:
    if value not in generate_vocebulary:
        generate_vocebulary.append(value)
print(generate_vocebulary)