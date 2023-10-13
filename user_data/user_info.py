class User:
    def __init__(self):
        self._receiver = None
        self._sender = None
        self._user = None

    @property
    def receiver(self):
        return self._receiver

    @receiver.setter
    def receiver(self, receiver):
        self._receiver = receiver

    @property
    def sender(self):
        return self._sender

    @sender.setter
    def sender(self, sender):
        self._sender = sender

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, user):
        self._user = user
