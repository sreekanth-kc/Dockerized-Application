# import os
# import mysql.connector
# from utils.client_secrets import ClientSecrets
#
#
# class ConnectSqlClient(object):
#     @staticmethod
#     def connection_string():
#
#
#         config = {
#             'user': ClientSecrets.get('sql')['username'],
#             'password': ClientSecrets.get('sql')['password'],
#             'host': 'db',
#             'port': '3306',
#             'database': ClientSecrets.get('sql')['database_name']
#         }
#         connection = mysql.connector.connect(**config)
#         return connection
#
#
#
#
#
#
#         # print("User :", user)
#         # print("Password:", password)
#         # print("database_name:", database_name)
#         #
#         # template = 'mysql+pymysql://%s:%s@db/%s'
#         # print("--------------------------------------------------------------------------------")
#         # print(template % (user, password, database_name))
#         # return template % (user, password, database_name)