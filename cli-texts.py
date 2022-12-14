def welcome_schema_check():
  presentation = f"""
    +---------------------------------------+
    |          Welcome to SchemaCheck       |
    +---------------------------------------+

    Before starting to examine the schema, it is necessary to create
    a correction schema, which will be used as a basis for comparison.

    Before starting to check the schemas, you need to enter in the database and run this following command:
    ```sh
      CREATE SCHEMA IF NOT EXISTS lesson;
      CREATE SCHEMA IF NOT EXISTS correction;
    ```

    Example of correction schema:
    /*
    tableNames=['oneTable', 'one_table', 'tableOne', 'TableOne']
    pkNames=['id', 'cpf', 'rg']
    pkTypes=['varchar']
    fkNames=['owner']
    fkTypes=['varchar varying']
    */
    CREATE TABLE TableOne(
      id integer not null,
      primary key(id)
    );

    When you use tableNames/pkNames/pkTypes/fkNames/fkTypes it turns the correction schema more flexible.

    Once you have created the correction schema in the root of the project with the filename equal to correction.sql
    you are able to place the schema to be corrected also in the root of the project with the filename equal to lesson.sql.
    After that, you are able to perform schema correction.
    """
  print(presentation)


def help_schema_check():
  txt = f"""
  schema_check <opt> \n\n

  Flags that you can use:
  -file_path  : to indicates where be a correction schema
  """
  print(txt)


def final_report():
  txt = f"""
  +---------------------------------------+
  |SchemaCheck -> Final Report            |
  +---------------------------------------+

  Table analyzed: name here
  Table Name: Probably wrong, check please.
  Primary Key column name: sadasdasd
  Type of primary key:

  """


welcome_schema_check()
