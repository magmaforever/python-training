# 把超过指定天数的文件移动的确定目录里

import argparse
import os
import shutil
import time

usage = 'python move_files_over_x_days.py -src [SRC] -dst [DST] -days [DAYS]'
description = 'Move files from src to dst if they are older than a certain number of days. Default is 240 days'

args_parser = argparse.ArgumentParser(usage=usage, description=description)
args_parser.add_argument(
    '-src',
    '--src',
    type=str,
    nargs='?',
    default='.',
    help='(OPTIONAL) Directory where files will be moved from. Defaults to current directory.'
)
args_parser.add_argument(
    '-dst',
    '--dst',
    type=str,
    nargs='?',
    required=True,
    help='(REQUIRED) Directory where files will be moved to.')
args_parser.add_argument(
    '-days',
    '--days',
    type=int,
    nargs='?',
    default=240,
    help='(OPTIONAL) Days value specifies the minimum age of files to be moved. Defaults is 240.'
)
args = args_parser.parse_args()

if args.days < 0:
    args.days = 0

src = args.src
dst = args.dst
days = args.days
now = time.time()

if not os.path.exists(dst):
    os.mkdir(dst)

for f in os.listdir(src):
    if os.stat(f).st_mtime < now - days * 86400:
        if os.path.isfile(f):
            shutil.move(f, dst)
