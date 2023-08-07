class ClientOutput:
    def __init__(self, client_obj):
        self.client_obj = client_obj

    def print_output(self):
        print(self.client_obj['STATUS'])
        if self.client_obj['STATUS'] == 'ERROR':
            print(self.client_obj['headers']['error-message'])
