#  MLB Analytics App
This app does analytics on Major League Baseball open datasets available on Kaggle using Druid, Flask and Python

Uses CSV Data From https://www.kaggle.com/pschale/mlb-pitch-data-20152018
* [Strike Events](https://www.kaggle.com/pschale/mlb-pitch-data-20152018?select=atbats.csv) - Strike Events
* [Games](https://www.kaggle.com/pschale/mlb-pitch-data-20152018?select=games.csv) - Games 
* [Players](https://www.kaggle.com/pschale/mlb-pitch-data-20152018?select=player_names.csv) - Games 


## 🧰 This project consists of three components 
* [PostgreSQL](https://www.postgresql.org/) - Primary transaction database (stores strike events, games and player tables)
* [Druid](https://druid.apache.org/) - Columnar Storage Datawarehouse For Analytics; Stores Denormalized Table
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - To Serve User Queries

## ⚡ Quick Deploy
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)](https://app.netlify.com/start/deploy?repository=https://github.com/colbyfayock/coronavirus-map-dashboard) [![Deploy with ZEIT Now](https://zeit.co/button)](https://zeit.co/import/project?template=https://github.com/colbyfayock/coronavirus-map-dashboard)

Once deployed, you'll need to add an environment variable `GATSBY_MAPBOX_KEY` with an access token from your [mapbox.com](https://www.mapbox.com) account.


## 🚀 Getting Started

### Requirements
* [PyDruid] (https://pythonhosted.org/pydruid/)
* [Flask](https://anaconda.org/anaconda/flask)

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
database/ddl/tables/*.sql files - confirm tables were created before proceeding.
3. Create a denormalized table by running the denormalized.sql query and export the file as CSV from pgAdmin client
```

* Inside the directory of your choice, scaffold a new Gatsby site:
```
gatsby new [directory] https://github.com/colbyfayock/coronavirus-map-dashboard
```
For example, if I want my installation in `~/Code/my-coronavirua-dashboard`, I would navigate to `~/Code` and run:
```
gatsby new my-coronavirua-dashboard https://github.com/colbyfayock/coronavirus-map-dashboard
```
* Navigate to your new directory and run:
```
yarn develop
```
* You should now be running a new Gatsby site locally! 🎉

