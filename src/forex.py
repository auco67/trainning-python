import argparse
import yfinance

# コマンドライン引数をパースする
parser = argparse.ArgumentParser(description="両替計算を行う")
parser.add_argument("-s", "--source", required=True, help="両替元の通貨")
parser.add_argument("-t", "--to", required=True, help="両替先の通貨")
parser.add_argument("-a", "--amount", required=True, type=float, help="両替")
args = parser.parse_args()

# 為替レートを取得する
rate = yfinance.Ticker(f"{args.source}{args.to}=X").info["regularMarketOpen"]

# 両替計算する
result = args.amount * rate

# 結果を表示する
print(f"{args.amount} {args.source} = {result} {args.to}")