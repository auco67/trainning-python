## Git

### Git ローカルリポジトリの作成

```
git init
```

コンソール上でリポジトリを確認する

```
ls -force
```

```
    Directory: C:\Users\<user_name>\Documents\github\trainning-python

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d--h-          2025/05/15    15:39                .git
d----          2025/05/15    15:39                bat
d----          2025/05/15    15:50                data
d----          2025/05/15    15:51                dist
d----          2025/05/15    15:39                docs
d----          2025/05/15    15:39                input
d----          2025/05/15    15:39                jsons
d----          2025/05/15    15:53                log
d----          2025/05/15    15:50                output
d----          2025/05/15    15:57                src
d----          2025/05/15    15:42                venv312
-a---          2025/05/15    15:53             17 .env
-a---          2025/05/15    16:03           3435 .gitignore
-a---          2025/05/15    16:04           5003 README.md
```

### Git リポジトリへ対象外とする（.gitignore）

.gitignore ファイルを作成しリポジトリから対象外としたいディレクトリまたはファイルを記述する

.gitignore

```
data/
dist/
docs/
Excel/
input/
jsons/
key/
log/
output/
pdf/
templates/
venv/
web/
.env
```

### Git ステージング（add）

```
git add ファイル名
```

### Git コミット(commit)

```
git commit -m メッセージ
```

### Git ステータス(status)

```
git status
```

### Git リモートレポジトリの作成

```
git remote add origin https://github.com/<username>/<repository_name>.git
```

### Git ブランチの作成

```
git checkout -b <branch_name>
```

### Git リモートレポジトリにプッシュ

ローカルリポジトリの内容をリモートレポジトリに更新する

```
git push origin <branch name>
```

### Git リモートリポジトリのクローン

リモートリポジトリをローカルに複製する

```
git clone https://github.com/<username>/<repository_name>.git
```

#### 複製後に package をインストールする

requirements.txt が存在する場合

```
pip install -r requirements.txt
```

### Git フル(pull)

リモートリポジトリから最新版をローカルリポジトリに取得する

```
git pull
```
