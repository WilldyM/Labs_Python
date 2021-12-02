import sys
import argparse
import shutil
import os
import subprocess

mp = argparse.ArgumentParser(description="trackmix_Lab2_7")
mp.add_argument('--source', '-s', type=str, required=True help='Путь')
mp.add_argument('--destination', '-d', type=str, default=None, help='Имя выходного файла')
mp.add_argument('--count', '-c', type=int, default=None, help='Кол-во файлов в "нарезке"')
mp.add_argument('--frame', '-f', type=int, default=10, help='Кол-во сек на файл')
mp.add_argument('--log', '-l', action='store_true', help='Нужно ли делать логи')
mp.add_argument('--extended', '-e', action='store_true', help='fade in/fade out')

source = mp.parse_args().source
destination = m.parse_args().destination
if destination is None:
    destination = source
count = mp.parse_args().count
frame = mp.parse_args().frame

log = mp.parse_args().log
