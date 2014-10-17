#!/bin/sh

echo "apt-get update..."
apt-get update

echo "apt-get install python-pip python-m2crypto supervisor..."
apt-get install python-pip python-m2crypto supervisor

echo "pip install shadowsocks..."
pip install shadowsocks

cat > /etc/shadowsocks.json <<EOF
{
    "server":"0.0.0.0",
    "server_port":7001,
    "local_port":8001,
    "password":"Bug@1874",
    "timeout":600,
    "method":"aes-256-cfb"
}
EOF

cat >> /etc/supervisor/conf.d/shadowsocks.conf <<EOF
[program:shadowsocks]
command=ssserver -c /etc/shadowsocks.json
autorestart=true
user=nobody
EOF

echo "ulimit -n 51200" >> /etc/default/supervisor

echo "start service..."
service supervisor start
supervisorctl reload

echo "success"
exit 0
