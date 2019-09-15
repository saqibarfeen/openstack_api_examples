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

#sess= session.Session( auth=v3.Password(auth_url='http://10.81.1.80:5000/v3', username='admin',  password='51d8ca1d90ec46dd',project_id='7f74bac0c5624988a0815d4aaf2ff049',user_domain_id='default'))
sess= session.Session( auth=v3.Password(auth_url='http://10.81.1.80:5000/v3', username='admin',  password='51d8ca1d90ec46dd',project_name='admin',user_domain_id='default',project_domain_id='default'))
keystone = client.Client(session=sess, include_metadata=True)
resp = keystone.projects.list()

#cloudkitty
from cloudkittyclient import client as cloudkitty_client
cc=cloudkitty_client.Client(1,session=sess)

p(cc.report.get_summary(groupby=['res_type']))



#gnocchi
from gnocchiclient import client as cloudkitty_client
cc=gnocchi_client.Client(1,session=sess)



#nova api
from novaclient import client as nova_client
nova=nova_client.Client(2,session=sess)
nova.servers.list()


#create network

{'gateway_ip': '1.9.9.1', 'name': 'sub1', 'ip_version': '4', 'cidr': '1.9.9.0/24', 'network_id': 'eec3c47e-d33a-4134-aa10-483dbca2e548'}

import openstack
flavor_data={'disk': 20, 'ephemeral_gb': 0, 'is_public': True, 'name': 'zxcsddsf', 'price': 0, 'ram': 1024, 'rxtx_factor': 1, 'swap': 0, 'vcpus': 2}
d={'auth_url': 'http://10.81.1.80:5000/v3', 'domain_name': 'Default', 'password': '51d8ca1d90ec46dd', 'project_name': 'admin', 'username': 'admin'}
conn=openstack.connect(**d)
connection.compute.create_flavor(**flavor_data)
