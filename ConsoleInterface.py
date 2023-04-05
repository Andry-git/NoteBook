# from scr import parserJSON as J
import parserJSON as J
import TimeInterval as TI


"""
readJSON
delTask
addTask
updateTask
printTaskALL"""


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
                print()

                print("1) На сегодня")
                print("2) За всё время")
                print("3) Ввести интервал")
                # print("4) За всё время")
                print("4) Назад")
                print()

                choice1 = input("Введите выбор: ")
                print()
                if (choice1 == "1"):
                    #Планы на сегодня
                    J.printTodayTasks(J.readJSON())
                    print()
                elif (choice1 == "2"):
                    #Планы За всё время
                    J.printTaskALL(J.readJSON())
                    print()

                elif (choice1 == "3"):
                    #интервал
                    print("Ввод границ временного интервала ")
                    dateTimeStart = input("Введите дату и время начала (дд/мм/гггг, чч:мм): ")
                    dateTimeEnd = input("Введите дату и время окончания (дд/мм/гггг, чч:мм): ")
                    print()
                    if not dateTimeStart or not dateTimeEnd or dateTimeStart[2]!="/" or dateTimeEnd[2]!="/":
                        print(bcolors.FAIL + "Вводимые поля пусты или ошибка формата" + bcolors.ENDC)
                    else:
                        J.printTasksInInterval(J.readJSON(), dateTimeStart, dateTimeEnd)
                        print()
                else:
                    break

                # elif (choice1 == "4"):
                #     #Планы за всё время

                # J.printTaskALL(J.readJSON())
                # print()
                break

                # else:
                # break

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
            dateTimeStart = input("Введите дату и время начала (дд/мм/гггг, чч:мм): ")
            if dateTimeStart in J.readJSON():
                print(bcolors.FAIL + "На это время есть план" + bcolors.ENDC)
                # break
            else:
                dateTimeEnd = input("Введите дату и время окончания (дд/мм/гггг, чч:мм): ")
                
                if not dateTimeStart or not dateTimeEnd or dateTimeStart[2]!="/" or dateTimeEnd[2]!="/":
                        print(bcolors.FAIL + "Вводимые поля пусты или ошибка формата" + bcolors.ENDC)
                
                elif not TI.ProverkaInterval(dateTimeStart, dateTimeEnd):
                    print(bcolors.FAIL + "Конечное время меньше начального" + bcolors.ENDC)
                    
                elif J.checkInterval(J.readJSON(), dateTimeStart, dateTimeEnd):
                    print(bcolors.FAIL + "На это время есть план" + bcolors.ENDC)
                    
                else:
                    prioritet = input("Введите приоритет задачи: ")
                    description = input("Введите описание плана: ")
                    
                    # if not dateTimeStart or not dateTimeEnd or dateTimeStart[2]!="/" or dateTimeEnd[2]!="/":
                        # print(bcolors.FAIL + "Вводимые поля пусты или ошибка формата" + bcolors.ENDC)

                    # Создание
                    # else:
                    J.addTask(dict_data=J.readJSON(),
                              key=dateTimeStart,
                              start=dateTimeStart,
                              end=dateTimeEnd,
                              name=name,
                              text=description,
                              priority=prioritet)
                    print(bcolors.OKGREEN + "План успешно создан" + bcolors.ENDC)
        elif (choice == "3"):
            print(bcolors.BOLD + bcolors.WARNING)
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
            # name = input("Введите название плана: ")
            date = input("Введите дату этого плана и время начала: ")
            if not date:
                print(bcolors.FAIL + "Вводимые поля не должны быть пусты" + bcolors.ENDC)
            elif not date in J.readJSON():
                print(bcolors.FAIL + "Такого плана к изменению нет" + bcolors.ENDC)
            else:
                print("Изменяем")
                J.printTask(J.readJSON(), date)
                nameNew = input("Введите название: ")
                dateTimeStartNew = input("Введите дату и время начала (дд/мм/гггг, чч:мм): ")
                dateTimeEndNew = input("Введите дату и время окончания (дд/мм/гггг, чч:мм): ")
                if not dateTimeStart or not dateTimeEnd or dateTimeStart[2]!="/" or dateTimeEnd[2]!="/":
                    print(bcolors.FAIL + "Вводимые поля пусты или ошибка формата" + bcolors.ENDC)
                
                elif not TI.ProverkaInterval(dateTimeStart, dateTimeEnd):
                    print(bcolors.FAIL + "Конечное время меньше начального" + bcolors.ENDC)
                elif J.checkIntervalUpdate(J.readJSON(), dateTimeStartNew, dateTimeEndNew, date):
                    print(bcolors.FAIL + "На это время есть план" + bcolors.ENDC)
                else:
                    prioritetNew = input("Введите приоритет задачи: ")
                    descriptionNew = input("Введите описание плана: ")
                    # if not dateTimeStart or not dateTimeEnd or dateTimeStart[2]!="/" or dateTimeEnd[2]!="/":
                        # print(bcolors.FAIL + "Вводимые поля пусты или ошибка формата" + bcolors.ENDC)
                        # break
                    # else:
                    J.updateTask(J.readJSON(),
                                 key=date,
                                 start=dateTimeStartNew,
                                 end=dateTimeEndNew,
                                 name=nameNew,
                                 text=descriptionNew,
                                 priority=prioritetNew)
                    print(bcolors.OKGREEN + "Изменение прошло успешно" + bcolors.ENDC)
                    print()
                """
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
                        break"""
        elif (choice == "4"):
            print(bcolors.OKGREEN)
            print("  /\_/\*")
            print(" ( o.o )")
            print("  > ^ <")
            print("Удаление плана")
            # name = input("Введите название плана: ")
            date = input("Введите дату начала этого плана: ")
            if not date:
                print(bcolors.FAIL + "Вводимые поля не должны быть пусты" + bcolors.ENDC)
            elif not date in J.readJSON():
                print(bcolors.FAIL + "Нет таких данных для удаления" + bcolors.ENDC)
                # break
            else:
                while True:
                    print("Вы уверены, что хотите удалить?")
                    print("1) Да")
                    print("2) Нет")
                    choice4 = input("Введите выбор: ")

                    if (choice4 == "1" or choice4 == "Да"):
                        # УДАЛЕНИЕ РАЗ И НАВСЕГДА
                        J.delTask(J.readJSON(), key=date)
                        print(bcolors.OKGREEN + "Удаление произошло успешно" + bcolors.ENDC)
                        break
                    else:
                        print(bcolors.FAIL + "Удаление отменено" + bcolors.ENDC)
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
            print("До свидания!" + bcolors.ENDC)
            return 0
        else:
            print(bcolors.FAIL + "Такой опции нет. Попробуйте цифры от 1 до 5" + bcolors.ENDC)


if __name__ == '__main__':
    ConsoleInterface()
