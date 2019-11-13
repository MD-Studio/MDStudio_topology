from enum import Enum

class TopologyNode(Enum):
    Atom       = 1
    Molecule   = 2
    Group      = 3
    Angle      = 4
    Dihedral   = 5
    ForceField = 6
