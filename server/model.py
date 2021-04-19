import json
import psycopg2
from server import db
import pandas as pd

def user_handler(obj):
  return obj.isoformat() if hasattr(obj,'isoformat') else obj

def data_frame(curs):
  data = pd.DataFrame(curs.fetchall())
  data .columns = [desc[0] for desc in curs.description]
  return data

def getAllPerson():
  conn = db.getConnection()
  curs = conn.cursor()
  sql = "SELECT COUNT(person_id) AS person FROM person;"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data

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
  sql = "SELECT count(person_id) as death_count FROM death;"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data

def getSerchConcept(serchIdx):
  serch = serchIdx
  conn = db.getConnection()
  curs = conn.cursor()
  sql = f"SELECT concept_name, concept_id FROM concept WHERE concept_id = {serch};"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data

def getGenderVisit():
  conn = db.getConnection()
  curs = conn.cursor()
  sql = "SELECT COUNT(p.gender_concept_id) AS gender_count , c.concept_name AS Gender\
          FROM person p \
          INNER JOIN visit_occurrence v \
          ON p.person_id = v.person_id \
          INNER JOIN concept c \
          ON c.concept_id = p.gender_concept_id \
          GROUP BY p.gender_concept_id , c.concept_name;"
  curs.execute(sql)
  data = data_frame(curs)
  conn.close()
  return data