# -*- coding: utf8 -*
#28nov19kg
#python 3.7.1

from os import path, getpid


'''
param.py - все настройки программы (сценарии+параметры)
*
Внутри функции ret_param_dict() правильно должны быть заполнены следующие переменные:

build_files - каталог на компьютере(в нашем примере "sr") из которого копируются все данные на машину где будет проходить тест.
  в каталоге должны быть тесты, файл cf конфигурации, файлы dt баз мэнеджера и клиента тестирования, каталоги с Ванессой.
  что бы не править все настройки все вышеперчисленные файлы должны быть расположеный в подкаталогах следующим образом:
  1. пример пути до каталога: '\\\\Kuznetsov-GI.dept07\\Users\\Kuznetsov_g\\BuildAddFiles\\Retail\\sr'
  2. карта подкаталогов и их наполнения:
    +-- sr
    |
    +---+-- cf
        |
        +---+-- 1Cv8.cf (файл конфигурации на которой будут проводится тесты)
        |
        +-- model
        |
        +---+-- manager.dt (файл мэнэджера тестирования, должен иметь имя "manager.dt")
        |   |
        |   +-- client_1.dt (эталоны баз для тестирования, имена задаются в функции "return_scenario()")
        |   |
        |   +-- client_2.dt
        |
        +-- platforms
        |
        +---+-- 8.3.15.1656 (папка с платформой, такое же название должно быть у переменной "platform_number")
        |
        +-- tests
        |
        +---+-- test.txt (текстовый файл с выгруженным после записи тестом, может быть много)
        |   |
        |   +-- head.txt (сценарий который должен прикрепляться к началу или концу основных тестов, может быть много)
        |
        +-- vanessa (каталог с Ванессой)
        |
        +---+-- vanessa-automation
            |
            +-- vanessa-tools


platform_number - имя папки(номер платформы) с определенной версией платформы в папке с файлами для теста.
platform - каталог платформы на компьютере где будет проводится тестирование
START_1cestart - каталог с файлом "1cestart.exe" на компьютере где будет проводится тестирование

NET_DOMAIN, NET_USER, NET_PASSWORD - данные о компьютере с которого будет копирвоаться папка с тестовыми файлами (в нашем примере "sr")

*

Функции return_scenario() возвращает список словарей.
каждый словарь в списке это настройки для прогона одного набора тестов.
Возможное содержание такого словаря:
  PREPARE_MODE - (True/False) копировать или нет данные с компьютера где находится папка с файлами для тестов.
  DT - ('role.dt') имя базы-эталона для данного тестирования
  ADM_USER - ('Администратор') пароль администратора от базы
  USER - ('take_from_testname'/'Кассир') пароль, задается один для всего набора тестов или берется из имени каждого теста(имя задается в специальных комментариях в файле общего теста) 
  TEST_FILE - ('role.txt') имя текстового файла с общим, выгруженным после записи, тестом
  ADD_HEAD - ('only_start'/'имя-файла.txt') - имя файла со сценарием, который должен проходить перед каждым тестом из данного набора. если такой сенарий не нужен, то указать "". 
    если нужно добавить тольлко шаг запуска теста, то следует указать 'only_start'.
  ADD_TAIL - ('имя-файла.txt') - имя файла со сценарием, который должен проходить после каждого теста из данного набора. если такой сенарий не нужен, то указать ""
'''



def ret_param_dict():
    current_directory = path.abspath(__file__)
    current_directory = path.split(current_directory)[0]
    current_directory = path.split(current_directory)[0]
    print('каталог со скриптом: ' + current_directory)
    print('----------------------------------------------- \n')
    
    pid_curr_proc = str(getpid())
    print('PID: ' + pid_curr_proc)

    platform_number = '8.3.15.1656'
    platform = 'C:\\Program Files (x86)\\1cv8\\' + platform_number
    build_files = '\\\\Kuznetsov-GI.dept07\\Users\\Kuznetsov_g\\BuildAddFiles\\Retail\\sr'

    storage = current_directory + '\\TEST_CATALOG'
    work = storage + '\\work\\'
    final_log = current_directory + '\\FINAL_LOG\\'

    param_dict = dict(REPO_TRUNK = '8.3.15.1656;;КузнецовГ;',
                      BUILD_FILES_Trunk = build_files,
                      PLATFORM_PATH = build_files + '\\platforms\\' + platform_number,
                      PLATFORM_PATH_ON_RUNNER = platform + '\\',
                      START_PL_1C = '\"' + platform + '\\bin\\1cv8.exe\"',
                      PID = pid_curr_proc,

                      START_1cestart = '\"C:\\Program Files (x86)\\1cv82\\common\\1cestart.exe\"',

                      BUILD_PATH = '\\\\builder-fat.dept07\\1c',
                      VANESSA_PATH = build_files+'\\vanessa\\vanessa-automation',
                      VANESSA_TOOLS = build_files+'\\vanessa\\vanessa-tools',
                      TEST_CATALOG = storage,
                      VANESSA_ON_RUNNER = storage + '\\vanessa\\vanessa-automation\\',
                      VANESSA_TOOLS_ON_RUNNER = storage + '\\vanessa\\vanessa-tools\\',
                      VANNESSA_EPF = storage + '\\vanessa\\vanessa-automation\\vanessa-automation.epf',
                      TESTS_PATH = build_files + '\\tests',
                      TESTS_ON_RUNNER = storage + '\\tests\\',
                      MODEL_PATH = build_files + '\\model',
                      MODEL_ON_RUNNER = storage + '\\model\\',
                      MODEL_ON_RUNNER_CURRENT_DT = '',
                      WORK_PATH = work,
                      WORK_PATH_BASE_M = work + 'base_M',
                      WORK_PATH_BASE_C = work + 'base_C',
                      WORK_PATH_BASE_CURR = '',
                      CF_PATH = build_files + '\\cf',
                      LOG_PATH = work + 'log.txt',
                      MODEL_ADMIN_USER = '',
                      MODEL_USER = '',

                      NET_DOMAIN = 'dept07',
                      NET_USER = 'Kuznetsov_G',
                      NET_PASSWORD = 'jlbyldfnhb',

                      REPO_PATH = 'tcp:\\\\anteros.dept07:4542\\Storage2_3_1',
                      REPO_VER = '657',
                      REPO_USER = 'КузнецовГ',
                      REPO_PASSWORD = '',

                      ESC_VANESSA = 'Истина',
                      ESC_TEST_CLIENT = 'Истина',
                      FINAL_LOG = final_log,
                      STORAGE_CURR_1CD = '',
                      
                      START_TIME = '',
                      END_TIME = ''
                          )

    return param_dict



def return_scenario():
    return [
        dict(PREPARE_MODE = True,
             DT = 'role.dt',
             ADM_USER = 'Администратор',
             USER = 'take_from_testname',
             TEST_FILE = 'role_test.txt',
             ADD_HEAD = 'only_start',
             ADD_TAIL = ''
        ),
        dict(PREPARE_MODE = False,
             DT = 'rmk.dt',
             ADM_USER = 'Администратор',
             USER = 'Администратор',
             TEST_FILE = 'rmk_test.txt',
             ADD_HEAD = 'addit_strings_head_rmk',
             ADD_TAIL = ''
        )
    ]
