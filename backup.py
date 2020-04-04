from conf import *
import os,logging,colorlog
def backup():
  #  try:
      #  os.system('mkdir -p $HOME/.kube && cp -i {0} $HOME/.kube/config && chown $(id -u):$(id -g) $HOME/.kube/config '.format(path))
     #   os.system('export KUBECONFIG=$HOME/.kube/config ')
   # except:
    #    logging.error('export KUBECONFIG=$HOME/.kube/config')
       # exit(1)
    for i in range(len(namespaces)):
        for j in range(len(resources)):
            if not os.path.exists('{0},{1}/{2}'.format(dir[0],namespaces[i],resources[j])):
                try:
                    os.makedirs('{0}/{1}/{2}'.format(dir[0],namespaces[i],resources[j]))
                except:
                    raise OSError("Can't create destination directory ('{0}/{1}/{2}')!".format(dir[0],namespaces[i],resources[j]))


backup()