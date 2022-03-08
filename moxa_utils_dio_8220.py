#!/usr/bin/env python3

##
#   \copyright Moxa Europe 2021
#   \brief sample for reading writing GPIO of UC8200 iiot gateway.
#   
#   \author Moxa Europe 
#   \date   06 June 2021

import os
import sys
import logging

__author__  = "Amjad B. Moxa Europe"
__license__ = "MIT"
__version__ = '0.0.1'
__status__  = "beta"

log_format = '%(asctime)s: %(levelname)s - %(name)s - %(message)s'
logging.basicConfig(level=logging.INFO, datefmt="[%Y-%m-%d %H:%M:%S]", format=log_format)
logger = logging.getLogger(__name__)


def getGPIO(mode, port):
    ##
    #   \brief Device Specific function for UC8220 to return GPIO status from the device. 
    #    
    #   \param mode, port 
    # 
    #   \returns  DIN\DOUT  port 2 state: 0, in that order when success otheriwse None
    #  
    # Retrieving GPIO status using mx-dio-ctl utility  
    logger.info("***************************************************") 
    logger.info("Calling mx-dio-ctl tool to get built-in GPIO")
    logger.info("***************************************************") 
    # Map user define IN/OUT to mx-dio-ctl utility definition   
    if   mode == "DIN":
         mode = mode
    elif mode == "DOUT":
         mode = mode
    else:
        logger.error("Invalid mode:{}. Valid mode [DIN/DOUT]".format(mode))
        sys.exit()
    # Validate port numbers 
    if port == 0 or port == 1 or port == 2 or port == 3:
        port = port
    else:
        logger.error("Invalid port number:{}. Valid ports [0, 1, 2, 3]".format(port))
        sys.exit()
    # Get value from digital input/output port 
    if mode == "DIN":
        stream = os.popen('sudo mx-dio-ctl -i' + str(port)) 
        output = stream.read()
        logger.info(output)
        return output    
    elif mode == "DOUT":
        stream = os.popen('sudo mx-dio-ctl -o ' + str(port)) 
        output = stream.read()
        logger.info(output) 
        return output    
       
         
def setGPIO(mode, port, state):
    ##
    #   \brief Device Specific function for UC8220 to set GPIO status on the device. 
    #    
    #   \param mode, port, state  
    #   \returns  DOUT port 2 state: 0, in that order.
    #
    # Changing GPIO status using mx-dio-ctl utility  
    logger.info("***************************************************") 
    logger.info("Calling mx-dio-ctl tool to set built-in GPIO")
    logger.info("***************************************************") 
    # Map user define IN/OUT to mx-dio-ctl utility definition   
    if   mode == "DIN":
         mode = mode
    elif mode == "DOUT":
         mode = mode
    else:
        logger.error("Invalid mode:{}. Valid mode [DIN/DOUT]".format(mode))
        sys.exit()    
    # Validate port numbers 
    if port == 0 or port == 1 or port == 2 or port == 3:
        port = port
    else:
        logger.error("Invalid port number:{}. Valid ports [0, 1, 2, 3]".format(port))
        sys.exit()
    # Set value to digital output ports
    if state is not None: 
        if mode == "DOUT":
            stream = os.popen('sudo mx-dio-ctl -o ' + str(port) + ' -s ' + str(state)) 
            output = stream.read()
            logger.info(output)
            return output    
        else:
            logger.error("Invalid mode:{} Please use the valid mode [DOUT]".format(mode))
            sys.exit()


if __name__ == '__main__':
    setGPIO(mode="DOUT", port=2, state=0)
    getGPIO(mode="DOUT", port=2)
