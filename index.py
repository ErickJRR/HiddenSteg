from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image
from pytea import TEA #Libreria TEA (metodo de encriptacion a emplear)
import hashlib #Libreria para crear el hash
import hmac #Libreria para crear el hash con clave para autenticación de mensajes

#   Ventana Principal
root=Tk()
root.title("-- Proyecto HiddenSteg --")
root.config(bg="brown")
root.geometry("600x350")
root.resizable(False, False)

#   Titulos principales
Label(root, text="Bienvenidos a Nuestro Proyecto", fg="white", bg="brown", font = ("Times", "28", "bold italic")).place(x=60, y=27)
Label(root, text="HiddenSteg", fg="white", bg="brown", font = ("Times", "26", "bold italic")).place(x=210, y=100)

# ----//Agregamos el logo de la uni
imagenL = PhotoImage(file="C:/Users/Alan/Desktop/PRGCN/Curso_Python/unitec.png")
imagenL = imagenL.zoom(6)
imagenL = imagenL.subsample(10)
logo = Label(root, image = imagenL).place(x=219, y=160)

#   Menu Barhttps://www.tutorialspoint.com/python3/tk_label.htm
menubar = Menu(root)
root.config(menu=menubar)
ruta_img = StringVar()
texto_mensaje = StringVar()
texto_oculto = StringVar()

#   funciones
def nombre_img(ruta):
    
    diag = [pos for pos, char in enumerate(ruta) if char == '/']
    diag_max = max(diag)
    nombre = ruta[diag_max+1:]
    return nombre

def ingresar():
    
       i = filedialog.askopenfilename(filetypes =[('png files', '*.png')])
       if i != '':
           ruta_img.set(i)
           img = PhotoImage(file=i)
           img = img.zoom(8)
           img = img.subsample(32)
           foto = Label(form_encriptar, image = img).place(x = 220, y = 135)
           foto.pack()
           
       
def ingresar_lectura():
       
       i = filedialog.askopenfilename(filetypes =[('png files', '*.png')]) 
       if i != '':
           ruta_img.set(i)
           img = PhotoImage(file=i)
           img = img.zoom(10)
           img = img.subsample(32)
           foto = Label(form_leer, image = img).place(x = 340, y = 70)
           foto.pack()


def guardarysalir():
    
    a = mensaje_texto
    ventana.destroy()
    
    pass    

       
def Encriptacion():
    
    mensaje = texto_mensaje.get()#Mensaje que se encriptara
    nom_img = nombre_img(ruta_img.get())
    
    key = nom_img.encode() #En el proyecto la llave se genera a partir del nombre de la imagen
    
    h = hashlib.sha256() 
    h.update(key) #Metodo que permite actualizar el hash en base a la cadena de valores hexadecimales antes creada (es el nombre de imagen)
    p = bytes.fromhex(h.hexdigest()[:32]) #Permite pasar de hexadecimal a bytes
    tea = TEA(p) #Se crea el objeto TEA que es el algortimo que se emplea para encriptar
    mensaje_oculto = tea.encrypt(mensaje.encode())
    
    clave = hmac.new(key,mensaje_oculto,hashlib.sha256).hexdigest() #Se crea el hash con clave para autenticación de mensajes
    # =============================================================================
    # .encode() pasa de texto a bytes 
    # .hexdigest() muestra el resultado en hexadecimal
    # =============================================================================
    secreto = "%s--:--%s" %(clave,bytes(mensaje_oculto).hex()) #Se concatena el mensaje con la clave
    encripta = tea.encrypt(secreto.encode()) #Se encripta el mensaje pasa de texto o hexadecimal a bytearray
    
    def plus(str):
     
        return str.zfill(8) 
     
    
    def get_key(strr):
        
        men = strr.hex()
        str = "" 
    
        for i in range(len(men)): 
    
             str = str+plus(bin(ord(men[i])).replace('0b',''))
    
        return str 
    
    def mod(x,y):
     
        return x%y;
     
    
    def func(str1,str2,str3):  
     
        im = Image.open(str1) 

        width = im.size[0] 
        height = im.size[1]
        count = 0 
    
        key = get_key(str2) 
     
        keylen = len(key) 
        tam = int(keylen/16)
      
        pixel = im.getpixel((0,0)) 
     
        if tam < 255:
            a = tam
            b = 0
            c = 0
        else:
            a = abs(255-tam)
            b = abs(255-a)
            c = abs(255-b)
            
        im.putpixel((0,0),(a,b,c))
        
        for h in range(0,height): 
     
            for w in range(1,width):
     
                pixel = im.getpixel((w,h)) 
     
                a=pixel[0] 
     
                b=pixel[1] 
     
                c=pixel[2] 
     
                if count == keylen: 
     
                    break
                
                      
                a= a-mod(a,2)+int(key[count])
     
                count+=1
     
                if count == keylen: 
     
                    im.putpixel((w,h),(a,b,c))
     
                    break
                
                b =b-mod(b,2)+int(key[count])
         
                count+=1
     
                if count == keylen: 
     
                    im.putpixel((w,h),(a,b,c))
     
                    break
     
                c= c-mod(c,2)+int(key[count])
         
                count+=1
     
                if count == keylen: 
     
                    im.putpixel((w,h),(a,b,c))
     
                    break
     
                if count % 3 == 0: 
     
                    im.putpixel((w,h),(a,b,c))
     
        im.save(str3)
        messagebox.showinfo(message="Tu mensaje ya fue ocultado", title="Guardado")
       
    old = ruta_img.get()
    
    new = ruta_img.get()
    
    enc = encripta
    
    func(old,enc,new)
#-------------------------------------------------------------------------     
def Lectura_img():
    
    def mod(x,y):
 
        return x%y;

    def toasc(strr):
 
        return int(strr, 2)
 

    def func2(str1):
  
        b=""
     
        im = Image.open(str1) 

        width = im.size[0]
        height = im.size[1]
        count = 0 
       
        pixeltam = im.getpixel((0, 0)) 
        
        lenth = (pixeltam[0] + pixeltam[1] + pixeltam[2]) * 16
        
        for h in range(0, height):
     
            for w in range(1, width):
      
                pixel = im.getpixel((w, h)) 
    
                if count%3==0:
     
                    count+=1 
    
                    b=b+str((mod(int(pixel[0]),2))) 
     
                    if count ==lenth: 
     
                        break
     
                if count%3==1:
     
                    count+=1
     
                    b=b+str((mod(int(pixel[1]),2)))
     
                    if count ==lenth:
     
                        break
     
                if count%3==2:
     
                    count+=1
     
                    b=b+str((mod(int(pixel[2]),2)))
     
                    if count ==lenth:
     
                        break
     
            if count == lenth:
     
                break
        
        r = ''
     
        for i in range(0,len(b),8): 
     
            stra = toasc(b[i:i+8])
            
            r = r + chr(stra)
    
        msm = bytearray.fromhex(r)
        
        nom_img = nombre_img(str1)
        key2 = nom_img.encode() 
        
        h2 = hashlib.sha256() #Se crea la interfaz sha256, la cual servira como llave del algoritmo TEA
        h2.update(key2) #Metodo que permite actualizar el hash en base a la cadena de valores hexadecimales antes creada (es el nombre de imagen)
        p2 = bytes.fromhex(h2.hexdigest()[:32]) #Permite pasar de hexadecimal a bytes
        dtea = TEA(p2) #Se crea otro objeto TEA cuya llave hash debe ser la misma (p) para descencriptar ya que es una encriptacion simetrica (ambos usuarios con la misma llave)
        descencripta = dtea.decrypt(msm) #Se descencripta el mensaje
        j = descencripta.decode() #Se pasa de byte a hexadecimal y texto respectivamente, gracias al .decode()
        mac,data = j.split('--:--') #Permite separara la clave del mensaje (empleando el separador declarado en la concatenacion de secreto)
        mensaje_ocultado = bytearray.fromhex(data)
        clave2 = hmac.new(key2,mensaje_ocultado,hashlib.sha256).hexdigest() 
        
        if clave2 == mac:
            mensajes = dtea.decrypt(mensaje_ocultado)
            m = mensajes.decode()
            messagebox.showinfo(message="Leido correctamente", title="Leer")
        else:
            m = "Error"
            messagebox.showinfo(message="Ocurrio un problema que genero un cambio en la imagen", title="Error")

        texto_oculto.set(m)

    new2 = ruta_img.get()

    func2(new2) 
   
#------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------Ventanas de interfaz---------------------------------------------------------       
def frmEncriptar():
    hide_frm()
    form_encriptar.pack(fill="both", expand=1)
    Label(form_encriptar, fg="white", bg="grey", text="A continuación presenciará el proceso de Esteganografía:", font=("Courier","12", "bold")).place(x=20, y= 15)
    
    Label(form_encriptar, fg="white", bg="grey", width=20, anchor="e", text="Capture su texto: ", font=("Courier","12", "bold")).place(x=25, y=50)
    
    
    Label(form_encriptar, fg="white", bg="grey", anchor="e", text="Seleccione una imagen: ",font=("Courier","12", "bold")).place(x=25, y=110)
    Button(form_encriptar, text="Buscar imagen", command=ingresar).place(x=45, y=140)
    
    Entry(form_encriptar, bg="pink", textvariable = texto_mensaje, width= 90).place(x=30,y=80)
    Label(form_encriptar, fg="white", bg="grey", anchor="e", text="Encriptar texto:", font=("Courier","12", "bold")).place(x=360, y=110)
    Button(form_encriptar, text="Encriptar", command = Encriptacion).place(x=490, y=140)
    
def frmLeer():
    hide_frm()
    form_leer.pack(fill="both", expand=1)    
    Label(form_leer, text="Seleccione la imagen que desea desencriptar:", bg="grey", fg="white", font=("Courier","14", "bold")).place(x=45, y=30)
    Button(form_leer, text="Buscar imagen", command=ingresar_lectura).place(x=50, y=65)
    Button(form_leer, text="Leer mensaje", command= Lectura_img).place(x=170, y=65)
    texto = Text(form_leer, width=28, height=8, bg="pink").place(x=45, y=100)
    
    
def frmInfo():
    hide_frm()
    form_info.pack(fill="both", expand=1)
    Label(form_info, fg="white", bg="brown", width=13, anchor="e", text= "Realizado por: ", font = ("Times", "20", "bold italic")).place(x=20,y=12)
    Label(form_info, fg="white", bg="brown", text= "Alan García Patiño", font = ("Times", "14", "bold italic")).place(x=180,y=45)
    Label(form_info, fg="white", bg="brown", text= "Jonathan Hernández Ortega", font = ("Times", "14", "bold italic")).place(x=180,y=65)
    Label(form_info, fg="white", bg="brown", text= "Erick Jair Rosete Ruiz", font = ("Times", "14", "bold italic")).place(x=180,y=85)
    Label(form_info, fg="white", bg="brown", text= "Diana Laura Almeraya Salas", font = ("Times", "14", "bold italic")).place(x=180,y=105) 
    
    Label(form_info, fg="white", bg="brown", anchor="e", text= "Materia: ", font = ("Times", "20", "bold italic")).place(x=70,y=125)
    Label(form_info, fg="white", bg="brown", text= "Procesamiento Digital de Imágenes", font = ("Times", "16", "bold italic")).place(x=180,y=150)
    
    Label(form_info, fg="white", bg="brown", anchor="e", text= "Profesor: ", font = ("Times", "20", "bold italic")).place(x=70,y=180)
    Label(form_info, fg="white", bg="brown", text= "Raymundo Soto Soto", font = ("Times", "16", "bold italic")).place(x=180,y=210)
    
    imagenM = PhotoImage(file="C:/Users/Alan/Desktop/PRGCN/Curso_Python/unitec.png")
    imagenM = imagenM.zoom(9)
    imagenM = imagenM.subsample(20)
    logo_2=Label(form_info, image = imagenM).place(x=430, y=200)
    logo_2.pack()
    
def myCommand():
    mylabel = Label(root, text="hiciste click").pack()

def hide_frm():
    
    form_encriptar.pack_forget()
    form_leer.pack_forget()
    form_info.pack_forget()
    
 
#   Crear menu item
file_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Archivo", menu=file_menu)

file_menu.add_command(label="Encriptar", command=frmEncriptar) 
file_menu.add_command(label="Leer", command=frmLeer)  
file_menu.add_command(label="Info", command=frmInfo)    
file_menu.add_separator()
file_menu.add_command(label="Salir", command=root.destroy)

#   Crear frames
form_encriptar = Frame(root, width=600, height=350, bg="gray")
form_leer = Frame(root, width=600, height=350, bg="gray")
form_info = Frame(root, width=600, height=350, bg="brown")

#entrada = Entry(form_leer, bg="pink", width=45, textvariable= texto_oculto, state = 'readonly').place(x=50,y=115)


#   Inicia app
root.mainloop()