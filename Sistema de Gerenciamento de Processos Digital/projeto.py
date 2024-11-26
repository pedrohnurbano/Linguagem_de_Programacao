import mysql.connector
import tkinter
from tkinter import *

conexao_banco = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = '',
    database = 'gerenciamento_processos'
)
cursor = conexao_banco.cursor()

# ----------------------------------------------------- #

def abrir_cad_processo():

    def cad_proc():
        number = number_cad.get()
        situation = situation_cad.get()
        date = date_cad.get()
        value = value_cad.get()
        nature = nature_cad.get()
        cod_cli = cod_cli_cad.get()
        cod_law = cod_law_cad.get()
        pass_cli = pass_cli_cad.get()
        pass_law = pass_law_cad.get()

        comando_sql = f'INSERT INTO processo (numero, situacao, inicio_processo, valor_causa, natureza, codcliente, codadvogado, parte_passiva_cli, parte_passiva_adv) VALUES ({number},"{situation}","{date}",{value},"{nature}",{cod_cli},{cod_law},"{pass_cli}","{pass_law}")'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    def deletar():
        number_cad.delete(0, END)
        situation_cad.delete(0, END)
        date_cad.delete(0, END)
        value_cad.delete(0, END)
        nature_cad.delete(0, END)
        cod_cli_cad.delete(0, END)
        cod_law_cad.delete(0, END)
        pass_cli_cad.delete(0, END)
        pass_law_cad.delete(0, END)

    # ----------------------------------------------------- #

    jan_cad_processo = Toplevel()

    jan_cad_processo.title("Cadastro do Processo")
    jan_cad_processo.geometry("700x900")

    img_path = PhotoImage(file=r"./imgs/jancadproc.png")
    bg_img = tkinter.Label(jan_cad_processo, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    number_cad = Entry(jan_cad_processo, font=("arial black",11), width=(42))
    number_cad.place(x=229, y=255)

    situation_cad = Entry(jan_cad_processo, font=("arial black",11), width=(42))
    situation_cad.place(x=229, y=322)

    date_cad = Entry(jan_cad_processo, font=("arial black",11), width=(42))
    date_cad.place(x=229, y=389)

    value_cad = Entry(jan_cad_processo, font=("arial black",11), width=(42))
    value_cad.place(x=229, y=456)

    nature_cad = Entry(jan_cad_processo, font=("arial black",11), width=(42))
    nature_cad.place(x=229, y=523)

    cod_cli_cad = Entry(jan_cad_processo, font=("arial black",11), width=(42))
    cod_cli_cad.place(x=229, y=590)

    cod_law_cad = Entry(jan_cad_processo, font=("arial black",11), width=(42))
    cod_law_cad.place(x=229, y=657)

    pass_cli_cad = Entry(jan_cad_processo, font=("arial black",11), width=(42))
    pass_cli_cad.place(x=229, y=724)

    pass_law_cad = Entry(jan_cad_processo, font=("arial black",11), width=(24))
    pass_law_cad.place(x=229, y=791)

    # ----------------------------------------------------- #

    submit = Button(jan_cad_processo, text="ENVIAR", command=cad_proc, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=480, y=788)

    delete = Button(jan_cad_processo, text="LIMPAR", command=deletar, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    delete.place(x=560, y=788)

    # ----------------------------------------------------- #

    jan_cad_processo.resizable(False,False)

    jan_cad_processo.mainloop()

    # ----------------------------------------------------- #

def abrir_cad_advogado():

    def cad_adv():
        oab = oab_cad.get()
        name = name_cad.get()
        uf = uf_cad.get()
        date = date_cad.get()
        cpf = cpf_cad.get()
        adress = adress_cad.get()
        phone = phone_cad.get()
        email = email_cad.get()
        expertise = expertise_cad.get()

        comando_sql = f'INSERT INTO advogado (numero_oab, nome_completo, uf_oab, data_nascimento, cpf, endereco, telefone, email, especialidade) VALUES ({oab},"{name}","{uf}","{date}",{cpf},"{adress}",{phone},"{email}","{expertise}")'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    def deletar():
        oab_cad.delete(0, END)
        name_cad.delete(0, END)
        uf_cad.delete(0, END)
        date_cad.delete(0, END)
        cpf_cad.delete(0, END)
        adress_cad.delete(0, END)
        phone_cad.delete(0, END)
        email_cad.delete(0, END)
        expertise_cad.delete(0, END)

    # ----------------------------------------------------- #

    jan_cad_advogado = Toplevel()

    jan_cad_advogado.title("Cadastro do Advogado")
    jan_cad_advogado.geometry("700x900")

    img_path = PhotoImage(file=r"./imgs/jancadadv.png")
    bg_img = tkinter.Label(jan_cad_advogado, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    oab_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(42))
    oab_cad.place(x=229, y=255)

    name_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(42))
    name_cad.place(x=229, y=322)

    uf_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(42))
    uf_cad.place(x=229, y=389)

    date_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(42))
    date_cad.place(x=229, y=456)

    cpf_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(42))
    cpf_cad.place(x=229, y=523)

    adress_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(42))
    adress_cad.place(x=229, y=590)

    phone_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(42))
    phone_cad.place(x=229, y=657)

    email_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(42))
    email_cad.place(x=229, y=724)

    expertise_cad = Entry(jan_cad_advogado, font=("arial black",11), width=(24))
    expertise_cad.place(x=229, y=791)

    # ----------------------------------------------------- #

    submit = Button(jan_cad_advogado, text="ENVIAR", command=cad_adv, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=480, y=788)

    delete = Button(jan_cad_advogado, text="LIMPAR", command=deletar, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    delete.place(x=560, y=788)

    # ----------------------------------------------------- #

    jan_cad_advogado.resizable(False,False)

    jan_cad_advogado.mainloop()

    # ----------------------------------------------------- #

def abrir_cad_cliente():

    def cad_cli():
        cod = cod_cad.get()
        name = name_cad.get()
        date = date_cad.get()
        civil_status = civil_status_cad.get()
        occupation = occupation_cad.get()
        adress = adress_cad.get()
        cpf = cpf_cad.get()
        phone = phone_cad.get()
        email = email_cad.get()

        comando_sql = f'INSERT INTO cliente (codigo, nome_completo, data_nascimento, estado_civil, ocupacao, endereco, cpf_cnpj, telefone, email) VALUES ({cod},"{name}","{date}","{civil_status}","{occupation}","{adress}",{cpf},{phone},"{email}")'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    def deletar():
        cod_cad.delete(0, END)
        name_cad.delete(0, END)
        date_cad.delete(0, END)
        civil_status_cad.delete(0, END)
        occupation_cad.delete(0, END)
        adress_cad.delete(0, END)
        cpf_cad.delete(0, END)
        phone_cad.delete(0, END)
        email_cad.delete(0, END)

    # ----------------------------------------------------- #

    jan_cad_cliente = Toplevel()

    jan_cad_cliente.title("Cadastro do Cliente")
    jan_cad_cliente.geometry("700x900")

    img_path = PhotoImage(file=r"./imgs/jancadcli.png")
    bg_img = tkinter.Label(jan_cad_cliente, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    cod_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(42))
    cod_cad.place(x=229, y=255)

    name_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(42))
    name_cad.place(x=229, y=322)

    date_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(42))
    date_cad.place(x=229, y=389)

    civil_status_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(42))
    civil_status_cad.place(x=229, y=456)

    occupation_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(42))
    occupation_cad.place(x=229, y=523)

    adress_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(42))
    adress_cad.place(x=229, y=590)

    cpf_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(42))
    cpf_cad.place(x=229, y=657)

    phone_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(42))
    phone_cad.place(x=229, y=724)

    email_cad = Entry(jan_cad_cliente, font=("arial black",11), width=(24))
    email_cad.place(x=229, y=791)

    # ----------------------------------------------------- #

    submit = Button(jan_cad_cliente, text="ENVIAR", command=cad_cli, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=480, y=788)

    delete = Button(jan_cad_cliente, text="LIMPAR", command=deletar, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    delete.place(x=560, y=788)

    # ----------------------------------------------------- #

    jan_cad_cliente.resizable(False,False)

    jan_cad_cliente.mainloop()

    # ----------------------------------------------------- #

# ----------------------------------------------------- #

def abrir_pes_processo():

    def pes_proc():
        number = number_cad.get()

        comando_sql = f'SELECT * FROM processo WHERE numero = {number}'
        cursor.execute(comando_sql)
        info = cursor.fetchone()

        situation_label['text'] = f"{info[1]}"
        date_label['text'] = f"{info[2]}"
        value_label['text'] = f"{info[3]}"
        nature_label['text'] = f"{info[4]}"
        cod_cli_label['text'] = f"{info[5]}"
        cod_law_label['text'] = f"{info[6]}"
        pass_cli_label['text'] = f"{info[7]}"
        pass_law_label['text'] = f"{info[8]}"

    # ----------------------------------------------------- #

    jan_pes_proc = Toplevel()

    jan_pes_proc.title("Pesquisa - Processo")
    jan_pes_proc.geometry("700x900")

    img_path = PhotoImage(file=r"./imgs/janpesproc.png")
    bg_img = tkinter.Label(jan_pes_proc, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    number_cad = Entry(jan_pes_proc, font=("arial black",11), width=(31))
    number_cad.place(x=229, y=255)

    situation_label = Label(jan_pes_proc, text="", font=("Arial black", 12))
    situation_label.place(x=229, y=322)

    date_label = Label(jan_pes_proc, text="", font=("Arial black", 12))
    date_label.place(x=229, y=389)

    value_label = Label(jan_pes_proc, text="", font=("Arial black", 12))
    value_label.place(x=229, y=456)

    nature_label = Label(jan_pes_proc, text="", font=("Arial black", 12))
    nature_label.place(x=229, y=523)

    cod_cli_label = Label(jan_pes_proc, text="", font=("Arial black", 12))
    cod_cli_label.place(x=229, y=590)

    cod_law_label = Label(jan_pes_proc, text="", font=("Arial black", 12))
    cod_law_label.place(x=229, y=657)

    pass_cli_label = Label(jan_pes_proc, text="", font=("Arial black", 12))
    pass_cli_label.place(x=229, y=724)

    pass_law_label = Label(jan_pes_proc, text="", font=("Arial black", 12))
    pass_law_label.place(x=229, y=791)

    # ----------------------------------------------------- #

    submit = Button(jan_pes_proc, text="ENVIAR",command=pes_proc,bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=560, y=253)

    # ----------------------------------------------------- #

    jan_pes_proc.resizable(False,False)

    jan_pes_proc.mainloop()

    # ----------------------------------------------------- #

def abrir_pes_advogado():

    def pes_adv():
        oab = oab_cad.get()

        comando_sql = f'SELECT * FROM advogado WHERE numero_oab = {oab}'
        cursor.execute(comando_sql)
        info = cursor.fetchone()

        name_label['text'] = f"{info[1]}"
        uf_label['text'] = f"{info[2]}"
        date_label['text'] = f"{info[3]}"
        cpf_label['text'] = f"{info[4]}"
        adress_label['text'] = f"{info[5]}"
        phone_label['text'] = f"{info[6]}"
        email_label['text'] = f"{info[7]}"
        expertise_label['text'] = f"{info[8]}"

    # ----------------------------------------------------- #

    jan_pes_adv = Toplevel()

    jan_pes_adv.title("Pesquisa - Advogado")
    jan_pes_adv.geometry("700x900")

    img_path = PhotoImage(file=r"./imgs/janpesadv.png")
    bg_img = tkinter.Label(jan_pes_adv, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    oab_cad = Entry(jan_pes_adv, font=("arial black",11), width=(31))
    oab_cad.place(x=229, y=255)

    name_label = Label(jan_pes_adv, text="", font=("Arial black", 12))
    name_label.place(x=229, y=322)

    date_label = Label(jan_pes_adv, text="", font=("Arial black", 12))
    date_label.place(x=229, y=389)

    uf_label = Label(jan_pes_adv, text="", font=("Arial black", 12))
    uf_label.place(x=229, y=456)

    cpf_label = Label(jan_pes_adv, text="", font=("Arial black", 12))
    cpf_label.place(x=229, y=523)

    adress_label = Label(jan_pes_adv, text="", font=("Arial black", 12))
    adress_label.place(x=229, y=590)

    phone_label = Label(jan_pes_adv, text="", font=("Arial black", 12))
    phone_label.place(x=229, y=657)

    email_label = Label(jan_pes_adv, text="", font=("Arial black", 12))
    email_label.place(x=229, y=724)

    expertise_label = Label(jan_pes_adv, text="", font=("Arial black", 12))
    expertise_label.place(x=229, y=791)

    # ----------------------------------------------------- #

    submit = Button(jan_pes_adv, text="ENVIAR",command=pes_adv,bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=560, y=253)

    # ----------------------------------------------------- #

    jan_pes_adv.resizable(False,False)

    jan_pes_adv.mainloop()

    # ----------------------------------------------------- #

def abrir_pes_cliente():

    def pes_cli():
        code = code_cad.get()

        comando_sql = f'SELECT * FROM cliente WHERE codigo = {code}'
        cursor.execute(comando_sql)
        info = cursor.fetchone()

        name_label['text'] = f"{info[1]}"
        date_label['text'] = f"{info[2]}"
        civil_label['text'] = f"{info[3]}"
        occupation_label['text'] = f"{info[4]}"
        adress_label['text'] = f"{info[5]}"
        cpf_label['text'] = f"{info[6]}"
        phone_label['text'] = f"{info[7]}"
        email_label['text'] = f"{info[8]}"

    # ----------------------------------------------------- #

    jan_pes_cli = Toplevel()

    jan_pes_cli.title("Pesquisa - Cliente")
    jan_pes_cli.geometry("700x900")

    img_path = PhotoImage(file=r"./imgs/janpescli.png")
    bg_img = tkinter.Label(jan_pes_cli, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    code_cad = Entry(jan_pes_cli, font=("arial black",11), width=(31))
    code_cad.place(x=229, y=255)

    name_label = Label(jan_pes_cli, text="", font=("Arial black", 12))
    name_label.place(x=229, y=322)

    date_label = Label(jan_pes_cli, text="", font=("Arial black", 12))
    date_label.place(x=229, y=389)

    civil_label = Label(jan_pes_cli, text="", font=("Arial black", 12))
    civil_label.place(x=229, y=456)

    occupation_label = Label(jan_pes_cli, text="", font=("Arial black", 12))
    occupation_label.place(x=229, y=523)

    adress_label = Label(jan_pes_cli, text="", font=("Arial black", 12))
    adress_label.place(x=229, y=590)

    cpf_label = Label(jan_pes_cli, text="", font=("Arial black", 12))
    cpf_label.place(x=229, y=657)

    phone_label = Label(jan_pes_cli, text="", font=("Arial black", 12))
    phone_label.place(x=229, y=724)

    email_label = Label(jan_pes_cli, text="", font=("Arial black", 12))
    email_label.place(x=229, y=791)

    # ----------------------------------------------------- #

    submit = Button(jan_pes_cli, text="ENVIAR",command=pes_cli,bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=560, y=253)

    # ----------------------------------------------------- #

    jan_pes_cli.resizable(False,False)

    jan_pes_cli.mainloop()

    # ----------------------------------------------------- #

# ----------------------------------------------------- #

def abrir_alt_processo():

    def alt_proc():
        number = number_cad.get()
        situation = situation_cad.get()
        value = value_cad.get()

        comando_sql = f'UPDATE processo SET situacao = "{situation}", valor_causa = {value} WHERE numero = {number}'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    # ----------------------------------------------------- #

    jan_alt_proc = Toplevel()

    jan_alt_proc.title("Alteração de Processo")
    jan_alt_proc.geometry("700x475")

    img_path = PhotoImage(file=r"./imgs/janaltproc.png")
    bg_img = tkinter.Label(jan_alt_proc, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    number_cad = Entry(jan_alt_proc, font=("arial black",11), width=(45))
    number_cad.place(x=213, y=238)

    situation_cad = Entry(jan_alt_proc, font=("arial black",11), width=(45))
    situation_cad.place(x=213, y=300)

    value_cad = Entry(jan_alt_proc, font=("arial black",11), width=(33))
    value_cad.place(x=213, y=362)

    # ----------------------------------------------------- #

    submit = Button(jan_alt_proc, text="ENVIAR",command=alt_proc,bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=570, y=358)

    # ----------------------------------------------------- #

    jan_alt_proc.resizable(False,False)

    jan_alt_proc.mainloop()

    # ----------------------------------------------------- #

def abrir_alt_advogado():

    def alt_adv():
        oab = oab_cad.get()
        expertise = expertise_cad.get()
        phone = phone_cad.get()

        comando_sql = f'UPDATE advogado SET especialidade = "{expertise}", telefone = {phone} WHERE numero_oab = {oab}'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    # ----------------------------------------------------- #

    jan_alt_adv = Toplevel()

    jan_alt_adv.title("Alteração de Advogado")
    jan_alt_adv.geometry("700x475")

    img_path = PhotoImage(file=r"./imgs/janaltadv.png")
    bg_img = tkinter.Label(jan_alt_adv, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    oab_cad = Entry(jan_alt_adv, font=("arial black",11), width=(45))
    oab_cad.place(x=213, y=238)

    expertise_cad = Entry(jan_alt_adv, font=("arial black",11), width=(45))
    expertise_cad.place(x=213, y=300)

    phone_cad = Entry(jan_alt_adv, font=("arial black",11), width=(33))
    phone_cad.place(x=213, y=362)

    # ----------------------------------------------------- #

    submit = Button(jan_alt_adv, text="ENVIAR",command=alt_adv,bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=570, y=358)

    # ----------------------------------------------------- #

    jan_alt_adv.resizable(False,False)

    jan_alt_adv.mainloop()

    # ----------------------------------------------------- #

def abrir_alt_cliente():

    def alt_cli():
        code = code_cad.get()
        name = name_cad.get()
        email = email_cad.get()

        comando_sql = f'UPDATE cliente SET nome_completo = "{name}", email = "{email}" WHERE codigo = {code}'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    # ----------------------------------------------------- #

    jan_alt_cli = Toplevel()

    jan_alt_cli.title("Alteração de Cliente")
    jan_alt_cli.geometry("700x475")

    img_path = PhotoImage(file=r"./imgs/janaltcli.png")
    bg_img = tkinter.Label(jan_alt_cli, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    code_cad = Entry(jan_alt_cli, font=("arial black",11), width=(45))
    code_cad.place(x=213, y=238)

    name_cad = Entry(jan_alt_cli, font=("arial black",11), width=(45))
    name_cad.place(x=213, y=300)

    email_cad = Entry(jan_alt_cli, font=("arial black",11), width=(33))
    email_cad.place(x=213, y=362)

    # ----------------------------------------------------- #

    submit = Button(jan_alt_cli, text="ENVIAR",command=alt_cli,bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=570, y=358)

    # ----------------------------------------------------- #

    jan_alt_cli.resizable(False,False)

    jan_alt_cli.mainloop()

    # ----------------------------------------------------- #

# ----------------------------------------------------- #

def abrir_exc_processo():
    
    def exc_proc():
        number = number_cad.get()

        comando_sql = f'DELETE FROM processo WHERE numero = {number}'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    # ----------------------------------------------------- #

    jan_exc_proc = Toplevel()

    jan_exc_proc.title("Exclusão de Processo")
    jan_exc_proc.geometry("700x410")

    img_path = PhotoImage(file=r"./imgs/janexcproc.png")
    bg_img = tkinter.Label(jan_exc_proc, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    number_cad = Entry(jan_exc_proc, font=("arial black",11), width=(42))
    number_cad.place(x=229, y=268)

    # ----------------------------------------------------- #

    submit = Button(jan_exc_proc, text="ENVIAR",command=exc_proc,bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=570, y=305)

    # ----------------------------------------------------- #

    jan_exc_proc.resizable(False,False)

    jan_exc_proc.mainloop()

    # ----------------------------------------------------- #

def abrir_exc_advogado():
    
    def exc_adv():
        cpf = cpf_cad.get()

        comando_sql = f'DELETE FROM advogado WHERE cpf = {cpf}'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    # ----------------------------------------------------- #

    jan_exc_adv = Toplevel()

    jan_exc_adv.title("Exclusão de Advogado")
    jan_exc_adv.geometry("700x410")

    img_path = PhotoImage(file=r"./imgs/janexcadv.png")
    bg_img = tkinter.Label(jan_exc_adv, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    cpf_cad = Entry(jan_exc_adv, font=("arial black",11), width=(42))
    cpf_cad.place(x=229, y=268)

    # ----------------------------------------------------- #

    submit = Button(jan_exc_adv, text="ENVIAR",command=exc_adv,bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=570, y=305)

    # ----------------------------------------------------- #

    jan_exc_adv.resizable(False,False)

    jan_exc_adv.mainloop()

    # ----------------------------------------------------- #

def abrir_exc_cliente():
    
    def exc_cli():
        cpf = cpf_cad.get()

        comando_sql = f'DELETE FROM cliente WHERE cpf_cnpj = {cpf}'
        cursor.execute(comando_sql)
        conexao_banco.commit()

    # ----------------------------------------------------- #

    jan_exc_cli = Toplevel()

    jan_exc_cli.title("Exclusão de Cliente")
    jan_exc_cli.geometry("700x410")

    img_path = PhotoImage(file=r"./imgs/janexccli.png")
    bg_img = tkinter.Label(jan_exc_cli, image=img_path)
    bg_img.pack()

    # ----------------------------------------------------- #

    cpf_cad = Entry(jan_exc_cli, font=("arial black",11), width=(42))
    cpf_cad.place(x=229, y=268)

    # ----------------------------------------------------- #

    submit = Button(jan_exc_cli, text="ENVIAR", command=exc_cli, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
    submit.place(x=570, y=305)

    # ----------------------------------------------------- #

    jan_exc_cli.resizable(False,False)

    jan_exc_cli.mainloop()

    # ----------------------------------------------------- #

# ----------------------------------------------------- #

first_pg = Tk()

first_pg.title("Sistema de Gerenciamento de Processos Digital")
first_pg.geometry("700x900")

img_path = PhotoImage(file=r"./imgs/bckground.png")
bg_img = tkinter.Label(first_pg, image=img_path)
bg_img.pack()

# ----------------------------------------------------- #

button = Button(first_pg, text="REGISTRAR NOVO PROCESSO\nJURÍDICO", command=abrir_cad_processo, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=56, y=285)

button = Button(first_pg, text="REGISTRAR NOVO(A)\nADVOGADO(A)", command=abrir_cad_advogado, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=92, y=355)

button = Button(first_pg, text="REGISTRAR NOVO(A) CLIENTE", command=abrir_cad_cliente, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=53, y=425)

# ----------------------------------------------------- #

button = Button(first_pg, text="CONSULTAR PROCESSOS\nCADASTRADOS", command=abrir_pes_processo, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=400, y=285)

button = Button(first_pg, text="CONSULTAR ADVOGADOS(AS)", command=abrir_pes_advogado, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=381, y=366)

button = Button(first_pg, text="CONSULTAR CLIENTES", command=abrir_pes_cliente, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=410, y=425)

# ----------------------------------------------------- #

button = Button(first_pg, text="ALTERAR PROCESSOS", command=abrir_alt_processo, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=87, y=660)

button = Button(first_pg, text="ALTERAR ADVOGADOS(AS)", command=abrir_alt_advogado, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=65, y=730)

button = Button(first_pg, text="ALTERAR CLIENTES", command=abrir_alt_cliente, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=97, y=800)

# ----------------------------------------------------- #

button = Button(first_pg, text="EXCLUIR PROCESSOS", command=abrir_exc_processo, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=416, y=660)

button = Button(first_pg, text="EXCLUIR ADVOGADOS(AS)", command=abrir_exc_advogado, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=397, y=730)

button = Button(first_pg, text="EXCLUIR CLIENTES", command=abrir_exc_cliente, bg="#d6c47c", fg="#474747", activebackground="#a89a60", activeforeground="#292929", font=("arial black",11), bd=0, cursor="hand2")
button.place(x=422, y=800)

# ----------------------------------------------------- #

first_pg.resizable(False,False)

first_pg.mainloop()

# ----------------------------------------------------- #