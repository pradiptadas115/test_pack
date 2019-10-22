from st2common.runners.base_action import Action

class python_deploy(Action):
    
    def run(self,param):
        print("this is workflow test python file")
        print(param)