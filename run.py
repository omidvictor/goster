import os
from pathlib import Path


forward = ""
with open("hosts.txt", "r") as f:
    for data in f.readlines():
        data = data.replace("\n", "")
        host = data.split(":")[0]
        port = data.split(":")[1]
        forward += f" -L=tcp://:{port}/[{host}]:{port}"


text = f"""[Unit]
Description=GO Simple Tunnel
After=network.target
Wants=network.target

[Service]
Type=simple
Environment="GOST_LOGGER_LEVEL=fatal"
ExecStart=/usr/local/bin/gost{forward}

[Install]
WantedBy=multi-user.target"""

file = "/usr/lib/systemd/system/gost_0.service"


if Path(file).is_file() is True:
    os.remove(file)

with open(file, "w") as f:
    f.writelines(text)
