# coding: utf-8
# license: GPLv3

from solar_objects import Star, Planet


def read_space_objects_data_from_file(input_filename):
    """Cчитывает данные о космических объектах из файла, создаёт сами объекты
    и вызывает создание их графических образов

    Параметры:

    **input_filename** — имя входного файла
    """

    objects = []
    with open(input_filename) as input_file:
        for line in input_file:
            if len(line.strip()) == 0 or line[0] == '#':
                continue  # пустые строки и строки-комментарии пропускаем
            object_type = line.split()[0].lower()
            if object_type == "star":  # FIXME: do the same for planet
                star = Star()
                star.type = "star"
                parse_star_parameters(line, star)
                objects.append(star)
            elif object_type == "planet":  # FIXME: do the same for planet
                planet = Planet()
                planet.type = "planet"
                parse_planet_parameters(line, planet)
                objects.append(planet)
            else:
                print("Unknown space object")

    return objects

def MASSIV_STROKA(a):
    b=""
    for i in range (0, len(a)):
      b=b+a[i]
    return b
def parse_star_parameters(line, star):
    """Считывает данные о звезде из строки.
    Входная строка должна иметь слеюущий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты зведы, (Vx, Vy) — скорость.
    Пример строки:
    Star 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание звезды.
    **star** — объект звезды.
    """

    a=[]
    b=0
    for i in range(0,len(line)): # FIXME: not done yet...
        if line[i]==" ":
            if b==1:
                star.R = float(MASSIV_STROKA(a))
            elif b==2:
                star.color = MASSIV_STROKA(a)
            elif b==3:
                star.m = float(MASSIV_STROKA(a))
            elif b==4:
                star.x = float(MASSIV_STROKA(a))
            elif b==5:
                star.y = float(MASSIV_STROKA(a))
            elif b==6:
                star.Vx = float(MASSIV_STROKA(a))
            b=b+1
            a=[]
        elif b!=0:
            a.append (line[i])
    star.Vy = float(MASSIV_STROKA(a))# FIXME: not done yet

def parse_planet_parameters(line, planet):
    """Считывает данные о планете из строки.
    Предполагается такая строка:
    Входная строка должна иметь слеюущий формат:
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Здесь (x, y) — координаты планеты, (Vx, Vy) — скорость.
    Пример строки:
    Planet 10 red 1000 1 2 3 4

    Параметры:

    **line** — строка с описание планеты.
    **planet** — объект планеты.
    """
    a=[]
    b=0
    for i in range(0,len(line)): # FIXME: not done yet...
        if line[i]==" ":
            if b==1:
                planet.R = float(MASSIV_STROKA(a))
            elif b==2:
                planet.color = MASSIV_STROKA(a)
            elif b==3:
                planet.m = float(MASSIV_STROKA(a))
            elif b==4:
                planet.x = float(MASSIV_STROKA(a))
            elif b==5:
                planet.y = float(MASSIV_STROKA(a))
            elif b==6:
                planet.Vx = float(MASSIV_STROKA(a))
            b=b+1
            a=[]
        elif(b!=0):
            a.append(line[i])
    planet.Vy = float(MASSIV_STROKA(a))# FIXME: not done yet


def write_space_objects_data_to_file(output_filename, space_objects):
    """Сохраняет данные о космических объектах в файл.
    Строки должны иметь следующий формат:
    Star <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>
    Planet <радиус в пикселах> <цвет> <масса> <x> <y> <Vx> <Vy>

    Параметры:

    **output_filename** — имя входного файла
    **space_objects** — список объектов планет и звёзд
    """
    with open(output_filename, 'w') as out_file:
        for obj in space_objects:
            s= str(obj.type)+" "+str(obj.R)+" "+str(obj.color)+" "+str(obj.m)+" "+str(obj.x)+" "+str(obj.y)+" "+str(obj.Vx)+" "+str(obj.Vy)+"\n"
            # FIXME: should store real values  "%s %d %s %f" %
            out_file.write(s)
        out_file.close()

# FIXME: хорошо бы ещё сделать функцию, сохранающую статистику в заданный файл...

if __name__ == "__main__":
    print("This module is not for direct call!")
