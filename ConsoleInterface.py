def ConsoleInterface():
    while True:
      print()
      print("С возвращением!")
      print()
      print("      ,/|         _.--''^``-...___.._.,;")
      print("    /, \'.     _-'          ,--,,,--'''")
      print("   { \    `_-''       '    /}")
      print("    `;;'            ;   ; ;")
      print("._.--''     ._,,, _..'  .;.'")
      print(" (,_....----'''     (,..--''")
      print("Что хотите сделать?")
      print("1) Посмотреть задачи")
      print("2) Добавить задачу")
      print("3) Редактировать задачу")
      print("4) Удалить задачу")
      print("5) Выйти")
      
      choice = input("Введите выбор: ")
      


      
      if (choice == "1"):
        while True:
            print()
            print("             *     ,MMM8&&&.            *")
            print("                  MMMM88&&&&&    .")
            print("                 MMMM88&&&&&&&")
            print("     *           MMM88&&&&&&&&")
            print("                 MMM88&&&&&&&&")
            print("                 'MMM88&&&&&&'")
            print("                   'MMM8&&&'      *")
            print("          |\___/|")
            print("          )     (             .              '")
            print("         =\     /=")
            print("           )===(       *")
            print("          |     |")
            print("          |     |")
            print("         |       |")
            print("         \       /")
            print("  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_")
            print("  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |")
            print("  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |")
            print("  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |")
            print("  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")
            print("  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")
            print("Список планов")
            print("1) На сегодня")
            print("2) На эту неделю")
            print("3) На этот месяц")
            print("4) За всё время")
            print("5) Назад")
            
            choice1 = input("Введите выбор: ")
            if (choice1 == "1"):
                #Планы на сегодня
                print()
            elif (choice1 == "2"):
                #Планы на эту неделю
                print()            
            elif (choice1 == "3"):
                #Планы на этот месяц 
                print()
            elif (choice1 == "4"):
                #Планы за всё время 
                print()
            else:
                break
      elif (choice == "2"):
        print()
        print("             *     ,MMM8&&&.            *")
        print("                  MMMM88&&&&&    .")
        print("                 MMMM88&&&&&&&")
        print("     *           MMM88&&&&&&&&")
        print("                 MMM88&&&&&&&&")
        print("                 'MMM88&&&&&&'")
        print("                   'MMM8&&&'      *")
        print("          |\___/|     /\___/\*")
        print("          )     (     )    ~( .              '")
        print("         =\     /=   =\~    /=")
        print("           )===(       ) ~ (")
        print("          /     \     /     \             *")
        print("          |     |     ) ~   (")
        print("         /       \   /     ~ \     '")
        print("         \       /   \~     ~/")
        print("  _/\_/\_/\__  _/_/\_/\__~__/_/\_/\_/\_/\_/\_")
        print("  |  |  |  |( (  |  |  | ))  |  |  |  |  |  |")
        print("  |  |  |  | ) ) |  |  |//|  |  |  |  |  |  |")
        print("  |  |  |  |(_(  |  |  (( |  |  |  |  |  |  |")
        print("  |  |  |  |  |  |  |  |\)|  |  |  |  |  |  |")
        print("  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |")
        print("Добавление плана")
        name = input("Введите название: ")
        dateTimeStart = input("Введите дату и время начала: ")
        dateTimeEnd = input("Введите дату и время начала: ")
        description = input("Введите описание плана: ")
        #Создание
        print("План успешно создан")
      elif (choice == "3"):
        print("                _")
        print("                \`*-.                   ")
        print("                 )  _`-.          ")      
        print("                .  : `. .               ")
        print("                : _   '  \              ")
        print("                ; *` _.   `*-._         ")
        print("                `-.-'          `-.      ")
        print("                  ;       `       `.    ")
        print("                 :.       .        \   ")
        print("                  . \  .   :   .-'   .  ")
        print("                  '  `+.;  ;  '      :  ")
        print("                  :  '  |    ;       ;-.")
        print("                  ; '   : :`-:     _.`* ;")
        print("         [bug] .*' /  .*' ; .*`- +'  `*'")
        print("               `*-*   `*-*  `*-*'   ")
        print("Изменение плана")
        name = input("Введите название плана: ")
        date = input("Введите дату этого плана: ")
        print("Изменяем")
        while True:
            print("1) Название")
            print("2) Время начала и конца")
            print("3) Описание")
            print("4) Назад")
            choice3 = input("Введите выбор: ")
            if (choice3 == "1"):
                #Смена названия
                print()
            elif (choice3 == "2"):
                #Смена времени и даты
                print()            
            elif (choice3 == "3"):
                #Смена описания 
                print()
            else:
                break
      elif (choice == "4"):
        print()    
        print("  /\_/\*")
        print(" ( o.o )")
        print("  > ^ <")
        print("Удаление плана")
        name = input("Введите название плана: ")
        date = input("Введите дату этого плана: ")
        while True:
            print("Вы уверены, что хотите удалить?")
            print("1) Да")
            print("2) Нет")
            choice4 = input("Введите выбор: ")
            if (choice4 == "1"):
                #УДАЛЕНИЕ РАЗ И НАВСЕГДА
                print("Удаление произошло успешно")
            else:
                print("Удаление отменено")
                break
      elif (choice == "5"):
        print("Завершение работы программы")
        print("До свидания!")
        return 0
      else:
        print("Такой опции нет. Попробуйте цифры от 1 до 5")
        
        
ConsoleInterface()