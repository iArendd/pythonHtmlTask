from js import console
from datetime import datetime

tasks = []


def atualiza_lista():

    tasks_criadas = Element('tasks_criadas')
    tasks_criadas.element.innerText = ""

    for i in tasks:

        tasks_criadas.element.innerText += f"{i['content']}\n"


def cria_task(*args, **kags):

    input_task = Element('input_task')

    task = input_task.element.value

    dict_task = {
        
                'task-id': len(task),
                'content': task,
                'data': datetime.now(),
                'status': 'Criada'                    

                }

    tasks.append(dict_task)
    atualiza_lista()





















#for i, j in dict_task.items():

#       console.log(i, j)
    
        

