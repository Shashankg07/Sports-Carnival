from CustomProtocol.CommunicationProtocol import CommunicationProtocol


class ISCResponse(CommunicationProtocol):
    header_parameters = {}
    STATUS = "status"
    ERROR_CODE = "error-code"
    ERROR_MESSAGE = "error-message"

    def __init__(self, json_obj):
        super().__init__()
        self.protocol_type = self.RESPONSE
        self.headers = json_obj["headers"]

    def set_error_message(self, message):
        self.headers[self.ERROR_MESSAGE] = message
