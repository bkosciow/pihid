
class Config(object):
    _id = 1

    def __init__(self):
        self.id = Config._id
        Config._id += 1
        self.params = {}
