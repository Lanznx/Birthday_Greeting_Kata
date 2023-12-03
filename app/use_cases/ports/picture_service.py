from abc import ABC, abstractmethod


class IPictureService(ABC):
    @abstractmethod
    def get_picture_url(self) -> str:
        pass
