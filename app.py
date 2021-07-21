class god:
    def __init__(self):
        print("god is ready")

    def superpower(self):
        print('superpower')

    def language(self):
        print('god language')

class human(god):
   #constructor
    def __init__(self):
        
        super().__init__()
        print('human ready')
       
    #method
    def talk(self):
        print('shawn is talking')
    def language(self):
        print('human language')

#interface detects which class file to call function
def say_hello(lang):
    lang.language()

shawn = human()
lord = god()
say_hello(lord)
