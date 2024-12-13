class Test:
    def __init__(self):
        print("123")
    def __call__(self, *args, **kwargs):
        print("diao yong",args)

t = Test()
t("123","456")
