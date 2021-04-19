from flask import Flask
from flask_restx import Api, Resource
from server import model
import pandas as pd
import psycopg2

app = Flask(__name__)
app.debug = True

#person 테이블 관련
@app.route("/person",methods=['GET'])
def getAllPerson():
  result = model.getAllPerson()
  print(result)
  return str(result)

@app.route("/person/gender",methods=['GET'])
def getAllGender():
  result = model.getAllGender()
  print(result)
  return str(result)

@app.route("/person/race",methods=['GET'])
def getRaceConcept():
  result = model.getRaceConcept()
  print(result)
  return str(result)

@app.route("/person/ethnicity",methods=['GET'])
def getAllEthnicity():
  result = model.getAllEthnicity()
  print(result)
  return str(result)

@app.route("/person/death",methods=['GET'])
def getDeathPerson():
  result = model.getDeathPerson()
  print(result)
  return str(result)

# 키워드 검색
@app.route("/serch/<int:serchIdx>",methods=['GET'])
def getSerchConcept(serchIdx):
  result = model.getSerchConcept(serchIdx)
  print(result)
  return str(result)

# visit 테이블 관련
@app.route("/visit/gender",methods=['GET'])
def getGenderVisit():
  result = model.getGenderVisit()
  print(result)
  return str(result)