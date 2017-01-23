from forum import database

engine =database.Engine()
con = engine.connect()
con.check_foreign_keys_status()
con.set_foreign_keys_support()
con.check_foreign_keys_status()

engine.create_users_table()
engine.create_users_profile_table()

"""engine.create_users_table()"""

