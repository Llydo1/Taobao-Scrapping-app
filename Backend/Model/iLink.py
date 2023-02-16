import abc

# Class represent a link that can be soup
class iLink(metaclass=abc.ABCMeta):
    # Every link will have URL
    @abc.abstractmethod
    def get_url(self):
        pass

    # Every Link can be soup
    @abc.abstractmethod    
    def _set_soup(self, url):
        pass