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

    def test_remove_task(self):
        task_manager = TaskManager();
        for task in DUMMY_TASKS:
            task_manager.add_task(task);

        task_manager.remove_task(0);

    def test_list_tasks(self):
        task_manager = TaskManager();
        for task in DUMMY_TASKS:
            task_manager.add_task(task);

        task_manager.list_tasks();

    def test_mark_as_done(self):
        task_manager = TaskManager();
        task = Task(0, "Placeholder", False);
        task_manager.add_task(task);
        task_manager.mark_task_as_done(0);
