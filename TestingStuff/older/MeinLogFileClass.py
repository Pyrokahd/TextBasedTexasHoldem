class MeinLogfile:
    def __init__(self, filename):
        self.filename = filename
        self.f = None
    def eintrag(self, text):
        toWrite = "{}\n".format(text)
        self.f.write(toWrite)
        print(toWrite)
    def __enter__(self):
        self.f = open(self.filename, "a")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()