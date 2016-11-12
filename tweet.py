class Tweet(object):
    __author = ""
    __text = ""
    __location = ""
    #__longitude = ""
    #__latitude = ""
    __creation = ""

    #def __init__(self, author, text, longitude, latitude):
    def __init__(self, author, text, location, creation):
        self.__author = author
        self.__text = text
        self.__location = location
        #self.__longitude = longitude
        #self.__latitude = latitude
        self.__creation = creation

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_text(self):
        return self.__text

    def set_text(self, text):
        self.__text = text

    def get_location(self):
        return self.__location

    def set_location(self, location):
        self.__location = location

    def get_creation(self):
        return self.__creation

    def set_creation(self, latitude):
        self.__creation = creation

    def to_string(self):
        return "Author:", self.get_author(), ", Text:", self.get_text(), ", Location:", self.get_location(), ", Creation:", self.get_creation()

'''
t = Tweet("Javi", "Wassup", "100,300", "5")
print t.to_string()
'''
