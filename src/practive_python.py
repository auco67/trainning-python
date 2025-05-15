import os
import json
from colorama import init, Fore

def clear_terminal()->None:
    """ターミナルをclearする"""
    os.system("cls" if os.name == "nt" else "clear")

def display_json_file_number(json_files:list)->None:
    """ファイル番号の表示
    
    Args: json_files(list): jsonファイル名のリスト
    """
    print("番号を入力してJSONファイルを選択してください。")
    for i, file in enumerate(json_files):
        print(f"{i+1}.{file}")
        
def display_question(question: dict)-> None:
    """問題を表示する

    Args: question(dict): 問題内容の辞書
    """
    print("問題ID：", question["id"])
    print("\n問題：", "\n\t",question["question"])
    print("\n選択肢：")
    for key, value in question["choices"][0].items():
        print(f"\t{key}:{value}")
    
def display_explanation(question:dict)-> None:
    """解説を表示する
    
    Args: question(dict): 問題内容の辞書
    """
    print("\n解説：", "\n\t",question["explanation"])
        
def display_result(correct_answers:int, questions:dict)->None:
    PASS_RATE = 70
    result = correct_answers / len(questions) * 100
    print(f"{Fore.BLUE}テストが終了しました{Fore.RESET}")
    print(f"{len(questions)}門中{correct_answers}門正解しました。")
    print(f"正解率：{result}%")
    if result >= PASS_RATE:
        print(f"{Fore.GREEN}合格です！おめでとうございます{Fore.RESET}")
    else:
        print(f"{Fore.RED}不合格です！残念でした{Fore.RESET}")
  
def get_json_files()->list:
    """jsonsディレクトリ内の.json拡張子のファイルを抽出する

    Returns:
        list: jsonファイル名のリスト
    """
    json_files = [f for f in os.listdir("jsons") if f.endswith(".json") ]
    if not json_files:
        print("jsonsディレクトリ内にJSONファイルがみつかりません。")
        return
    return json_files
          
def recive_response(json_files:list)->int:
    """ユーザーの選択を受け付ける

    Args:
        json_files (list): jsonファイル名のリスト

    Retruns:
        choice(int): 入力値
        
    Raises:
        ValueError: 入力値が１以下またはJSONファイルリストの数より大きい場合はエラー
    """
    while True:
        try:
            choice = int(input("番号を入力してください："))
            
            if choice < 1 or choice > len(json_files):
                raise ValueError
            
            break # whileループを抜ける
        except ValueError:
            print("無効な入力です。有効な番号を入力してください。")
    return choice

def read_json_file(json_files:list, choice:int)->dict:
    """選択されたJSONファイルを読み込む

    Args:
        json_files (list): jsonファイル名のリスト
        choice (int): 入力された番号

    Returns:
        dict: jsonファイルの中身
    """
    selected_file = json_files[choice-1]
    with open(os.path.join("jsons",selected_file), encoding="utf-8") as f:
        return json.load(f)

def run_test(questions:dict, correct_answers:int)->int:
    """テストを実施する

    Args:
        questions (dict): 問題内容辞書
        
    Returns:
        correct_answers(int): 正解数
    """        
    # 問題文を表示する
    for question in questions:
        display_question(question)
        
        while True:
            answer = input("\n回答を入力してください（A, B, C, D）:").upper() # 小文字は大文字に
            if answer not in ["A", "B", "C", "D"]:
                print("無効な回答です。A, B, C, Dのいずれかを入力してください。")
            else:
                break
        
        if answer == question["answer"]:
            correct_answers += 1
            print(f"\n{Fore.GREEN}結果：\t正解です！{Fore.RESET}")
        else:
            print(f"\n{Fore.RED}結果：\t不正解です！{Fore.RESET}")
            
        # 解説を表示
        display_explanation(question)
        
        # 区切り線を表示
        print("-" * os.get_terminal_size().columns)
        
    return correct_answers
        
def main():
    """メイン処理"""
    try:
        # jsonsディレクトリ内の.json拡張子のファイルを抽出する
        json_files = get_json_files()
            
        # ファイル番号の表示
        display_json_file_number(json_files)

        # ユーザーの選択を受け付ける
        choice = recive_response(json_files)
        
        # 選択されたJSONファイルを読み込む
        questions = read_json_file(json_files, choice)

        # ターミナルをclearする
        clear_terminal()
        
        # 正解数を初期化する
        correct_answers = 0
        
        # 問題文を表示する
        correct_answers = run_test(questions, correct_answers)
        
        # 結果を表示する
        display_result(correct_answers, questions)
    
    except KeyboardInterrupt:
        pass
        
if __name__ == "__main__":
    init()
    clear_terminal()
    main()