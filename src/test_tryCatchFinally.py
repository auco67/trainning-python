import traceback

def test():
    content={}
    
    try:
        print("try")
        
    except Exception as e:
        print("Exception")        
        print(e)
        print(traceback.format_exc())
        return {
            'result': False,
            'error': {
                'type': e.__class__.__name__,
                'msg': traceback.format_exc(),
            },
            'content': {}
        }
        
    finally:
        print("finally")
        

if __name__ == "__main__":
    test()