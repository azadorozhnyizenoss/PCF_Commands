"""
list channels script
"""
from pymqi import QueueManager, CMQCFC, PCFExecute, MQMIError, cd
import argparse
import logging


logger = logging.getLogger('PCF__channels_collect')


def run_pcf_command(queue_manager, channel, host_ip, port, user_name, password):
    """
    :param queue_manager:
    :param channel:
    :param host_ip:
    :param port:
    :param user_name:
    :param password:
    :return:
    """
    conn_info = "%s(%s)" % (host_ip, port)
    qmgr = QueueManager(None)
    args = {CMQCFC.MQCACH_CHANNEL_NAME: '*',
            CMQCFC.MQIACF_CHANNEL_ATTRS: CMQCFC.MQIACF_ALL}

    try:
        qmgr.connectTCPClient(queue_manager, cd(), channel, conn_info, user_name, password)
        pcf = PCFExecute(qmgr)
        response = pcf.MQCMD_INQUIRE_CHANNEL(args)
    except MQMIError as e:
        logger.error("Could not read information about channels")
        logger.error(e.errorAsString())
        logger.error(e.reason)
    else:
        for channel_info in response:
            logger.info("CHANNEL INFO")
            logger.info("MQCACH_CHANNEL_NAME: " + (channel_info.get(CMQCFC.MQCACH_CHANNEL_NAME,
                                                                    "UNKNOWN")).strip())
            logger.info("MQCACH_CONNECTION_NAME: " +
                        (channel_info.get(CMQCFC.MQCACH_CONNECTION_NAME,
                                          "UNKNOWN")).strip())
            logger.info("MQCACH_DESC: " + channel_info.get(CMQCFC.MQCACH_DESC, "UNKNOWN"))
            logger.info("MQIACH_CHANNEL_TYPE: " + str(channel_info.get(CMQCFC.MQIACH_CHANNEL_TYPE,
                                                                       "UNKNOWN")).strip())
            logger.info("\n")
        qmgr.disconnect()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-qmgr", "--queue_manager", help="IBM MQ queue manager", required=True)
    parser.add_argument("-chl", "--channel", help="IBM MQ svrconn channel", required=True)
    parser.add_argument("-ip", "--host_ip", help="IBM MQ IP address", required=True)
    parser.add_argument("-p", "--port", help="IBM MQ port", required=True)
    parser.add_argument("-u", "--user", help="user name", required=True)
    parser.add_argument("-pswd", "--password", help="password", required=True)
    parser.add_argument("-o", "--output_file_name", help="output file name", required=True)
    args = parser.parse_args()
    file_hndlr = logging.FileHandler(args.output_file_name, mode='w')
    formatter = logging.Formatter('%(message)s')
    file_hndlr.setFormatter(formatter)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(file_hndlr)
    logger.addHandler(ch)
    logger.setLevel(logging.INFO)
    logger.info('*' * 50)
    logger.info("Start collecting PCF output")
    logger.info('*' * 50)
    run_pcf_command(args.queue_manager, args.channel, args.host_ip, args.port, args.user,
                    args.password)
