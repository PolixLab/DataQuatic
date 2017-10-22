#This make fastest the SSL connection between raspberry and computer

FILE="/etc/ssh/sshd_config"

if ! grep -q "UseDNS" $FILE; then
    echo "Configuring file : $FILE"
    echo "UseDNS=no" >> $FILE
else
    echo "Configuration was already applied."
fi
