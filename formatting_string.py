from string import Template

""" Форматирование строк  % """
team1_num = 5
team2_num = 6
print("В команде Мастера кода участников: %s ! " % team1_num)
print("В команде Мастера кода участников: %s и %s ! " % (team1_num, team2_num))

""" Форматирование строк  .format()"""
score_2 = 42
team1_time = 18015.2
print("Команда Волшебники данных решила задач: {0} за {1} !".format(score_2, team1_time))
print("Волшебники данных решили задачи за {} с !".format(team1_time))

""" Форматирование строк  f """
score_1, score_2 = 40, 42
tasks_total = 82
time_avg = 350.4
challenge_result = 'победа команды Мастера кода!'
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")

""" Форматирование строк @Шаблонные строки 'framework Template Strings' """
name = 'Teacher'
t = Template('Hello, $name!')
print(t.substitute(name=name))

templ_string = 'Hey $name, here a $new FrameWork!'
framework = 'new'
print(Template(templ_string).substitute(name=name, new=framework))








