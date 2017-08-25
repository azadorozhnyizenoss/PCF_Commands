Scripts for grabbing PCF commands output 
========================================
Requirements:
+++++++++++++

PyMQI must be installed.

Queue Manager must have defined the channel of type SVRCONN, Listener type TCP. The Listener must be started. Appropriate AUTHREC  record must be specified for this channel.

Grab information about QUEUES
+++++++++++++++++++++++++++++

Scripts usage:
++++++++++++++

python list_queues.py [-h] -qmgr QUEUE_MANAGER -chl CHANNEL -ip HOST_IP -p PORT -u USER -pswd PASSWORD -o OUTPUT_FILE_NAME

Arguments:
++++++++++

  -qmgr QUEUE_MANAGER, --queue_manager  QUEUE_MANAGER  IBM MQ queue manager

  -chl CHANNEL, --channel CHANNEL  IBM MQ SVRCONN channel name

  -ip HOST_IP,  --host_ip HOST_IP  IBM MQ IP address

  -p PORT, --port PORT Lister Port defined for QUEUE_MANAGER

  -u USER,  --user USER  User name (user must belong to the mqm group)

  -pswd PASSWORD, --password PASSWORD  user password

  -o OUTPUT_FILE_NAME, --output_file_name OUTPUT_FILE_NAME output file name

Grab information about CHANNELS
+++++++++++++++++++++++++++++++

Scripts usage:
++++++++++++++

python list_channels.py [-h] -qmgr QUEUE_MANAGER -chl CHANNEL -ip HOST_IP -p PORT -u USER -pswd PASSWORD -o OUTPUT_FILE_NAME

Arguments:
++++++++++

  -qmgr QUEUE_MANAGER, --queue_manager  QUEUE_MANAGER  IBM MQ queue manager

  -chl CHANNEL, --channel CHANNEL  IBM MQ SVRCONN channel name

  -ip HOST_IP,  --host_ip HOST_IP  IBM MQ IP address

  -p PORT, --port PORT Lister Port defined for QUEUE_MANAGER

  -u USER,  --user USER  User name (user must belong to the mqm group)

  -pswd PASSWORD, --password PASSWORD  user password

  -o OUTPUT_FILE_NAME, --output_file_name OUTPUT_FILE_NAME output file name


CLUSTERING DEPLOYMENT
+++++++++++++++++++++
In case if user has clustering deployment of IBM QM user can run cluster_list_queue_managers.py script

Scripts usage:
++++++++++++++

python cluster_list_queue_managers.py [-h] -qmgr QUEUE_MANAGER -chl CHANNEL -ip HOST_IP -p PORT -u USER -pswd PASSWORD -o OUTPUT_FILE_NAME

Arguments:
++++++++++

  -qmgr QUEUE_MANAGER, --queue_manager  QUEUE_MANAGER  IBM MQ queue manager. Must be Queue manager with full repository

  -chl CHANNEL, --channel CHANNEL  IBM MQ SVRCONN channel name

  -ip HOST_IP,  --host_ip HOST_IP  IBM MQ IP address

  -p PORT, --port PORT Lister Port defined for QUEUE_MANAGER

  -u USER,  --user USER  User name (user must belong to the mqm group)

  -pswd PASSWORD, --password PASSWORD  user password

  -o OUTPUT_FILE_NAME, --output_file_name OUTPUT_FILE_NAME output file name
