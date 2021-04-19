import json
import pymysql
from server import db
import pandas as pd

def user_handler(obj):
  return obj.isoformat() if hasattr(obj,'isoformat') else obj

def data_frame(curs):
  data = pd.DataFrame(curs.fetchall())
  data .columns = [desc[0] for desc in curs.description]
  return data

# def getAllUsers():
#   conn = getConnection()
#   curs = conn.cursor(pymysql.cursors.DictCursor)
#   sql = "SELECT userID,nickname,email,contribution FROM User;"
#   curs.execute(sql)
#   rows = curs.fetchall()
#   conn.close()
#   return json.dumps(rows, default = user_handler)

def getAllPerson():
  conn = db.getConnection()
  curs = conn.cursor()
  sql = "SELECT COUNT(person_id) AS person FROM person;"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data

# def getAllGender():
#   conn = db.getConnection()
#   curs = conn.cursor()
#   sql = "SELECT COUNT(gender_concept_id) AS gender FROM person GROUP BY gender_concept_id;"
#   curs.execute(sql)
#   result = curs.fetchall()
#   conn.close()
#   return result

def getAllGender():
  conn = db.getConnection()
  curs = conn.cursor()
  sql =   "SELECT c.concept_name, COUNT(p.gender_concept_id) \
          FROM person p INNER JOIN concept c \
          ON c.concept_id = p.gender_concept_id \
          GROUP BY c.concept_name, p.gender_concept_id;"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data

def getRaceConcept():
  conn = db.getConnection()
  curs = conn.cursor()
  sql =  "SELECT c.concept_name, COUNT(p.race_concept_id)\
          FROM person p \
          INNER JOIN concept c \
          ON c.concept_id = p.race_concept_id \
          GROUP BY c.concept_name , p.race_concept_id;"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data

def getDeathPerson():
  conn = db.getConnection()
  curs = conn.cursor()
  sql =  "SELECT c.concept_name, COUNT(p.ethnicity_concept_id)\
          FROM person p \
          INNER JOIN concept c \
          ON c.concept_id = p.ethnicity_concept_id \
          GROUP BY c.concept_name , p.ethnicity_concept_id;"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data

def getDeathPerson():
  conn = db.getConnection()
  curs = conn.cursor()
  sql = "SELECT count(person_id) as death_count FROM death;"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data

def getSerchConcept(serchIdx):
  serch = serchIdx
  conn = db.getConnection()
  curs = conn.cursor()
  sql = "SELECT concept_name FROM concept WHERE concept_id = %s;"
  curs.execute(sql,serch)
  data = data_frame(curs)
  conn.close()
  return data