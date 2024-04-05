from customtkinter import *
import customtkinter

root = customtkinter.CTk()
root.title("Conversor de Unidades")
root.geometry("300x500")
root.minsize(300, 500)
root.maxsize(300, 500)
root.iconbitmap("unidade.ico")

opcoes = ["M", "KM", "L", "ML", "kg", "G"]
opcoes2 = ["KM"]
var = StringVar(root)
var.set(opcoes[0])
var1 = StringVar(root)
var1.set(opcoes2[0])

def converter(*args):
    if var.get() == 'M':
        opcoes2.clear()
        opcoes2.append("KM")
        var1.set(opcoes2[0])
    elif var.get() == 'KM':
        opcoes2.clear()
        opcoes2.append("M")
        var1.set(opcoes2[0])
    elif var.get() == 'kg':
        opcoes2.clear()
        opcoes2.append("G")
        var1.set(opcoes2[0])
    elif var.get() == 'G':
        opcoes2.clear()
        opcoes2.append("kg")
        var1.set(opcoes2[0])
    elif var.get() == 'L':
        opcoes2.clear()
        opcoes2.append("ML")
        var1.set(opcoes2[0])
    elif var.get() == 'ML':
        opcoes2.clear()
        opcoes2.append("L")
        var1.set(opcoes2[0])
    else:
        opcoes2.clear()
        var1.set("")

var.trace('w', converter)

def passar():
    try:
        dados = int(valor.get())   
        if var.get() == 'M':
            return resultado.configure(text=(dados/1000, var1.get()))    
        elif var.get() == 'KM':
            return resultado.configure(text=(dados*1000, var1.get()))  
        elif var.get() == 'kg':
            return resultado.configure(text=(dados*1000, var1.get()))  
        elif var.get() == 'G':
            return resultado.configure(text=(dados/1000, var1.get()))  
        elif var.get() == 'L':
            return resultado.configure(text=(dados*1000, var1.get()))  
        elif var.get() == 'ML':
            return resultado.configure(text=(dados/1000, var1.get() )) 
        
    except:
        return resultado.configure(text="Insira um valor inteiro")
    
ola = customtkinter.CTkLabel(root, text="Converta Unidades aqui: ")
ola.place(relx=0.5, y=30, anchor="center")

opcao1 = customtkinter.CTkOptionMenu(root, variable=var, values=opcoes)
opcao1.place(relx=0.5, y=100, anchor="center")

de = customtkinter.CTkLabel(root, text="DE:")
de.place(relx=0.5, y=60, anchor="center")

para = customtkinter.CTkLabel(root, text="PARA:")
para.place(relx=0.5, y=140, anchor="center")

opcao2 = customtkinter.CTkOptionMenu(root, variable=var1, values=opcoes2)
opcao2.place(relx=0.5, y=180, anchor="center")

escreva = customtkinter.CTkLabel(root, text="INSIRA O VALOR:")
escreva.place(relx=0.5, y=230, anchor="center")

valor = customtkinter.CTkEntry(root)
valor.place(relx=0.5, y=270, anchor="center")

converter_btn = customtkinter.CTkButton(root, text="converter", command=passar)
converter_btn.place(relx=0.5, y=320, anchor="center")

resultado = customtkinter.CTkLabel(root, text="")
resultado.place(relx=0.5, y=360, anchor="center")
root.mainloop()
