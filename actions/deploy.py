from st2common.runners.base_action import Action

class Test(Action):

    def run(self,args):
        response = "Welcome {}, to stackstorm".format(args)
        return (True,response)