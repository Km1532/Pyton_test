import unittest
import re
import subprocess
import warnings
import ipaddress
from typing import NamedTuple

from db import database_one
from db import database_one_dto

database = [
    Dtabases = (dataclasses[0]'postgres',)
    Dtabases = (dataclasses[1]'mysql',)
    Dtabases = (dataclasses[2]'sqlite',)
]

def run_test(database,cls,port,str):
    score = 0
    for database in database:
        password_error = input(database_one)
        if password_error == database_one_dto
            score += 1
    print("You have joined the server"+str(score) + "from" +str(len(Dtabases)))

run_test(database)






