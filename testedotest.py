from tkinter import *

root = Tk()
root.title("Teste Tkinter")
#root.geometry("300x300")

def save():
   n_save = nome_imput.get()
   s_save = sobrenome_imput.get()
   cep_save = cep_imput.get()
   rua_save = rua_imput.get()
   num_save = num_imput.get()
   bairro_save = bairro_imput.get()
   cidade_save = cidade_imput.get()
   estado_save = estado_imput.get()

   variavel = ("Nome: " + n_save + "\n" 
   + "Sobrenome: " + s_save + "\n"
   + "CEP: " + cep_save + "\n"
   + "Rua: " + rua_save + "\n"
   + "Numero: " + num_save + "\n"
   + "Bairro: " + bairro_save + "\n"
   + "Cidade: " + cidade_save + "\n"
   + "Estado: " + estado_save)

   f = open("{} {}.txt".format(n_save, s_save), "w")
   f.write(variavel)
   f.close()

   root.destroy()
  

# FRAMES
frame = LabelFrame(root, text="Cadastro")
frame.grid(row=0, column=0, columnspan=2)

frame1 = LabelFrame(root, text="Resultado")
frame1.grid(row=3, column=0)

# NOME
nome = Label(frame, text="Nome")
nome.grid(row=0, column=0)
nome_imput = Entry(frame)
nome_imput.grid(row=0, column=1)

# SOBRENOME
sobrenome = Label(frame, text="Sobrenome")
sobrenome.grid(row=1, column=0)
sobrenome_imput = Entry(frame)
sobrenome_imput.grid(row=1, column=1)

# CEP
cep = Label(frame, text="CEP")
cep.grid(row=2, column=0)
cep_imput = Entry(frame)
cep_imput.grid(row=2, column=1)

# Rua
rua = Label(frame, text="Rua")
rua.grid(row=3, column=0)
rua_imput = Entry(frame)
rua_imput.grid(row=3, column=1)

# Numero
num = Label(frame, text="Numero")
num.grid(row=4, column=0)
num_imput = Entry(frame)
num_imput.grid(row=4, column=1)

# Bairro
bairro = Label(frame, text="Bairro")
bairro.grid(row=5, column=0)
bairro_imput = Entry(frame)
bairro_imput.grid(row=5, column=1)

# Cidade
cidade = Label(frame, text="Cidade")
cidade.grid(row=6, column=0)
cidade_imput = Entry(frame)
cidade_imput.grid(row=6, column=1)

# Estado
estado = Label(frame, text="Estado")
estado.grid(row=7, column=0)
estado_imput = Entry(frame)
estado_imput.grid(row=7, column=1)

salvar = Button(root, text="Save", command=save)
salvar.grid(row=1, column=0)

root.mainloop()
