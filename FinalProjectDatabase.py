#=================================
# Morgan Jensen
# 05/05/2024
# Final Project
#=================================

#This file contains all of the database functions that will
#needed for my final project as well as a few other extranious functions

import psycopg2
from datetime import date
import datetime

#===============================
# Database Functions
#===============================

# Connection functions
#-------------------------------
def ConnectDB():
    con = psycopg2.connect(
        host = "localhost",
        database="FinalProject",
        user = "postgres",
        password = "Ih8passwards!",
        port = 5432
    )
    return con

def DisconnectDB(con):
    con.close()

# Query input functions
#-------------------------------

#enter watering page
def new_wat_log(dateW, aW, fert, aF, userID, plantID):
    con = ConnectDB()
    cur = con.cursor()
    if fert == 0:
        fertz = False
        amountF = 0
    else:
        fertz = True
        amountF = aF

    id = newID('watering_log')

    date = convertDate(str(dateW))

    cur.execute("INSERT INTO watering_log VALUES ({}, '{}', {}, {}, {}, {}, {})".format(id, date, aW, fertz, amountF, userID, plantID))
    con.commit()
    DisconnectDB(con)

#new plant page
def new_plant(userID, plant):
    con = ConnectDB()
    cur = con.cursor()
    plantID = getPlantID(plant)
    id = newID('plants_owned')
    cur.execute('INSERT INTO plants_owned VALUES ({}, {}, {})'.format(id, userID, plantID))
    con.commit()
    DisconnectDB(con)

#sign up page
def new_user(userN, passw, firstN, lastN):
    con = ConnectDB()
    cur = con.cursor()
    id = newID('users')
    cur.execute("INSERT INTO users VALUES ({}, '{}', '{}', '{}', '{}')".format(id, userN, passw, firstN, lastN))
    con.commit()
    DisconnectDB(con)

# Query output functions
#-------------------------------

#gets all the user names
def getUserNames():
    con = ConnectDB()
    cur = con.cursor()

    cur.execute('SELECT username FROM users')
    names = cur.fetchall()

    DisconnectDB(con)

    return names

#gets specific user name
def getSpecFName(userID):
    con = ConnectDB()
    cur = con.cursor()
    cur.execute('SELECT firstname FROM users WHERE id={}'.format(userID))
    name = cur.fetchone()
    return name

#gets password
def getPassword(userName):
    con = ConnectDB()
    cur = con.cursor()

    cur.execute("SELECT password FROM users WHERE username = '{}'".format(userName))
    passw = cur.fetchall()
    password = passw[0][0]

    DisconnectDB(con)
    return password

#This function gets the id for a specific user
def getUserID(user):
    con = ConnectDB()
    cur = con.cursor()

    cur.execute("SELECT id FROM users WHERE username = '{}'".format(user))
    id = cur.fetchall()
    idNum = id[0][0]

    DisconnectDB(con)

    return idNum

#gets the last user ID that was inputed into the database
def getMaxID(table):
    con = ConnectDB()
    cur = con.cursor()
    cur.execute("SELECT MAX(id) FROM {}".format(table))
    lastID = cur.fetchall()
    DisconnectDB(con)
    return lastID

# gets the plant ID
def getPlantID(pName):
    con = ConnectDB()
    cur = con.cursor()
    cur.execute("select id from plant_info where commonname='{}'".format(pName))
    id = cur.fetchall()[0][0]
    DisconnectDB(con)
    return id

#get user's Plants
def getUserPlants(userID):
    con = ConnectDB()
    cur = con.cursor()
    cur.execute("SELECT plant_id FROM plants_owned WHERE user_id = {}".format(userID))
    plants = cur.fetchall()
    plant_ids = []
    for p in plants:
        plant_ids.append(p[0])

    DisconnectDB(con)
    return plant_ids

#gets just the names of the plants specified
def getPlantNames(plant_ids):
    names = []

    for plant in plant_ids:
        con = ConnectDB()
        cur = con.cursor()
        cur.execute("SELECT commonname FROM plant_info WHERE ID = {}".format(plant))
        name = cur.fetchall()
        names.append(name[0][0])
        DisconnectDB(con)

    return names

#this gets the name of 1 specific plant
def get1PlantName(plantID):
    con = ConnectDB()
    cur = con.cursor()
    cur.execute(f'SELECT commonname FROM plant_info WHERE ID = {plantID}')
    plant = cur.fetchone()[0]
    DisconnectDB(con)
    return plant

# get all plants is used for the search page
def getAllPlants():
    con = ConnectDB()
    cur = con.cursor()
    cur.execute('SELECT commonname FROM plant_info')
    allPlants = cur.fetchall()
    allPlantNames = []
    for plant in allPlants:
        allPlantNames.append(plant[0])
    DisconnectDB(con)
    return allPlantNames

# gets the watering history from the specific user
def getWatLog(user):
    con = ConnectDB()
    cur = con.cursor()
    cur.execute('sELECT * FROM watering_log WHERE user_id = {}'.format(user))
    rawLog = cur.fetchall()
    DisconnectDB(con)
    return rawLog

# gets the care tips for any specified plant
def getPlantInfo(plant):
    con = ConnectDB()
    cur = con.cursor()
    cur.execute("SELECT * FROM plant_info JOIN care ON plant_info.id = care.id\
                WHERE care.id = {}".format(plant))
    info = cur.fetchall()
    plantInfo = info[0]
    DisconnectDB(con)
    return plantInfo

# Query delete function
#-------------------------------
def remove_plant(userID, plantID):
    con = ConnectDB()
    cur = con.cursor()
    cur.execute('DELETE FROM plants_owned WHERE user_id={} and plant_id={}'.format(userID, plantID))
    con.commit()
    DisconnectDB(con)

#===============================
# Other Functions
#===============================

#this function produces a user ID for new users
def newID(table):
    
    id = getMaxID(table)
    newID = id[0][0]+1
    return newID

# This function take the date in the format month/day/year and 
#converts it to the datetime format year-month-day
def convertDate(date):   
    new_date = datetime.datetime.strptime(str(date), "%m/%d/%y")
    formated_date = new_date.strftime("%Y-%m-%d")
    return formated_date