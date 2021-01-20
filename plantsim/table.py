"""
Copyright (c) 2021 Tilo van Ekeris / TMDT, University of Wuppertal
Distributed under the MIT license, see the accompanying
file LICENSE or https://opensource.org/licenses/MIT
"""

from texttable import Texttable

from typing import List, Union, Dict


class Table:

    def __init__(self, plantsim, table_name):
        """
        Table mapping for PlantSim Tables (e.g., DataTable, ExplorerTable)
        :param plantsim: Plantsim instance (with loaded model) that is queried
        :param table_name: The object name within Plantsim relative to the current path context
        """
        self._rows = []
        self._rows_coldict = []

        row_count = plantsim.get_value(f'{table_name}.YDim')
        col_count = plantsim.get_value(f'{table_name}.XDim')
        if row_count > 0 and col_count > 0:
            for row_idx in range(row_count + 1):
                row = []
                row_coldict = {}
                for col_idx in range(col_count + 1):
                    cell_value = plantsim.get_value(f'{table_name}[{col_idx}, {row_idx}]')
                    row.append(cell_value)
                    if row_idx > 0:
                        col_header = self.rows[0][col_idx]
                        row_coldict[col_header] = cell_value
                self._rows.append(row)
                if row_idx > 0:
                    self._rows_coldict.append(row_coldict)

    @property
    def rows(self) -> List[List]:
        """
        Returns table data row-first indexed
        :return: 2-dim list containing table data row-first indexed
        """
        return self._rows

    @property
    def header(self) -> List:
        """
        Returns header (first table row)
        :return: list containing header elements
        """
        return self.rows[0]

    @property
    def rows_body(self) -> List[List]:
        """
        Returns table data row-first indexed without header
        :return: 2-dim list containing table data row-first indexed without first row
        """
        return self.rows[1:]

    @property
    def rows_coldict(self) -> List[Dict]:
        """
        Returns table data row-first indexed. Each column is a Dict with header as key
        :return: list of dictionaries
        """
        return self._rows_coldict

    @property
    def row_count(self) -> int:
        """
        Returns total row count (including header)
        :return: row count as integer
        """
        return len(self.rows)

    @property
    def columns(self) -> List[List]:
        """
        Returns table data column-first indexed.
        :return: 2-dim list containing table data column-first indexed
        """
        return list(map(list, zip(*self.rows)))

    @property
    def columns_body(self) -> List[List]:
        """
        Returns table data column-first indexed without header
        :return: 2-dim list containing table data column-first indexed without header
        """
        return list(map(list, zip(*self.rows_body)))

    def get_columns_by_idx(self, col_idxs: Union[int, List[int]], clip_header=False) -> Union[List, List[List]]:
        """
        Returns data from the table column-first indexed - filtered to certain columns
        :param col_idxs: column indexes you want to extract from table as single int or list of ints, e.g. 1 or [0, 2]
        :param clip_header: if True, removes the first line (usually header) from the column
        :return: specified column(s) from table as 1- or 2-dim list
        """
        if not isinstance(col_idxs, list):
            col_idxs = [col_idxs]

        if clip_header:
            columns_input = self.columns_body
        else:
            columns_input = self.columns

        columns_output = []
        for col_idx in col_idxs:
            if col_idx >= len(columns_input):
                raise IndexError('Column index ist not valid!')
            columns_output.append(columns_input[col_idx])

        if len(columns_output) == 1:
            return columns_output[0]
        else:
            return columns_output

    def get_columns_by_header(self, col_headers: Union[str, List[str]], include_header=False) -> Union[List, List[List]]:
        """
        Returns data from the table column-first indexed - filtered to certain columns
        :param col_headers: headers of columns that shall be returned (single string or list of strings)
        :param include_header: determines if headers are returned
        :return: specified column(s) from table as 1- or 2-dim list
        """
        if not isinstance(col_headers, list):
            col_headers = [col_headers]

        columns_input = self.columns

        columns_output = []
        for col_header in col_headers:
            if col_header not in self.header:
                raise IndexError(f'Column header "{col_header}" is not valid')
            column = columns_input[self.header.index(col_header)]
            if not include_header:
                column = column[1:]
            columns_output.append(column)

        if len(columns_output) == 1:
            return columns_output[0]
        else:
            return columns_output

    def __str__(self):
        """
        Returns string representation via Texttable
        :return: string representation of table
        """
        if self.row_count > 0:
            texttable = Texttable(200)
            texttable.add_rows(self.rows)
            texttable.set_deco(Texttable.HEADER)
            return texttable.draw()
        else:
            return '<empty table>'
