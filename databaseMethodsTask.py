from forum import database

engine =database.Engine()
con = engine.connect()
con.check_foreign_keys_status()
con.set_foreign_keys_support()
con.check_foreign_keys_status()

USER1_NICKNAME = 'sqlcoder'
USER1_ID = 1
USER1 = {'public_profile': {'registrationdate': 1362015937,
                            'nickname': USER1_NICKNAME,
                            'signature': 'Well, hello there! Blah ...',
                            'avatar': 'avatar_2.gif'},
         'restricted_profile': {'firstname': 'Mystery', 'lastname': 'Williams',
                                'email': 'jane@imaginecompany.com', 'age': 22,
                                'residence': 'New York', 'gender': 'Female',
                                'picture': 'photo1.jpg', 'website': None,
                                'mobile': None, 'skype': None}
         }
         
#print con.create_message("SQL is not bad","Yes sql is not bad, but why do i need to turn on foreign keys support when running sqlite query eachtime",sender=USER1_NICKNAME)
#print con.modify_message("msg-26","SQL Rules","Anyway let me study how sqlite works",editor="admin")

#print con.create_message("MongoDB is better","Yes it is better . it is NOSQL",sender="troll",replyto="msg-26")


print con.delete_message("msg-27")
