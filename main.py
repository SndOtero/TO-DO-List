import json
import os
from datetime import date
from datetime import time

def show_employer():
    employer_id = int(input("Digite el ID de el empleado: "))

    with open("data.json","r",encoding="utf-8") as employers_list:
        employers = json.load(employers_list)

    for employer in employers["employers"]:
        if employer["id"] == employer_id:
            print(f'Nro. Id: {employer["id"]} \n Empleado: {employer["name"]}, {employer["surname"]}. \n Turno: {employer["hour"]} \n D.N.I: {employer["dni"]} \n Email: {employer["email"]} \n Telefono: {employer["number"]} \n Direccion: {employer["direccion"]} \n')


def show_employers():

    with open("data.json","r",encoding="utf-8") as employers_list:
        employers = json.load(employers_list)

    for employer in employers["employers"]:
        
        print(f'Nro. Id: {employer["id"]} \n Empleado: {employer["name"]}, {employer["surname"]}. \n Turno: {employer["hour"]} \n D.N.I: {employer["dni"]} \n Email: {employer["email"]} \n Telefono: {employer["number"]} \n Direccion: {employer["direccion"]} \n')


def show_this_week():
    with open("data.json", "r",encoding="utf-8") as employer_list:
        employers = json.load(employer_list)
    
    for employer in employers["employers"]:     
        print(f'Nro. Id: {employer["id"]} \n Empleado: {employer["name"]}, {employer["surname"]}. \n Turno: {employer["hour"]}\n')
    
def show_last_week():
    with open("data.json", "r",encoding="utf-8") as employer_list:
        employers = json.load(employer_list)
    
    for employer in employers["employers"]:
        if employer["group"] == "A":
            if employer["hour"] == "06:00hs a 14:00hs":
                employer["hour"] = "22:00hs a 06:00hs"
            else:
                employer["group"] = "B"
                if employer["hour"] == "22:00hs a 06:00hs":
                    employer["hour"] = "14:00hs a 22:00hs"
                else:
                    employer["hour"] = "06:00hs a 14:00hs"
        else:
            employer["group"] = "A"

    for employer in employers["employers"]:     
        print(f'Nro. Id: {employer["id"]} \n Empleado: {employer["name"]}, {employer["surname"]}. \n Turno: {employer["hour"]}\n')
    
    select = int(input("Digite 1 si quiere guardar y reemplazar estos turnos o digite cualquier otro numero si quiere volver al menu anterior: "))

    if select == 1:

        with open("data.json","w",encoding="utf-8") as employer_list:
            json.dump(employers,employer_list, indent=4)

def show_next_week():
    with open("data.json", "r",encoding="utf-8") as employer_list:
        employers = json.load(employer_list)

    for employer in employers["employers"]:
        
        if employer["group"] == "B":
            employer["group"] = "A"
            
            if employer["hour"] == "06:00hs a 14:00hs":
                employer["hour"] = "14:00hs a 22:00hs"
            else:
                employer["hour"] = "22:00hs a 06:00hs"

        elif employer["hour"] != "22:00hs a 06:00hs":
            employer["group"] = "B"
        else:
            employer["hour"] = "06:00hs a 14:00hs"

    for employer in employers["employers"]:     
        print(f'Nro. Id: {employer["id"]} \n Empleado: {employer["name"]}, {employer["surname"]}. \n Turno: {employer["hour"]}\n')
    
    select = int(input("Digite 1 si quiere guardar y reemplazar estos turnos o digite cualquier otro numero si quiere volver al menu anterior: "))

    if select == 1:

        with open("data.json","w",encoding="utf-8") as employer_list:
            json.dump(employers,employer_list, indent=4)
    

    
            














if __name__ == "__main__":
    
    show_this_week()
    
  
    select = int(input("Digite un numero de la siguiente lista: \n1- Mostrar datos de un empleado. \n2- Mostrar los datos de todos los empleados. \n3- Visualizar semana siguiente. \n4- Visualizar semana anterior. \n5- Salir \n"))
    
    while select != 5:
        if select == 1:
            show_employer()
        elif select == 2:
            show_employers()
        elif select == 3:
            show_next_week()
        elif select == 4:
            show_last_week()
        select = int(input("Digite un numero de la siguiente lista: \n1- Mostrar datos de un empleado. \n2- Mostrar los datos de todos los empleados. \n3- Visualizar semana siguiente. \n4- Visualizar semana anterior. \n5- Salir \n"))

