# coding: utf-8
# license: GPLv3

import tkinter
from tkinter.filedialog import *
from solar_vis import *
from solar_model import *
from solar_input import *

perform_execution = False
"""Флаг цикличности выполнения расчёта"""

physical_time = 0
"""Физическое время от начала расчёта.
Тип: float"""

displayed_time = None
"""Отображаемое на экране время.
Тип: переменная tkinter"""

time_step = None
"""Шаг по времени при моделировании.
Тип: float"""

space_objects = []
file=open("stats.txt", 'w')
file.close
"""Список космических объектов."""
file=0
st=0
graph_time=1

def execution():
    """Функция исполнения -- выполняется циклически, вызывая обработку всех небесных тел,
    а также обновляя их положение на экране.
    Цикличность выполнения зависит от значения глобальной переменной perform_execution.
    При perform_execution == True функция запрашивает вызов самой себя по таймеру через от 1 мс до 100 мс.
    """
    global physical_time
    global displayed_time
    recalculate_space_objects_positions(space_objects, time_step.get(), t_const)
    for body in space_objects:
        update_object_position(space, body)
    physical_time += time_step.get()
    if st==1:
        save_stat(space_objects[int(num.get())])
    displayed_time.set(str(int(((physical_time * t_const)//(3600*24))%(30))) + " d "+ str(int(((physical_time * t_const)//(3600*24*365.25/12))%(12))) + " m "+str(int((physical_time * t_const)//(3600*24*365.25)))+ " y")
    if perform_execution:
        space.after(101 - int(time_speed.get()), execution)

def save_stat(obj):
     s = str(physical_time)+ " " + str(obj.x) + " " + str(obj.y) + " " + str(obj.Vx) + " " + str(obj.Vy) + "\n"
     file.write(s)

def start_execution():
    """Обработчик события нажатия на кнопку Start.
    Запускает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = True
    start_button['text'] = "Выключить"
    start_button['command'] = stop_execution
    execution()
    print('Started execution...')


def stop_execution():
    """Обработчик события нажатия на кнопку Start.
    Останавливает циклическое исполнение функции execution.
    """
    global perform_execution
    perform_execution = False
    start_button['text'] = "Включить"
    start_button['command'] = start_execution
    print('Paused execution.')


def open_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    global space_objects
    global perform_execution
    global physical_time
    physical_time = 0
    perform_execution = False
    st=0
    file=open("stats.txt", 'w')
    file.close
    for obj in space_objects:
        space.delete(obj.image)  # удаление старых изображений планет
    in_filename = askopenfilename(filetypes=(("Text file", ".txt"),))
    space_objects = read_space_objects_data_from_file(in_filename)
    max_distance = max([max(abs(obj.x), abs(obj.y)) for obj in space_objects])
    calculate_scale_factor(max_distance)
    num_scale['to']=len(space_objects)-1
    for obj in space_objects:
        if obj.type == 'star':
            create_star_image(space, obj)
        elif obj.type == 'planet':
            create_planet_image(space, obj)
        else:
            raise AssertionError()


def save_file_dialog():
    """Открывает диалоговое окно выбора имени файла и вызывает
    функцию считывания параметров системы небесных тел из данного файла.
    Считанные объекты сохраняются в глобальный список space_objects
    """
    out_filename = asksaveasfilename(filetypes=(("Text file", ".txt"),))
    write_space_objects_data_to_file(out_filename, space_objects)
def start_stat():
    global st,file,graph_time_start
    st=1
    graf_start_button['text'] = "Закончить сохранять статистику для графиков"
    graf_start_button['command'] = stop_stat
    graph_time_start = physical_time
    graf_ris_button.pack_forget()
    num_scale.pack_forget()
    num_label.pack_forget()
    file=open("stats.txt", 'a')
def stop_stat():
    global st,file, graph_time
    st=0
    graf_start_button['text'] = "Начать сохранять статистику для графиков"
    graf_start_button['command'] = start_stat
    graph_time = physical_time
    file.close()
    graf_ris_button.pack(side=tkinter.LEFT)
    num_scale.pack(side=tkinter.RIGHT)
    num_label.pack(side=tkinter.RIGHT)
    
def graphs():
    graph1()
    graph2()
    graph3()
    
def graph1():
    root1 = tkinter.Tk()
    graph1 = tkinter.Canvas(root1, width=500, height=500, bg="white")
    graph1.pack(side=tkinter.BOTTOM)
    frame1 = tkinter.Frame(root1)
    frame1.pack(side=tkinter.TOP)
    name_label1 = tkinter.Label(frame1, text="Модуль скорости планеты от времени")
    name_label1.pack(side=tkinter.TOP)
    if(graph_time!=0):
        dt = 500/graph_time
    else:
        dt=1
    vm=[0]*(int(graph_time))
    tm=[0]*(int(graph_time))
    vmax=0
    i=0
    with open("stats.txt") as file:
        for line in file:
            tm[i]= int(float(line.split()[0]))
            vm[i]=(float(line.split()[3])**2+float(line.split()[4])**2)**(1/2)
            i=i+1
    for i in range(0,int(graph_time)):
        if vm[i]>vmax:
            vmax=vm[i]
    if(vmax!=0):
        dv=500/vmax
    else:
        dv=1
    for i in range(0,int(graph_time-1)):
        graph1.create_oval(dt*tm[i],550-vm[i]*dv,dt*(tm[i]),550-vm[i]*dv,width=2)
        if(tm[i+1]-tm[i]==1):
            graph1.create_line(dt*tm[i],550-vm[i]*dv,dt*(tm[i+1]),550-vm[i+1]*dv,width=4)
    file.close

def graph2():
    root2 = tkinter.Tk()
    graph2 = tkinter.Canvas(root2, width=500, height=500, bg="white")
    graph2.pack(side=tkinter.BOTTOM)
    frame2 = tkinter.Frame(root2)
    frame2.pack(side=tkinter.TOP)
    name_label2 = tkinter.Label(frame2, text="Расстояние от планеты до звезды от времени")
    name_label2.pack(side=tkinter.TOP)
    if(graph_time!=0):
        dt = 500/graph_time
    else:
        dt=1
    rm=[0]*(int(graph_time))
    tm=[0]*(int(graph_time))
    rmax=0
    i=0
    with open("stats.txt") as file:
        for line in file:
            tm[i]= int(float(line.split()[0]))
            rm[i]=(float(line.split()[1])**2+float(line.split()[2])**2)**(1/2)
            i=i+1
    for i in range(0,int(graph_time)):
        if rm[i]>rmax:
            rmax=rm[i]
    if(rmax!=0):
        dr=500/rmax
    else:
        dr=1
    for i in range(0,int(graph_time-1)):
        graph2.create_oval(dt*tm[i],550-rm[i]*dr,dt*(tm[i]),550-rm[i]*dr,width=2)
        if(tm[i+1]-tm[i]==1):
            graph2.create_line(dt*tm[i],550-rm[i]*dr,dt*(tm[i+1]),550-rm[i+1]*dr,width=4)
    file.close


def graph3():
    root3 = tkinter.Tk()
    graph3 = tkinter.Canvas(root3, width=500, height=500, bg="white")
    graph3.pack(side=tkinter.BOTTOM)
    frame3 = tkinter.Frame(root3)
    frame3.pack(side=tkinter.TOP)
    name_label3 = tkinter.Label(frame3, text="Модуль скорости планеты от расстояния до звезды")
    name_label3.pack(side=tkinter.TOP)
    vm=[0]*(int(graph_time))
    rm=[0]*(int(graph_time))
    tm=[0]*(int(graph_time))
    vmax=0
    rmax=0
    i=0
    with open("stats.txt") as file:
        for line in file:
            tm[i]= int(float(line.split()[0]))
            rm[i]=(float(line.split()[1])**2+float(line.split()[2])**2)**(1/2)
            vm[i]=(float(line.split()[3])**2+float(line.split()[4])**2)**(1/2)
            i=i+1
    for i in range(0,int(graph_time)):
        if vm[i]>vmax:
            vmax=vm[i]
    if(vmax!=0):
        dv=500/vmax
    else:
        dv=1
    for i in range(0,int(graph_time)):
        if rm[i]>rmax:
            rmax=rm[i]
    if(rmax!=0):
        dr=500/rmax
    else:
        dr=1
    for i in range(0,int(graph_time-1)):
        graph3.create_oval(dr*rm[i]-50,550-vm[i]*dv,dr*(rm[i])-50,550-vm[i]*dv,width=2)
        if(tm[i+1]-tm[i]==1):
            graph3.create_line(dr*rm[i]-50,550-vm[i]*dv,dr*(rm[i+1])-50,550-vm[i+1]*dv,width=4)
    file.close    

def main():
    """Главная функция главного модуля.
    Создаёт объекты графического дизайна библиотеки tkinter: окно, холст, фрейм с кнопками, кнопки.
    """
    global physical_time
    global displayed_time
    global time_step
    global time_speed
    global space
    global start_button
    global graf_ris_button
    global graf_start_button
    global t_const
    global num
    global num_scale
    global num_label

    print('Modelling started!')
    physical_time = 0
    t_const = 100000
    root = tkinter.Tk()
    # космическое пространство отображается на холсте типа Canvas
    space = tkinter.Canvas(root, width=window_width, height=window_height, bg="black")
    space.pack(side=tkinter.TOP)
    # нижняя панель с кнопками
    frameA = tkinter.Frame(root)
    frameB = tkinter.Frame(root)
    frameB.pack(side=tkinter.BOTTOM)
    frameA.pack(side=tkinter.BOTTOM)

    start_button = tkinter.Button(frameA, text="Включить", command=start_execution, width=10)
    start_button.pack(side=tkinter.LEFT)
    graf_ris_button = tkinter.Button(frameB, text="Построить графики", command=graphs)
    graf_start_button = tkinter.Button(frameA, text="Начать сохранять статистику для графиков", command=start_stat, width=60)
    graf_start_button.pack(side=tkinter.RIGHT)

    time_step = tkinter.DoubleVar()
    time_step.set(1)

    time_speed = tkinter.DoubleVar()
    num = tkinter.DoubleVar()
    
    scale = tkinter.Scale(frameA, variable=time_speed, orient=tkinter.HORIZONTAL)
    scale.pack(side=tkinter.LEFT)

    load_file_button = tkinter.Button(frameA, text="Открыть файл...", command=open_file_dialog)
    load_file_button.pack(side=tkinter.LEFT)
    save_file_button = tkinter.Button(frameA, text="Сохранить в файл...", command=save_file_dialog)
    save_file_button.pack(side=tkinter.LEFT)

    displayed_time = tkinter.StringVar()
    displayed_time.set(str(physical_time*t_const) + " d 0 m 0 y")
    time_label = tkinter.Label(frameA, textvariable=displayed_time, width=30)
    time_label.pack(side=tkinter.RIGHT)
    num_label = tkinter.Label(frameB, text="Номер тела:", width = 20)
    num_scale = tkinter.Scale(frameB, variable=num,from_=0,to=0, orient=tkinter.HORIZONTAL)
    num_scale.pack(side=tkinter.RIGHT)
    num_label.pack(side=tkinter.RIGHT)
    root.mainloop()
    print('Modelling finished!')

if __name__ == "__main__":
    main()
