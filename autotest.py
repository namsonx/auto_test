'''
   This is main script to run automation test
   Author: Son Mai
'''

import os
import sys
import argparse
import robot
import getpass
from argparse import Action

def main():
    
    if len(sys.argv) <= 2:
        print 'The server ip and port must be input. \n'
        print ''
        sys.exit(0)
        
    local_dir = os.getcwd()    
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server_ip', help='Input server ip address')
    parser.add_argument('-p', '--port', help='Input port of server')
    parser.add_argument('-tc', '--testconf', help='Adding test config file', action='append')
    parser.add_argument('-d', '--outputdir', help='Directory to store output log', default=local_dir)
    
    args = parser.parse_args()
    
    server_ip = args.server_ip
    port = args.port
    
    print 'server ip: ', server_ip
    print 'port: ', port
    
    autotestlogfile = args.outputdir + '\\autotest.log'
    
    
    if not os.path.exists(os.path.dirname(autotestlogfile)):
        try:
            os.makedirs(os.path.dirname(autotestlogfile))
        except OSError as exc:
            print 'Creating log failed'
            
    autotestlog = open(autotestlogfile, 'w')
    autotestlog.write('Start running the auto test script')
    
    autotestlog.close()
            
if __name__ == '__main__':
    main()
    pass
        