# Plant Nursery Application

This github has a plant nursery application for plant lovers to help manage their plants at home. It has a way for people to track the plants they own, when they last watered, and provides tips on plant care needs.


This application is made using Python, the Tkinter library, and a PostgreSQL database. With this application, I have set up an automatic testing and DevOp pipeline. When code is pushed, unit and integration tests are automatically run. If successful, the code is then deployed as a .exe file and is made available for download as an artifact.


To download the executable:
- Go to the "Actions" tab
- Click on the latest successful workflow run
- In the "Artifacts" section, download "HousePlantNursery"


## Instructions

#### Please Note!
These commands are intended for Windows machines.

### To run program manually:

From the root directory use the command:

```bash
python -m src.FinalProjectApplication
```

### To run the tests manually:

From the root directory use the command:
```bash
python -m pytest tests/
```

This will run the unit and integration tests for the code