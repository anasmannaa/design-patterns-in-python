import document_state

class Document:
    def __init__(self):
        self.__content = ""
        self.__font_name = ""
        self.__font_size = 0
    
    def create_state(self):
        return document_state.Document(self.__content, self.__font_name, self.__font_size)

    def restore (self, state):
        self.__content = state.get_content()
        self.__font_name = state.get_font_name()
        self.__font_size = state.get_font_size()

    def get_content(self):
        return self.__content

    def set_content(self, content):
        self.__content = content

    def get_font_name(self):
        return self.get_font_name

    def set_font_name(self, font_name):
        self.__font_name = font_name

    def get_font_size(self):
        return self.get_font_size

    def set_font_size(self, font_size):
        self.__font_size = font_size

    def __str__(self):
        return f"Document( content = {self.__content}, font name = {self.__font_name}, font size= {self.__font_size})"
