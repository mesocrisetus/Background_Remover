import flet as ft
from flet import UserControl, TextButton, Row, Page
import os
import datetime
from datetime import datetime
from rembg import remove


class Test(UserControl):
    def __init__(self,input_folder,output_folder):
        super().__init__()       
        self.input = input_folder
        self.output = output_folder
        
        # self.btn_pick = ft.ElevatedButton(
        # text="Elegir imagenes",
        # data='pick',
        # on_click=self.clicked)
        
        self.extract = ft.ElevatedButton(
        text="Remover fondo",
        data='extract',
        on_click=self.clicked) 
        self.view = Row(controls=[self.extract])
        

    def clicked(self, e):
        if e.control.data == 'pick':
            print("Has elegido PICK")
        elif e.control.data == 'extract':
            self.procesar_imgs()
            
            
            
    def procesar_imgs(self):
        day = datetime.now().strftime('%Y-%m-%d %H-%M-$S')
        proccessed_folder = os.path.join(self.output,day)
        os.makedirs(proccessed_folder, exist_ok=True)
        
        for filename in os.listdir(self.input):
            if filename.endswith(('.png','.jpg','.jpeg')):
                input_path = os.path.join(self.input,filename)
                output_path = os.path.join(proccessed_folder,filename)
                
                self._removerbck_imgs(input_path,output_path)
                self._mover_imgsOriginales(input_path,proccessed_folder)
                
        dlg = ft.AlertDialog(
                title=ft.Text("Imagenes convertidas!"), on_dismiss=lambda e: print("Cerrado")
                )
        self.page.dialog = dlg
        dlg.open = True
        self.page.update()           

                
                
    def _removerbck_imgs(self,input_p,output_p):
        
        with open(input_p,'rb') as inp, open(output_p, 'wb') as output:
            back_output = remove(inp.read())
            output.write(back_output)
            pass
           
        
    def _mover_imgsOriginales(self,input_p, dest_p):
        
        original_f = os.path.join(dest_p,'Imagenes Originales')
        os.makedirs(original_f, exist_ok=True)
        filename = os.path.basename(input_p)
        new_path = os.path.join(original_f,filename)
        os.rename(input_p,new_path)
     
                
    def build(self):
        return self.view


def main(page: Page):

    page.window_center()
    page.window_height = 300
    page.window_width = 300
    page.window_max_height = 300
    page.window_max_width = 300
    input_folder = "input"
    output_folder = "output"
    t = Test(input_folder,output_folder)
    page.add(t)


app = ft.app(target=main)