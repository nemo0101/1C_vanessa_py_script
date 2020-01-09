# Пример скрипта для автоматического прогона тестов для конфигураций 1С при помощи Vanessa-automation
[Скачать Ванессу](https://github.com/Pr-Mex/vanessa-automation)

* Системные требования:
	  Чем больше тем лучше.
	  Постоянно происходит копирование файлов и обращение к 1С.

# При запуске скрипт делает:
---
1. Запуск скрипта происходит из файла main.py. Скрипт делится на два процесса: процесс основной программы и процесс "сервера" "следящего" за работой процессов и убивающего их. Процессы обмениваются сообщениями. На данный момент отладка работы процессов не закончена.
---
2. Инициализируются настройки. Все настройки собраны в одном месте в файле param.py. Т.е. для простоты все настройки задаются прямо в коде приложения в одном месте.
---
3. Предполагается, что скрипт работает на компьютере для проведения тестов, далее "раннер", а нужные для работы файлы копируются из другого компьютера, далее "компьютер пользователя". Как должны располагаться файлы на "компьютере пользователя" описано в файле param.py.
По очереди вызываются скрипты:
   * "раннер" устанавливает соединение с "компьютером пользователя" при помощи NET USE.
   * "раннер" копирует себе нужные для работы файлы с "компьютера пользователя" при помощи XCOPY. Копируются файлы .cf(версия конфигурации которую нужно протестировать), .dt(базы с наполнением для тестов), тесты в формате .txt, vanessa-automation. Есть возможность указать в настройках, что бы файлы с тестами вытягивались из git репозитория, а файл .cf формировался из хранилища конфигурации.
   * создаются две базы 1С "менеджер" и "клиент" тестирования. Загружаются .dt. Происходит обновление клиента на .cf. Запускаются автотесты согласно очереди указанной в param.py.
   * формируются логи и автотесты завершившиеся с ошибкой. программа предоставляет возможность запустить ошибочные тесты снова.
---

# Подготовка тестов к запуску:

Тесты, созданные с помощью Ванессы, должны быть перенесены в файл с форматом .txt. Начало и конец теста должны быть отмечены специальными тегами:
#!$название%имя_пользователя - начало теста
#$! - конец теста
Т.е. в одном файле .txt может быть большая "лапша" текста сценариев разделенная данными тэгами. Скрипт сам "разрежет" по тэгам файл создав множество тестов, для каждого будет предоставлена чистая эталонная база и отдельный запуск. Если в теге начала теста после знака % стоит имя пользователя и в настройках файла param.py указано USER = 'take_from_testname', то пользователь для теста будет браться из этого тэга начала теста.
	Так же есть возможность примитивной линковки тестов. Можно сделать так, что к каждому "отрезанному" по тэгам тесту будет "прилепляться" дополнительный тест в начало и в конец. За это отвечают настройки ADD_HEAD, ADD_TAIL в файле param.py. Это нужно например для обеспечения наилучшего покрытия 1С тестами за один прогон. Если большой тест остановится по ошибке, то далее будет запущен следующий тест и часть программы будет не проверена. Если в тесте есть множество независящих друг от друга сценариев их разумно вынести в отдельные тесты, ничего не меняя, а просто правильно расставив тэги. Если настроить ADD_HEAD то к каждому такому "отрезанному" тесту будет добавляться "шаг" для запуска плюс любые дополнительные шаги которые вы укажите. 
Таким образом при тестировнии "отрезанный" тест с ошибкой "упадет", но пройдут другие тесты. Но лучше изначально проектировать тесты правильно.

---

* Почему сделано именно так, ведь у Ванессы множество настроек можно было использовать их в некоторых ситуациях?
  	 Девиз скрипта - меньше полагаться на сторонние решения и больше использовать питон или проверенные консольные команды(не 1С). Например, в конфигурационном файле для Ванессы установлен режим закрытия себя и закрытия клиентской базы если тест завершился или найдена ошибка. На данный момент, если ошибка возникает в "особых" местах, Ванесса закрывает себя, но не закрывает клиент тестирования. В таких случаях программа убивает клиент самостоятельно, потому, что следит за процессами. Кроме того консольные команды 1С могут не работать в зависимости от версии платформы. Тогда тесты можно выполнять только на более стабильной версии.

* Зачем было все настройки указывать прямо в скрипте?
  	Для простоты. Скрипт написан на скорую руку и многие вещи нужно переделать или доделать.

* Зачем соединять строки плюсиками есть же замечательный 'str'.format() ?
  	Кому как удобно.





