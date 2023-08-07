class CommunicationProtocol:
    def __init__(self):
        self.size = None
        self.REQUEST = "request"
        self.RESPONSE = "response"
        self.data = None
        self.protocolVersion = None
        self.protocolFormat = None
        self.protocolType = None
        self.sourceIp = None
        self.sourcePort = None
        self.destIp = None
        self.destPort = None
        self.headers = {}