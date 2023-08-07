from CustomProtocol.CommunicationProtocol import CommunicationProtocol


class ISCRequest(CommunicationProtocol):
    def __init__(self):
        super().__init__()
        self.headerParameters = {}
        self.METHOD = "method"
        self.protocolType = self.REQUEST
        self.headerParameters[self.METHOD] = ""
        self.headers = self.headerParameters