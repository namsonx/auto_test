'''
   This is main script to run automation test
   Author: Son Mai
'''

import os
import sys
import argparse
import glob
import robot
import getpass
import subprocess

workspace = None

def runtests_and_collectlogs(args, config_files, autotestlog):
    autotestlog.write('------------------ Test run details ----------------\n')
    
    logs = []
    status = 0
    
    print 'log dir: ', args.outputdir
    try:
        '''
        for _f in glob.glob(args.outputdir + '\\*'):
            autotestlog.write('\n Clean up file %s \n' % _f)
            os.remove(_f)
        '''
        autotestlog.write('\n Clean up old log files ')
        os.remove(args.outputdir + '\\output.xml')
        os.remove(args.outputdir + '\\report.html')
        os.remove(args.outputdir + '\\log.html')
    except os.error:
        pass
    
    
                

def main():
    
    global workspace    
    workspace = check_output('git rev-parse --show-toplevel', shell=True)
    
    if len(sys.argv) <= 2:
        print 'The server ip and port must be input. \n'
        print ''
        sys.exit(0)
        
    local_dir = os.getcwd()    
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help='testsuite or testsuite directory')
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

    mapfile = workspace + '\\scripts\\config_map.conf'
    

    config_files = ''    
    runtests_and_collectlogs(args, config_files, autotestlog)
    
    
    autotestlog.close()
            
if __name__ == '__main__':
    main()
    pass
        