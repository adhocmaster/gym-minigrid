from enum import Enum

class SingleActions(Enum):
    """Forward actions are relative to the world coordinate system"""
    FORWARD = "FORWARD"
    VEHICLE = "VEHICLE"
    POSITION = "POSITION"
    #KEEP = "KEEP"
