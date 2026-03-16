from typing import Any

class classproperty:
    def __init__(self, func) -> None:
        self.fget = func

    def __get__(self, instance, owner) -> Any:
        return self.fget(owner)
