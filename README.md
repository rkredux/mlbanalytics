#  MLB Analytics App
This app does analytics on Major League Baseball open datasets available on Kaggle using Druid, Flask and Python

Uses CSV Data From https://www.kaggle.com/pschale/mlb-pitch-data-20152018
* [Strike Events](https://www.kaggle.com/pschale/mlb-pitch-data-20152018?select=atbats.csv)
* [Games](https://www.kaggle.com/pschale/mlb-pitch-data-20152018?select=games.csv)
* [Players](https://www.kaggle.com/pschale/mlb-pitch-data-20152018?select=player_names.csv) 


## 🧰 This project consists of three components 
* [PostgreSQL](https://www.postgresql.org/) - Primary transaction database (stores strike events, games and player tables)
* [Druid](https://druid.apache.org/) - Columnar Storage Datawarehouse For Analytics; Stores Denormalized Table
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - To Serve User Queries


## 🚀 Getting Started

### Requirements
* [PyDruid](https://pythonhosted.org/pydruid/)
* [Flask](https://anaconda.org/anaconda/flask)
* [Postgres](https://www.postgresql.org/)
* [Docker-compose](https://docs.docker.com/compose/install/)


### Setting up the App
Run the following in your favorite terminal assuming you use Conda for Python env/package management
if not run the equivalent using pip
```
conda install -c conda-forge pydruid
conda install -c anaconda flask
```

* Ingest the CSV data into PostgreSQL database
```
1. Start an instance of PostgreSQL on localhost
2. Using a psql client (either on terminal or pgAdmin client) set up the tables using DDL queries given in 
   ./database/ddl/tables/*.sql files - confirm tables were created before proceeding.
3. Please update the full path to where the CSV files are stored on your machine
4. Run indexer_main.py to load the data into Postgres. Confirm data loaded by querying the tables created in Postgres
5. Create a denormalized table by running the denormalized.sql query and export the file as CSV from pgAdmin client
```

* Start a Druid Cluster + Ingest data into Druid
```
1. Run docker-compose.yml - this should give you a fully operational druid cluster
2. Open Druid UI on localhost:8888 in your browser
3. Use Druid console to ingest the denormalized CSV generated from Step 3 above - follow the steps
   on this page - https://druid.apache.org/docs/latest/tutorials/tutorial-batch.html#loading-data-with-a-spec-via-console
   Use the file ./druid/ingestion_specs/denormalized_spec.json file as your spec file. Once this file is submitted, it 
   will trigger an ingestion task which can be monitored in Tasks console on localhost:8888 in the browser
4. Confirm that the csv was ingested by going to the query pane and querying the data. 
5. You are set - data is in Druid. 
```

* Start your Flask server to start sending queries from the browser
```
Run the below three commands from terminal 

export FLASK_APP=flaskr
export FLASK_ENV=development
flask run

Then navigate to flask app running on http://127.0.0.1:5000/
```

* You should now be running a new Flask app locally! 🎉
Try the following end points from the browser which will query the Druid cluster and respond back with JSON results
1. /player_score_count
2. /games_per_venue
3. /strike_type_count
4. /strike_type_count/<strike_event> e.g. /strike_type_count/Home%20Run

TODO
1. Render the data on the browser through D3.js (https://d3js.org/)


