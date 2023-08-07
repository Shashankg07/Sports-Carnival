import json

from CustomProtocol.CommunicationProtocol import CommunicationProtocol
from CustomProtocol.DataSerializer import DataSerializer


class JSONSerializer(DataSerializer):

    def deserialize(self, data: str) -> json:
        communication_protocol_obj: CommunicationProtocol = json.loads(data)
        return communication_protocol_obj

    def serialize(self, protocol: CommunicationProtocol) -> str:
        data = json.dumps(protocol.__dict__)
        return data
