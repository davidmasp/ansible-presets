#!/usr/bin/env python
# coding=utf-8

import os
import subprocess
from dotenv import load_dotenv
from helpers import *

load_dotenv()
today_str = today()

## set up discord bot details
webhook_1 = os.getenv("WH1")
webhook_2 = os.getenv("WH2")
base_url = "https://discord.com/api/webhooks/{}/{}".format(webhook_1, webhook_2)

## small test
## send_webhook(base_url, "test", "BackUp Villager")

## set up rsync details
remote_folder = os.getenv("REMOTE_FOLDER")
remote_user = os.getenv("REMOTE_USER")
remote_ip = os.getenv("REMOTE_IP")
cmd_tmp = "{}@{}:{}".format(remote_user, remote_ip, remote_folder)

## other params
destination_folder = "./world_rsync2"
params_compress = True
archive_type = "zip"
max_old_bu = 3

if params_compress:
    td_st = today()
    bn = os.path.basename(os.path.normpath(destination_folder))
    archive_name = "{}_{}.{}".format(td_st, bn, archive_type)

## DOWNLOAD PROCESS
array_cmd = ["rsync", "-chavzP", "--stats", cmd_tmp, destination_folder]
#array_cmd = ["ls","-l"]
return_cmd = subprocess.run(array_cmd, capture_output=True)
return_cmd.check_returncode()
rcode = return_cmd.returncode

## COMPRESS PROCESS
if params_compress:
    compress_cmd = ["zip", "-r", archive_name, destination_folder]
    return_cmd3 = subprocess.run(compress_cmd, capture_output=True)
    return_cmd3.check_returncode()
    rcode3 = return_cmd.returncode
    array_cmd2 = ["du", "-sh", archive_name]
else:
    rcode3 = "NULL"
    array_cmd2 = ["du", "-sh", destination_folder]

## SIZE PROCESS
return_cmd2 = subprocess.run(array_cmd2, capture_output=True)
return_cmd2.check_returncode()
rcode2 = return_cmd.returncode

size_stdo = return_cmd2.stdout.decode("utf-8").strip().split("\t")
folder_size = size_stdo[0]

## RM old backups

## LOG run
log_msg = "Backup run succesful, some info below\n"
data_to_embed = [
        {
            "title" : ":world_map: World D Backup {}".format(today_str),
            "fields" : [
                {"name" : "Total size",
                "value": folder_size,
                "inline": False},
                {"name" : "rsync",
                "value": rcode,
                "inline": True},
                {"name" : "zip",
                "value": rcode3,
                "inline": True},
                {"name" : "du",
                "value": rcode2,
                "inline": True}
            ]
        }
    ]

send_webhook(base_url, log_msg, "BackUp Villager", embeds = data_to_embed)
