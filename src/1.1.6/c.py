# Задача C


class Student:
    def __init__(self) -> None:
        self._knowledge_level = 0

    def get_python_skill(self) -> int:
        return self._knowledge_level

    def learn_python(self) -> None:
        self._knowledge_level += 1
