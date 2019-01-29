import os
import psutil
import sys
import shutil
import random

def ch_dir():
    answer3_path = os.getcwd()
    print(answer3_path, "- изменить каталог выполнения операции? y/n")
    answer2_2 = input()  
    if answer2_2 == 'y':
            answer3_path = input("укажите путь")   # переменная папки для удаления дубликатов
    return answer3_path


def del_dupl(path):  # удалить дубликаты в папке
    #path = os.getcwd(path)  #!!!
    file_list = os.listdir(path) 
    print("Файлов в директории - ", len(file_list))
    print(file_list)
    i = 0
    for f in file_list:
        full_name = os.path.join(path,f)
        if f.endswith('.dupl') and os.path.isfile(f):
            print(i, "-" , f)  #
            os.remove(full_name) 
            if not os.path.exists(full_name):
                print('файл',f,'удален')
                i += 1
    print("Удалено ", i, "файлов из " , len(file_list))  #
    return i    

def dupl_all(answer3_path):
    print("Дублирую все файлы")
    file_list = os.listdir(answer3_path)
    print(file_list)
    i = 0
    
    while  i < len(file_list):
        fullpath = os.path.join(answer3_path, file_list[i])
        copy_file(fullpath)
        i += 1


def copy_file(full_name):  # дублировать один файл
    if os.path.isfile(full_name):
        newfile = full_name + '.dupl'
        shutil.copy(full_name, newfile)
        # добавить проверку существования нового файла
        print("Ok, дублирован ", full_name)

def del_rnd(answer3_path):
    file_list = os.listdir(answer3_path)
    if file_list:
        len(file_list)
        full_name = os.path.join(answer3_path,file_list[random.randrange(0,len(file_list))])
        if os.path.isfile(full_name):
            os.remove(full_name)
        if not os.path.exists(full_name):
            print('файл',full_name,'удален')

def main():

    print(" New edu programm", '\n''\n', "Привет программист!"'\n')
    name = input("Ваше имя:")
    print(name, ", добро пожаловать в мир Python!")
    answer = ''
    answer3_path = os.getcwd()

    while answer != "q":
    #    answer = input('\nДавай поработаем? y/n')

    #if answer == 'y':
        
    #print('\nОтлично!\n              ')
        print("Я могу: " ) 
        print("1 - смотреть текущую директорию"  )
        print("2 - смотреть системное окружение" ) 
        print("3 - смотреть список процессов" ) 
        print("4 - дублировать все файлы" ) 
        print("5 - дублировать один файл" )      
        print("6 - удалить дубликаты" )                     
        print("7 - сменить рабочий каталог" )    
        print("8 - удалить случайный файл \n" )    

        answer2 = int(input("Что будем делать?"))    


        #print(answer2, "- отличный выбор!")

        if answer2 == 1:  # 1 - смотреть текущую директорию 
            #print(os.listdir())  # os.getcwd()
            print(answer3_path)

        elif answer2 == 2:  # 2 - смотреть системное окружение
            print(os.getcwd(), '\n',  # путь
                os.name,
                os.uname()[2], sys.platform,'\n', # ос, версия  sys.platform
                sys.getfilesystemencoding(),'\n',
                psutil.users()[1][0], os.getlogin(), '\n', # логин
                
                "количество ядер" , psutil.cpu_count(),
                )
        elif answer2 == 3:  # 3 - смотреть список процессов
            print(psutil.pids())

        elif answer2 == 4:  # 4 - дублировать все файлы
            dupl_all(answer3_path)

        elif answer2 == 5:  # 5 - дублировать один файл

            ch_dir()
            
            file_list = os.listdir(answer3_path) 
            print(file_list)
            n_del_file = int(input("какой по счету файл продублировать?"))
            
            full_name = os.path.join(answer3_path,file_list[n_del_file-1])
                        
            copy_file(full_name)
            
            newfile = file_list[n_del_file-1] + '.dupl'
            shutil.copy(file_list[n_del_file-1], newfile)
            print("Ok, дублирован ", file_list[n_del_file-1])
            
        elif answer2 == 6:  # 6 - удалить дубликаты

            ch_dir()
            #answer3_path = os.getcwd()
            n_del = del_dupl(answer3_path)
            file_list = os.listdir(answer3_path) 

            print(file_list)
            print("done") 

        elif answer2 == 7:  # 7 - сменить рабочий каталог
            answer3_path = input('Укажи директорию')

        elif answer2 == 8:  # 8 - удалить случайный файл
            answer3_path = input('Укажи директорию')
            del_rnd(answer3_path)


        else:
            print("Неизвестный ответ")
    
#    elif answer == 'q':
#        print("До свидания!")
#        exit()
    
    else:
        print("Неизвестный ответ")

if __name__ == "__main__":
    main()


