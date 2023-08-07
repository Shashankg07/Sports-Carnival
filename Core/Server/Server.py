import socket

from CustomProtocol.ISCRequest import ISCRequest
from CustomProtocol.ISCResponse import ISCResponse
from CustomProtocol.JSONSerializer import JSONSerializer
from Configuration.Config import ServerConstraints
from Controller.TeamController import TeamController
from Controller.FixtureController import FixtureController
from Models.TeamsOutput import TeamsOutput
from Validations.CustomException import NullValueException, FixtureException
from Configuration.Config import Command

if __name__ == "__main__":

    ip: str = ServerConstraints.destIp
    port: int = ServerConstraints.destPort

    server: socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)

    client, address = server.accept()
    print(f"Connection Established - {address[0]}:{address[1]}")
    while True:
        string: bytes = client.recv(1024)
        string: str = string.decode(Command.encoding)
        requestObj: ISCRequest = JSONSerializer().deserialize(string)
        responseObj: ISCResponse = ISCResponse(requestObj)
        try:
            if requestObj['headers']['method'] == Command.create_team_method:
                data: TeamsOutput = TeamController().create_team(requestObj['data'])
                print(data)
                TeamController().save_team(requestObj['headers']['outputPath'], data)
                responseObj.STATUS = Command.success
                client.send(bytes(JSONSerializer().serialize(responseObj), Command.encoding))
            elif requestObj['headers']['method'] == Command.create_fixture_method:
                data: dict = FixtureController().create_fixture(requestObj['data'])
                FixtureController().save_fixture(requestObj['headers']['outputPath'], data)
                responseObj.STATUS = Command.success
                client.send(bytes(JSONSerializer().serialize(responseObj), Command.encoding))
            else:
                responseObj.STATUS = Command.error
                responseObj.set_error_message("wrong input")
                client.send(bytes(JSONSerializer().serialize(responseObj), Command.encoding))
            print(responseObj.headers)
        except NullValueException as err:
            responseObj.STATUS = Command.error
            responseObj.set_error_message((str(err)))
            client.send((bytes(JSONSerializer().serialize(responseObj), Command.encoding)))
        except FixtureException as err:
            responseObj.STATUS = Command.error
            responseObj.set_error_message((str(err)))
            client.send((bytes(JSONSerializer().serialize(responseObj), Command.encoding)))
