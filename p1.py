from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
auth = v3.Password(auth_url='http://192.168.24.18:5000/v3', user_id='8ceabf44a8e047718741f0fe7dcdfd0b',  password='babloo',
                   project_id='f1b0fed0c651431c92e12a796ad3054e')
sess = session.Session(auth=auth)
keystone = client.Client(session=sess, include_metadata=True)
resp = keystone.projects.list()


#import pretty print
import pprint
pp=pprint.PrettyPrinter(indent=4).pprint



#nova api
from novaclient import client as nova_client
nova=nova_client.Client(2,session=sess)
nova.servers.list()




#gnocchi
from gnocchiclient import client as gnocchi_client
g=gnocchi_client.Client(1,session=sess)
pp(dir(g))
