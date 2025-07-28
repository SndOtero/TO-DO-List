import json


def show():
    with open("json.JSON","r",encoding="utf-8") as todo:
        datos = json.load(todo)
    
    print(datos["tareas"])
    for tarea in datos["tareas"]:
        print(tarea["id"])



if __name__ == "__main__":
    show()