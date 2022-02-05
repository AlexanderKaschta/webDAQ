

class Setting:
    """
    Model class representing sensor settings
    """

    def __init__(self, name: str, required=False):
        self.name = name
        self.required = required
