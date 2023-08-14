from ps4controller_v1 import MyController
from variables import Variable
import random

if __name__=='__main__':
    s   = Variable("S")
    lm  = Variable("LM")
    mel = Variable("MEL")
    
    MyController.MEL = False
    
    s.set_value(random.uniform(0.300000000, 0.800000000))
    lm.set_value(random.uniform(0.300000000, 0.800000000))
    print("valor de la variable s: ",s.get_value())
    print("valor de la variable lm: ", lm.get_value())
    
    controller = MyController(s,lm,mel,interface="/dev/input/js0", connecting_using_ds4drv=False)
    controller.listen()
