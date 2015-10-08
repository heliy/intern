
class RemoteError(Exception):
    """
    A generic error arising from an issue pertaining
    to ndio Remotes.
    """
    def __init__(self, message):
        super(Exception, self).__init__(message)


class RemoteDataNotFoundError(RemoteError):
    """
    Called when data is requested from a Remote but the
    server either cannot access it (maybe a permissions issue?)
    or the data does not exist.
    """
    def __init__(self, message):
        super(RemoteError, self).__init__(message)
