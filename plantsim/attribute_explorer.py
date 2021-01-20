"""
Copyright (c) 2021 Tilo van Ekeris / TMDT, University of Wuppertal
Distributed under the MIT license, see the accompanying
file LICENSE or https://opensource.org/licenses/MIT
"""

from .table import Table


class AttributeExplorer:

    def __init__(self, plantsim, object_name):

        self.plantsim = plantsim
        self.object_name = object_name

    @property
    def table(self):
        # This is now a property so that it is newly fetched every time you ask about it
        return Table(self.plantsim, f'{self.object_name}.ExplorerTable')
