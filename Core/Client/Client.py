import socket

from CustomProtocol.ISCRequest import ISCRequest
from CustomProtocol.JSONSerializer import JSONSerializer
from Configuration.Config import ClientConstraints
from Configuration.Config import Command
from Utils.ClientOutput import ClientOutput
from Utils.FIleHandler import FileHandler
from Validations.Validate import Validate


class Client:

    @staticmethod
    def connect_to_server():
        ip: str = ClientConstraints.sourceIp
        port: int = ClientConstraints.sourcePort
        server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.connect((ip, port))
        while True:
            command: str = input("Enter Command : ")
            command: list = command.split(" ")
            request_obj: ISCRequest = ISCRequest()
            if Validate().command_validator(command):
                print("Wrong Command")
                continue
            data: dict = FileHandler().read_file(command[4][1:-1])
            request_obj.data = data
            request_obj.headerParameters['method'] = command[2]
            request_obj.headerParameters["outputPath"] = command[6][1:-1]
            server.send(bytes(JSONSerializer().serialize(request_obj), Command.encoding))
            buffer: bytes = server.recv(1024)
            buffer: str = buffer.decode(Command.encoding)
            response_obj = JSONSerializer().deserialize(buffer)
            ClientOutput(response_obj).print_output()
        server.close()


Client.connect_to_server()
