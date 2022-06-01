from tkinter import *

ventana = Tk()
ventana.title("Calculator")

i = 0

e_texto = Entry (ventana, font= ("Calibri 20"))
e_texto.grid (row=0, column = 0,columnspan= 4, padx = 5, pady = 5)

#Funciones
def click_button(valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar():
    e_texto.delete (0, END)
    i= 0

def hacer_operacion():
    ecuacion= e_texto.get()
    resultado = eval(ecuacion)
    e_texto.delete (0, END)
    e_texto.insert(0,resultado)
    i=0

    #Validacion de si es un numero primo 
    if resultado > 1:
        for i in range(2, int(resultado/2)+1):
            if (resultado % i) == 0:
                print("El resultado no es un numero primo")
                break
        else:
            print("El resultado es un numero primo")

    #Validacion de si el numero es palindromo 
    num = resultado

    print ("El resultado es : " + str(num)) 
    
    res = str(num) == str(num)[::-1]  

    print ("Es ese numero palindromo? : " + str(res)) 

#Caracteristicas de los botones
button1 = Button(ventana,text="1", width=5, height=2, command= lambda: click_button(1))
button2 = Button(ventana,text="2", width=5, height=2, command= lambda: click_button(2))
button3 = Button(ventana,text="3", width=5, height=2, command= lambda: click_button(3))
button4 = Button(ventana,text="4", width=5, height=2, command= lambda: click_button(4))
button5 = Button(ventana,text="5", width=5, height=2, command= lambda: click_button(5))
button6 = Button(ventana,text="6", width=5, height=2, command= lambda: click_button(6))
button7 = Button(ventana,text="7", width=5, height=2, command= lambda: click_button(7))
button8 = Button(ventana,text="8", width=5, height=2, command= lambda: click_button(8))
button9 = Button(ventana,text="9", width=5, height=2, command= lambda: click_button(9))
button0 = Button(ventana,text="0", width=15, height=2, command= lambda: click_button(0))

button_borrar = Button(ventana,text="AC", width=5, height=2, command= lambda: borrar())
button_parentesis1 = Button(ventana,text="(", width=5, height=2, command= lambda: click_button("("))
button_parentesis2 = Button(ventana,text=")", width=5, height=2, command= lambda: click_button(")"))
button_punto = Button(ventana,text=".", width=5, height=2, command= lambda: click_button("."))

button_div = Button(ventana,text="/", width=5, height=2, command= lambda: click_button("/"))
button_mult = Button(ventana,text="*", width=5, height=2, command= lambda: click_button("*"))
button_sum = Button(ventana,text="+", width=5, height=2, command= lambda: click_button("+"))
button_rest = Button(ventana,text="-", width=5, height=2, command= lambda: click_button("-"))
button_igual = Button(ventana,text="=", width=5, height=8, command= lambda: hacer_operacion())

# Botones en pantalla
button_borrar.grid (row="1", column=0, padx=5, pady=5)
button_parentesis1.grid (row="1", column=1, padx=5, pady=5)
button_parentesis2.grid (row="1", column=2, padx=5, pady=5)
button_div.grid (row="1", column=3, padx=5, pady=5)

button7.grid (row=2, column=0, padx=5, pady= 5)
button8.grid (row=2, column=1, padx=5, pady= 5)
button9.grid (row=2, column=2, padx=5, pady= 5)
button_mult.grid (row=2, column=3, padx=5, pady= 5)

button4.grid (row=3, column=0, padx=5, pady= 5)
button5.grid (row=3, column=1, padx=5, pady= 5)
button6.grid (row=3, column=2, padx=5, pady= 5)
button_sum.grid (row=3, column=3, padx=5, pady= 5)

button1.grid (row=4, column=0, padx=5, pady= 5)
button2.grid (row=4, column=1, padx=5, pady= 5)
button3.grid (row=4, column=2, padx=5, pady= 5)
button_rest.grid(row=4, column=3, padx=5, pady= 5)

button0.grid (row=5, column=0, columnspan=2, padx=5, pady= 5)
button_punto.grid (row=5, column=2, padx=5, pady= 5)
button_igual.grid (row=5, column=3, padx=5, pady= 5)

ventana.mainloop()

