from spire.doc import Document
from spire.doc import FileFormat
from spire.doc import XHTMLValidationType

# Document クラスのオブジェクトを作成します
doc = Document()

# HTML ファイルを読み込みます
doc.LoadFromFile("./dist/cover_letter.html", FileFormat.Html, XHTMLValidationType.none)

# ファイルを PDF 形式に変換して保存します
doc.SaveToFile("./output/cover_letter.pdf", FileFormat.PDF)
doc.Close()
