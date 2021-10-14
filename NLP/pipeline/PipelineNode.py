from abc import ABC, abstractmethod


class PipelineNode(ABC):

    @abstractmethod
    def handle(self, input):
        raise NotImplementedError('Method handle not implemented')
