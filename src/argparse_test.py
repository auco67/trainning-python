import argparse

# メソッド
def squared(x):
    try:
        value = int(x)
    except ValueError:
        raise argparse.ArgumentTypeError(f"{x}はint型で入力ください")
    return value * value

def total(num_list):
    return sum(num_list)
        
# クラス
class Person:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return f"私の名前は{self.name}です"
        
arg_parse = argparse.ArgumentParser(description="スクリプトの説明")

# 位置引数（positional arguments) 必須引数
arg_parse.add_argument("arg1", help="数値(int型)", type=int)
arg_parse.add_argument("arg2", help="数値(int型)", type=int)

# オプション(options) 任意
arg_parse.add_argument("-n", "--num", help="数値(int型) 初期値3", type=int, default=3, nargs="?") # nargs="?"は引数を0個または1個指定する
arg_parse.add_argument("-p", "--path", help="パスを指定する(str型)", type=str, required=False) # requiredをTrueにすると必須オプション
arg_parse.add_argument("-s", "--square", help="２乗する値を指定する(int型)", type=squared)
arg_parse.add_argument("-m", "--myname", help="氏名を設定する(str型)", type=Person)
arg_parse.add_argument("-c", "--choice", choices=["typeA", "typeB", "typeC"] ,help="タイプを選択する")
arg_parse.add_argument("-t", "--total", help="２つの数値を合計する" , type=int, nargs=2) # nargs=2は引数を２つ必ず必要とする
arg_parse.add_argument("-l", "--list", help="数値(int型) のリスト", type=int, default=3, nargs="*") # nargs="*"は引数を0個以上指定する
arg_parse.add_argument("-r", "--required_list", help="数値(int型) のリスト", type=int, default=3, nargs="+") # nargs="+"は引数を0個以上必ず指定する

if __name__ == "__main__":
    arg = arg_parse.parse_args()
    print(f"arg1={arg.arg1} type={type(arg.arg1)}型")
    print(f"arg1={arg.arg2} type={type(arg.arg2)}型")
    print(f"num={arg.num} type={type(arg.num)}型")
    print(f"list={arg.list} type={type(arg.list)}型")
    print(f"required_list={arg.required_list} type={type(arg.required_list)}型")
    if arg.path:
        print(f"path={arg.path} type={type(arg.path)}型")
    if arg.square:
        print(f"square={arg.square} type={type(arg.square)}型")
    if arg.myname:
        print(f"myname={arg.myname} type={type(arg.myname)}型")
    if arg.choice:
        print(f"choice={arg.choice} type={type(arg.choice)}型")
    if arg.total:
        print(f"total={total(arg.total)} type={type(arg.total)}型")