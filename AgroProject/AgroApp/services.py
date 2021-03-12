# from django.db import  connection
# from contextlib import closing
# from .models import *
#
#
# def get():
#     with closing(connection.cursor()) as cursor:
#         cursor.execute("""select * from News""")
#         result = cursor.fetchall()
#     return result
