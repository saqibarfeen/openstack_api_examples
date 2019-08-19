from keystoneauth1.identity import v3
from keystoneauth1 import session
from keystoneclient.v3 import client
#import pretty print
import pprint
p=pprint.PrettyPrinter(indent=4).pprint
def pp(y):
  return p(dir(y))
#auth = v3.Password(auth_url='http://10.81.1.80:5000/v3', user_id='d6d7abde8b3541dd83c913cfa59672a9',  password='51d8ca1d90ec46dd',project_id='7f74bac0c5624988a0815d4aaf2ff049')
#sess = session.Session(auth=auth)
#keystone = client.Client(session=sess, include_metadata=True)
keystone = client.Client(session= session.Session( auth=v3.Password(auth_url='http://10.81.1.80:5000/v3', username='admin',  password='51d8ca1d90ec46dd',project_id='7f74bac0c5624988a0815d4aaf2ff049',user_domain_id='default')) , include_metadata=True)
resp = keystone.projects.list()





#nova api
from novaclient import client as nova_client
nova=nova_client.Client(2,session=sess)
nova.servers.list()




#gnocchi
from gnocchiclient import client as gnocchi_client
g=gnocchi_client.Client(1,session=sess)
pp(dir(g))




#cloudkitty
from cloudkittyclient import client as cloudkitty_client
cc=cloudkitty_client.Client(1,session=sess)
pp(dir(g))
