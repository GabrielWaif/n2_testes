from src.task import Task;

class TestTask:
    def test_create_task(self):
        task = Task(0, "Placeholder", False);
        assert task.id == 0;
        assert task.description == "Placeholder";
        assert not task.done;
