import logging

def setup_logger(logfile):
    logger = logging.getLogger('AgentLogger')
    logger.setLevel(logging.INFO)
    fh = logging.FileHandler(logfile, mode='w')
    fh.setFormatter(logging.Formatter('%(asctime)s %(message)s'))
    logger.addHandler(fh)
    return logger
