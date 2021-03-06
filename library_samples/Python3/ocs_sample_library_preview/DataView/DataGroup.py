import json


class DataGroup(object):
    """
    DataGroup definition
    """

    @property
    def Tokens(self):
        return self.__tokens

    @Tokens.setter
    def Tokens(self, tokens):
        self.__tokens = tokens

    @property
    def DataItems(self):
        return self.__dataItems

    @DataItems.setter
    def DataItems(self, dataItems):
        self.__dataItems = dataItems

    def toJson(self):
        return json.dumps(self.toDictionary())

    def toDictionary(self):
        # required properties
        dictionary = {'DataItems': self.DataItems, 'Tokens': self.Tokens}

        return dictionary

    @staticmethod
    def fromJson(jsonObj):
        return DataGroup.fromDictionary(jsonObj)

    @staticmethod
    def fromDictionary(content):
        dataGroup = DataGroup()

        if not content:
            return dataGroup

        if 'DataItems' in content:
            dataGroup.DataItems = content['DataItems']

        if 'Tokens' in content:
            dataGroup.Tokens = content['Tokens']

        return dataGroup
