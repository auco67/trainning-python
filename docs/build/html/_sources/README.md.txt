# Sphinx

[Sphinx](https://www.sphinx-doc.org/ja/master/) はブラウザーで表示するドキュメント（オンラインマニュアル 等）を作成するツールです。 具体的には reStructredText を使用してマークダウン記法で書いたファイルを HTML 形式や PDF 形式などのファイルに変換するツールです。 元々は Python のドキュメント用に作成されたものですが、現在は多くのドキュメントを作成するのに使用されています。 名称は Sphinx ですが、「ホルスの目」のアイコンが使用されています。

## 環境構築

1. Sphinx のインストール

```
pip install -U sphinx
```

2. Sphinx の拡張機能のインストール

```
pip install myst-parser
```

3. 作業ディレクトリ docs を作成する

```
mkdir docs
```

4. Sphinx プロジェクトの雛形を作成する

```
sphinx-quickstart docs
```

```
> Separate source and build directories (y/n) [n]: (1)
> Project name: (2)
> Author name(s):　(3)
> Project release []:　(4)
> Project language [en]:　(5)
```

(1):ソースファイルとビルドファイルを別のディレクトリに分けるかどうか

(2):プロジェクト名を入力する

(3):作者名を入力する

(4):プロジェクトのバージョンを入力する

(5):プロジェクトの言語を指定する（例：日本語の場合「ja」）

上記実行後、作業ディレクトリ docs に以下のようなサブディレクトリとファイルが生成される

```
docs
├── make.bat
├── Makefile
├── build
└── source
   ├── conf.py
   ├── index.rst
   ├── _static
   └── _templates
```

3. conf.py を編集する

3-1. 作成した Python ファイルを読み込めるよう以下を最上部に追加する

```
import os, sys
sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('..'))
```

3-2. extensions を以下のように変更する

```
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser'
]
```

- sphinx.ext.autodoc: docstring を自動的に読み込むための拡張機能
- sphinx.ext.napoleon: Numpy スタイルや Google スタイルの docstring をパースするための拡張機能
- myst_parser: Markdown ファイルからドキュメントを生成するための拡張機能

3-3. source_suffix 変数を追記する

各拡張子と各マークアップ言語と紐づけする

```
source_suffix = {
    '.rst': 'restructuredtext',
    '.txt': 'markdown',
    '.md': 'markdown',
}
```

4. ドキュメントを自動生成したい Python ファイルを docs と同じ階層に、README.md は docs/source に配置する

```
docs
├── make.bat
├── Makefile
├── example_google.py *
├── example_numpy.py *
├── example_japanese.py *
├── build
└── source
   ├── conf.py
   ├── index.rst
   ├── README.md *
   ├── _static
   └── _templates
```

5. index.rst を編集する

   index.rst はドキュメントのトップページを生成するためのファイル

```
####
目次
####

.. toctree::
  :numbered:

  ./README
　./modules

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
```

- .. toctree:: ドキュメントの目次を作成するためのディレクティブ
- :numbered: ナンバリングする

6. index.rst を複製して modules.rst を作成する

```
###############
example_google
###############
.. toctree::
   :maxdepth: 4

.. automodule:: example_google
  :menbers:

################
example_numpy
################
.. toctree::
   :maxdepth: 4

.. automodule:: example_numpy
   :members:

###############
example_japanese
###############
.. toctree::
   :maxdepth: 4

.. automodule:: example_japanese
  :menbers:
```

- .. automodule:: python ファイル名
- :members:

7. 以下コマンドを実行する

```
sphinx-build -M html docs/source/ docs/build/
```

上記実行後、作業ディレクトリ docs に以下の\*が付いたサブディレクトリとファイルが生成される

```
docs
├── make.bat
├── Makefile
├── example_google.py
├── example_japanese.py
├── example_numpy.py
└── build
├   ├── doctrees *
├   ├   ├── environment.pickle *
├   ├   ├── index.doctree *
├   ├   ├── modules.doctree *
├   └── html *
├       ├── .buildinfo *
├       ├── genindex.html *
├       ├── index.html *
├       ├── objects.inv *
├       ├── py-modindex.html *
├       ├── search.html *
├       ├── searchindex.js *
├       ├── sources *
├       ├   ├── index.rst.txt *
├       ├   └── modules.rst.txt *
├       └── static *
├           ├── alabaster.css *
├           ├── basic.css *
├           ├── custom.css *
├           ├── doctools.js *
├           ├── documentation_options.js *
├           ├── file.png *
├           ├── language_data.js *
├           ├── minus.png *
├           ├── plus.png *
├           ├── pygments.css *
├           ├── searchtools.js *
├           ├── sphinx_highlight.js *
├           └── translations.js *
└── source
   ├── conf.py
   ├── index.rst
   ├── README.md
   ├── _static
   └── _templates
```

8. index.html をブラウザで開く

   docs/build/html/index.html をブラウザで開くとドキュメントが確認できる
