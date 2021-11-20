# GraphOwl

GraphOwl displays time series data as graphs in a dashboard. To get you started, the project contains a sample dashboard. (TO BE ADDED!)

You can configure the app to connect to various data sources (such as MongoDb or SQLite) and show the data as multi-plot graphs. The data should contain *time* and *value* columns, which are used as the x and y coordinates on the graphs, and a *name* column, which determines which data points belong to the same plot. This column could contain, for example, the names of sensors that were used to collect the data.

[Screenshot](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/Screenshot%202021-11-15%20212921.png) tämänhetkisestä projektin vaiheesta sekä esimerkki 

## Documentation

The following docs describe the app further:
* [Requirement specification](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/reqs.md)
* [UML class diagram](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/classes.yuml)
* [Work tracking sheet](https://github.com/mikkokallio/ot-harkka/blob/master/project/docs/hours.md)

## Usage

**Note:** The app has been tested with Python `3.8`.

Run the following commands in the `project` folder.

* To install, run `poetry install`.
* To start the app, run `poetry run invoke start`.
* To run tests, run `poetry run invoke test`.
* For test coverage report, run `poetry run invoke coverage-report`.
* To run the linter, run `poetry run invoke lint`. TO BE ADDED!

TO BE ADDED: Build phase
