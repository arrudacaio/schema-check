# -*- coding: utf-8 -*-


# try:

# except KeyboardInterrupt:
#   print("Obrigado por usar esse script!")

# Cenário só pra teste ------------------------
from utils import get_correction_possible_data
from helper import get_info, compare_in_depth, apply_correction_db, apply_lesson_db, check_name_by_leven


possible_data_correction = get_correction_possible_data('./correction.sql')

# ## Só pra deixar o nome da tabela dentro do tableNames
for name in possible_data_correction.keys():
  possible_data_correction[name]['tableNames'].insert(0, name)

# print('\n\n\n possible-info -<', possible_data_correction)


## Aplicando a query da correção no banco
apply_correction_db('./correction.sql') # TODO Resgatar esse path da linha do comando?
correction_db_info = get_info('correction')


apply_lesson_db('./lesson.sql') # TODO Resgatar esse path da linha do comando?
lesson_db_info = get_info('lesson')

## Realizando a mescla para obter o objeto final de correction
final = []

for j in possible_data_correction.keys():
  final_report = dict()
  final_report['tableName'] = False
  final_report['pkName'] = False
  final_report['pkType'] = False
  final_report['pkCompose'] = False
  final_report['fkName'] = False
  final_report['fkType'] = False


  for d in correction_db_info:
    equal_table_names = check_name_by_leven(d['table_name'], j)
    if(equal_table_names):
      obj = possible_data_correction[j]
      if (d['table_name'] not in obj['tableNames']):
        obj['tableNames'].insert(0, str(d['table_name']))

      if(d['key'] == 'PRIMARY KEY'): # Validação da chave primária
        if('pkNames' in obj):
          if (d['key_column'] not in obj['pkNames']):
            obj['pkNames'].insert(0, str(d['key_column']))

        if('pkTypes' in obj):
          if (d['type'] not in obj['pkTypes']):
            obj['pkTypes'].insert(0, str(d['type']))

        # Falta validar a chave composta

      if(d['key'] == 'FOREIGN KEY'): # Validação da chave primária
        if('fkNames' in obj):
          if (d['key_column'] not in obj['fkNames']):
            obj['fkNames'].insert(0, str(d['key_column']))

        if('fkTypes' in obj):
          if (d['type'] not in obj['fkTypes']):
            obj['fkTypes'].insert(0, str(d['type']))

  # Corrigindo a lesson
  for x in lesson_db_info:
    equal_table_names = check_name_by_leven(x['table_name'], j)

    if (equal_table_names):
      obj = possible_data_correction[j]

      if(x['table_name'] not in final):
        final_report['table_analyzed'] = x['table_name']
        final_report['tableName'] = True

      if(x['key'] == 'PRIMARY KEY'): # Validação da chave primária
        if('pkNames' in obj):
          pk_name_equals = compare_in_depth(x['key_column'], obj['pkNames'])
          if(pk_name_equals):
            final_report['pkName'] = True

          else:
            final_report['pkName'] = False

        if('pkTypes' in obj):
          pk_type_equals = compare_in_depth(x['type'], obj['pkTypes'])
          if(pk_type_equals):
            final_report['pkType'] = True
          else:
            final_report['pkType'] = False

        if('pkHasCompose' in obj):
          if(x['position'] == 2):
            if (obj['pkHasCompose']):
              final_report['pkCompose'] = True


      if(x['key'] == 'FOREIGN KEY'): # Validação da chave primária
        if('fkNames' in obj):
          fk_name_equals = compare_in_depth(x['key_column'], obj['fkNames'])
          if(fk_name_equals):
            final_report['fkName'] = True
          else:
            final_report['fkName'] = False


        if('fkTypes' in obj):
          fk_type_equals = compare_in_depth(x['type'], obj['fkTypes'])
          if(fk_type_equals):
            final_report['fkType'] = True

          else:
            final_report['fkType'] = False


  final.append(final_report)



if (len(final) > 0 ):
  t = ''
  about_table = ''
  about_pkName = ''
  about_pkType = ''
  about_pkCompose = ''
  about_fkName = ''
  about_fkType = ''


  text = f"""
  +---------------------------------------+
  |SchemaCheck -> Final Report            |
  +---------------------------------------+
  """
  print(text)
  for item in final:
    t = 'Table -< ' + item['table_analyzed']

    if(item['tableName']):
      about_table = '✅ The table name is probably correct.'
    else:
      about_table = '❌ The table name is probably wrong, check the sql file.'


    if(item['pkName']):
      about_pkName =  '✅ Primary key column name is probably correct.'
    else:
      about_pkName =  '❌ Primary key column name is probably wrong, check the sql file.'


    if(item['pkType']):
      about_pkType =  '✅ Primary key column type is probably correct.'
    else:
      about_pkType =  '❌ Primary key column type is probably wrong, check the sql file.'


    if(item['pkCompose']):
      about_pkCompose = '✅ Primary key compose is probably correct.'
    else:
      about_pkCompose =  '❌ Primary key compose is probably wrong, check the sql file.'


    if(item['fkName']):
      about_fkName =  '✅ Foreign key column name is probably correct.'
    else:
      about_fkName =  '❌ Foreign key column name is probably wrong, check the sql file.'



    if(item['fkType']):
      about_fkType =  '✅ Foreign key column type is probably correct.'
    else:
      about_fkType =  '❌ Foreign key column type is probably wrong, check the sql file.'

    print(t)
    print('Table: ', about_table)
    print('Primary Key: ', about_pkName)
    print('Type of Primary Key: ', about_pkType)
    print('Primary Key Compose: ',about_pkCompose)
    print('Foreign Key: ', about_fkName)
    print('Type of Foreign Key: ', about_fkType)



