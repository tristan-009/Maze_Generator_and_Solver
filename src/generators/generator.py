from abc import ABC, abstractmethod

class Generator(ABC):

    @abstractmethod
    def generate(self, maze):
        pass