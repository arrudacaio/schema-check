import psycopg2


def connect_db(schema):
  opt = "-c search_path={}".format(schema)
  connection = psycopg2.connect(
    host='localhost',
    database='postgres',
    user='postgres',
    password='postgres',
    options=opt
  )

  return connection


def execute_sql(sql, should_return_data, schema):
  connection = connect_db(schema)
  cursor = connection.cursor()
  recset = 'nothing'

  try:
    cursor.execute(sql)
    if(should_return_data):
      recset = cursor.fetchall()
    connection.commit()
    return recset

  except (Exception, psycopg2.DatabaseError) as error:
    print("Error: %s" % error)
    connection.rollback()
    cursor.close()
    return 1
  cursor.close()