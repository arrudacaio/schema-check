def welcome_schema_check():
  presentation = f"""
    +---------------------------------------+
    |          Welcome to SchemaCheck       |
    +---------------------------------------+

    Before starting to examine the schema, it is necessary to create
    a correction schema, which will be used as a basis for comparison.

    Example of correction schema:

    CREATE TABLE TableOne(
      id integer not null,
      primary key(id)
    );
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