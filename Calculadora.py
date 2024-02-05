import tkinter as tk
import math

def calculate(operation):
    try:
        if operation == "Suma":
            result = float(entry1.get()) + float(entry2.get())
        elif operation == "Resta":
            result = float(entry1.get()) - float(entry2.get())
        elif operation == "Multiplicacion":
            result = float(entry1.get()) * float(entry2.get())
        elif operation == "División":
            num2 = float(entry2.get())
            if num2 == 0:
                result = "No puede dividir por cero"
            else:
                result = float(entry1.get()) / num2
        elif operation == "Raiz Cuadrada":
            result = math.sqrt(float(entry1.get()))
        elif operation == "Potencia":
            result = float(entry1.get()) ** float(entry2.get())
        elif operation == "Logaritmo":
            result = math.log(float(entry1.get()))
        else:
            result = "Operación Inválida!"
            
        result_label.config(text = "resultado: " + str(result))
    except ValueError:
        result_label.config(text="Entrada Inválida!")
        
root = tk.Tk()
root.title("Calculadora")
    
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=5, pady=5)
    
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, padx=5, pady=5)
    
operations = [
        "Suma",
        "Resta",
        "Multiplicacion",
        "División",
        "Raiz Cuadrada",
        "Potencia",
        "Logaritmo"
]
    
row_val = 2
for operation in operations:
        operation_button = tk.Button(root, text=operation, command=lambda op=operation: calculate(op))
        operation_button.grid(row=row_val, column=0, columnspan=2, padx=5, pady=5)
        row_val +=1

result_label = tk.Label(root)
result_label.grid(row=row_val, column=0, columnspan=2)

root.mainloop()
    