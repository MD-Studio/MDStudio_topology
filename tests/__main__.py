from lie_graph import GraphAxis
from enum import Enum

class NodeType(Enum):
    Atom     = 1
    Molecule = 2
    Group    = 3
    Angle    = 4
    Dihedral = 5

class EdgeType(Enum):
    Bond     = 1
    Angle    = 2
    Dihedral = 3

if __name__ == '__main__':

    print('running debug version of lie_topology')
    system = GraphAxis()

    # testing a molecule graph setup
    system = GraphAxis()
    system.add_node(type=NodeType.Atom, name='H1', atom_number='0', element='H')
    system.add_node(type=NodeType.Atom, name='H2', atom_number='1', element='H')
    system.add_node(type=NodeType.Atom, name='C1', atom_number='2', element='C')
    system.add_node(type=NodeType.Atom, name='H3', atom_number='3', element='H')
    system.add_node(type=NodeType.Atom, name='C2', atom_number='4', element='C')
    system.add_node(type=NodeType.Atom, name='H4', atom_number='5', element='H')
    system.add_node(type=NodeType.Atom, name='H5', atom_number='6', element='H')
    system.add_node(type=NodeType.Atom, name='C3', atom_number='7', element='C')
    system.add_node(type=NodeType.Atom, name='H6', atom_number='8', element='H')
    system.add_node(type=NodeType.Atom, name='H7', atom_number='9', element='H')
    system.add_node(type=NodeType.Atom, name='H8', atom_number='10', element='H')
    
    system.add_node(type=NodeType.Molecule, name='Propane')

    angle_1_nid = system.add_node(type=NodeType.Angle)

    print(system)
    print(system.query_nodes(query={'element':'H'}))
    print(system.query_nodes(query={'name':'H8'}))
    print(system.query_nodes(query={'type':NodeType.Atom}))
    print(system.query_nodes(query={'type':NodeType.Molecule}))
    
    system.add_edge(system.query_nodes(query={'name':'H1'}).nid, 
                    system.query_nodes(query={'name':'C1'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'H2'}).nid, 
                    system.query_nodes(query={'name':'C1'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'C1'}).nid, 
                    system.query_nodes(query={'name':'H3'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'C1'}).nid, 
                    system.query_nodes(query={'name':'C2'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'C2'}).nid, 
                    system.query_nodes(query={'name':'H4'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'C2'}).nid, 
                    system.query_nodes(query={'name':'H5'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'C2'}).nid, 
                    system.query_nodes(query={'name':'C3'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'C3'}).nid, 
                    system.query_nodes(query={'name':'H6'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'C3'}).nid, 
                    system.query_nodes(query={'name':'H7'}).nid,
                    type=EdgeType.Bond)
    system.add_edge(system.query_nodes(query={'name':'C3'}).nid, 
                    system.query_nodes(query={'name':'H8'}).nid,
                    type=EdgeType.Bond)

    system.add_edge(angle_1_nid, system.query_nodes(query={'name':'H1'}).nid, type=EdgeType.Angle)
    system.add_edge(angle_1_nid, system.query_nodes(query={'name':'C1'}).nid, type=EdgeType.Angle)
    system.add_edge(angle_1_nid, system.query_nodes(query={'name':'H3'}).nid, type=EdgeType.Angle)

    #system.add_node(type=Type.Molecule, node=system )
    print ( "___TEST_EDGES__" )
    print(system)
    print(system.query_edges(query={'type':EdgeType.Angle}))