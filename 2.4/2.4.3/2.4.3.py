import psutil, sqlite3, datetime

con = sqlite3.connect("metanit.db")
cursor = con.cursor()
cursor.execute("""
    CREATE TABLE if not exists monitoring
    (
        monitoring_ID INTEGER PRIMARY Key AUTOINCREMENT,
        CPU_load INTEGER NOT NULL,
        used_RAM INTEGER NOT NULL,
        disk_load INTEGER NOT NULL,
        monitoring_time TEXT NOT NULL
    );
""")

class Monitor:
    def __init__(self):
        pass

    def monitoring(self):
        monitoring_info = [psutil.cpu_percent(interval=1), round(psutil.virtual_memory()[3]/pow(10, 9), 2), psutil.disk_usage('/')[3], datetime.datetime.today().strftime("%d.%m.%Y:%H.%M.%S")]
        cursor.executemany("INSERT INTO monitoring (CPU_load, used_RAM, disk_load, monitoring_time) VALUES (?, ?, ?, ?)", (monitoring_info,))

    def display_whole_monitoring(self):
        cursor.execute("SELECT * FROM monitoring")
        print(f"                                                     monitoring\n"
              f"------------------------------------------------------------------------------------------------------------------------")
        for monitoring in cursor.fetchall():
            print(f"monitoring_ID: {monitoring[0]} - CPU_load: {monitoring[1]}% - used_RAM: {monitoring[2]}GB - disk_load: {monitoring[3]}% - monitoring_time: {monitoring[4]}")
        print("------------------------------------------------------------------------------------------------------------------------")

cursor.close()