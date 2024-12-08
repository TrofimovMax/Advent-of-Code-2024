### --- День 15: Библиотека Линз ---

Новонастроенное параболическое зеркало направляет весь собранный свет на точку на стороне ещё одной горы — самой высокой горы на Острове Лавы. Подойдя к горе, вы обнаруживаете, что свет собирается на стене большого комплекса, врезанного в склон горы.

Под большим знаком "Лавовая Производственная Фабрика" и рядом с меньшей вывеской "Опасность — за этой точкой требуется защитное снаряжение" вы находите дверь.

Зайдя внутрь, вы сразу же сталкиваетесь с немного перепуганным оленем в защитных очках и каске. Олень подводит вас к полке с очками и касками (вы быстро подбираете подходящие) и ведёт вас дальше вглубь здания. В какой-то момент вы проходите мимо кнопки с едва заметным отпечатком носа и надписью "НАЖАТЬ ДЛЯ ПОМОЩИ". Неудивительно, что вас так быстро загрузили в требушет!

Вы проходите через последние двери, окружённые ещё более угрожающими предупреждающими знаками, и оказываетесь, вероятно, в комнате, где собирается весь внешний свет. Любуетесь большим ассортиментом линз для дополнительного фокусирования света, и тут олень подаёт вам книгу под названием "Руководство по Инициализации".

"Здравствуйте!", бодро начинает книга, явно не замечая взволнованного оленя, читающего через ваше плечо. "Эта процедура позволит вам запустить Лавовую Производственную Фабрику — и при этом ничего лишнего не сожжётся или не расплавится!"

"Прежде чем начать, убедитесь, что вы готовы использовать алгоритм 'Holiday ASCII String Helper' (приложение 1A)." Вы открываете приложение 1A. Олень наклоняется поближе, заинтересованно разглядывая страницы.

Алгоритм HASH — это способ преобразовать любую строку символов в одно число от 0 до 255. Чтобы выполнить алгоритм HASH для строки, начните с текущего значения 0. Затем для каждого символа строки по порядку выполните следующие шаги:

1. Определите ASCII-код текущего символа строки.
2. Увеличьте текущее значение на этот ASCII-код.
3. Перемножьте текущее значение на 17.
4. Возьмите остаток от деления текущего значения на 256.

После выполнения этих шагов для каждого символа строки итоговое текущее значение будет результатом алгоритма HASH.

Например, чтобы вычислить результат для строки "HASH":

- Начальное значение: 0
- Первый символ 'H' (код 72):
  - Текущее значение: 0 + 72 = 72
  - 72 * 17 = 1224
  - 1224 % 256 = 200 (остаток)
- Второй символ 'A' (код 65):
  - Текущее значение: 200 + 65 = 265
  - 265 * 17 = 4505
  - 4505 % 256 = 153
- Третий символ 'S' (код 83):
  - Текущее значение: 153 + 83 = 236
  - 236 * 17 = 4012
  - 4012 % 256 = 172
- Четвёртый символ 'H' (код 72):
  - Текущее значение: 172 + 72 = 244
  - 244 * 17 = 4148
  - 4148 % 256 = 52

Итог: HASH("HASH") = 52.

Инициализационная последовательность (ваши входные данные) — это разделённый запятыми список шагов для запуска Лавовой Производственной Фабрики. Игнорируйте символы новой строки при парсинге. Для проверки правильности работы вашего алгоритма HASH, книга предлагает сложить результаты вычисления HASH для каждого шага в последовательности.

Например:

```
rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
```


Эта инициализационная последовательность задаёт 11 отдельных шагов. Результаты для каждого шага таковы:

- `rn=1` = 30.
- `cm-` = 253.
- `qp=3` = 97.
- `cm=2` = 47.
- `qp`- = 14.
- `pc=4` = 180.
- `ot=9` = 9.
- `ab=5` = 197.
- `pc`- = 48.
- `pc=6` = 214.
- `ot=7` = 231.

Сумма этих результатов равна 1320.

Однако олень утащил страницу с ожидаемым проверочным числом и сейчас бегает с ней по помещению.

Ваша задача: запустить алгоритм HASH для каждого шага в вашей инициализационной последовательности и вывести сумму полученных значений.

(Инициализационная последовательность — это одна длинная строка; будьте внимательны при копировании.)

