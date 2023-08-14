
class Variable:

    UPPER_LIMIT = 1.000000000
    LOWER_LIMIT = 0.000000000
    RESOLUTION = 4096
    VALUE_INCREMENT  = (1/RESOLUTION)
    
    def __init__(self,name):
        self.name = name
        self.value = Variable.LOWER_LIMIT
        
    def set_value(self,value):
        if (value >= Variable.LOWER_LIMIT and value <= Variable.UPPER_LIMIT ):
            self.value = value
        else:
            #cuando value esté entre el 0.0 y la resoñución establezco a value a 0.0
            if (self.value > Variable.LOWER_LIMIT and self.value < Variable.VALUE_INCREMENT):
                self.value = Variable.LOWER_LIMIT
            else:
                    #cuando value esté entre el 1-1/4096 y 1.0, establezco a value a 1.0
                    if(self.value >(Variable.UPPER_LIMIT - Variable.VALUE_INCREMENT ) and self.value < Variable.UPPER_LIMIT):
                        self.value = Variable.UPPER_LIMIT
                    else:
                        print("el valor estafuera del rango permitido [0.0 - 1.0]")

    
    def get_value(self):
        return self.value
    
    @staticmethod
    def get_upper_limit():
        return  Variable.UPPER_LIMIT

    @staticmethod
    def get_lower_limit():
        return  Variable.LOWER_LIMIT

    @staticmethod
    def get_increment():
        return  Variable.VALUE_INCREMENT
        