from time import sleep
import sqloperations

def cleardbTables():
    sqloperations.SqlOperation().cleardbTable("english_songs")
    sqloperations.SqlOperation().cleardbTable("hindi_songs")

def repopulatedbTables():
    #Refreshing English Songs
    # fp = open("eng_pls.txt")
    # for u in fp:
    #     sqloperations.SqlOperation().insertData('english_songs',u[:len(u)-1])
    # fp.close()

    #Refreshing Hindi Songs
    fp = open("hin_pls.txt")
    for u in fp:
        sqloperations.SqlOperation().insertData('hindi_songs',u[:len(u)-1])
    fp.close()


if __name__ == "__main__":
    while True:
        # cleardbTables()
        repopulatedbTables()
        print("sleeping....  *_*")
        sleep(60*60*24)
    