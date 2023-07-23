import json

def create_nation(userid, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12,
                  c13, c14, c15, c16):
  economic_freedom = 50
  civil_liberties = 50
  political_freedom = 50
  gdp = 5000000
  communism = 0
  capitalism = 0
  socialism = 0
  authoritarianism = 0
  crime = 40
  youth_crime = 15
  nationalism = 50
  drugs = 15
  social_welfare = 30
  technological_advancement = 20
  defence = 30
  pacifism = 30
  international_aggression = 15
  international_relations = 30
  environment = 50
  eco_friendly = 50
  justice = 30
  corruption = 15
  social_conservatism = 10
  education = 30
  wealth_gap = 20
  taxation = 25
  culture = 20
  immigration = 20
  healthcare = 20
  religion = 30
  police = 30
  secularism = 0
  happiness = 40
  #policies
  democratic = False
  economy = "msgnotfnd"
  cultured = False
  monarchy = False
  athiest = False
  #handling questions
  if c1 == "1":
    democratic = True
    political_freedom += 15
  elif c1 == "2":
    police += 15
    political_freedom -= 20
    crime += 5
    authoritarianism += 15
  elif c1 == "3":
    monarchy = True
    political_freedom -= 20
    religion += 15
    taxation += 10
    social_conservatism += 10
  elif c1 == "4":
    corruption += 30
    economic_freedom += 10
    capitalism += 15
    wealth_gap += 15
    social_welfare -= 5
  if c2 == "1":
    capitalism += 25
    drugs += 10
    corruption += 10
    economic_freedom += 15
  elif c2 == "2":
    socialism += 25
    capitalism -= 5
    economic_freedom -= 5
  elif c2 == "3":
    communism += 25
    capitalism -= 10
    economic_freedom -= 10
    healthcare += 5
    civil_liberties -= 10
  elif c2 == "4":
    capitalism += 10
    socialism += 15
    economic_freedom += 5
  if c3 == "1":
    social_welfare -= 15
    healthcare -= 10
    drugs += 10
    crime += 10
    youth_crime += 5
    civil_liberties -= 10
  elif c3 == "2":
    healthcare += 5
    social_welfare += 10
    drugs += 5
  elif c3 == "3":
    healthcare += 10
    social_welfare += 15
    taxation += 10
  elif c3 == "4":
    social_welfare += 5
    corruption += 5
    gdp += 50000
    social_conservatism += 5
    wealth_gap += 5
  if c4 == "1":
    technological_advancement += 20
    gdp += 25000
    education += 5
    healthcare += 10
    secularism += 5
    environment -= 5
    socialism += 5
    eco_friendly -= 10
    defence += 10
  elif c4 == "2":
    technological_advancement += 5
    healthcare += 5
    environment -= 5
  elif c4 == "3":
    technological_advancement -= 15
    healthcare -= 5
    culture += 10
    social_conservatism += 5
  elif c4 == "4":
    gdp += 50000
    technological_advancement += 10
    capitalism += 10
    wealth_gap += 5
  if c5 == "1":
    international_relations += 15
    happiness += 10
    immigration += 10
    environment += 5
  elif c5 == "2":
    international_relations += 10
    international_aggression += 5
    defence += 10
  elif c5 == "3":
    international_relations += 5
    pacifism += 20
    drugs += 10
  elif c5 == "4":
    international_aggression += 10
    defence += 15
    authoritarianism += 10
    happiness -= 10
    immigration -= 10
  if c6 == "1":
    environment += 10
    eco_friendly += 25
    drugs += 10
    youth_crime += 10
    taxation += 10
    happiness -= 5
  elif c6 == "2":
    environment += 10
    eco_friendly += 15
    happiness += 10
    taxation += 5
  elif c6 == "3":
    capitalism += 10
    environment -= 15
    eco_friendly -= 10
    corruption += 5
    economic_freedom += 15
  elif c6 == "4":
    civil_liberties += 5
    environment += 5
    eco_friendly += 5
    socialism += 10
  if c7 == "1":
    happiness += 10
    police += 10
    crime -= 15
    drugs -= 10
    civil_liberties += 15
    youth_crime -= 5
    social_conservatism -= 10
    justice += 20
    taxation += 5
  elif c7 == "2":
    drugs -= 5
    youth_crime -= 10
    justice += 5
    crime -= 10
    police += 20
    happiness -= 10
    authoritarianism += 15
    political_freedom -= 5
    civil_liberties -= 10
  elif c7 == "3":
    social_conservatism += 20
    religion += 10
    police += 10
    crime += 10
    youth_crime += 10
    drugs += 10
    happiness -= 10
  elif c7 == "4":
    social_welfare += 5
    socialism += 15
    communism += 10
    justice += 10
    police += 15
    crime -= 5
    youth_crime += 5
    social_conservatism -= 10
  if c8 == "1":
    civil_liberties += 25
    socialism += 5
    political_freedom += 5
    economic_freedom += 5
    social_welfare += 5
    religion += 10
    taxation += 5
  elif c8 == "2":
    civil_liberties += 10
    authoritarianism += 5
    gdp += 50000
  elif c8 == "3":
    civil_liberties -= 15
    authoritarianism += 20
    nationalism -= 10
    happiness -= 10
    crime += 10
    police += 10
    social_welfare -= 5
  elif c8 == "4":
    civil_liberties += 5
    religion += 10
    nationalism += 5
  if c9 == "1":
    education += 25
    wealth_gap -= 10
    happiness += 10
    communism += 10
    socialism += 5
  elif c9 == "2":
    education += 10
    wealth_gap -= 5
  elif c9 == "3":
    education -= 15
    social_conservatism += 10
    authoritarianism += 10
  elif c9 == "4":
    authoritarianism += 5
    education += 10
    nationalism += 10
  if c10 == "1":
    taxation += 20
    economic_freedom -= 10
    social_conservatism -= 10
    capitalism -= 10
    wealth_gap -= 15
  elif c10 == "2":
    capitalism += 10
    wealth_gap -= 5
    economic_freedom += 10
    taxation += 5
  elif c10 == "3":
    socialism += 10
    communism += 9
    taxation += 10
    happiness += 10
    crime -= 10
    economic_freedom += 5
    civil_liberties += 10
  elif c10 == "4":
    capitalism += 10
    wealth_gap += 10
    youth_crime += 5
    healthcare += 5
    happiness += 10
    nationalism += 5
  if c11 == "1":
    pacifism += 10
    defence += 5
    international_aggression -= 10
    international_relations += 10
  elif c11 == "2":
    pacifism -= 10
    defence += 20
    international_aggression += 15
    international_relations += 5
  elif c11 == "3":
    pacifism += 15
    international_relations += 15
  elif c11 == "4":
    capitalism += 15
    international_aggression += 5
    international_relations += 15
    taxation -= 10
  if c12 == "1":
    cultured = True
    culture += 15
    happiness += 10
    social_conservatism -= 5
  elif c12 == "2":
    culture += 10
    religion += 5
  elif c12 == "3":
    culture -= 10
    nationalism += 10
  elif c12 == "4":
    culture += 10
    corruption += 15
    authoritarianism += 10
  if c13 == "1":
    immigration += 20
    happiness += 5
    culture += 10
  elif c13 == "2":
    immigration += 10
    authoritarianism += 5
    police += 10
  elif c13 == "3":
    immigration -= 15
    nationalism += 15
    healthcare += 5
  elif c13 == "4":
    immigration += 5
  if c14 == "1":
    defence += 15
  elif c14 == "2":
    defence += 20
    international_aggression += 10
  elif c14 == "3":
    defence -= 15
    pacifism += 15
  elif c14 == "4":
    defence += 5
    international_relations += 10
    political_freedom -= 5
    capitalism += 10
    socialism += 5
  if c15 == "1":
    healthcare += 25
    social_welfare += 10
    civil_liberties += 10
  elif c15 == "2":
    healthcare += 10
    social_welfare += 5
  elif c15 == "3":
    healthcare -= 10
    civil_liberties -= 10
    social_welfare -= 5
    gdp += 100000
  elif c15 == "4":
    healthcare += 5
    social_welfare += 5
    capitalism += 5
    gdp += 75000
  if c16 == "1":
    secularism += 25
    religion -= 10
    political_freedom -= 10
  elif c16 == "2":
    secularism -= 5
    religion += 5
  elif c16 == "3":
    religion += 15
    secularism -= 15
  elif c16 == "4":
    happiness += 5
    culture += 10
    religion += 10
    secularism += 10
  
  #evaluate economy
  economies = {
    'communism': communism,
    'capitalism': capitalism,
    'socialism': socialism
  }
  largest_value = max(economies.values())
  largest_variable = [
    var_name for var_name, value in economies.items() if value == largest_value
  ][0]
  economy = largest_variable
  if economy == "capitalism" and gdp > 5090000:
    type = "Powerhouse Economy"
  elif economic_freedom > 60:
    type = "Drug empire"
  else:
    type = "Undefined nation"
  e = "The " + type + " of " + userid
  user_data = {
    "type": type,
    "economic_freedom": economic_freedom,
    "civil_liberties": civil_liberties,
    "political_freedom": political_freedom,
    "gdp": gdp,
    "economy": economy,
    "communism": communism,
    "capitalism": capitalism,
    "socialism": socialism,
    "authoritarianism": authoritarianism,
    "crime": crime,
    "youth_crime": youth_crime,
    "nationalism": nationalism,
    "drugs": drugs,
    "social_welfare": social_welfare,
    "technological_advancement": technological_advancement,
    "defence": defence,
    "pacifism": pacifism,
    "international_aggression": international_aggression,
    "international_relations": international_relations,
    "envirnoment": environment,
    "eco_friendly": eco_friendly,
    "justice": justice,
    "corruption": corruption,
    "social_conservatism": social_conservatism,
    "education": education,
    "wealth_gap": wealth_gap,
    "taxation": taxation,
    "culture": culture,
    "immigration": immigration,
    "healthcare": healthcare,
    "religion": religion,
    "police": police,
    "secularism": secularism,
    "happiness": happiness,
    "democratic": democratic,
    "cultured": cultured,
    "monarchy": monarchy,
    "athiest": athiest
  }
  file_path = "nation_data.json"
  with open(file_path, "r") as json_file:
    users_data = json.load(json_file)
  users_data[userid] = user_data
  json_data = json.dumps(users_data)
  with open(file_path, "w") as json_file:
    json_file.write(json_data)

  return e
