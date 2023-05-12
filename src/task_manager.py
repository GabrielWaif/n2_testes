from src.task import Task;

class TaskManager:
    def __init__(self):
        self.__tasks = [];

    def add_task(self, task: Task):
        self.__tasks.append(task);

    def list_tasks(self):
        return self.__tasks;

    def mark_task_as_done(self, id: int):
        for index in range(0, len(self.__tasks)):
            if (self.__tasks[index].id == id):
                self.__tasks[index].done = True;

    def remove_task(self, id: int):
        for index in range(0, len(self.__tasks)):
            if (self.__tasks[index].id == id):
                self.__tasks.remove(self.__tasks[index]);
                return;
