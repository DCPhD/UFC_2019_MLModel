
import urllib.request
import bs4 as bs
import pandas as pd


pd.set_option("display.width", 2000)
pd.set_option("display.max_columns", 80)
pd.set_option("display.max_rows", 2000000)


## UFC FIGHT NIGHT- KOREAN ZOMBIE VS FRANKIE EDGAR ##
# read in source webpage
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/74fefd43f073cd2f').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/74fefd43f073cd2f', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNKZ = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNKZ)


## UFC 245 ##

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/4565d435005319c0').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/4565d435005319c0', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_245 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_245)


## UFC FIGHT NIGHT OVEREEM ROZENSTRUIK

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/b09890ba7ce1d1e2').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/b09890ba7ce1d1e2', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNUBER = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNUBER)


## UFC FIGHT NIGHT JACARE BLACHOWITZ

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/81ca2c245b19b3c5').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/81ca2c245b19b3c5', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNJACARE = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNJACARE)



## UFC FIGHT NIGHT ZABIT KATTAR

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/8d5daf67983b65ba').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/8d5daf67983b65ba', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNZABIT = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNZABIT)


## UFC 244

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/fd87b1bbfcde9d5e').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/fd87b1bbfcde9d5e', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_244 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_244)


## UFC FIGHT NIGHT ASKREN MAIA

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/df05aa15b2d66f57').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/df05aa15b2d66f57', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNASKREN = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNASKREN)


## UFC FIGHT NIGHT REYES WEIDMAN

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/3ae10ac4df3df05c').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/3ae10ac4df3df05c', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNWEIDMAN = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNWEIDMAN)



## UFC FIGHT NIGHT JOANNA WATERSON

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/0941df56f6ac954b').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/0941df56f6ac954b', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNJOANNA = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNJOANNA)


## UFC 243

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/3cf68c1d17f66af7').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/3cf68c1d17f66af7', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_243 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_243)



## UFC FIGHT NIGHT HERMANSON CANNONIER

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/1bf49bf829964144').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/1bf49bf829964144', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNHERM = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNHERM)

## UFC FIGHT NIGHT RODRIGUEZ STEPHENS

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/94a5aaf573f780ad').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/94a5aaf573f780ad', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNSTEPHENS = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNSTEPHENS)



## UFC FIGHT NIGHT COWBOY GAETHJE

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/4834ff149dc9542a').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/4834ff149dc9542a', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNCOWBOY = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNCOWBOY)


## UFC 242

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/a79bfbc01b2264d6').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/a79bfbc01b2264d6', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_242 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_242)



## UFC FIGHT NIGHT ANDRADE ZHANG

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/2c104b7e59a72629').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/2c104b7e59a72629', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNZHANG = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNZHANG)



## UFC 241

source = urllib.request.urlopen('http://www.ufcstats.com/event-details/70167689d6a01793').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/70167689d6a01793', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_241 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_241)



## UFC FIGHT NIGHT SHEVCHENKO CARMOUCHE 2
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/e5d03e4d966126bd').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/e5d03e4d966126bd', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNVAL = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNVAL)


## UFC FIGHT NIGHT COLBY LAWLER
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/03da33a102d9a45f').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/03da33a102d9a45f', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_FNCOLBY = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_FNCOLBY)


## UFC 240
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/abcf7e55a0a9ed89').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/abcf7e55a0a9ed89', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_240 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_240)



## UFC FIGHT NIGHT DOS ANJOS EDWARDS
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/9e0f28d1f639ad73').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/9e0f28d1f639ad73', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_DOS = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_DOS)



## UFC FIGHT NIGHT DE RANDAMIE LADD
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/2f8f3c69522db931').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/2f8f3c69522db931', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_LADD = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_LADD)



## UFC 239
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/6c9383ffab2725a5').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/6c9383ffab2725a5', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_239 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_239)



## UFC FIGHT NIGHT NGANNOU DOS SANTOS
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/c0c1bc0766df4c00').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/c0c1bc0766df4c00', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_NGANNO = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_NGANNO)

## UFC FIGHT NIGHT MOICANO KOREAN ZOMBIE
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/b16a7e6a627e9789').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/b16a7e6a627e9789', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_ZOMBIE = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_ZOMBIE)



## UFC 238
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/e31502e3f79d00c5').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/e31502e3f79d00c5', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_238 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_238)


## UFC GUSTAFFSON SMITH
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/cbc071cb20ea59c7').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/cbc071cb20ea59c7', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_GUS = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_GUS)


## UFC DOS SANTOS LEE
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/6b8f28da9a483049').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/6b8f28da9a483049', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_LEE = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_LEE)

## UFC 237
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/9de7c97e1c0d7927').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/9de7c97e1c0d7927', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_237 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_237)



## UFC IAQUINTA COWBOY
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/351264d11286d09a').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/351264d11286d09a', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_AL = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_AL)


## UFC JACARE HERMANNSON
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/c912f676692c353a').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/c912f676692c353a', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_JAC = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_JAC)


## UFC OVEREEM OLEINIK
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/7dcf06c1967801c1').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/7dcf06c1967801c1', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_OVEREEM = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_OVEREEM)


## UFC 236
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/b0550072e5f0afa7').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/b0550072e5f0afa7', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_236 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_236)

## UFC BARBOZA GATJGE
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/9649d75defe0dedb').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/9649d75defe0dedb', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_BARB = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_BARB)


## UFC THOMPSON PETTIS
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/487c170da059857d').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/487c170da059857d', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_PETTIS = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_PETTIS)


## UFC MASVIDAL TILL
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/80eacd4da0617c57').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/80eacd4da0617c57', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_TILL = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_TILL)


## UFC LEWIS DOS SANTOS
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/e96d8538d3f9d0ed').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/e96d8538d3f9d0ed', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_LEWIS = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_LEWIS)


# UFC 235
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/2d5fbe2103f97053').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/2d5fbe2103f97053', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_235 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_235)


# UFC BLACHOWICZ SANTOS
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/6546af7ab545b90c').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/6546af7ab545b90c', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_SANTOS = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_SANTOS)

# UFC NGANNOU VELASQUEZ
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/a7a79b8efbceaaac').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/a7a79b8efbceaaac', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_CAIN = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_CAIN)


# UFC 234
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/b5882371e2a3900d').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/b5882371e2a3900d', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_234 = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_234)


# UFC ASSUNCAO MORAES
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/84283233ec42be5f').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/84283233ec42be5f', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_ASS = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_ASS)



# UFC CEJUDO DILLASHAW
source = urllib.request.urlopen('http://www.ufcstats.com/event-details/d4da8995fc91e7ef').read()

# create BS document
soup = bs.BeautifulSoup(source, features="lxml")

# get all text from page
table = soup.table
table_rows = table.find_all('tr')


# iterate through rows, print those with 'table data' type
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    #print(row)

# create dataframe
dfs = pd.read_html('http://www.ufcstats.com/event-details/d4da8995fc91e7ef', header=0)
for df in dfs:
    df = df.drop('W/L', 1)
    break

# split winner/loser names, W/L strikes, W/L Td attempts, W/L sub attempts
dff = pd.DataFrame(df.Fighter.str.split('  ',1).tolist(), columns = ['Winner','Loser'])
dfstrike = pd.DataFrame(df.Str.str.split('  ',1).tolist(), columns = ['Winner_Str','Loser_Str'])
dftd = pd.DataFrame(df.Td.str.split('  ',1).tolist(), columns = ['Winner_Td','Loser_Td'])
dfsub = pd.DataFrame(df.Sub.str.split('  ',1).tolist(), columns = ['Winner_Sub_Attempt','Loser_Sub_Attempt'])

# add columns in from original df
dfother = df[['Weight class', 'Method', 'Time','Round']]
#print(dfother.head())


#combine all dfs as new comprehensive df.  axis=1 will stack dfs to the right of each other
data_frames_CEJUDO = pd.concat([dff, dfstrike, dftd, dfsub, dfother], axis=1)
#print(data_frames_CEJUDO)

full_dataset = pd.concat([data_frames_FNKZ, data_frames_245, data_frames_FNUBER, data_frames_FNJACARE,
                          data_frames_FNZABIT, data_frames_244, data_frames_FNASKREN, data_frames_FNWEIDMAN,
                          data_frames_FNJOANNA, data_frames_243, data_frames_FNHERM, data_frames_FNSTEPHENS,
                          data_frames_FNCOWBOY, data_frames_242, data_frames_FNZHANG, data_frames_241,
                          data_frames_FNVAL, data_frames_FNCOLBY, data_frames_240, data_frames_DOS,
                          data_frames_LADD, data_frames_239, data_frames_NGANNO, data_frames_ZOMBIE,
                          data_frames_238, data_frames_GUS, data_frames_LEE, data_frames_237, data_frames_AL,
                          data_frames_JAC, data_frames_OVEREEM, data_frames_236, data_frames_BARB, data_frames_PETTIS,
                          data_frames_TILL, data_frames_LEWIS, data_frames_235, data_frames_SANTOS, data_frames_CAIN,
                          data_frames_234, data_frames_ASS, data_frames_CEJUDO], axis=0)

export_csv = full_dataset.to_csv("UFC2018fights.csv")
print(export_csv)

