import os
import pandas as pd

from loader.plantsim_loader import PlantsimLoader

class PandasTable():

    def __init__(self, object_name, table_buffer_path=''):
        """
        Table mapping for PlantSim Tables (e.g., DataTable, ExplorerTable)
        - stores table in a .txt file in the python script directory
        - returns that table as a pandas Dataframe
        :param plantsim: Plantsim instance (with loaded model) that is queried
        :param table_name: The object name within Plantsim relative to the current path context
        """
        self.plantsim = PlantsimLoader.get_plantsim()
        self._table = None
        self._table_name = object_name
        self._table_buffer_path = os.path.join(table_buffer_path, 'table_buffer')

        self.update()

    def update(self):
        # create table buffer directory
        if not os.path.exists(self._table_buffer_path):
            os.makedirs(self._table_buffer_path)

        abs_table_buffer_path = os.path.abspath(self._table_buffer_path)
        buffer_file_name = f'{self._table_name}_tool_buffer.txt'
        abs_buffer_file_path = os.path.join(abs_table_buffer_path, buffer_file_name)

        # store table from Plant Simulation
        command = f'{self._table_name}.schreibeDatei("{abs_buffer_file_path}")'
        self.plantsim.execute_simtalk(command)

        # readout table from buffer
        self._table = pd.read_csv(f'{abs_buffer_file_path}', delimiter='\t')

    @property
    def table(self):
        return self._table
