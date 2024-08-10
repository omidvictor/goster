sudo apt install python3

rm -r /root/gost

git clone "https://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@github.com/omidvictor/goster.git" /root/gost/

wget -O /tmp/gost.tar.gz https://github.com/go-gost/gost/releases/download/v3.0.0-nightly.20240806/gost_3.0.0-nightly.20240806_linux_amd64.tar.gz
tar -xvzf /tmp/gost.tar.gz -C /usr/local/bin/
chmod +x /usr/local/bin/gost

pkill -9 gost
cd /root/gost
python3 run.py

sudo systemctl enable "gost_0.service"
sudo systemctl start "gost_0.service"
sudo systemctl daemon-reload
sudo systemctl restart "gost_0.service"

ps -ef | grep gost
