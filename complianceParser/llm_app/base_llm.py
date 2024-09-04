from abc import ABC, abstractmethod

class BaseLLM(ABC):

    @abstractmethod
    def initialize_client(self, model):
        pass

    @abstractmethod
    def get_response():
        pass
