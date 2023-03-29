class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
            print(bcolors.OKCYAN)
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
        print(bcolors.HEADER)
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
        if not name or not dateTimeStart or not dateTimeEnd or not description:
            print(bcolors.FAIL+"Вводимые поля не должны быть пусты"+bcolors.ENDC)
        #Создание
        print(bcolors.OKGREEN+"План успешно создан"+bcolors.ENDC)
      elif (choice == "3"):
        print(bcolors.BOLD+bcolors.WARNING)
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
        if not name or not date:
            print(bcolors.FAIL+"Вводимые поля не должны быть пусты"+bcolors.ENDC)
        print("Изменяем")
        while True:
            print("1) Название")
            print("2) Время начала и конца")
            print("3) Описание")
            print("4) Всё")
            print("5) Назад")
            choice3 = input("Введите выбор: ")
            if (choice3 == "1"):
                #Смена названия
                nameNew = input("Введите название: ")
                if not nameNew:
                    print(bcolors.FAIL+"Вводимые поля не должны быть пусты"+bcolors.ENDC)
                ##############################
                print(bcolors.OKGREEN+"Изменение прошло успешно"+bcolors.ENDC)
                print()
            elif (choice3 == "2"):
                #Смена времени и даты
                dateTimeStartNew = input("Введите дату и время начала: ")
                dateTimeEndNew = input("Введите дату и время начала: ")
                if not dateTimeStartNew or not dateTimeEndNew:
                    print(bcolors.FAIL+"Вводимые поля не должны быть пусты"+bcolors.ENDC)
                ##############################
                print(bcolors.OKGREEN+"Изменение прошло успешно"+bcolors.ENDC)
                print()            
            elif (choice3 == "3"):
                #Смена описания 
                descriptionNew = input("Введите описание плана: ")
                if not descriptionNew:
                    print(bcolors.FAIL+"Вводимые поля не должны быть пусты"+bcolors.ENDC)
                ##############################
                print(bcolors.OKGREEN+"Изменение прошло успешно"+bcolors.ENDC)
                print()
            elif (choice3 == "4"):
                #Смена всего 
                nameNew = input("Введите название: ")
                dateTimeStartNew = input("Введите дату и время начала: ")
                dateTimeEndNew = input("Введите дату и время начала: ")
                descriptionNew = input("Введите описание плана: ")
                if not nameNew or not dateTimeStartNew or not dateTimeEndNew or not descriptionNew:
                    print(bcolors.FAIL+"Вводимые поля не должны быть пусты"+bcolors.ENDC)
                ##############################
                print(bcolors.OKGREEN+"Изменение прошло успешно"+bcolors.ENDC)
                print()
            else:
                break
      elif (choice == "4"):
        print(bcolors.OKGREEN)  
        print("  /\_/\*")
        print(" ( o.o )")
        print("  > ^ <")
        print("Удаление плана")
        name = input("Введите название плана: ")
        date = input("Введите дату этого плана: ")
        if not name or not date:
            print(bcolors.FAIL+"Вводимые поля не должны быть пусты"+bcolors.ENDC)
        while True:
            print("Вы уверены, что хотите удалить?")
            print("1) Да")
            print("2) Нет")
            choice4 = input("Введите выбор: ")
            if (choice4 == "1"):
                #УДАЛЕНИЕ РАЗ И НАВСЕГДА
                print(bcolors.OKGREEN+"Удаление произошло успешно"+bcolors.ENDC)
                break
            else:
                print(bcolors.FAIL+"Удаление отменено"+bcolors.ENDC)
                break
      elif (choice == "5"):
        print(bcolors.OKBLUE) 
        print(" *                  *")
        print("             __                *")
        print("          ,db'    *     *")
        print("         ,d8/       *        *    *")
        print("         888")
        print("         `db\       *     *")
        print("           `o`_                    **")
        print("      *               *   *    _      *")
        print("            *                 / )")
        print("         *    (\__/) *       ( (  *")
        print("       ,-.,-.,)    (.,-.,-.,-.) ).,-.,-.")
        print("      | @|  ={      }= | @|  / / | @|o |")
        print("     _j__j__j_)     `-------/ /__j__j__j_")
        print("     ________(               /___________")
        print("      |  | @| \              || o|O | @|")
        print("      |o |  |,'\       ,   ,''|  |  |  |  ")
        print("     vV\|/vV|`-'\  ,---\   | \Vv\hjwVv\//v")
        print("                _) )    `. \ /")
        print("               (__/       ) )")
        print("                         (_/")
        print("Завершение работы программы")
        print("До свидания!"+bcolors.ENDC)
        return 0
      else:
        print(bcolors.FAIL+"Такой опции нет. Попробуйте цифры от 1 до 5"+bcolors.ENDC)
        
        
ConsoleInterface()

