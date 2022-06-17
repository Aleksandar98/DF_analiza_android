
import sqlite3
from sqlite3 import Error
import subprocess
from pick import pick

if __name__ == '__main__':

    title = 'Izaberite koje informacije zelite da izvucete iz telefona: '
    options = ['Koordinate sa kojih su poruke slate', 'Na kojim lokacijama se nalazio vlasnik i kada', 'Poslednja interakcija korisnika sa Facebook aplikacijom','Kada se poslednji put korisnik ulogovao na Facebook','Newsfeed data', 'Netaknut imenik']
    option, index = pick(options, title)
    print(option)

    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by the db_file
        :param db_file: database file
        :return: Connection object or None
        """
        conn = None
        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        return conn


    def select_last_fetch_time(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM preferences WHERE key = '/config/gk/last_fetch_time_ms'")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def select_last_login_time(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM preferences WHERE key = '/fb_android/last_login_time'")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def select_all_nearby_tiles(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM nearby_tiles")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def select_all_home_stories(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT fetched_at,story_type,cache_file_path FROM home_stories")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def select_all_message_coordinates(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM messages")

        rows = cur.fetchall()

        for row in rows:
            print(row)

    def select_all_imenik(conn):
        """
        Query all rows in the tasks table
        :param conn: the Connection object
        :return:
        """
        cur = conn.cursor()
        cur.execute("SELECT * FROM phonebookcontact")

        rows = cur.fetchall()

        for row in rows:
            print(row)


    def koordinate_poruka():
        procId = subprocess.Popen("script.BAT", shell=True, stdin=subprocess.PIPE)
        str2 = "cp /data/data/com.facebook.katana/databases/threads_db2 /storage/self/primary\nexit\ndir"
        my_str_as_bytes = str.encode(str2)
        procId.communicate(my_str_as_bytes)
        procId.wait(100)
        procId2 = subprocess.Popen("pullThreadsDb2.BAT", shell=True, stdin=subprocess.PIPE)
        procId2.wait(1000)
        database = r"C:\Users\Aleksandar\Desktop\ssd\threads_db2"
        conn = create_connection(database)

        with conn:
            select_all_message_coordinates(conn)

    def lokacije():
        procId = subprocess.Popen("script.BAT", shell=True, stdin=subprocess.PIPE)
        str2 = "cp /data/data/com.facebook.katana/databases/nearbytiles_db /storage/self/primary\nexit\ndir"
        my_str_as_bytes = str.encode(str2)
        procId.communicate(my_str_as_bytes)
        procId.wait(100)
        procId2 = subprocess.Popen("pullNearbytiles.BAT", shell=True, stdin=subprocess.PIPE)
        procId2.wait(1000)
        database = r"C:\Users\Aleksandar\Desktop\ssd\nearbytiles_db"
        conn = create_connection(database)

        with conn:
            select_all_nearby_tiles(conn)

    def interakcija_sa_facebookom():
        procId = subprocess.Popen("script.BAT", shell=True, stdin=subprocess.PIPE)
        str2 = "cp /data/data/com.facebook.katana/databases/prefs_db /storage/self/primary\nexit\ndir"
        my_str_as_bytes = str.encode(str2)
        procId.communicate(my_str_as_bytes)
        procId.wait(100)
        procId2 = subprocess.Popen("pullPrefs.BAT", shell=True, stdin=subprocess.PIPE)
        procId2.wait(1000)
        database = r"C:\Users\Aleksandar\Desktop\ssd\prefs_db"
        conn = create_connection(database)

        with conn:
            select_last_fetch_time(conn)

    def login_time():
        procId = subprocess.Popen("script.BAT", shell=True, stdin=subprocess.PIPE)
        str2 = "cp /data/data/com.facebook.katana/databases/prefs_db /storage/self/primary\nexit\ndir"
        my_str_as_bytes = str.encode(str2)
        procId.communicate(my_str_as_bytes)
        procId.wait(100)
        procId2 = subprocess.Popen("pullPrefs.BAT", shell=True, stdin=subprocess.PIPE)
        procId2.wait(1000)
        database = r"C:\Users\Aleksandar\Desktop\ssd\prefs_db"
        conn = create_connection(database)

        with conn:
            select_last_login_time(conn)

    def newsfeed_data():
        procId = subprocess.Popen("script.BAT", shell=True, stdin=subprocess.PIPE)
        str2 = "cp /data/data/com.facebook.katana/databases/newsfeed_db /storage/self/primary\nexit\ndir"
        my_str_as_bytes = str.encode(str2)
        procId.communicate(my_str_as_bytes)
        procId.wait(100)
        procId2 = subprocess.Popen("bullNewsFeed.BAT", shell=True, stdin=subprocess.PIPE)
        procId2.wait(1000)
        database = r"C:\Users\Aleksandar\Desktop\ssd\newsfeed_db"
        conn = create_connection(database)

        with conn:
            select_all_home_stories(conn)

    def netaknut_imenik():
        procId = subprocess.Popen("script.BAT", shell=True, stdin=subprocess.PIPE)
        str2 = "cp /data/data/com.viber.voip/databases/viber_data /storage/self/primary\nexit\ndir"
        my_str_as_bytes = str.encode(str2)
        procId.communicate(my_str_as_bytes)
        procId.wait(100)
        procId2 = subprocess.Popen("pullViberData.BAT", shell=True, stdin=subprocess.PIPE)
        procId2.wait(1000)
        # database = r"C:\Users\Aleksandar\Desktop\ssd\prefs_db"
        database = r"C:\Users\Aleksandar\Desktop\ssd\viber_data"
        conn = create_connection(database)

        with conn:
            select_all_imenik(conn)

    match index :
        case 0:koordinate_poruka()
        case 1:lokacije()
        case 2:interakcija_sa_facebookom()
        case 3:login_time()
        case 4:newsfeed_data()
        case 5:netaknut_imenik()

