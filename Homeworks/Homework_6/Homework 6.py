# ## Task 1_14 # Розробіть функцію total_salary(path) (параметр path - шлях до файлу), яка буде розбирати текстовий файл
# # і повертати загальну суму заробітної плати всіх розробників компанії.


# def total_salary(path): #(параметр path - шлях до файлу)
#     fh = open(path, 'r')
#     t_slr = 0
#     while True:
#         line = fh.readline()
#         if not line:
#             break
#         print(line)
#         name, salary = line.split(",")
#         t_slr += int(salary)
#         print(t_slr)

#     fh.close()
#     print(t_slr)
#     return float(t_slr)

# ## Task 2_14 #запишіть вміст employee_list у файл, використовуючи режим "w"
# def write_employees_to_file(employee_list, path):
#     all =[]
#     fh = open(path, 'w')
#     for d in employee_list:
#         for e in d:
#             all.append(e+'\n')
#     str = ''.join(all)
#     fh.write(str)
#     fh.close()

# ## Task 3_14 #Виконаємо тепер зворотнє завдання і створимо функцію read_employees_from_file(path),
# #  яка читатиме дані з файлу та повертатиме список співробітників у вигляді:
# #['Robert Stivenson,28', 'Alex Denver,30', 'Drake Mikelsson,19']
# def read_employees_from_file(path):
#     all = []
#     fh = open(path, 'r') # відкр файл для читання
#     while True:
#         line = fh.readline() # читання вмісту файлу по рядках #Robert Stivenson,28
                                                                #Alex Denver,30
                                                                #Drake Mikelsson,19
#         if not line:
#             break
#         line = line.replace("\n","")  #символ кінця рядка \n під час читання даних із файлу необхідно прибирати
#                                     #при додаванні прочитаного рядка до списку
#         all.append(line)

#     # print(all)
#     fh.close()
#     return(all)

## Task 4_14 #у файл (параметр path - шлях до файлу) буде додавати співробітника
            # (параметр record) у вигляді рядка "Drake Mikelsson,19".
# def add_employee_to_file(record, path):

#     fh = open(path, 'a')
#     fh.write(record + '\n')
#     fh.close()

## Task 5_14
# get_cats_info(path):
#     cats_info = [] #порожній список cats_info, у який будемо додавати словники із даними котів.
#     with open(path, 'r') as file: # Відкриваємо файл path у режимі "r" за допомогою менеджера контексту with open(...) as file:. Це дозволяє автоматично закрити файл після виконання блоку with.
#         for line in file:
#             cat_data = line.strip().split(',') #strip() видаляємо зайві пробіли з початку та кінця рядка.  split(',') розділяємо рядок на складові, використовуючи кому як роздільник.
#             cat = {'id':cat_data[0], 'name':cat_data[1], 'age': cat_data[2]}
#             cats_info.append(cat) #Додаємо словник cat до списку cats_info
#     return(cats_info)  #Після проходження всіх рядків у файлі, повертаємо список cats_info.


# ## Task 6_14
# def get_recipe(path, search_id): #дані в файлі "recipe.txt"
#     recipe = []
#     with open(path, 'r') as fh:
#         for line in fh:
#             rec_data = line.strip().split(',')
#             if rec_data[0] == search_id:
#                 recipe = {'id':rec_data[0], 'name': rec_data[1], 'ingredients':  rec_data[2:]}
#                 return(recipe)
#             else:
#                 return None

# ## Task 7_14 #
# def sanitize_file(source, output): #функцію sanitize_file(source, output), що переписує у текстовий файл output вміст текстового файлу source,
# #очищений від цифр.
# #Текст в файлі  source: 'test text 123test'
#     with open(source, 'r') as fh:
#         text = fh.read()
#     sanitized_text = ''.join(filter(lambda x: not x.isdigit(), text)) #використовуємо функцію filter з лямбда-функцією, щоб відфільтрувати цифри з тексту
#     #Далі ми з'єднуємо отриманий список символів у рядок, використовуючи метод join
#     with open(output, 'w') as fh:
#         fh.write(sanitized_text) #записуємо очищений вміст у новий файл, використовуючи метод write

# ## Task 8_14 # [
#     [{   "name": "Kovalchuk Oleksiy", "specialty": 301, "math": 175, "lang": 180, "eng": 155,},
#     {   "name": "Ivanchuk Boryslav", "specialty": 101, "math": 135, "lang": 150,  "eng": 165,},
#     {   "name": "Karpenko Dmitro",  "specialty": 201, "math": 155, "lang": 175,  "eng": 185,},
# ]
# def save_applicant_data(source, output):
#      with open(output, "w") as fh:
#          for applicant in source:
#              name = applicant["name"]
#              specialty = str(applicant["specialty"])
#              math = str(applicant["math"])
#              lang = str(applicant["lang"])
#              eng = str(applicant["eng"])
#              fh.write("{},{},{},{},{}\n".format(name, specialty, math, lang, eng))

 ## Task 9_14 # Є два рядки у різних кодуваннях - "utf-8" та "utf-16".
             #Реалізуйте функцію is_equal_string(utf8_string, utf16_string),
             #  яка повертає True, якщо рядки дорівнюють собі, і False — якщо ні.
# def is_equal_string(utf8_string, utf16_string):

#      # print(utf8_string) # перевірка, щож там за рядки
#      # print(utf16_string)# перевірка, щож там за рядки

#      # перетворити байтів у рядки
#      utf8_dec = utf8_string.decode('utf-8')
#      utf16_dec = utf16_string.decode('utf-16')

# #     # порівняти рядки
#      if utf8_dec == utf16_dec:
#          return True
#      else:
#          return False

## Task 10_14 #
# def save_credentials_users(path, users_info): #зберігає інформацію про користувачів з паролями в бінарний файл.
#                                             #users_info - словник типу {'andry':'uyro18890D', 'steve':'oppjM13LL9e'}
#                                              #ключ — логін (username) користувача, а значення — його пароль (password)
#      with open(path, 'wb') as fh:            #Відкрийте файл для запису
#          for username, password in users_info.items():
#              data = f'{username}:{password},\n'.encode('utf-8') #збережіть ключ та значення зі словника users_info у вигляді
#                                              # окремого рядка username:password для кожного елемента словника users_info
#              fh.write(data)

## Task 11_14 # ЧИТАННЯ БІНАРНИХ ФАЙЛІВ У PYTHON
# def get_credentials_users(path): #повертає список рядків із бінарного файлу, from Task 10_14

#     with open(path, 'rb') as fh:
#         lines = [line.decode('utf-8').strip() for line in fh]
#     return lines

## Task 12_14 #Функція get_credentials_users із попереднього завдання повертає нам список рядків username:password:
                                #['andry:uyro18890D', 'steve:oppjM13LL9e']
# import base64


# def encode_data_to_base64(data):#приймає у параметрі data зазначений список, виконує кодування кожної пари username:password
    # у формат Base64 та повертає список із закодованими парами username:password у вигляді:
    #['YW5kcnk6dXlybzE4ODkwRA==', 'c3RldmU6b3Bwak0xM0xMOWU=']

    # encoded_data = []
    # for item in data:
    #     encoded_item = base64.b64encode(item.encode('utf-8')).decode('utf-8')
    #     encoded_data.append(encoded_item)
    # return encoded_data

## Task 13_14
import shutil

# for shortcut, description in shutil.get_archive_formats():
#     print('{:<10} | {:<10}'.format(shortcut, description))
# def create_backup(path, file_name, employee_residence):


#     backup_folder = shutil.make_archive('backup_folder', 'zip') # створять файл backup.zip в поточній робочій папці
    # archive_name = shutil.make_archive('backup_folder', 'zip', 'some_folder/inner') # в archive_name буде рядок з повним шляхом до архіву
                                                                # 'some_folder/inner' -запакувати іншу папку, можна вказати
                                                                #  шлях до папки третім аргументом:
