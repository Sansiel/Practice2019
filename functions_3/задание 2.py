import datetime

def decorator(function_to_decorate):
    def time_to_work():
        beginTime = datetime.datetime.now()
        print("Начал работу в " + beginTime.__str__())
        function_to_decorate()
        totalTime = datetime.datetime.now() - beginTime
        print("Закончил работу в " + datetime.datetime.now().__str__())
        print("Затраченое время = " + totalTime.__str__())
    return time_to_work

def funct():
    print("Ну я есть - радуйся этому")

funct=decorator(funct)
funct()

@decorator
def another_funct():
     print("Оставь меня в покое")

another_funct()