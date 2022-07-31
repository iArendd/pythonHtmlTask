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

    y = list(filter(lambda x: x['content'] == task, tasks))

    if len(y) > 0:

        message = Element('message')
        message.element.style.display = 'flex'
        return None

    dict_task = {
        
                'task-id': len(task),
                'content': task,
                'data': datetime.now(),
                'status': 'Criada'                    

                }

    tasks.append(dict_task)
    input_task.element.value = ""
    atualiza_lista()


def add_task_event(e):

    if e.key == "Enter":
        cria_task()
        console.log(e.key)


input_task = Element('input_task')
input_task.element.onkeypress = add_task_event





















#for i, j in dict_task.items():

#       console.log(i, j)
    
        

