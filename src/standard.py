print("== print関数 ==")
# print("\n== print関数 ==")
# print("aaa", "bbb", "ccc")
# print("python", end="\n")
# print("rudy", end="\n")
# print("aaa", "bbb", "ccc", sep="-")

print("\n== input関数 == ")
# #name = input("名前を入力してください\n")
# #print(f'こんにちは、{name}さん')
# #age = int(input("年齢を入力してください\n"))
# #print(f'あなたは{age}歳です')

# #変数への代入方法(多重代入)
print("\n== 変数への代入方法(多重代入) ==")
# first_name, last_name = "suzuki", "taro"
# print(first_name, last_name)
# first_name, last_name = last_name, first_name
# print(first_name, last_name)

# #動的型付け
print("\n== 動的型付け ==")
# a=100
# print("a=" , a)
# a="hyaku"
# print("a= " + a)

# #snake_case形式
# #定数(大文字)形式
print("\n== 定数(大文字)形式 ==")
# print("POINT='ポイント'")

# #型確認
print("\n== 型確認 ==")
# a = "a"
# b = 1
# c = 1.1
# d = True
# e = {}
# f = []
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))

# #キャスト（型変換）
print("\n== キャスト（型変換） ==")
# print("int→str：", str(1))
# print("str→int：", int("1"))
# print("str→float：", float("1.1"))

# #真偽値
print("\n== 真偽値 ==")
# age = 10
# print("age= " , age)
# adult = 20
# print("adult= " , adult)
# isAdult = age >= adult
# print("isAdult=" , isAdult)

# print("数値が0の場合", bool(0))
# print("数値が0以外場合", bool(2))
# print("文字列が空欄の場合", bool(""))
# print("文字列が空欄以外場合", bool("ああ"))
# print("配列が初期化の場合", bool([]))
# print("配列が初期化以外場合", bool([0, 1]))

# #datetime型
print("\n== datetime型 ==")
# import datetime
# today = datetime.date.today()
# print("today=",today)
# print("2030年01月01日を表示", datetime.date(2030,1,1))
# now = datetime.datetime.now()
# print("time=", now)
# print("10時50分30秒を表示=", datetime.time(10,50,30))
# print("現在時刻を表示=", datetime.time(now.hour, now.minute, now.second))
# current = datetime.datetime.now()
# print("現在日時=", current)
# ten_days_age = now - datetime.timedelta(days=10)
# print("現在日時から10日前=", ten_days_age)
# ten_days_later = now + datetime.timedelta(days=10)
# print("現在日時から10日後=", ten_days_later)
# two_hours_age = now - datetime.timedelta(hours=2)
# print("現在日時から2時間前=", two_hours_age)
# two_hours_later = now + datetime.timedelta(hours=2)
# print("現在日時から2時間後=", two_hours_later)
# one_week_three_days_age = now - datetime.timedelta(weeks=1, days=3)
# print("現在日時から1週間と3日前=", one_week_three_days_age)
# one_week_three_days_later = now + datetime.timedelta(weeks=1, days=3)
# print("現在日時から1週間と3日後=", one_week_three_days_later)

# #None型
print("\n== None型 ==")
# a = None
# def isNone(a) -> bool:
#     return a == None
# print("isNone=" ,isNone(a))
# a = 1
# print("isNone=" ,isNone(a))

#コレクション型(range型/list型/tuple型/set型/dictionary型)
print("\n== list型 ==")
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)
# nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
# print(f"numsの先頭文字：{nums[0]}")
# print(f"numsの最終文字：{nums[-1]}")
# nums.append("10")
# nums += ["11"]
# print("numsに追加：", nums)
# nums.insert(len(nums),"12")
# print("numsに挿入：", nums)
# nums2 = ["13", "14", "15"]
# nums.extend(nums2)
# print("numsを拡張：", nums)
# print("popで末尾を取り出す", nums.pop())
# print("popでindex指定(14)して値を取り出す", nums.pop(14))
# print("元のnumsの値：", nums)
# nums.remove("13")
# print("removeで13を削除する：", nums)
# del nums[12]
# print("delで12番目を削除する：", nums )

# fruits = ["apple", "banaka", "orange"]
# copy_fruits = fruits.copy()
# fruits[0] = "mango"
# print("一次元配列の場合のコピーの場合：コピー元を変更してもコピー先は変わらない")
# print(f"コピー元：{fruits}")
# print(f"コピー先：{copy_fruits}")

# multi_fruits = [
#     ["apple", "cherry"],
#     ["mango", "banana"],
#     ["orange"]
# ]
# copy_multi_fruits = multi_fruits.copy()
# multi_fruits[0][0] = "kiwi"
# print("多次元配列の場合のコピーの場合：コピー元を変更するとコピー先も変更される")
# print(f"コピー元：{multi_fruits}")
# print(f"コピー先：{copy_multi_fruits}")
# print("多次元配列の場合のコピーの場合：コピー元を変更してもコピー先は変わらない対応")
# import copy
# copy_multi_fruits = copy.deepcopy(multi_fruits)
# multi_fruits[0][0] = "apple"
# print(f"コピー元：{multi_fruits}")
# print(f"コピー先：{copy_multi_fruits}")

print("\n== range型 ==")
# nums = list(range(10))
# print("range型を使用してlist型に0~9までを格納する：", nums)
# print("numsの最大値：", max(nums))
# print("numsの最小値：", min(nums))
# print("numsの合計値：", sum(nums))

# for _ in nums:
#     print(_)

# names = ["taro", "jiro", "saburo"]
# for i in range(len(names)):
#     print(i, names[i])
    
# for i, name in enumerate(names):
#     print(i, name)

# print("\n== tuple型 ==")
# numTuple = (0,)
# numsTuple = (1,2,3,4,5,)
# print(numTuple[0])
# for _ in numsTuple:
#     print(_)

# strTuple = ("a",)
# strsTuple = ("a", "b", "c", "d")
# print(strTuple[0])
# for _ in strsTuple:
#     print(_)

# print("list型をtuple型にする")
# l = [1,2,3,4,5,6,7,8,9,10]
# l = tuple(l)
# print(l)
# print(type(l))

# print("list型は変更可能だがtuple型は変更不可")
# print("list型とtuple型のメモリ比較")
# import sys
# LENGTH = 999999
# l_type = list(range(LENGTH))
# t_type = tuple(range(LENGTH))
# print(f'list:{sys.getsizeof(l_type)}')
# print(f'tuple:{sys.getsizeof(t_type)}')

# def t_func(num):
#     return num+1, num**2

# num = t_func(10)
# print(type(num))
# print(num)
# print(num[0], num[1])

print("\n== set型 ==")
# print("重複のないlist型またはtuple型をset型という")
# s_type = {1,1,2,3,1,4,6,4}
# print(s_type)
# print(type(s_type))
# l_type = [1,1,2,3,1,4,6,4]
# t_type = (1,1,2,3,1,4,6,4)
# print(set(l_type))
# print(set(t_type))

# A_names = {"yamada", "sato", "suzuki"}
# B_names = {"yamada", "suzuki", "takahashi"}
# print(f"A_name:{A_names}")
# print(f"B_name:{B_names}")
# print(f"和集合：{A_names.union(B_names)}")
# print(f"積集合：{A_names.intersection(B_names)}")
# print(f"差集合：{A_names.difference(B_names)}")
# print(f"対称差：{A_names.symmetric_difference(B_names)}")

print("\n== dictionary型 ==")
# colors = {"red":"赤", "blue": "青", "yellow":"黄"}
# print(type(colors))
# print(colors)
# print(f"colors['red']:{colors["red"]}")

# colors = dict(red="赤", blue="青", green="緑")
# print(type(colors))
# print(colors)
# print(f"colors['green']:{colors["green"]}")

# #文字列操作に使う演算子
print("\n== 文字列操作に使う演算子 ==")
# print('+演算子：' , 'suzuki ' + 'taro')
# print('*演算子：' , 'suzuki ' * 5)

# #算術演算子
print("\n== 算術演算子 ==")
# print("乗算(10*2)：", 10*2)
# print("累乗(10**2)：", 10**2)
# print("除算(10/2)：", 10/2)
# print("商(10//3)：", 10//3)
# print("剰余(10%3)：", 10%3)

# #累算演算子
print("\n== 累算演算子 ==")
# a = 10
# print("a=", a)
# a += 1
# print("a+=1", a)
# a -= 1
# print("a-=1", a)

# x = 18
# print("x=", x)
# print("10 < x < 20 ", 10 < x < 20)

# #メモリに保存されるID
print("\n== メモリに保存されるID ==")
# name = "taro"
# print(f'{name}がメモリ上に保存されIDが付与される', name, id(name))
# print(f'{name}がメモリ上に保存されIDが付与される', name, id("taro"))

# #
# s = """
# これは
# 改行を
# 含む
# 文字列です
# """

# ss = "これは\n改行を\n含む\n文字列です"
# print(s)
# print(ss)

# print('docstringは"""で囲む')

print("\n== formatメソッド ==")
# midle = " "
# print("Hi {}{}{}".format(first_name, midle, last_name))
# print("Hi {0}{1}{2}".format(first_name,midle,last_name))
# print("Hi {first_name}{midle}{last_name}".format(first_name=first_name,midle=midle,last_name=last_name))
# pi = 3.141592653589793
# print("円周率は{pi:.2f}です".format(pi=pi))
# amout = 100000
# print("支払金額は{amout:,}円です".format(amout=amout))
# card = """
# ---------
# |{0}     |
# |   {1}   |
# |     {2}|
# ---------"""
# spade = "♠"
# diamond = "♦"
# heart = "♥"
# clover = "☘"
# nums = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
# for num in nums:
#     print(card.format(num.ljust(2,' '), spade, num.rjust(2,' ')))
#     print(card.format(num.ljust(2,' '), diamond, num.rjust(2,' ')))
#     print(card.format(num.ljust(2,' '), heart, num.rjust(2,' ')))
#     print(card.format(num.ljust(2,' '), clover, num.rjust(2,' ')))
    
print("\n== リテラルの整頓にfやrをつける文字列 ==")
print("f文字列")
# greet = f'My name is {first_name} {last_name}.'
# print(greet)
print("r文字列")
# print("C:\\Users\\aaaa\\Documents\\Zoom")
# print(r"C:\Users\aaaa\Documents\Zoom")

print("\n== len関数 ==")
# letter = "Python"
# print(f"{letter}の文字数：", len(letter))

print("\n== strip関数 ==")
# print(f"{letter}の文字からthonを削除した文字列：", letter.strip("thon"))
# space_in_letter = " Python "
# print(f"{space_in_letter.strip()}からspaceを削除した文字列：", space_in_letter.strip())

print("\n== replace関数 ==")
# print(f"{letter}を置換してsimpson：", letter.replace("Py", "").replace("th","simps"))

print("\n== zfill関数 ==")
# print("10を00010にする：", "10".zfill(5))
# today = datetime.date.today()
# now = datetime.datetime.now()
# year = today.year
# month = today.month
# day = today.day
# print(f"今日は{year}年{str(month).zfill(2)}月{str(day).zfill(2)}日です")

print("\n== find関数・index関数 ==")
# search = "abcdefghijklmnopqrstuvwxyz"
# letter = "l"
# print(f"{search}から指定文字{letter}の位置を返す：{search.find(letter)}番目")
# print(f"{search}から指定文字{letter}の位置を返す：{search.index(letter)}番目")

print("\n== find関数とindex関数の相違点 ==")
# letter = "1"
# print(f"find関数は{search}から指定文字{letter}が見つからない場合：{search.find(letter)}を返す")
# print(f"index関数は{search}から指定文字{letter}が見つからない場合：ValueErrorになる")

print("\n== 三項演算子の記述 ==")
# age = 18
# is_adult = True if age >=18 else False
# print(f"{age}は成人かどうか：", is_adult)


# s = 'あいうえお'
# b = s.encode('unicode-escape').decode('unicode-escape')
# print(b)

# s = '\u5927\u8f1d'
# b = s.encode('unicode-escape').decode('unicode-escape')
# print(b)

# text = r"\u516c\u5f66"
# decoded_text = bytes(text, "utf-8").decode("unicode_escape")
# print(decoded_text)

# リスト内包表記
print("\n== 内包表記 ==")
# nums = [1, 2, 3, 4, 5]
# squares = [x**2 for x in nums]
# print("numsの2乗のlist型：", squares)

# セット内包表記
print("\n== セット内包表記 ==")
# number_list = {10 ,20 ,10, 100, 200, 400, 100, 200}
# over_100_set = {x for x in number_list if x >= 100}
# print(over_100_set)

# タプル（ジェネレータ式）
print("\n== タプル（ジェネレータ式） ==")
# my_tubple = tuple((x for x in range(10)))
# print(my_tubple)

# 辞書内包表記
print("\n== 辞書内包表記 ==")
# en_seasons = ["sprint", "summer", "autumn", "winter"]
# jn_seasons = ["春", "夏", "秋", "冬"]
# seasons_dict = {en: jn for en, jn in zip(en_seasons, jn_seasons)}
# print(seasons_dict)

print("\n== 多重辞書内包表記 ==")
# person_info = [
#     {"name": "John","age": 30,"address": "123 Main St","phone": "555-1234"},
#     {"name": "Jane","age": 25,"address": "456 Elm St","phone": "555-5678"},
#     {"name": "Bob","age": 40,"address": "789 Oak St","phone": "555-9012"}
# ]

# person_dict = {}
# for person in person_info:
#     info = {}
#     for key, value in person.items():
#         if key != "name":
#             info[key] = value
#     person_dict[person["name"]] = info
# print(person_dict)

# person_dict = {
#     person["name"]:{key:value for key, value in person.items() if key != "name"} for person in person_info
# }
# print(person_dict)

# all(),any()
print("\n== all(),any() ==")

# list1 = [True, True, True]
# list2 = [False, False, True]
# list3 = [False, False, False]

# print(all(list1))
# print(all(list2))
# print(all(list3))
# print(any(list1))
# print(any(list2))
# print(any(list3))

# print("\n== all(),any() 例 ==")
# subjects = {
#     "japanease":80,
#     "english":70,
#     "math":85,
#     "science":60,
#     "society":50
# }
# print(f'subjects={subjects}')
# print("== subjectsをsubjectに格納しsubjectが80以上の場合値を返す ==")
# print("== all(subject >=80 for subject in subjects.values()) ==")
# result = all(subject >=80 for subject in subjects.values())
# if result:
#     print("all():合格")
# else:
#     print("all():不合格")
    
# print("== subjectsをsubjectに格納しsubjectが80以上の場合値をsujectに設定する ==")
# print("== all( subject for subject in subjects.values() if subject >=80) ==")
# result = all( subject for subject in subjects.values() if subject >=80)
# if result:
#     print("all():合格")
# else:
#     print("all():不合格")
    
    
# 呼び出し可能関数
print("== 呼び出し可能型 関数 callable type ==")
# my_print = print
# my_print("callable type")

# print("== 呼び出し可能型 関数 例 ==")
# def add(x,y):
#     return x + y

# def muinus(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def division(x, y):
#     return x / y

# def calculate(func, x, y):
#     return func(x, y)

# print(f'加算：{calculate(add, 10,5)}')
# print(f'減算：{calculate(muinus, 10,5)}')
# print(f'乗算：{calculate(multiply, 10,5)}')
# print(f'除算：{calculate(division, 10,5)}')

print("\n== 型確認 ==")
# value = 1
# print(f'int型か？{isinstance(value, int)}')
# print(type(value))

# print("\n== 可変長引数(タプル) *args ==")
# def sum_func(multi,*args, div):
#     if len(args) >= 3:
#         print(*args)
#         print(multi,div)
#         return sum(args)
#     else:
#         print("引数は3つ以上必要です")
#         return None

# total = sum_func(10, 1, 2, 3, 4 ,5, div=100)
# print(total)

print("\n== 可変長引数(辞書) **kwargs ==")
# def sample_func(**kwargs):
#     print(kwargs)
#     for key, value in kwargs.items():
#         if key == "name":
#             print(f"name is {value}")
    
# sample_func(name="john", age=30, city="Tokyo")


print("\n== 可変長引数 アンパック ==")
# number = (1,2,3)
# a, b, c = number
# print(a, b, c)

# def print_student_info(name, age, grade):
#     print(f"Name: {name}, Age: {age}, Grade: {grade}")
    
# student = {
#     "name": "John",
#     "age": 20,
#     "grade": "A"
# }
# print(*student)
# print(*student.values())
# print(*student.keys())
# print(*student.items())
# print_student_info(**student)

# students = [
#     {"name": "John", "age": 20, "grade": "A"},
#     {"name": "Jane", "age": 22, "grade": "B"},
#     {"name": "Bob", "age": 21, "grade": "C", "address":"Tokyo"}
# ]

# def print_students_info(**kwargs):
#     print(f'Name:{kwargs["name"]} ' 
#           f'Age:{kwargs["age"]} '
#           f'Grade:{kwargs["grade"]} '
#           f'Address:{kwargs.get("address","None") }')
    
# for student in students:
#     print_students_info(**student)
    
# print("\n== 特殊引数(/ *) ==")

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#     print(f"pos1: {pos1}")
#     print(f"pos2: {pos2}")
#     print(f"pos_or_kwd: {pos_or_kwd}")
#     print(f"kwd1: {kwd1}")
#     print(f"kwd2: {kwd2}")
    
# f(1, 2, 3, kwd1="Key1", kwd2="Key2")
# f(1, 2, pos_or_kwd=3, kwd1="Key1", kwd2="Key2")

print("\n== 特殊引数(/ *) 例 ==")
# def order_summary(customer_id,
#                   order_id,
#                   /,
#                   item_name,
#                   *,
#                   quantity=1,
#                   price,
#                   discount=0):
#     print(f"Customer ID: {customer_id}")
#     print(f"Order ID: {order_id}")
#     print(f"Item Name: {item_name}")
#     print(f"Quantity: {quantity}")
#     print(f"Price: {price}")
#     print(f"Discount: {discount}")
#     print(f"Total: {quantity * price - discount}")
    
# order_summary(123,456,"Apple", quantity=2, price=100, discount=10)
# order_summary(222,333,item_name="Banana", price=50)

# print("\n")

# def student_details(student_id,
#                     first_name,
#                     last_name,
#                     /,
#                     *,
#                     age=None,
#                     major=None,
#                     gpa=None):
#     print(f"Student ID: {student_id}")
#     print(f"First Name: {first_name}") 
#     print(f"Last Name: {last_name}")
    
#     if age is not None:
#         print(f"Age: {age}")
        
#     if major is not None:
#         print(f"Major: {major}")
        
#     if gpa is not None:
#         print(f"GPA: {gpa}")
    
# student_details(1, "John", "Doe", age=20, major="Computer Science", gpa=3.5)
# student_details(2, "Jane", "Smith", major="Mathematics")
# student_details(3, "Bob", "Johnson", gpa=3.8)

print("\n== 変数のスコープ ==")
print("== グローバルスコープとローカルスコープ ==")
# total = 999 # グローバルスコープの変数
# print(total, id(total))
# def sum_numbers(*args):
#     global total    # グローバル変数totalを参照
#     total = 0
#     for num in args:
#         total += num
#     print(total, id(total))
    
# sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(total, id(total)) # グローバルスコープの変数

print("\n== ジェネレータ関数 ==")
# def count_up_to(max_number):
#     count = 0
#     while count <= max_number:
#         yield count
#         count += 1

# my_generator = count_up_to(5)
# print(next(my_generator))
# print(next(my_generator))
# print(next(my_generator))

# for number in my_generator:
#     print(number)
    
    
print("\n== ジェネレータ関数(大容量データの扱い) ==")
# import random
# import sys

# def unique_random_numbers(num):
#     randams = set()
#     while len(randams) < num:
#         randam_num = random.randint(1, sys.maxsize)
#         if randam_num not in randams:
#             randams.add(randam_num)
#             yield randam_num
            
# num_length = 100_000
# my_number = unique_random_numbers(num_length)
# print(f'ジェネレータの容量：{sys.getsizeof(my_number)}')

# my_number_list = list(unique_random_numbers(num_length))
# print(f'リストの容量：{sys.getsizeof(my_number_list)}')

# print("\n== メモリ上のDataFrameのサイズを確認する ==")
# import pandas as pd
# csv_file = "input/csv/重要_集計データ（mst2000010622／株式会社トラストバンク）_20241216-20241231.csv"
# df = pd.read_csv(csv_file, encoding="utf-8")
# print(df.info())
# print(df.memory_usage(index=True).sum())

print("\n== map関数 ==")
print("map関数はリストの各要素に関数を適用する")
# def square(num):
#     return num ** 2

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)
# print("map関数を使用して2乗のリストを作成：", list(squared_numbers))

print("\n== filter関数 ==")
print("filter関数は条件に合った(trueとなる)要素を抽出する")
# def is_even(num):
#     return num % 2 == 0

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = filter(is_even, numbers)
# print("偶数のリスト：", list(even_numbers))

print("\n== sortメソッド ==")
print("sortメソッドは元のリストを変更する")
# def sort_length(word):
#     return len(word)

# fruits = ["banana", "apple", "cherry", "orange"]
# fruits.sort(key=sort_length)
# print("sortメソッドを使用して長さでソート：", fruits)
# fruits.sort(reverse=True)
# print("sortメソッドを使用して長さで逆順ソート：", fruits)   


print("\n== sorted関数 ==")
print("sorted関数とはsortメソッドと同じようにソートするが元のリストは変更しない")
# cars = ["Toyota", "Honda", "Nissan", "Mazda"]
# print(cars)
# print(sorted(cars, key=sort_length))
# print(sorted(cars, key=sort_length , reverse=True))

# print("\n== map関数、filter関数のキャスト ==")
# print("map関数、filter関数で取得した値をリスト変数でキャストすると元の変数はnullになる")

# def square(num):
#     return num ** 2

# numbers = [1, 2, 3, 4, 5]
# squared_numbers = map(square, numbers)
# print("map関数を使用して2乗してmapオブジェクトをリスト変数でキャストする：", list(squared_numbers))
# print("リスト変数でキャスト後mapオブジェクトはnullになる：", list(squared_numbers))


print("\n== ラムダ式 ==")
print("ラムダ式は無名関数で、関数を定義せずにその場で関数を作成する")

print("\n通常の関数の場合")
print("def smaller(x, y):")
print("  if x > y:")
print("    return y")
print("  else:")
print("    return x")

print("\nラムダ式の場合")
print("smaller = lambda x, y: y if x > y else x")
# smaller = lambda x, y: y if x > y else x
# print("smaller(10, 20)=", smaller(10, 20))  

# print("\n== ラムダ式の例 ==")
# def by_last_letter(word):
#     return word[-1]

# words = ["banana", "apple", "cherry", "orange"]
# sorted_words = sorted(words, key= lambda word: word[-1])
# print("by_last_letter関数を使用してソート：", sorted_words)

# students = [
#     {"name": "John", "age": 20, "grade": "A"},
#     {"name": "Jane", "age": 22, "grade": "B"},
#     {"name": "Bob", "age": 21, "grade": "C"}
# ]

# def student_age(student:dict) -> int:
#     return student["age"]


# sorted_students = sorted(students, key= lambda student: student["age"])
# print("student_age関数を使用してソート：", sorted_students)

print("\n== デコレータ関数 ==")
print("デコレータ関数は関数を引数に取り、別の関数を返す関数")

# import time

# def timer_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"関数{func.__name__}は {end_time - start_time:.2f} 秒かかりました")
#         return result
#     return wrapper

# @timer_decorator
# def count_up(number):
#     total = 0
#     for i in range(number):
#         total += i
#     return total

# total_timer = timer_decorator(count_up)
# print(count_up(5000000))

print("\nオブジェクト指向プログラミングに至るまでの歴史")
print("1940-1950年代: 機械言語")
print("1950-1960年代: アセンブリ言語")
print("1960-1970年代: 手続き型プログラミング")
print("　FORTRAN(1957年), COBOL(1959年),C言語(1972年)")
print("1970-1980年代: 構造化プログラミング")
print("　Pascal(1970年), C言語(1972年)")
print("1980-1990年代: オブジェクト指向プログラミング")
print("　Smalltalk(1972年),C++(1983年), Java(1995年),Python(1991年)")
print("1990-2000年代: 関数型プログラミング")
print("　Lisp(1958年),Haskell(1900年), Scala(2004年)")
print("2000-2020年代: マルチパラダイムプログラミング")
print("　Python,JavaScript, Ruby, Scala, C#")


print("\n== クラスのイテレーション ==")
print("例：カウントダウンクラス")
# class CountDown:
#     def __init__(self, start:int):
#         self.number = start
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.number <= 0:
#             raise StopIteration
#         self.number -= 1
#         return self.number + 1
    
# count_down = CountDown(5)
# for number in count_down:
#     print(number)
    
    
# print("\n例：寿司")

# SUSHI = [
#     {"name": "マグロ", "price": 1000},
#     {"name": "サーモン", "price": 800},
#     {"name": "イカ", "price": 600},
#     {"name": "タコ", "price": 700},
#     {"name": "ウニ", "price": 1200},
#     {"name": "イクラ", "price": 1500},
#     {"name": "エビ", "price": 900},
# ]

# class Sushi:
#     def __init__(self, deposit:int):
#         print(f"{deposit}円内で寿司を握ってください。")
#         self.deposit = deposit
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         neta_list = [ neta for neta in SUSHI if neta["price"] <= self.deposit]
        
#         if len(neta_list) == 0:
#             print("提供するネタはありません")
#             raise StopIteration
        
#         neta = random.choice(neta_list)
#         self.deposit -= neta["price"]
#         return neta
    
# sushi = Sushi(5000)
# for neta in sushi:
#     print(f"{neta['price']}円の{neta['name']}を握りました。")
#     print(f"残金は{sushi.deposit}円です。")
#     if sushi.deposit <= 0:
#         print("お金が足りません")
#         break
    
print("\n== クラスの多態性 ==")
print("多態性とは同じメソッド名で異なる動作をすること")

# class Dog:
#     def __init__(self, sound:str):
#         self.sound = sound
        
#     def speak(self):
#         print(f"犬は{self.sound}と鳴きます")
#         return self.sound
    
# class Cat:
#     def __init__(self, sound:str):
#         self.sound = sound
        
#     def speak(self):
#         print(f"猫は{self.sound}と鳴きます")
#         return self.sound
    
# class Cow:
#     def __init__(self, sound:str):
#         self.sound = sound
        
#     def speak(self):
#         print(f"牛は{self.sound}と鳴きます")
#         return self.sound   
    
# animals = [
#     {"class": Dog, "sound": "ワンワン"},
#     {"class": Cat, "sound": "ニャー"},
#     {"class": Cow, "sound": "モーモー"},
# ]

# animals_dict = random.choice(animals)
# animal = animals_dict["class"](animals_dict["sound"])

# def speak(animal):
#     if hasattr(animal, "speak"):
#         animal.speak()
#     else:
#         print(f"{animal.type}はspeakメソッドがありません。")
        
# speak(animal)


print("\n== クラスの隠蔽 ==")
print("隠蔽とはクラスの内部状態を外部から直接アクセスできないようにすること")
print("publicメソッドを用意しその中でプライベートメソッドを呼び出す")

# class Cunstomer:
#     def __init__(self, name:str, age:int, weight:int, height:int):
#         self._name = self._set_name(name)
#         self._age = self._set_age(age)
#         self._weight = self._set_weight(weight)
#         self._height = self._set_height(height)
        
#     @property
#     def age(self):
#         return self._age
    
#     @staticmethod
#     def _set_age(age:int):
#         if not isinstance(age, int):
#             raise TypeError("年齢は整数でなければなりません")
#         if age < 0:
#             raise ValueError("年齢は0以上でなければなりません")
#         return age
    # @age.setter
    # def age(self, age:int):
    #     if not isinstance(age, int):
    #         raise TypeError("年齢は整数でなければなりません")
    #     self._age = age
        
    # @property
    # def name(self):
    #     return self._name
    
    # @staticmethod
    # def _set_name(name:str):
    #     if not isinstance(name, str):
    #         raise TypeError("名前は文字列でなければなりません")
    #     return name
    
    # @name.setter
    # def name(self, name:str):
    #     if not isinstance(name, str):
    #         raise ValueError("名前は文字列でなければなりません")
    #     self._name = name
        
    # @property
    # def weight(self):
    #     return self._weight
    
    # @staticmethod
    # def _set_weight( weight:int):
    #     if not isinstance(weight, (int, float)):
    #         raise TypeError("体重は整数でなければなりません")
    #     if weight < 0:
    #         raise ValueError("体重は0以上でなければなりません")
    #     return weight
    
    # @weight.setter
    # def weight(self, weight:int):
    #     if not isinstance(weight, (int, float)):
    #         raise TypeError("体重は整数でなければなりません")
    #     if weight < 0:
    #         raise ValueError("体重は0以上でなければなりません")
    #     self._weight = weight
    
    # @property
    # def height(self):
    #     return self._height
    
    # @staticmethod
    # def _set_height( height:int):
    #     if not isinstance(height, (int, float)):
    #         raise TypeError("身長は整数でなければなりません")
    #     if height < 0:
    #         raise ValueError("身長は0以上でなければなりません")
    #     return height
    
    # @height.setter
    # def height(self, height:int):
    #     if not isinstance(height, (int, float)):
    #         raise TypeError("身長は整数でなければなりません")
    #     if height < 0:
    #         raise ValueError("身長は0以上でなければなりません")
    #     self._height = height
    
#     @property
#     def bmi(self):
#         return self._weight / ((self._height / 100) ** 2)
#     pass

# try:
#     yamada = Cunstomer("山田太郎", 30, 70, 170)
#     yamada.name = "山田花子"
#     # yamada.age = 25
#     # yamada.weight = 50.5
#     # yamada.height = 160.5
#     print(f"BMIは{yamada.bmi}です")
    
# except Exception as e:
#     print(f"エラーが発生しました：{e}")
    
print("\n== クラスの継承 ==")
print("継承とは既存のクラスを基に新しいクラスを作成すること")
print("親クラスのメソッドを子クラスでオーバーライドすることができる")
print("")

# 親クラス
# class Human:
#     """Humanクラス"""
    
#     def __init__(self, name:str, age:int) -> None:
#         """Humanクラスの初期化メソッド
        
#         Args:
#             name (str): 名前
#             age (int): 年齢
            
#         """
#         self._name = self._set_name(name)
#         self._age = self._set_age(age)
    
#     @property
#     def name(self)-> str:
#         """名前を取得するプロパティ
        
#         Returns:
#             str: 名前
#         """
#         return self._name
    
#     @staticmethod
#     def _set_name(name:str)-> str:
#         """名前を設定するメソッド
        
#         Args:
#             name (str): 名前
            
#         Returns:
#             str: 名前
#         """
#         if not isinstance(name, str):
#             raise TypeError("名前は文字列でなければなりません")
#         return name
    
#     @property
#     def age(self) -> int:
#         """年齢を取得するプロパティ
        
#         Returns:
#             int: 年齢
#         """
#         return self._age
    
#     @staticmethod
#     def _set_age(age) -> int:
#         """年齢を設定するメソッド

#         Args:
#             age (int): 年齢

#         Raises:
#             TypeError: 型エラー
#             ValueError: 値エラー

#         Returns:
#             int: 年齢
#         """
#         if not isinstance(age, int):
#             raise TypeError("年齢は整数でなければなりません")
#         if age < 0:
#             raise ValueError("年齢は0以上でなければなりません")
#         return age
    
#     def greeting(self) -> None:
#         """挨拶をするメソッド"""
#         print(f"こんにちは、私は{self.name}です。年齢は{self.age}歳です。")
        
# 子クラス    
# class Staff(Human):
#     """StaffクラスはHumanクラスを継承します。

#     Args:
#         Human : Staffクラスの親クラス
#     """
#     def __init__(self, address:str, **keyargs)-> None:
#         """Staffクラスの初期化メソッド
        
#         :param **keyargs: name(str)、age(int)を含む辞書型の引数
#         :param address: 住所
            
#         """
#         super().__init__(**keyargs)
#         self._address = self._set_address(address)
        
#     @property
#     def address(self) -> str:
#         """住所を取得するプロパティ
        
#         Returns:
#             str: 住所
#         """
#         return self._address
    
#     @staticmethod
#     def _set_address(address:str) -> str:
#         """住所を設定するメソッド
        
#         Args:
#             address (str): 住所
            
#         Returns:
#             str: 住所
#         """
#         if not isinstance(address, str):
#             raise TypeError("住所は文字列でなければなりません")
#         return address
    
#     def greeting(self):
#         """挨拶をするメソッド"""
#         super().greeting()
#         print(f"私は{self.address}に住んでいます。")

# suzuki = Staff(name="鈴木", age=30, address="東京都")
# suzuki.greeting()

# print(dir(Human))
# print(dir(Staff))
# print(dir(suzuki))


print("\n== クラスの多重継承 ==")
print("多重継承とは複数の親クラスを持つ子クラスを作成すること")
print("多重継承で親クラスに同じメソッドが存在した場合、最初に継承した親クラスのメソッドが優先される")
print("")

# class Car:
#     """車クラス"""
#     def __init__(self, max_fuel_liter:int, fuel_liter:int)-> None:
#         """車クラスの初期化メソッド
        
#         Args:
#             max_fuel_liter (int): 最大燃料量(L)
#             fuel_liter (int): 現在の燃料量(L)
            
#         """
#         self._max_fuel_liter:int = max_fuel_liter
#         self._fuel_liter:int = fuel_liter
#         self._mileage_km:float = self._max_fuel_liter / 10
    
#     def run(self, distance_km:int)-> None:
#         """車を走らせるメソッド
        
#         Args:
#             distance_km (int): 走行距離(km)
#         """
#         if distance_km <= 0:
#             raise ValueError("走行距離は0以上でなければなりません")
        
#         if self._fuel_liter <= 0 | distance_km > self._mileage_km:
#             print("燃料が足りません。給油してください")
#             self.stop()
#             return
#         if distance_km > self._mileage_km:
#             print(f"車は{distance_km}kmのうち{self._mileage_km}km走りました。給油してください。")
#             self.stop()
#             return
#         self._mileage_km -= distance_km
#         self._fuel_liter -= distance_km * 10
#         print(f"車が{distance_km}km走りました。残りの燃料は{self._fuel_liter}Lです")
        
#     def stop(self) -> None:
#         """車を止めるメソッド"""
#         print("車が止まります")
        
#     def horn(self) -> None:
#         print("車がクラクションを鳴らします")
    
#     def refuel(self, amount:int)-> None:
#         """車に給油するメソッド
        
#         Args:
#             amount (int): 給油量(L)
#         """
#         if amount <= 0:
#             raise ValueError("給油量は0以上でなければなりません")
#         if self._fuel_liter + amount > self._max_fuel_liter:
#             print(f"{amount}Lのうち{amount-self._fuel_liter}Lで満タンの{self._max_fuel_liter}Lになりました。")
#             self._fuel_liter = self._max_fuel_liter
#             self._mileage_km = self._max_fuel_liter / 10
#             return
#         self._fuel_liter += amount
#         self._mileage_km = self._fuel_liter / 10
#         print(f"{amount}L給油しました。残量は{self._fuel_liter}Lです")
    
# class Aircondition:
#     """エアコンクラス"""
#     def __init__(self, temperature:int)-> None:
#         """エアコンクラスの初期化メソッド
        
#         Args:
#             temperature (int): 温度設定(摂氏)
#         """
#         self._temperature = self._set_temperature(temperature)
#         self._status = False
    
#     def on(self)-> None:
#         """エアコンをONにするメソッド"""        
#         self._status = True
#         self.set_mode("auto")
#         print("エアコンをONにしました")
        
#     def off(self)-> None:
#         """エアコンをOFFにするメソッド"""
#         self._status = False
#         print("エアコンをOFFにしました")
        
#     def _set_temperature(self, temperature:int)-> int:
#         """エアコンの温度を設定するメソッド
        
#         Args:
#             temperature (int): 温度設定(摂氏)
            
#         Returns:
#             int: 温度設定(摂氏)
#         """        
#         if not isinstance(temperature, int):
#             raise TypeError("温度は整数でなければなりません")            
#         return temperature
    
#     def set_mode(self, mode)-> None:
#         """エアコンのモードを設定するメソッド
        
#         Args:
#             mode (str): モード(cool, heat, dry, fan, auto)
#         """
#         if mode not in ["cool", "heat", "dry", "fan","auto"]:
#             raise ValueError("モードはcool, heat, dry, fan, autoのいずれかでなければなりません")
        
#         if mode == "cool":
#             self._mode = "cool"
#             print("冷却")
#         elif mode == "heat":
#             self._mode = "heat"
#             print("暖房")
#         elif mode == "dry":
#             self._mode = "dry"
#             print("除湿")
#         elif mode == "fan":
#             self._mode = "fan"
#             print("送風")
#         elif mode == "auto":
#             if self._temperature >= 25:
#                 self._mode = "cool"
#                 print("自動->冷却")
#             elif self._temperature <= 20:
#                 self._mode = "heat"
#                 print("自動->暖房")
                
#     def change_mode(self, mode)-> None:
#         """エアコンのモードを変更するメソッド
        
#         Args:
#             mode (str): モード(cool, heat, dry, fan, auto)
#         """
#         if self._status:
#             self.set_mode(mode)
#         else:
#             print("エアコンがOFFのためモードを変更できません")
#     pass

# class Radio:
#     """"ラジオクラス"""
#     def __init__(self)-> None:
#         """ラジオクラスの初期化メソッド"""
#         self._power = False
#         self._max_volume = 50
#         self._volume = 10
#         self._channel = self._set_channel(1)
    
#     def on(self)-> None:
#         """ラジオをONにするメソッド"""
#         self._power = True
#         print("ラジオをONにしました")
        
#     def off(self)-> None:
#         self._power = False
#         print("ラジオをOFFにしました")
        
#     def _set_channel(self, channel)-> int:
#         """ラジオのチャンネルを設定するメソッド
        
#         Args:
#             channel (int): チャンネル(1-100)
            
#         Returns:
#             int: チャンネル(1-100)
#         """
#         if self._power == False:
#             raise ValueError("ラジオがOFFのためチャンネルを変更できません")
#         if not isinstance(channel, int):
#             raise TypeError("チャンネルは整数でなければなりません")
#         if channel < 1 or channel > 100:
#             raise ValueError("チャンネルは1から100の範囲でなければなりません")
#         print(f"チャンネル{channel}に設定しました")
#         return channel
        
#     def volume_up(self)-> None:
#         """音量を上げるメソッド"""
#         if self._power == False:
#             raise ValueError("ラジオがOFFのため音量を変更できません")
#         if self._volume <= self._max_volume:
#             self._volume += 1
#             print(f"音量を{self._volume}に設定しました")
#         else:
#             print("音量は最大です")
            
#     def volume_down(self)-> None:
#         """音量を下げるメソッド"""
#         if self._power == False:
#             raise ValueError("ラジオがOFFのため音量を変更できません")
#         if self._volume >= 0:
#             self._volume -= 1
#             print(f"音量を{self._volume}に設定しました")
#         else:
#             print("音量はミュートされてます")
            
# class CarWithAircondition(Car, Aircondition):
#     """エアコン付き車クラス"""
#     def __init__(self, max_fuel_liter:int, fuel_liter:int, temperature:int)-> None:
#         """エアコン付き車クラスの初期化メソッド
        
#         Args:
#             max_fuel_liter (int): 最大燃料量(L)
#             fuel_liter (int): 現在の燃料量(L)
#             temperature (int): 温度設定(摂氏)
            
#         """
#         Car.__init__(self, max_fuel_liter, fuel_liter)
#         Aircondition.__init__(self, temperature)
#         print(f"最大燃料量(L):{max_fuel_liter} 現在の燃料量(L):{fuel_liter} 走行可能距離(km):{self._mileage_km} 温度設定(摂氏):{temperature}")

# small_car = CarWithAircondition(50, 20, 25)
# small_car.run(1)
# small_car.refuel(50)
# small_car.run(6)


print("\n== クラスの抽象 ==")
print("抽象クラスとは具体的な実装を持たないメソッドを定義するクラスのこと")

# from abc import ABC, abstractmethod

# class AbstractAnimal(ABC):
#     """抽象動物クラス"""
    
#     @abstractmethod
#     def sound(self)-> str:
#         """動物の鳴き声を返すメソッド"""
#         pass
    
# class Dog(AbstractAnimal):
#     """犬クラス"""
    
#     def sound(self)-> str:
#         """犬の鳴き声を返すメソッド
        
#         Returns:
#             str: 犬の鳴き声
#         """
#         return "ワンワン"
    
# class Cat(AbstractAnimal):
#     """猫クラス"""
    
#     def sound(self)-> str:
#         """猫の鳴き声を返すメソッド
        
#         Returns:
#             str: 猫の鳴き声
#         """
#         return "ニャー"
    
# dog = Dog()
# cat = Cat()
# print(f"犬の鳴き声: {dog.sound()}")
# print(f"猫の鳴き声: {cat.sound()}")


print("\n== 名前空間 ==")
print("名前空間とは変数や関数の名前を管理するための領域")

# from pprint import pprint

# # グローバル変数
# x = 10
# def outer():
#     # エンクロージング変数
#     x = 20
#     def inner():
#         # ローカル変数
#         x = 30
#         print(f"inner関数のx: {x}")
#     print(f"outer関数のx: {x}")
#     inner()

# outer()

# print("\n== 例外処理 ==")
# print("エラー種類")
# print("1. SyntaxError: 構文エラー")
# print("2. NameError: 名前エラー")
# print("3. TypeError: 型エラー")
# print("4. ValueError: 値エラー")
# print("5. IndexError: インデックスエラー")
# print("6. KeyError: キーエラー")
# print("7. AttributeError: 属性エラー")
# print("8. ZeroDivisionError: ゼロ除算エラー")
# print("9. FileNotFoundError: ファイルが見つからないエラー")
# print("10. IOError: 入出力エラー")
# print("11. ImportError: インポートエラー")
# print("12. Exception: 一般的なエラー")
# print("13. KeyboardInterrupt: キーボード割り込みエラー")
# print("14. MemoryError: メモリエラー")
# print("15. OverflowError: オーバーフローエラー")
# print("16. RecursionError: 再帰エラー")
# print("17. StopIteration: イテレーション終了エラー")
# print("18. TimeoutError: タイムアウトエラー")
# print("19. AssertionError: アサーションエラー")
# print("20. IndentationError: インデントエラー")
# print("21. UnicodeError: Unicodeエラー")
# print("22. ModuleNotFoundError: モジュールが見つからないエラー")
# print("23. NotImplementedError: 未実装エラー")
# print("24. RuntimeError: 実行時エラー")
# print("25. SystemError: システムエラー")
# print("26. SystemExit: システム終了エラー")

# print("\n例外処理の構文")
# print("try:")
# print("    # エラーが発生する可能性のあるコード")
# print("except (エラータイプ):")
# print("    # エラーが発生した場合の処理")
# print("else:")
# print("    # エラーが発生しなかった場合の処理")
# print("finally:")
# print("    # エラーの有無にかかわらず実行される処理")

# try:
#     num = int(input("整数を入力してください："))
    
# except ValueError:
#     print("無効な入力です。整数を入力してください。")
# else:
#     print(f"入力された整数は{num}です。")
# finally:
#     print("プログラムが終了しました。")

print("\n== 例外処理の例 ==")
print("ユーザーに数値を入力してもらうまで入力を繰り返させるプログラムを作成してください")
print("数値が入力されたら、その数値を2乗した値を出力してください。")

# try:
#     while True:
#         num = input("数値を入力してください：")
#         if isinstance(num, int):
#             num = int(num)
#             print(f"{num}の2乗は{num ** 2}です")
#             break
#         if isinstance(num, str):
#             try:
#                 num = int(num)
#                 print(f"{num}の2乗は{num ** 2}です")
#                 break
#             except ValueError:
#                 print("無効な入力です。整数を入力してください。")
            
# except KeyboardInterrupt:
#     print("プログラムが中断されました。")

print("\n == ユーザー定義例外 == ")
print("ユーザー定義例外は独自のエラーを作成することができる")

# class NegativeNumberError(ValueError):
#     """負の数エラー"""
#     def __init__(self, value:int)-> None:
#         self.value = value
        
#     def __str__(self):
#         return f"{self.__class__.__name__}: 負の数エラー: {self.value}は負の数です"
    
# class NotAdultError(ValueError):
#     """成人でないエラー"""
#     def __init__(self, value:int)-> None:
#         self.value = value
        
#     def __str__(self):
#         return f"{self.__class__.__name__}: 未成年です: {self.value}"
    
# class Customer:
#     def __init__(self, name:str, age:int)-> None:
#         self._name = self._set_name(name)
#         self._age = self._set_age(age)
        
#     @property
#     def name(self)-> str:
#         return self._name
    
#     def _set_name(self, name:str)-> str:
#         if not isinstance(name, str):
#             raise TypeError("名前は文字列でなければなりません")
#         return name
    
#     @property
#     def age(self)-> int:
#         return self._age
    
#     def _set_age(self, age:int)-> int:
#         if not isinstance(age, int):
#             raise TypeError("年齢は整数でなければなりません")
#         if age < 0:
#             raise NegativeNumberError(age)
#         elif age < 20:
#             raise NotAdultError(age)
#         return age
    
# try:
#     name = "山田太郎"
#     age = 18
#     customer = Customer(name, age)

# except (NegativeNumberError,NotAdultError) as e:
#     print(e)
# else:
#     print(f"顧客名: {customer.name} 年齢: {customer.age}歳")
    
print("\n== モジュール ==")
# import calendar
# print(calendar.calendar(2026))

print("\n == osパッケージ == ")
# # import os
# # print("カレントディレクトリ:", os.getcwd())

# print("\n == sysパッケージ == ")
# import sys

# print("\n == zlibパッケージ == ")
# import zlib

# current_dir = os.getcwd()
# csv_file = os.path.join(current_dir, "input\csv\重要_集計データ（mst2000010622／株式会社トラストバンク）_20241216-20241231.csv")
# zip_file = os.path.join(current_dir, "input\csv\compressed_data.zlib")

# with open(csv_file, "rb") as f:
#     file_data = f.read()
#     compressed_data = zlib.compress(file_data, level=9)
#     print(f"圧縮前のサイズ: {len(file_data)} bytes")
#     print(f"圧縮後のサイズ: {len(compressed_data)} bytes")
    
# with open(zip_file, "wb") as f:
#     f.write(compressed_data)
#     print("圧縮データをcompressed_data.zlibに保存しました")

print("\n == unittestパッケージ == ")

# import unittest

# def add(x:int, y:int) -> int:
#     """2つの整数を加算する関数
    
#     Args:
#         x (int): 整数1
#         y (int): 整数2
        
#     Returns:
#         int: 加算結果
#     """
#     return x + y

# class TestAddFunction(unittest.TestCase):
#     """add関数のテストクラス"""
    
#     def test_add(self):
#         """add関数のテストメソッド"""
#         self.assertEqual(add(1, 2), 3)
#         self.assertEqual(add(-1, 1), 0)
#         self.assertEqual(add(0, 0), 0)
#         self.assertEqual(add(-1, -1), -2)
#         self.assertEqual(add(1000000000, 2000000000), 3000000000)
#         self.assertEqual(add(1.5, 2.5), 4.0)
        
# unittest.main()

print("\n == pip == ")
print("pipはPythonのパッケージ管理ツール")
print("pip install <パッケージ名>でパッケージをインストールできる")
print("pip uninstall <パッケージ名>でパッケージをアンインストールできる")
print("pip listでインストールされているパッケージの一覧を表示できる")
print("pip freeze でインストールされているパッケージのバージョンを表示できる")

print("\n == requirements.txt == ")
print("requirements.txtはPythonのパッケージ管理ファイル")
print("pip install -r requirements.txtでrequirements.txtに記載されたパッケージをインストールできる")
print("pip freeze > requirements.txtでインストールされているパッケージをrequirements.txtに出力できる")
print("pip uninstall -r requirements,txt -yでrequirements.txtに記載されたパッケージをアンインストールできる")


print("\n == numpyモジュール == ")
print("numpyは数値計算ライブラリ")
print("numpyは多次元配列を扱うことができる")
# import numpy as np

# arr1 = np.array([1, 2, 3, 4, 5])
# print("一次元配列:", arr1)
# print(arr1[0], arr1[-1])

# arr2 = np.array([[1, 2, 3], [4, 5, 6]])
# print("二次元配列:", arr2)

# print("一次元配列の形状:", arr1.shape)
# print("二次元配列の次元数:", arr2.shape)

# print("一次元配列の次元数:", arr1.ndim)
# print("二次元配列の次元数:", arr2.ndim)

# print("一次元配列のデータ型:", arr1.dtype)
# print("二次元配列のデータ型:", arr2.dtype)

# print("一次元配列の合計", arr1.sum())
# print("二次元配列の合計", arr2.sum())


print("\n == requestsモジュール == ")
print("requestsはHTTPリクエストを簡単に送信できるライブラリ")

# import requests
# from bs4 import BeautifulSoup
# response = requests.get("https://yahoo.co.jp")
# print("HTTPステータスコード:", response.status_code)
# soup = BeautifulSoup(response.text, "html.parser")
# print("HTMLタイトル:", soup.title.text)
# print(soup.h1.text)
# # print("HTML本文:", soup.body)
# # print("レスポンスヘッダー:", response.headers)
# # print("レスポンスボディ:", response.text)

print("\n == pathlib == ")
print("ファイルシステムのパスを操作する標準ライブラリの１モジュール")

from pathlib import Path

# current_dir_path = Path(__file__).parent
# print(current_dir_path)
# print(type(current_dir_path))

# print(__name__)
# print(__file__)

# weather_py = current_dir_path / 'weather.py'
# print(weather_py)
# print(type(weather_py))
# print(weather_py.exists())
# print(weather_py.name)
# print(weather_py.stem)
# print(weather_py.suffix)

print("\n == shutil == ")
print("ファイルのコピー、移動、削除を操作する標準ライブラリの１モジュール")

# import shutil
# from datetime import datetime 
# copy_weather_py = f"{weather_py.stem}_{datetime.today().strftime("%Y%m%d")}{weather_py.suffix}"
# copy_weather_py = current_dir_path / copy_weather_py
# print(copy_weather_py)

# # ファイルをコピーする
# shutil.copy(weather_py,copy_weather_py)

# # backupフォルダを作成する
# move_dir_path = current_dir_path / "backup"
# move_dir_path.mkdir(exist_ok=True)

# try:
#     # ファイルを移動する
#     shutil.move(copy_weather_py,move_dir_path)
# except:
#     # ファイルをコピーする
#     shutil.copy(copy_weather_py,move_dir_path)
#     # ファイルを削除する
#     copy_weather_py.unlink()

# # カレントディレクトリ直下の.pyファイルをすべて取得する
# files = current_dir_path.glob("*.py")
# print(type(files))

# for file in files:
#     print(file)
    
# # backupフォルダ（中身にファイルが存在する）を削除する
# print(move_dir_path)
# shutil.rmtree(move_dir_path)

print("\n == open(path, modo, encording) == ")
print("ファイルを開く")
print("path: ファイルのパス")
print("modo: ファイルを開くモード")
print("\tr: 読み込みモード")
print("\tw: 書き込みモード")
print("\ta: 追記モード")
print("\tb: バイナリモード")
print("\tt: テキストモード")
print("encording: エンコーディング")

current_dir_path = Path(__file__).parent
# env_file_path = current_dir_path / ".env"

# env = open(env_file_path, "r", encoding="utf-8")
# for line in env.readlines():
#     print(line, end="")
# env.close()


print("\n == with open == ")
print("with openはファイルを開くと同時に自動で閉じることができる")
print("")
# with open(env_file_path, "r", encoding="utf-8") as env:
#     for line in env.readlines():
#         print(line, end="")
        
print("\n == with open (書き込み) == ")

output_dir_path = current_dir_path / "output"
# sample_file_path = output_dir_path / "sample.txt"

# with open(sample_file_path, "w", encoding="utf-8") as sample:
#     sample.write("Hello World\n")
#     sample.write("Python is great!\n")
#     sample.write("This is a sample file.\n")
    
print("\n == csv.reader == ")
print("csv.readerはCSVファイルを読み込むためのモジュール")
print("")

# import csv
# csv_dir_path = output_dir_path / "csv"
# user_csv_path = csv_dir_path / "connectedUsers.csv"
# with open(user_csv_path, "r", encoding="utf-8") as user_csv:
#     reader = csv.reader(user_csv)
#     for row in reader:
#         print(row)
        
print("\n == csv.DictWriter == ")
print("csv.DictWriterはCSVファイルに辞書型データを書き込むためのモジュール")

# import faker
# fake = faker.Faker("ja_JP")

# connected_user_csv_path = csv_dir_path / "connected_users.csv"
# headers = ["No", "社員番号","氏名", "パソコンID", "接続状況","現在時刻"]
# with open(connected_user_csv_path, "w", encoding="utf-8", newline="") as user_csv:
#     writer = csv.DictWriter(user_csv, fieldnames=headers)
#     writer.writeheader()
    
#     for i in range(10):
#         writer.writerow({
#             "No": i+1,
#             "社員番号": fake.random_int(min=1000, max=9999),
#             "氏名": fake.name(),
#             "パソコンID": fake.random_int(min=100000, max=999999),
#             "接続状況": fake.random_element(elements=("接続中", "切断中")),
#             "現在時刻": fake.date_time_this_year()
#         })
        
print("\n == json.load == ")
print("json.loadはJSONファイルを読み込むためのモジュール")
print("")

# import json
# json_dir_path = output_dir_path / "json"
# ramens_json_file = json_dir_path / "ramens.json"
# with open(ramens_json_file, "r", encoding="utf-8") as f:
#     ramens_dict = json.load(f)
#     for ramen in ramens_dict:
#         print(f"店名:{ramen["name"]}")
#         print(f"所在地:{ramen["address"]}")
#         tel = ramen["phone"] if ramen["phone"] else "なし"
#         print(f"TEL:{tel}")
#         print(f"メニュ:")
#         for i,menu in enumerate(ramen["menu"]):    
#             print(f"  {i+1}:{menu["name"]} {menu["price"]}円")
#         print(f"評価:{ramen["ranking"]}")
#         yoyaku =  "可" if ramen["reservation"] else "不可"
#         print(f"予約:{yoyaku}\n")


print("\n == json.dump == ")
print("json.dumpはJSONファイルに書き込むためのモジュール")
print("")

# ramens_json_file_from_py = json_dir_path / "ramens_from_py.json"
# ramen_shops_dict = [
#     {
#         "name": "蔦",
#         "ranking": 4.6,
#         "address": "東京都千代田区神田須田町2-5-4",
#         "menu": [
#             {
#                 "name": "特製醤油 Soba",
#                 "price": 3000
#             },
#             {
#                 "name": "チャーシュー 味玉醤油 Soba",
#                 "price": 2500
#             }
#         ],
#         "phone": "03-1234-5678",
#         "reservation": False
#     },
#     {
#         "name": "らーめん山頭火",
#         "ranking": 4.2,
#         "address": "東京都渋谷区道玄坂2-9-6",
#         "menu": [
#         {
#             "name": "豚骨ラーメン",
#             "price": 900
#         },
#         {
#             "name": "辛味噌ラーメン",
#             "price": 950
#         }
#         ],
#         "phone": "03-9876-5432",
#         "reservation": True
#   }
# ]

# with open(ramens_json_file_from_py, "w", encoding="utf-8") as f:
#     json.dump(ramens_dict, f, ensure_ascii=False, indent=2)

print("\n == sys.argv == ")
print("sys.argvはコマンドライン引数を取得するためのモジュール")
print("""
    argv_multiply.py
    --
    from sys import argv
    def multiply(x, y):
        return x * y
    print(multiply(int(argv[1]), int(argv[2])))
    --
""")

print("\n == argparse == ")
print("argparseはコマンドライン引数を取得するためのモジュール")


