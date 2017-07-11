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
from subprocess import check_output

workspace = None

def runtests_and_collectlogs(args, testdir_path, testsuites, config_map, autotestlog):
    autotestlog.write('------------------ Test run details ----------------\n')
    
    config_files = []
    test_name = []
    test_conf = []
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
    
    for test in testsuites:
        test_name.append(test.split('\\')[-1])
        
    for testsuite in test_name:
        if testsuite in config_map:
            config_files.append(testdir_path + '\\' + config_map[testsuite])
            test_conf.append(config_map[testsuite])
        else:
            print sys.stderr, 'Could not find the testsuite in config_map.conf file'
            sys.exit(1)

    print 'test config files: ', config_files
    print 'test name is: ', test_name
    print 'test conf is: ', test_conf
    
    status = robot.run(testsuites[0])
    
    print 'Runing status is: ', status

def main():
    
    global workspace    
    workspace = check_output('git rev-parse --show-toplevel', shell=True)
    workspace = workspace.strip(' \n\t')
    
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
    config_map = {}
    
    with open(mapfile, 'r') as f:
        for line in f:
            if line.endswith('\n'):
                line = line.rstrip()
            items = line.split(': ')
            key, value = items[0], items[1]
            config_map[key] = value
            
    print 'config map: ', config_map
    
    testsuites = []
    if not args.source.endswith('.txt'):     # source is a folder which containning testsuites
        print 'Will implement later'
    else:       # source is a specific testsuite  
        testsuites.append(args.source)
        n = len(args.source.split('\\'))
        testdir_path = args.source.rsplit('\\', 1)[0]
        print 'testsuites is: ', testsuites
        print 'test path is: ', testdir_path
              
    runtests_and_collectlogs(args, testdir_path, testsuites, config_map, autotestlog)
    
    
    autotestlog.close()
            
if __name__ == '__main__':
    main()
    pass
        