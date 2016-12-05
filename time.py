## Replace America/New_York With your Timezone
## They can be found here
## https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

from datetime import datetime 
from pytz import timezone 
us = timezone('America/New_York') 
sa_time = datetime.now(us)
print sa_time.strftime("Today is %B %d, %Y" " The Time is " "%I:%M%P")
