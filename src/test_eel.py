import eel
import os

# eel.expose直下のsay_hello_pyはjavascript側で呼び出すことができる
@eel.expose
def say_hello_py(x):
        print("Hello from %s" %x)

#python側でsay_hello_pyを呼び出すとjavascript側より最初に呼び出される
say_hello_py('Python World! First action.')

def view(link='hello.html'):
        eel.init(f'{os.path.dirname(os.path.realpath(__file__))}/web')
        eel.start(link)

# 最初に読み込まれる
if __name__ == "__main__":
    view()