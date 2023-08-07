from CustomProtocol.DataSerializer import DataSerializer
from CustomProtocol.JSONSerializer import JSONSerializer
from Validations.CustomException import FatalException


class DataSerializerFactory:
    JSON = "json"
    XML = "xml"

    @staticmethod
    def get_serializer(protocol_format: str) -> DataSerializer:
        if protocol_format.lower() == DataSerializerFactory.JSON:
            return JSONSerializer()
        else:
            raise FatalException(f"Invalid DataSerializer Format: {protocol_format}")
