class Package:
    def __init__(self, pkg_id, position, destination):
        self.id = pkg_id
        self.position = position
        self.destination = destination
        self.is_carried = False
        self.carrier_id = None
