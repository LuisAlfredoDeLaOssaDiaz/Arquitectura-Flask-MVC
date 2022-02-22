import ossaudiodev


class Document(object):
    """
    Class used to represent an Person
    """

    def __init__(self, id_document: int, title: str = 'Name', pag: str = "LastName"):
        """ Person constructor object.

        :param id_person: id of person.
        :type id_person: int
        :param name: name of person.
        :type name: str
        :param last_name: last name of person.
        :type last_name: str
        :returns: Person object
        :rtype: object
        """
        self._id_document = id_document
        self._title = title
        self._pag = pag

    @property
    def id_document(self) -> int:
        """ Returns id person of the person.
          :returns: id of person.
          :rtype: int
        """
        return self._id_document

    @id_document.setter
    def id_document(self, id_document: int):
        """ The id of the person.
        :param id_person: id of person.
        :type: int
        """
        self._id_document = id_document

    @property
    def title(self) -> str:
        """ Returns the name of the person.
          :returns: name of person.
          :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """ The name of the person.
        :param name: name of person.
        :type: str
        """
        self._title = title

    @property
    def pag(self) -> str:
        """ Returns the last name of the person.
          :returns: last name of person.
          :rtype: str
        """
        return self._pag

    @pag.setter
    def pag(self, pag: str):
        """ The last name of the person.
        :param last_name: last name of person.
        :type: str
        """
        self._pag = pag

    def __str__(self):
        """ Returns str of person.
          :returns: sting person
          :rtype: str
        """
        return '({0}, {1}, {2})'.format(self.id_document, self.title, self.pag)


if __name__ == '__main__':
    osso = Document(id_person=73577376, name="Edwin", last_name="Puertas")
    osso.name = "Edwin. A"
    print(osso)
