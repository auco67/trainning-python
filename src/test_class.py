
class Test:
    def __init__(self) -> None:
        self.param1 = ""
        self.param2 = ""
        self.param3 = ""
        print("初期化")
        
    def __init__(self, param1:str, param2:str, param3:str) -> None:
        self.param1 = param1
        self.param2 = param2
        self.param3 = param3
        print("引数で初期化")
    
    def __del__(seft) -> None:
        print("インスタンスが破棄されました")
        
    def setParam1(self, param1:str) -> None:
        self.param1 = param1
    
    def setParam2(self, param2:str) -> None:
        self.param2 = param2
        
    def setParam3(self, param3:str) -> None:
        self.param3 = param3
        
    def getParam1(self) -> str:
        return self.param1
    
    def getParam2(self) -> str:
        return self.param2
    
    def getParam3(self) -> str:
        return self.param3
    
if __name__ == '__main__':
    t = Test("a", "b", "c")
    print(t.getParam1())
    t.setParam1("str")
    print(t.getParam1())
    print(t)