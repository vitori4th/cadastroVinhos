import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Entry,Label

class Vinho:
    def __init__(self, codigo, nome, tipo, variedade, origem, preco):
        self.codigo = codigo
        self.nome = nome
        self.tipo = tipo
        self.variedade = variedade
        self.origem = origem
        self.preco = preco
    
    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getTipo(self):
        return self.tipo

    def getVariedade(self):
        return self.variedade

    def getOrigem(self):
        return self.origem

    def getPreco(self):
        return self.preco

    def getVinho(self):
        return "Nome: " + str(self.getNome())\
        + "\nCodigo: " + str(self.getCodigo())\
        + "\nTipo: " + str(self.getTipo())\
        + "\nVariedade: " + str(self.getVariedade())\
        + "\nOrigem: " + str(self.getOrigem())\
        + "\nPreço: " + str(self.getPreco())


class tipoInv(Exception):
    pass

class variedadeInv(Exception):
    pass

class origemInv(Exception):
    pass

class campoVazio(Exception):
    pass
    

class LimiteInsereVinho(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Vinho")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameTipo = tk.Frame(self)
        self.frameVariedade = tk.Frame(self)
        self.frameOrigem = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameTipo.pack()
        self.frameVariedade.pack()
        self.frameOrigem.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelTipo = tk.Label(self.frameTipo, text="Tipo: ")
        self.labelVariedade = tk.Label(self.frameVariedade, text="Variedade: ")
        self.labelOrigem = tk.Label(self.frameOrigem, text="Origem: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelTipo.pack(side="left")
        self.labelVariedade.pack(side="left")
        self.labelOrigem.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputTipo = tk.Entry(self.frameTipo, width=15)
        self.inputVariedade = tk.Entry(self.frameVariedade, width=20)
        self.inputOrigem = tk.Entry(self.frameOrigem, width=15)
        self.inputPreco = tk.Entry(self.framePreco, width=10)
        self.inputCodigo.pack(side="left")
        self.inputNome.pack(side="left")
        self.inputTipo.pack(side="left")
        self.inputVariedade.pack(side="left")
        self.inputOrigem.pack(side="left")
        self.inputPreco.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteConsultaVinho(tk.Toplevel):
    def __init__(self, controle):
        self.controle=controle

        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Consulta Vinhos")

        self.frameTipo = tk.Frame(self)
        self.frameTipo.pack()

        
        self.labelTipo = tk.Label(self.frameTipo,text="Tipo: ")
        self.labelTipo.pack(side="left")

        self.escolhaComboTipo = tk.StringVar()
        self.comboboxTipo = ttk.Combobox(self.frameTipo, width = 15 , textvariable = self.escolhaComboTipo)
        self.comboboxTipo.pack(side="left")
        self.comboboxTipo['values'] = controle.listaTipos
        self.comboboxTipo.bind("<<ComboboxSelected>>", controle.exibeTipo)

        self.frameVar = tk.Frame(self)
        self.frameVar.pack()

        self.labelVar = tk.Label(self.frameVar,text="Variedade: ")
        self.labelVar.pack(side="left")

        self.escolhaComboVar = tk.StringVar()
        self.comboboxVar = ttk.Combobox(self.frameVar, width = 15 , textvariable = self.escolhaComboVar)
        self.comboboxVar.pack(side="left")
        self.comboboxVar['values'] = controle.listaVar
        self.comboboxVar.bind("<<ComboboxSelected>>", controle.exibeVariedade)

        self.lbl2 = tk.Label(self, text="")
        self.lbl2.pack(side="left")

    def mostraJanela(self,str):
        messagebox.showinfo('Lista de disciplinas', str)

class CtrlVinho():
    def __init__(self, controlador):
        self.controlador = controlador
        self.listaTipos = ["Branco", "Tinto", "Rose", "Espumante"]
        self.listaVar = ["Cabernet Sauvignon", "Carmenere", "Merlot", "Malbec", "Sauvignon Blanc", "Pinot Grigio"]
        self.listaPaises = ["Brasil", "Argentina", "Chile", "Itália", "França", "Portugal", "África do Sul"]

        self.listaVinhos =  []
    
    def cadastraVinho(self):
        self.limiteIns = LimiteInsereVinho(self)

    def consultaVinho(self):
        self.limiteCons = LimiteConsultaVinho(self)
    
    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get()
        tipo = self.limiteIns.inputTipo.get()
        variedade = self.limiteIns.inputVariedade.get()
        origem = self.limiteIns.inputOrigem.get()
        preco = self.limiteIns.inputPreco.get()

        try:
            if tipo == "" or variedade == "" or  origem == "":
                raise campoVazio
            tem1=False
            for a in self.listaTipos:
                if a == tipo:
                    tem1=True
                    break
            if tem1==False:
                raise tipoInv

            tem2=False
            for a in self.listaVar:
                if a == variedade:
                    tem2=True
                    break
            if tem2==False:
                raise variedadeInv
        
            tem3=False
            for a in self.listaPaises:
                if a == origem:
                    tem3=True
                    break
            if tem3==False:
                raise origemInv
            vinho = Vinho(codigo, nome, tipo, variedade, origem, preco)
            self.listaVinhos.append(vinho)            
            self.limiteIns.mostraJanela('Sucesso', 'Vinho cadastrado com sucesso')
            self.clearHandler(event)

        except tipoInv:
            self.limiteIns.mostraJanela('Fracasso', 'Tipo Inválido')
        except variedadeInv:
            self.limiteIns.mostraJanela('Fracasso', 'Variedade Inválida')
        except origemInv:
            self.limiteIns.mostraJanela('Fracasso', 'Origem Inválida')
        except campoVazio:
            self.limiteIns.mostraJanela('Fracasso', 'Campo Vazio')   
        self.limiteIns.lift()
    
    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputTipo.delete(0, len(self.limiteIns.inputTipo.get()))
        self.limiteIns.inputVariedade.delete(0, len(self.limiteIns.inputVariedade.get()))
        self.limiteIns.inputOrigem.delete(0, len(self.limiteIns.inputOrigem.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def exibeTipo(self,event):
        tipo =event.widget.get()
        var = '\n'
        for v in self.listaVinhos:
            if v.getTipo()== tipo:
                var += 'Código:' + v.getCodigo() + '\n'
                var += 'Nome:' + v.getNome() + '\n'
                var += 'Tipo:' + v.getTipo() + '\n'
                var += 'Variedade:' + v.getVariedade() + '\n'
                var += 'Origem:' + v.getOrigem() + '\n'
                var += 'Preço:' + v.getPreco() + '\n'
                var += '\n'
        self.limiteCons.lbl2.config(text=var)

    def exibeVariedade(self, event):
        variedade =event.widget.get()
        var = '\n'
        for v in self.listaVinhos:
            if v.getVariedade()== variedade:
                var += 'Código:' + v.getCodigo() + '\n'
                var += 'Nome:' + v.getNome() + '\n'
                var += 'Tipo:' + v.getTipo() + '\n'
                var += 'Variedade:' + v.getVariedade() + '\n'
                var += 'Origem:' + v.getOrigem() + '\n'
                var += 'Preço:' + v.getPreco() + '\n'
                var += '\n'
        self.limiteCons.lbl2.config(text=var)
