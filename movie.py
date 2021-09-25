import sqlite3

#Creating a database named movies
conn = sqlite3.connect('moviesdb.sqlite')


curs = conn.cursor()
curs.executescript('''

DROP TABLE IF EXISTS MOVIES;
CREATE TABLE MOVIES(
    MOVIE_NAME CHAR(20) NOT NULL,
    LEAD_ACTOR CHAR(20),
    LEAD_ACTRESS CHAR(25),
    YEAR_OF_RELEASE INT(6),
    DIRECTOR CHAR(20)
);
''')
#printing if the table is created successfully
print("Table created successfully........")
#inserting the data in the table movies
curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('RAMBO', 'sharan', 'pooja', 2021, 'YOGRAJ')''')

curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('DRAMA', 'YASH', 'RADHIKA', 2013 , 'YOGRAJ')''')

curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('HUCHAA ', 'SUDHEEP', 'RAGINI', 2018, 'HAMSALEKHA')''')

curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('UGRAM', 'VISHAL', ' SHEELA', 2019, 'RAJKUMAR')''')

curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('VISWASAM', 'AJITH', 'NAYANTHARA', 2014, 'SIVA')''')

curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('THUPPAKKI', 'VIJAY', 'KAJAL AGARWALL', 2017, 'A R MURGADOSS')''')

curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('KABHALI', 'RANJINIKANTH', 'SIMRAN', 2018, 'KARTHIK SUBBURAJ')''')

curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('SETHUATHI', 'VIJAY SETHUPATHI', 'RAMYA NAMBEESAN', 2016, 'ARUN KUMAR')''')

curs.execute('''INSERT INTO MOVIES(
   MOVIE_NAME, LEAD_ACTOR, LEAD_ACTRESS, YEAR_OF_RELEASE, DIRECTOR) VALUES 
   ('KARABHU', 'DRUVA', 'RASHMIKA', 2021, 'CHAKRAVARTHI')''')

 
sql_all = 'SELECT * FROM Movies'
print ("\n{:<30} {:<25}{:<25} {:<25} {:<20}\n".format('MOVIE_NAME','LEAD_ACTOR','LEAD_ACTRESS','YEAR_OF_RELEASE','DIRECTOR'))
for row in curs.execute(sql_all):
    MOVIE_NAME,LEAD_ACTOR,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR=row
    print (" {:<30} {:<25}{:<25} {:<25} {:<20}".format(MOVIE_NAME,LEAD_ACTOR,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR))

actor_search=input("\nEnter the actor name: ")
print('\nMovies starring '+actor_search+' are: \n' )
print("{:<30}{:<25}{:<25}{:<20}\n".format('MOVIE_NAME','LEAD_ACTRESS','YEAR_OF_RELEASE','DIRECTOR'))
for row in curs.execute('SELECT MOVIE_NAME,LEAD_ACTRESS,DIRECTOR,YEAR_OF_RELEASE FROM Movies WHERE LEAD_ACTOR= ?',(actor_search,)):
    MOVIE_NAME,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR=row
    print("{:<30}{:<25}{:<25}{:<20}".format(MOVIE_NAME,LEAD_ACTRESS,YEAR_OF_RELEASE,DIRECTOR))


conn.commit()


conn.close()
