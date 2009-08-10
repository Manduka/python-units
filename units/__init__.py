"""Provides support for quantities and units, which strictly disallow
invalid operations between incompatible quantities. For example, we cannot add 
2 metres to 5 seconds, because this doesn't make sense.
"""

REGISTRY = {}

import units.si

import units.leaf_unit
import units.named_composed_unit


def unit(unit_str):
    """Create a unit object from a given string specification"""
    if unit_str in REGISTRY:
        return REGISTRY[unit_str]
    if units.si.can_make(unit_str):
        return units.si.make(unit_str)
    else:
        return units.leaf_unit.make(unit_str, is_si=False)