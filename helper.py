from database.db import execute_sql
from Levenshtein import ratio
import os

array = []

def parse_list(response):
    array.clear()
    for info in response:
        result = dict()
        result['key'] = info[0]
        result['table_name'] = info[1]
        result['constraint_name'] = info[2]
        result['position'] = info[3] # se tiver position = 2 é pq usou de chave composta.
        result['key_column'] = info[4]
        result['type'] = info[5]
        array.append(result)
    return array

def get_info(schema):
  if (schema == 'lesson'):
    query = open('./queries/get-lesson.sql', 'r').read()
  if (schema == 'correction'):
    query = open('./queries/get-correction.sql', 'r').read()
  response = execute_sql(query, True, schema)
  if response != 'nothing':
      return parse_list(response)
  return response

def clean_db():
    array = []
    query = open('./queries/drop.sql', 'r').read()
    return execute_sql(query, False, 'lesson')

def check_name_by_leven(possibleName, n):
  result = ratio(possibleName, n)
  if (result > 0.5):
    return True
  return False

def compare_in_depth(n, array):
  for i in array:
    if (check_name_by_leven(n, i)):
      return True
  return False

def apply_correction_db(correction_path):
    f = open(correction_path, 'r').read()
    data = execute_sql(f, False, 'correction')
    print('Correction expected was applied')


def apply_lesson_db(lesson_path):
    f = open(lesson_path, 'r').read()
    data = execute_sql(f, False, 'lesson')
    print('Lesson expected was applied')