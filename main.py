# Importation de librairies
from tkinter import *
from tkinter import ttk

def convert(amount, devise_1, devise_2):
    amount = verif_entry(amount)
    if amount != "ERROR":
        devise_1 = get_change_rate(devise_1)
        devise_2 = get_change_rate(devise_2)
        if devise_1[0] == "Euro" or devise_2[0] == "Euro":
            if devise_1[0] == "Euro":
                result = amount * devise_2[1]

            else:
                result = amount / devise_1[1]

        else:
            result = (amount * devise_2[1]) / devise_1[1]
        history(amount, result, devise_1, devise_2)
        # On supprime les decimal a partir des millièmes car non utile dans notre cas
        # Utilisation de format qui permet de ne pas arrondir et donc permet d'avoir la valeur arrondi inférieur et non supérieur
        print_result.set(format(result, '.2f'))
    else:
        return ("Une erreur est survenue")


def get_change_rate(devise):
    array = fetch_array()
    i = 0
    for x in array:
        try:
            result = x.index(devise)
            return get_1d_array(i)
        except ValueError:
            i += 1
    print("Une erreur est survenue")


def verif_entry(amount):
    amount = amount.replace(',', '.')
    try:
        amount = int(amount)
    except ValueError:
        try:
            # Convertion du string en float puis format reconverti ce float en string ce qui necessite une reconvertion en float
            amount = float(format(float(amount), '.2f'))
        except ValueError:
            return "ERROR"
    return amount


def history(amount, result, devise1, devise2):
    amount = str(amount)
    result = format(result, '.2f')
    from datetime import datetime
    date_now = datetime.now()
    standart_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
    f = open("history.txt", "a", encoding="utf-8")
    phrase = standart_date + ": " + amount + " " + devise1[0] + "s" + " sont équivalent à " + result + " " + devise2[
        0] + "s\n"
    f.write(phrase)
    f.close()


# Fonctions Job bonus (Création devise)


def fetch_array():
    import json
    f = open("test.json", "r")
    array = f.read()
    f.close
    # Retourne un array a 2 dimentions
    return json.loads(array)


def get_1d_array(index):
    array = fetch_array()
    if index < len(array):
        # Retourne un array a 1 dimention
        return array[index]
    else:
        return "ERROR"


def get_combo_array():
    i = 0
    combo_array = []
    twoD_array = fetch_array()
    for x in twoD_array:
        combo_array.append(x[0])
        i += 1
    return combo_array


def insert(name, value):
    import json
    verif_entry(value)
    current_list = fetch_array()
    for x in current_list:
        if x[0] == name:
            print("Cette devise existe déjà")
            return 0
    insert_array = [[name, value]]
    current_list.extend(insert_array)
    f = open("test.json", "w")
    json_value = json.dumps(current_list)
    f.write(json_value)
    f.close()


def prompt_windows():
    sub = Tk()
    sub.title("Ajouter une devise")
    sub.resizable(False, False)
    devise_name = StringVar()
    euro_equal_to_devise = StringVar()
    add = ttk.Frame(sub, borderwidth=2, relief="ridge", padding="10 10 5 5")
    add.grid(column=0, row=0, sticky=("N", "S", "W"))
    add.columnconfigure(0, weight=1)
    add.rowconfigure(0, weight=1)
    ttk.Entry(add, textvariable=devise_name, width=20).grid(column=1, row=0)
    ttk.Entry(add, textvariable=euro_equal_to_devise, width=20).grid(column=1, row=1)
    ttk.Button(add, text='Ajouter devise', command=lambda: insert(devise_name.get(),euro_equal_to_devise.get())).grid(column=1, row=2)
    sub.mainloop()
# Affichage
main = Tk()
main.title("Convertisseur de devises")
main.resizable(False, False)

conv = ttk.Frame(main, borderwidth=2, relief="ridge", padding="10 10 5 5")
conv.grid(column=0, row=0, sticky=("N", "S", "W"))
conv.columnconfigure(0, weight=1)
conv.rowconfigure(0, weight=1)

initial_devise = StringVar()
init_combo = ttk.Combobox(conv, textvariable=initial_devise, width=17)
init_combo.state(["readonly"])
init_combo['values'] = get_combo_array()
init_combo.grid(column=1, row=1)
init_combo.set(get_combo_array()[0])

final_devise = StringVar()
final_combo = ttk.Combobox(conv, textvariable=final_devise, width=17)
final_combo.state(["readonly"])
final_combo['values'] = get_combo_array()
final_combo.grid(column=1, row=2)
final_combo.set(get_combo_array()[1])
print_result = StringVar()
amount_enter = StringVar()
ttk.Label(conv, text="Quantité:", padding="10").grid(column=0, row=0)
ttk.Label(conv, text="De:", padding="10").grid(column=0, row=1)
ttk.Label(conv, text="à:", padding="10").grid(column=0, row=2)
ttk.Entry(conv, textvariable=amount_enter, width=20).grid(column=1, row=0)
ttk.Button(conv, text='Convertir',command=lambda: convert(amount_enter.get(), initial_devise.get(), final_devise.get())).grid(column=1, row=3)
ttk.Button(conv, text='Ajouter devise', command=lambda: prompt_windows()).grid(column=1, row=5)
ttk.Label(conv, textvariable=print_result, padding="10").grid(column=0, row=4)
main.mainloop()