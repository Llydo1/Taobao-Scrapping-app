import abc

class iStore(metaclass=abc.ABCMeta):
    _store_name = None
    _store_id = None
    # EVerything will have store name
    def __init__(self, store_name) -> None:
        self._store_name = store_name

    @abc.abstractmethod
    def get_store_name(self):
        pass

    # Every Link can be soup
    @abc.abstractmethod
    def get_store_id(self):
        pass