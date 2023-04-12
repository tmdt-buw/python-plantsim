import os
import time

from plantsim.plantsim import Plantsim
from plantsim.table import Table


plantsim = Plantsim(version='16.1', license_type='Research')#, visible=False)
plantsim.load_model(os.getcwd() + '\model.spp')

plantsim.set_path_context('.Modelle.Modell')

plantsim.set_value('procTime', '30:00.00000')
# if you want to set the time as a real time you can do this by executing a 
# simtalk lambda function
#plantsim.execute_simtalk("procTimeT := str_to_time(\"45:00.0\")")

# do the simulation run
plantsim.set_event_controller()
plantsim.reset_simulation()
plantsim.start_simulation()

# wait until the simulation has finished
while plantsim.is_simulation_running():
    time.sleep(0.1)
    
# get main kpi
print("Counted sinks in totalSinks:", plantsim.get_value('totalSinks'))
print("Statistic value (parts in) of sink:", plantsim.get_value('Senke.StatAnzahlEin'))

# print table with indexes
table = Table(plantsim, 'ResultTable')
print(table) 

# print table without index
table1 = Table(plantsim, 'ResultTable1')
print(table1) 

plantsim.quit()