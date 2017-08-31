"""
The uplink is the way robots communicate with satellites
"""
class Uplink(object):

    satellite = None
    override_missing_satellite = False

    def __init__(self, satellite=None):
        self.satellite = satellite

    def is_position_clear(self, posX, posY):
        if self.satellite is not None:
            occupado = self.satellite.is_coordinates_occupied(posX, posY)
            if occupado is False:
                return True
        return False if self.override_missing_satellite is not True else True

    def is_position_out_of_bounds(self, posX, posY):
        if self.satellite is not None:
            return self.satellite.is_coordinates_out_of_bounds(posX, posY)
        return True if self.override_missing_satellite is not True else False