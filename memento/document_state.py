class Document:
    def __init__(self, content, font_name, font_size):
        self.__content = content
        self.__font_name = font_name
        self.__font_size = font_size

    def get_content(self):
        return self.__content

    def get_font_name(self):
        return self.__font_name

    def get_font_size(self):
        return self.__font_size