import os
from flask import Flask
from flask import request
from pydruid.client import *
from pydruid.utils.aggregators import doublesum
from pydruid.utils.filters import Dimension
from markupsafe import escape


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #client to interact with our Apache Druid cluster running on
    #locahost and druid's historical service listenting on port 8083
    druid_client = PyDruid('http://localhost:8083', 'druid/v2/')


    ####### App routes registration starts ##############

    @app.route('/')
    def hello():
        """Home page route"""
        return "Hello from MLB Analytics"

    @app.route('/games_per_venue')
    def games_per_venue():
        """Route to retrieve count of games per venue."""

        group = druid_client.groupby(
            datasource='denormalized_strike_events',
            granularity='all',
            intervals='2015-01-01/2018-01-01',
            dimensions=["venue_name", "game_id"]
        )
        games_per_venue = {}
        for entry in group.result:
            venue = entry["event"]["venue_name"]
            if venue not in games_per_venue:
                games_per_venue[venue] = 1
            else: 
                games_per_venue[venue] += 1

        return games_per_venue


    @app.route('/strike_type_count')
    def strike_type_count():
        """Route to retrieve count of each strike type."""

        group = druid_client.groupby(
            datasource='denormalized_strike_events',
            granularity='all',
            intervals='2015-01-01/2018-01-01',
            dimensions=["strike_type"],
            aggregations={"count": doublesum("count")}
        )
        strike_type_count = {}
        for entry in group.result:
            key = entry["event"]["strike_type"]
            value = int(entry["event"]["count"])
            strike_type_count[key] = value
        return strike_type_count
    

    @app.route('/player_strike_count')
    def player_score_count():
        """Route to retrieve count of each strike type per player"""

        group = druid_client.groupby(
            datasource='denormalized_strike_events',
            granularity='all',
            intervals='2015-01-01/2018-01-01',
            dimensions=["first_name", "last_name", "strike_type"],
            aggregations={"count": doublesum("count")}
        )
        return group.result_json

        
    @app.route('/strike_type_count/<strike_event>')
    def strikes_of_a_type(strike_event):
        """Returns total count of a type of a selected strike event."""

        group = druid_client.groupby(
            datasource='denormalized_strike_events',
            granularity='all',
            intervals='2015-01-01/2018-01-01',
            dimensions=["strike_type"],
            filter = Dimension("strike_type") == escape(strike_event),
            aggregations={"count": doublesum("count")}
        )

        strike_type_count = {}
        for entry in group.result:
            key = entry["event"]["strike_type"]
            value = int(entry["event"]["count"])
            strike_type_count[key] = value
        return strike_type_count

    ####### App routes registration ends ##############

    return app