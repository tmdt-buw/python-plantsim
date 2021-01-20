# Python Package for communication with Siemens Tecnomatix Plant Simulation

This package enables the communication with the simulation software product "Tecnomatix Plant Simulation" by
Siemens. It speaks to PlantSim via the COM interface from within Python and includes useful mappings for
some more complex PlantSim data types like tables.


## Example

```python
from plantsim.plantsim import Plantsim
from plantsim.table import Table

plantsim = Plantsim(version='15.2', license_type='Research')
plantsim.load_model('model.spp')
plantsim.set_path_context('.Context.In.Your.Model')
table = Table(plantsim, 'TableName')
print(table) 
```


## Setup

### Requirements

You need a working version of Tecnomatix Plant Simulation installed on your system to be able to use this package.


### System settings

If you have a NVIDIA 3D graphics card installed, make sure to select it as the default in the "NVIDIA Control Panel".
Otherwise when loading a model into Plant Simulation, you will get an information window that you need to manually
click every time.


## Acknowledgements

This repository was created within the Public Research Project
[AlphaMES](https://www.tmdt.uni-wuppertal.de/de/projekte/alphames.html) run by the
[Chair of Technologies and Management of Digital Transformation](https://www.tmdt.uni-wuppertal.de/de/startseite.html)
within the [University of Wuppertal](https://www.uni-wuppertal.de/).

It was funded via a research grant by the German Federal Ministry for Economics and Energy (BMWi).


## Maintainers

This package is currently maintained by Tilo van Ekeris and Constantin Waubert de Puiseau.


## Disclaimer

Tecnomatix, Plant Simulation etc. are brand names of Siemens. This is NOT an official Siemens product.

This software is provided "as is" without warranty of any kind. See the LICENSE file for details.

Furthermore, this software is currently actively developed and used in research so that there are no guarantees
for stable interfaces etc.


## Copyright

```
Copyright (c) 2021 Tilo van Ekeris / TMDT, University of Wuppertal
Distributed under the MIT license, see the accompanying
file LICENSE or https://opensource.org/licenses/MIT
```
