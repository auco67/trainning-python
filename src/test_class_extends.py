from test_class import Test

class Test2(Test):
    
    def __init__(self) -> None:
        super().__init__()
    
    def __init__(self, param1:str, param2:str, param3:str) -> None :
        super().__init__(param1=param1, param2=param2,param3=param3)
        self.param1 = "init"
        
if __name__ == '__main__':
    t = Test2("a", "b", "c")
    print(t.getParam1())