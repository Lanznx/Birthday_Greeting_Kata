from abc import ABC, abstractmethod
from typing import Any


class IPresenter(ABC):
    @abstractmethod
    def present_birthday_greeting(self, data: Any) -> Any:
        pass
