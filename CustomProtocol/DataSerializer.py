from abc import ABC, abstractmethod

from CustomProtocol.CommunicationProtocol import CommunicationProtocol


class DataSerializer(ABC):
    REQUEST = "request"
    RESPONSE = "response"

    @abstractmethod
    def deserialize(self, data: str) -> CommunicationProtocol:
        pass

    @abstractmethod
    def serialize(self, protocol: CommunicationProtocol) -> str:
        pass


