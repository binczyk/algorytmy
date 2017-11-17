import random

from Tables.ChainedTable import ChainedTable
from Tables.HashTable import HashTable
from Tables.SortedTable import SortedTable
from Tables.Table import Table
import time

list = []
find = []

for _ in range(1024):
    list.append(random.randrange(999999))

for _ in range(64):
    list.append(random.randrange(999999))

print('Table')
t = Table()

start = time.perf_counter()
for i in list:
    t.add(i)
end = time.perf_counter()

print('Adding time: ', end - start)

start = time.perf_counter()
for i in find:
    t.exists(i)
end = time.perf_counter()

print('Checking if exists time: ', end - start)

start = time.perf_counter()
for i in find:
    t.remove(i)
end = time.perf_counter()

print('Removing time: ', end - start)

print('\nSortedTable')
t = SortedTable()
start = time.perf_counter()
for i in list:
    t.add(i)
end = time.perf_counter()

print('Adding time: ', end - start)

start = time.perf_counter()
for i in find:
    t.exists(i)
end = time.perf_counter()

print('Checking if exists time: ', end - start)

start = time.perf_counter()
for i in find:
    t.remove(i)
end = time.perf_counter()

print('Removing time: ', end - start)

print('\nHashTable')
t = HashTable(1024)
start = time.perf_counter()
for i in list:
    t.add(i)
end = time.perf_counter()

print('Adding time: ', end - start)

start = time.perf_counter()
for i in find:
    t.exists(i)
end = time.perf_counter()

print('Checking if exists time: ', end - start)

start = time.perf_counter()
for i in find:
    t.remove(i)
end = time.perf_counter()

print('Removing time: ', end - start)

print('\nChainedTable')
t = ChainedTable(1024)
start = time.perf_counter()
for i in list:
    t.add(i)
end = time.perf_counter()

print('Adding time: ', end - start)

start = time.perf_counter()
for i in find:
    t.exists(i)
end = time.perf_counter()

print('Checking if exists time: ', end - start)

start = time.perf_counter()
for i in find:
    t.remove(i)
end = time.perf_counter()

print('Removing time: ', end - start)
