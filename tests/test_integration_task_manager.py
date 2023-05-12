from src.task import Task;
from src.task_manager import TaskManager;

DUMMY_TASKS = [
        Task(0, "Placeholder1", False),
        Task(1, "Placeholder2", False),
        Task(2, "Placeholder3", False),
        Task(3, "Placeholder4", False),
        Task(4, "Placeholder5", False)
]

class TestTaskManager:
    def test_add_one_task(self):
        task_manager = TaskManager();
        task = Task(0, "Placeholder", False);
        task_manager.add_task(task);

        assert task_manager.list_tasks() == [task];

    def test_remove_task(self):
        task_manager = TaskManager();
        for task in DUMMY_TASKS:
            task_manager.add_task(task);

        task_manager.remove_task(0);

        for task in task_manager.list_tasks():
            assert task.id != 0;

        assert len(task_manager.list_tasks()) == 4;

    def test_list_tasks(self):
        task_manager = TaskManager();
        for task in DUMMY_TASKS:
            task_manager.add_task(task);

        list_of_tasks = task_manager.list_tasks()

        for i in range(0, len(list_of_tasks)):
            assert list_of_tasks[i].description == DUMMY_TASKS[i].description;
            assert list_of_tasks[i].id == DUMMY_TASKS[i].id;
            assert list_of_tasks[i].done == DUMMY_TASKS[i].done;
        

    def test_mark_as_done(self):
        task_manager = TaskManager();
        task = Task(0, "Placeholder", False);
        task_manager.add_task(task);
        task_manager.mark_task_as_done(0);

        assert task_manager.list_tasks()[0].done == True;
