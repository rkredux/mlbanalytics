from pydruid.client import *
from pydruid.utils.aggregators import doublesum

query = PyDruid('http://localhost:8083', 'druid/v2/')

group = query.groupby(
            datasource='denormalized_strike_events',
            granularity='day',
            intervals='2015-10-04/2018-01-01',
            dimensions=["strike_type"],
            aggregations={"count": doublesum("count")}
        )

print(group)