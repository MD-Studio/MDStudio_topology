
from lie_graph import GraphAxis
from lie_topology.core.io.yaml.yaml_ext import ordered_load
from lie_topology.core.topology.nodes import TopologyNode

def read_meta_data(ff_definitions, ff_graph):

    if not 'meta' in ff_definitions:
        raise KeyError("meta section not available in ff_definitions")

    meta_section = ff_definitions['meta']

    if not all([x in meta_section for x in ('version', 'forcefield')]):
        raise KeyError("meta section in ff_definitions not fully implemented")

    name = meta_section['version']
    forcefield = meta_section['forcefield']

    ff_node_id = ff_graph.add_node(type=TopologyNode.ForceField, name=name, forcefield=forcefield)

    return ff_node_id

def read_mass_types(ff_definitions, ff_graph, ff_node_id):

    if not 'mass_types' in ff_definitions:
        raise KeyError("mass_types section not available in ff_definitions")

    mass_types_section = ff_definitions['mass_types']

    

def read_mdtop(ifs):
    
    ff_definitions = ordered_load(ifs)

    #now start to build a new graph
    ff_graph = GraphAxis()

    ff_node_id = read_meta_data(ff_definitions, ff_graph)

