import ast

def get_correction_possible_data(path):
  file = open(path, 'r').read().split('\n')
  final_correction = dict()
  final_v2 = []
  correction_data = dict()
  count = 0
  possibles = []

  for item in file:
    i = item.strip()

    if i.startswith('/*'):
      continue
    if i.startswith('*/'):
      continue

    if i.startswith('CREATE TABLE'):
      table_analyzed = i.split('CREATE TABLE ')[1]
      final_correction[table_analyzed] = correction_data
      final_v2.append(correction_data)
      correction_data = dict()
      continue

    if i.startswith('tableNames='):
      text = i
      k = ast.literal_eval(text.split('tableNames=')[1])
      correction_data['tableNames'] = k

    if i.startswith('pkNames='):
      text = i
      k = ast.literal_eval(text.split('pkNames=')[1])
      correction_data['pkNames'] = k

    if i.startswith('pkTypes='):
      text = i
      k = ast.literal_eval(text.split('pkTypes=')[1])
      correction_data['pkTypes'] = k

    if i.startswith('pkHasCompose='):
      text = i
      k = ast.literal_eval(text.split('pkHasCompose=')[1])
      correction_data['pkHasCompose'] = k

    if i.startswith('fkNames='):
      text = i
      k = ast.literal_eval(text.split('fkNames=')[1])
      correction_data['fkNames'] = k

    if i.startswith('fkTypes='):
      text = i
      k = ast.literal_eval(text.split('fkTypes=')[1])
      correction_data['fkTypes'] = k

  return final_correction

