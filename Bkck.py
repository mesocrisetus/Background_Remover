import flet as ft
import os
import datetime
from datetime import datetime
from rembg import remove



class BackgroundRemover:
    
    def __init__(self,input_folder,output_folder):
        self.input = input_folder
        self.output = output_folder
        
    def procesar_imgs(self):
        day = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        proccessed_folder = os.path.join(self.output,day)
        os.makedirs(proccessed_folder, exist_ok=True)
        
        for filename in os.listdir(self.input):
            if filename.endswith(('.png','.jpg','.jpeg')):
                input_path = os.path.join(self.input,filename)
                output_path = os.path.join(proccessed_folder,filename)
                
                self._removerbck_imgs(input_path,output_path)
                self._mover_imgsOriginales(input_path,proccessed_folder)
        
    def _removerbck_imgs(self,input_p,output_p):
        
        with open(input_p,'rb') as inp, open(output_p, 'wb') as output:
            back_output = remove(inp.read())
            output.write(back_output)
            pass
           
        
    def _mover_imgsOriginales(self,input_p, dest_p):
        
        original_f = os.path.join(dest_p,'originals')
        os.makedirs(original_f, exist_ok=True)
        filename = os.path.basename(input_p)
        new_path = os.path.join(original_f,filename)
        os.rename(input_p,new_path)
        
if __name__ == '__main__':
    
    input_folder = "input"
    output_folder = "output"
    
    remover = BackgroundRemover(input_folder,output_folder)
    remover.procesar_imgs()
        
        
        

    
