"""
list all queues script
"""
from pymqi import QueueManager, CMQC, CMQCFC, PCFExecute, MQMIError, cd
import argparse
import logging


logger = logging.getLogger('PCF_queues_collect')


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
    args = {CMQC.MQCA_Q_NAME: '*',
            CMQCFC.MQIACF_Q_ATTRS: CMQCFC.MQIACF_ALL}

    try:
        qmgr.connectTCPClient(queue_manager, cd(), channel, conn_info, user_name, password)
        pcf = PCFExecute(qmgr)
        response = pcf.MQCMD_INQUIRE_Q(args)
    except MQMIError as e:
        logger.error("Could not read information about queues")
        logger.error(e.errorAsString())
        logger.error(e.reason)
    else:
        for queue in response:
            logger.info("QUEUE INFO")
            logger.info("MQCA_Q_NAME: " + (queue.get(CMQC.MQCA_Q_NAME,
                                                     "UNKNOWN")).strip())
            logger.info("MQCA_Q_DESC: " + (queue.get(CMQC.MQCA_Q_DESC,
                                                     "UNKNOWN")).strip())
            logger.info("MQIA_Q_TYPE: " + str(queue.get(CMQC.MQIA_Q_TYPE,
                                                        "UNKNOWN")).strip())
            logger.info("MQIA_MAX_Q_DEPTH: " + str(queue.get(CMQC.MQIA_MAX_Q_DEPTH,
                                                             "UNKNOWN")).strip())
            logger.info("MQIA_USAGE: " + str(queue.get(CMQC.MQIA_USAGE,
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
