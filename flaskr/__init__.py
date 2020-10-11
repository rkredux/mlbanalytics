import os
from flask import Flask
from pydruid.client import *
from pydruid.utils.aggregators import doublesum
from pydruid.utils.filters import Dimension
from markupsafe import escape
import pandas as pd


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    #boiler plate
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    druid_client = PyDruid('http://localhost:8083', 'druid/v2/')

    #routes
    @app.route('/')
    def hello():
        return "Hello from MLB Analytics"

    # retrieve count for each strike type for all players
    @app.route('/player_score_count')
    def player_score_count():
        group = druid_client.groupby(
            datasource='denormalized_strike_events',
            granularity='all',
            intervals='2015-01-01/2018-01-01',
            dimensions=["first_name", "last_name", "strike_type"],
            aggregations={"count": doublesum("count")}
        )
        return group.result[10]
    
    #count of each strike type
    @app.route('/strike_type_count')
    def strike_type_count():
        group = druid_client.groupby(
            datasource='denormalized_strike_events',
            granularity='all',
            intervals='2015-01-01/2018-01-01',
            dimensions=["strike_type"],
            aggregations={"count": doublesum("count")}
        )
        return group.result[1]

    #total count of a type of strike event
    @app.route('/strike_type_count/<strike_event>')
    def strikes_of_a_type(strike_event):
        group = druid_client.groupby(
            datasource='denormalized_strike_events',
            granularity='all',
            intervals='2015-01-01/2018-01-01',
            dimensions=["strike_type"],
            filter = Dimension("strike_type") == escape(strike_event),
            aggregations={"count": doublesum("count")}
        )
        return group.result[0]

    return app