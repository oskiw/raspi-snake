
class Treat(object):

    def __init__(self, color, position, startturn, expiration):
        self.color = color
        self.startturn = startturn
        self.expiration = expiration
        self.position = position

    def get_color(self):
        return self.color

    def has_expired(self, turn):
        return self.startturn + self.expiration < turn

    def on_contact(self, snake):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_points(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def get_position(self):
        return self.position
