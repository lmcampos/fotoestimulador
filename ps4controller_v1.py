from pyPS4Controller.controller import Controller
from variables import Variable
import datetime
import csv
import os
import sys

class MyController(Controller):

    MEL = False
      
    def __init__(self,s,lm,mel,**kwargs):
        self.s = s
        self.lm = lm
        self.mel = mel

        super().__init__(**kwargs)

    def on_R2_press(self,value):
        pass    
    def on_R2_release(self):
        pass    
    
    #PWM1 - Variable S
    # def on_up_arrow_press(self):
    def on_R3_down(self,value):    
        new_value = self.s.get_value() + Variable.get_increment()
        self.s.set_value(new_value)
        print("valor de la variable s:",self.s.get_value())  
        
        
    #def on_down_arrow_press(self):
    def on_R3_up(self,value):
        
        self.s.set_value(self.s.get_value() - Variable.get_increment())
        print("valor de la variable s:", self.s.get_value())

    def on_R3_y_at_rest(self):
        pass
    
    #Analógico izquierdo
    def on_L3_up(self,value):
        
        self.s.set_value(self.s.get_value() + Variable.get_increment())
        print("valor de la variable s:", self.s.get_value())         

        
    def on_L3_down(self,value):
           
        self.s.set_value(self.s.get_value() - Variable.get_increment())
        print("valor de la variable s:",self.s.get_value())
    
    def on_L3_x_at_rest(self):
        
        pass
    
    def on_L3_y_at_rest(self):
        
        pass
    
    def on_L3_left(self,value):
        pass


    #PWM2 --> Variable LM 
    #def on_triangle_press(self):
    def on_square_press(self):    
       self.lm.set_value(self.lm.get_value() + Variable.get_increment())
       print("valor de la variable lm:",self.lm.get_value())

    def on_square_release(self):
        pass   

    #def on_x_press(self):
    def on_circle_press(self):
        
        self.lm.set_value(self.lm.get_value() - Variable.get_increment())
        print("valor de la variable lm:",self.lm.get_value())

    def on_circle_release(self):
        pass    
    
    #Analógico derecho    
    #def on_R3_up(self,value):
    def on_R3_left(self,value):
        
        self.lm.set_value(self.lm.get_value() + Variable.get_increment()) 
        print ("valor de la variable lm:",self.lm.get_value())

    def on_R3_x_at_rest(self):
        
        pass

    #def on_R3_down(self,value):
    def on_R3_right(self,value):    
        self.lm.set_value(self.lm.get_value() - Variable.get_increment())   
        print("valor de la variable lm:",self.lm.get_value())

        

    #Variabble MEL   
    def on_L1_press(self):
        if(MyController.MEL == False):
            self.mel.set_value(Variable.LOWER_LIMIT)
            MyController.MEL = True
        print("valor de la variable mel:",self.mel.get_value())

    def on_L1_release(self):
        pass   
    
    def on_R1_press(self):
        if(MyController.MEL == False):
            self.mel.set_value(Variable.UPPER_LIMIT)
            MyController.MEL = True
        print("valor de la variable mel:",self.mel.get_value()) 

    def on_R1_release(self):
        pass   
    
    def on_playstation_button_press(self):
        #aqui debo convertir los datos de las variables en listas
        data = []
        #title = (self.s.name,self.lm.name,self.mel.name,"datatime")
        values = (self.s.get_value(),self.lm.get_value(),self.mel.get_value(),str(datetime.datetime.now()))
        #data.append(title)
        data.append(values)
        print(data)
        with open ("archive_log.csv","a",encoding="UTF-8")as f:
            writer = csv.writer(f)
            writer.writerows(data)
        print("datos guardados en el archivo CSV!!!!")
        print("reiniciando el script.......")
        python = sys.executable
        os.execl(python,python,*sys.argv)
        

   # def listen(self):    
        #self.init_all()
        #self.listen_for_events()