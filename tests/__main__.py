import sys
import argparse

from lie_graph import GraphAxis
from enum import Enum

from mdstudio_topology.parsers.topology import read_mdtop

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

def verify_graph():

    print('running debug version of mdstudio_topology')
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

    for edge in system.query_edges(query={'type':EdgeType.Angle}).edges:
        print(edge)

    for node in system.query_edges(query={'type':EdgeType.Angle}).nodes:
        print(node)

def main(argv):

    parser = argparse.ArgumentParser(description='Convert an atb mtb file to polff using the field fit atom types')
    parser.add_argument('--mdtop', required=True, type=str, help='a mdtop file')
    args = parser.parse_args(argv)

    with open(args.mdtop, 'r') as ifs:
        read_mdtop(ifs)

# commands
# pipenv install --skip-lock --dev --sequential
# pipenv shell
# pip install -e components/my_component
# python -m my_component

if __name__ == "__main__":
    #raise Exception("DISABLED AS TEMPLATES WERE MANUALLY EDITED, KNOWN WHAT YOU DO BEFORE REACTIVATING")
    main(sys.argv[1:])