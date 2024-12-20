### --- День 9: Фрагментатор диска ---

Очередное нажатие на кнопку переносит вас в знакомые коридоры, где обитают дружелюбные амфифоды! Хорошо, что у каждого из вас есть своя мини-субмарина. Историки уплывают в поисках Вождя, в основном врезаясь прямо в стены.

Пока Историки быстро осваивают управление субмаринами, вы замечаете амфифода в углу, который пытается упорядочить файлы на своём компьютере. Он хочет добиться более непрерывного свободного пространства, сжимая все файлы влево, но его программа не работает. Вы предлагаете помочь.

Он показывает вам карту диска (входные данные задачи), которую он уже подготовил. Например:

```
2333133121414131402
```


Карта диска использует плотный формат для представления расположения файлов и свободного места на диске. Цифры чередуются, указывая длину файла и длину свободного пространства.

Таким образом, карта диска вида `12345` будет означать: файл длиной 1 блок, за ним 2 свободных блока, затем файл длиной 3 блока, 4 свободных блока, и затем файл длиной 5 блоков. Карта `90909` будет означать три файла по 9 блоков каждый подряд (без свободного места между ними).

Каждый файл на диске имеет свой ID, исходя из порядка появления файлов до их перестановки, начиная с ID 0. Таким образом, у карты `12345` есть три файла:
- Файл длиной 1 блок с ID 0,
- Файл длиной 3 блока с ID 1,
- Файл длиной 5 блоков с ID 2.

Используя один символ для каждого блока, где цифры обозначают ID файла, а `.` — свободное пространство, карта `12345` будет выглядеть так:

```
0..111....22222
```


Первый пример из условия `2333133121414131402` будет представлять блоки так:

```
00...111...2...333.44.5555.6666.777.888899
```


Амфифод хочет перемещать блоки файлов по одному, начиная с конца диска в самую левую доступную свободную позицию (пока не исчезнут все разрывы между блоками файлов). Для карты `12345` этот процесс идёт так:

```
Исходно: 0..111....22222
 Шаг 1: 02.111....2222. 
 Шаг 2: 022111....222.. 
 Шаг 3: 0221112...22... 
 Шаг 4: 02211122..2.... 
 Шаг 5: 022111222......
```


Первый длинный пример требует больше шагов, в итоге файлы сдвигаются до уплотнённого состояния. После всех перестановок мы должны вычислить контрольную сумму (checksum) файловой системы.

Для вычисления контрольной суммы:
1. Просматриваем итоговое состояние диска слева направо.
2. Для каждого блока файла умножаем позицию этого блока на ID файла.
3. Складываем все полученные результаты. Свободные блоки пропускаем.

В примере с `12345`, после уплотнения, вычисление идёт так: для первых нескольких блоков — позиция 0 * ID 0 = 0, позиция 1 * ID 0 = 0, позиция 2 * ID 9 = 18, позиция 3 * ID 9 = 27, позиция 4 * ID 8 = 32 и так далее. В примере сумма в итоге равна 1928.

Ваша задача — уплотнить жёсткий диск амфифода по описанному процессу и вычислить итоговую контрольную сумму.

**Вопрос**: Какова результирующая контрольная сумма файловой системы?

### --- Часть Вторая ---

По завершении сразу становится ясно два момента. Во-первых, на диске теперь действительно гораздо больше непрерывного свободного пространства, о чём и мечтал амфифод. Во-вторых, компьютер работает значительно медленнее! Возможно, внесение всей этой фрагментации файловой системы было плохой идеей?

У амфифода уже есть новый план: вместо перемещения отдельных блоков он хочет попробовать уплотнить файлы на диске, перемещая целые файлы сразу.

Теперь, попытайтесь перемещать целые файлы в самое левое место, где есть достаточно свободного пространства для размещения всего файла. Пытайтесь переместить каждый файл ровно один раз, в порядке уменьшения номеров идентификаторов файлов (начиная с файла с наибольшим ID). Если слева от файла нет достаточно длинного свободного участка, чтобы разместить его целиком, файл не перемещается.

Первый пример из предыдущего этапа теперь выглядит по-другому:

```
00...111...2...333.44.5555.6666.777.888899
0099.111...2...333.44.5555.6666.777.8888..
0099.1117772...333.44.5555.6666.....8888..
0099.111777244.333....5555.6666.....8888..
00992111777.44.333....5555.6666.....8888..
```


Процесс обновления контрольной суммы файловой системы остаётся тем же; теперь контрольная сумма в этом примере равна 2858.

Начните сначала, уплотняя жёсткий диск амфифода по новому методу. Какова результирующая контрольная сумма файловой системы?

