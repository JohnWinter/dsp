# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'


from datetime import datetime
date_start = '01-02-2013'
date_stop = '07-28-2015'

dayz = (datetime.strptime(date_stop,"%m-%d-%Y")-datetime.strptime(date_start,"%m-%d-%Y")).days



print(dayz)

####b)  
date_start = '12312013'  
date_stop = '05282015'

from datetime import datetime
date_start = '12312013'
date_stop = '05282015'

dayz = (datetime.strptime(date_stop,"%m%d%Y")-datetime.strptime(date_start,"%m%d%Y")).days



print(dayz)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'

from datetime import datetime



date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

dayz = (datetime.strptime(date_stop,"%d-%b-%Y")-datetime.strptime(date_start,"%d-%b-%Y")).days



print(dayz)