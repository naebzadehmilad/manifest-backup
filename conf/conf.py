import logging,colorlog
colorlog.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', datefmt='%H:%M:%S')
import configparser
conf = configparser.ConfigParser()
def write_conf():
    conf.add_section('RESOURCES-TYPE')
    conf.set('RESOURCES-TYPE','resources','deployment,svc,cm')
    conf.add_section('NAMESPACES')
    conf.set('NAMESPACES','namespaces','prod,stg,monitoring')
    conf.add_section('PATH-KUBECTL-CA')
    conf.set('PATH-KUBECTL-CA','path','/repo/ca/')
    conf.add_section('BACKUP-DIR')
    conf.set('BACKUP-DIR','dir','/tmp/')
    with open('conf.cfg','w') as configfile:
        conf.write(configfile)
def read_conf():
    conf.read('conf.cfg')
    global namespaces
    global resources
    global path
    global dir
    namespaces = str(conf.get('NAMESPACES', 'namespaces')).replace(' ', '').split(',')
    resources = str(conf.get('RESOURCES-TYPE', 'resources')).replace(' ', '').split(',')
    path = str(conf.get('PATH-KUBECTL-CA', 'path')).replace(' ', '').split(',')
    dir = str(conf.get('BACKUP-DIR', 'dir')).replace(' ', '').split(',')
write_conf()
read_conf()
