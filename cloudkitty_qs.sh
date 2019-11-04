mysql << EOF
DROP DATABASE cloudkitty;
CREATE DATABASE cloudkitty;
GRANT ALL PRIVILEGES ON cloudkitty.* TO 'cloudkitty'@'localhost' IDENTIFIED BY 'cloudkitty';
EOF

mysql << EOF
GRANT ALL PRIVILEGES ON cloudkitty.* TO 'cloudkitty'@'%' IDENTIFIED BY 'cloudkitty';
EOF

cloudkitty-storage-init

cloudkitty-dbsync upgrade
cloudkitty module enable hashmap 



x=`cloudkitty hashmap service create ip.floating | grep ip.floating | awk '{print $4}' `

cloudkitty hashmap mapping create 1 \
 --service-id $x \
 -t flat



 y=`cloudkitty hashmap service create instance | grep instance | awk '{print $4}'`

z=`cloudkitty hashmap field create $y flavor_id | grep flavor_id | awk '{print $4}'`

 cloudkitty hashmap mapping create 1 \
 --field-id $z \
 --value 1 \
 -t flat


x=`cloudkitty hashmap service create volume.size | grep volume.size | awk '{print $4}' `
y=`cloudkitty hashmap mapping create 5 --service-id $x
