import os
import psutil
import sys
import shutil

print(" New edu programm", '\n''\n', "Привет программист!"'\n')
name = input("Ваше имя:")
print(name, ", добро пожаловать в мир Python!")
answer = ''

while answer != "q":
    answer = input('\nДавай поработаем? y/n')

    if answer == 'y':
        
        print('\nОтлично!\n              ')
        print("Я могу: " ) 
        print("1 - смотреть текущую директорию"  )
        print("2 - смотреть системное окружение" ) 
        print("3 - смотреть список процессов" ) 
        print("4 - дублировать все файлы" ) 
        print("5 - дублировать один файл" )      
        print("6 - удалить дубликаты\n" )                     
             
        
        answer2 = int(input("Что будем делать?"))    
        
        #print(answer2, "- отличный выбор!")

        if answer2 == 1:
            print(os.listdir())  # os.getcwd()
            
        elif answer2 ==2:
            print(os.getcwd(), '\n',  # путь
                os.name,
                os.uname()[2], sys.platform,'\n', # ос, версия  sys.platform
                sys.getfilesystemencoding(),'\n',
                psutil.users()[1][0], os.getlogin(), '\n', # логин
                
                "количество ядер" , psutil.cpu_count(),
                )
        elif answer2 == 3:
            print(psutil.pids())
        
        elif answer2 == 4:
            print("Дублирую файлы")
            file_list = os.listdir()
            print(file_list)
            i = 0
            while  i < len(file_list) :
                if os.path.isfile(file_list[i]):
                    newfile = file_list[i] + '.dupl'
                    shutil.copy(file_list[i], newfile)
                    i += 1
            print("done") 
         
        elif answer2 == 5:  # 5 - дублировать один файл
            print("Текущий каталог:", os.getcwd())
            file_list = os.listdir() 
            print(file_list)
            n_del_file = int(input("какой по счету файл продублировать?"))
            newfile = file_list[n_del_file-1] + '.dupl'
            shutil.copy(file_list[n_del_file-1], newfile)
            print("Ok, дублирован ", file_list[n_del_file-1])
            
        elif answer2 == 6:
            print("Текущий каталог:", os.getcwd(), "Изменить? y/n")
            answer2_2 = input()
            if answer2_2 == 'y':
                    answer3_path = input("укажите путь и папку")
                    os.chdir(answer3_path)
            
            print("Удаляю все дубли")
            
            file_list = os.listdir() 
            print("Всего файлов - ", len(file_list))
            print(file_list)
            i = 0
            print("____")
            while  i < len(file_list) :
                
                if file_list[i].endswith('.dupl'):
                    print(i, "-" , file_list[i])
                    os.remove(file_list[i])  # os.path.isfile(file_list[i]) and 
                    print('файл',file_list[i],'удален')
                i += 1
            
            file_list = os.listdir()
            print(file_list)

            print("done") 
            
        
        
        else:
            pass
    elif answer == 'n':
        
        print("До свидания!")

    else:
        
        print("Неизвестный ответ - buy!")


