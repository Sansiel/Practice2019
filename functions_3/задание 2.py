def decorator(function_to_decorate):
    def worker():
        print("Начал работу")
        function_to_decorate()
        print("Закончил")
    return worker

def funct():
    print("Ну я есть - радуйся этому")

funct=decorator(funct)
funct()

@decorator
def another_funct():
     print("Оставь меня в покое")

another_funct()