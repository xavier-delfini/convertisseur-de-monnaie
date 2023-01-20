def convert(amount,devise_1,devise_2):
    if devise_1[0] == "euro" or devise_2[0] == "euro":
        if devise_1[0] == "euro":
            result =amount * devise_2[1]

        else:
            result = amount * devise_1[1]
            #On supprime les decimal a partir des millièmes car non utile dans notre cas
            #Utilisation de format qui permet de ne pas arrondir et donc permet d'avoir la valeur arrondi inférieur et non supérieur
    else:
        result=(amount * devise_1[1])*devise_2[1]
    history(amount, result, devise_1, devise_2)
    return format(result, '.2f')


def verif_entry(amount,devise1,devise2):
    try:
        amount=int(amount)
    except ValueError:
        try:
            #Convertion du string en float puis format reconverti ce float en string ce qui necessite une reconvertion en float
            amount=float(format(float(amount),'.2f'))
        except ValueError:
            return "ERROR"
    return convert(amount, devise1, devise2)


def history(amount,result,devise1,devise2):
    amount=str(amount)
    result=format(result, '.2f')
    from datetime import datetime
    date_now = datetime.now()
    standart_date = date_now.strftime("%d/%m/%Y %H:%M:%S")
    f = open("history.txt", "a",encoding="utf-8")
    phrase = standart_date+": "+amount+" " + devise1[0]+"s" +" sont équivalent à "+ result +" "+ devise2[0]+"s\n"
    f.write(phrase)
    f.close()


#Fonctions Job bonus (Création devise)


def fetch_array():
    f = open("test.json", "r")
    array = f.read()
    f.close
    return json.loads(array)


def insert(name,value):
    current_list=fetch_array()
    for x in current_list:
        if x[0]== name:
            print("Cette devise existe déjà")
            return 0
    insert_array = [[name, value]]
    current_list.extend(insert_array)
    f = open("test.json", "w")
    json_value=json.dumps(current_list)
    f.write(json_value)
    f.close()