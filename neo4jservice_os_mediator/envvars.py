import os

NEO4J_SERVICE_URL = os.getenv('NEO4J_SERVICE_URL1', 'http://x.x.x.x:15135/neo4j')
OS_AUTH_URL = os.getenv('OS_AUTH_URL', "http://x.x.x.x:5000/v3")
OS_USERNAME = os.getenv('OS_USERNAME', "xxxxxx")
OS_PASSWORD = os.getenv('OS_PASSWORD', "xxxxxxxx")
OS_PROJECT_NAME = os.getenv('OS_PROJECT_NAME', "xxxxxx_project")
OS_USER_DOMAIN_NAME=os.getenv('OS_USER_DOMAIN_NAME', 'Default')
OS_PROJECT_DOMAIN_ID=os.getenv('OS_PROJECT_DOMAIN_ID', 'default')
OS_API_VERSION = os.getenv('OS_API_VERSION', "2")
CONFIG_FILE_PATH = os.getenv('CONFIG_FILE_PATH', '/cloud_reconnoiterer/openstack_info.json')
NOTIFICATION_TRANSPORT_URL = os.getenv('NOTIFICATION_TRANSPORT_URL', "rabbit://xxxxxxxxxxx:xxxxxxx@x.x.x.x:5672")
OPENSTACK_NOTIFICATION_EXCHANGE_NAME = os.getenv('OPENSTACK_NOTIFICATION_EXCHANGE_NAME', "openstack")
OPENSTACK_NOTIFICATION_TOPIC_NAME = os.getenv('OPENSTACK_NOTIFICATION_TOPIC_NAME', "notifications")
DOCKER_NOTIFICATION_EXCHANGE_NAME = os.getenv('DOCKER_NOTIFICATION_EXCHANGE_NAME', "docker")
DOCKER_NOTIFICATION_TOPIC_NAME = os.getenv('DOCKER_NOTIFICATION_TOPIC_NAME', "docker_notifications")
PRIVATE_KEYS_FOLDER = os.getenv('PRIVATE_KEYS_FOLDER', "/keys")
VM_USERNAME = os.getenv('VM_USERNAME', "xxxx")
TIME_TO_WAIT = os.getenv("TIME_TO_WAIT", '1000')
GRAPH_ELEMENT_TYPE_PREFIX = os.getenv("GRAPH_ELEMENT_TYPE_PREFIX","xxxx")
CLOUD_TYPE = os.getenv("CLOUD_TYPE","openstack")
COMPONENT_EVENT_MAPPING_FILE=os.getenv('CONFIG_FILE_PATH', '/cloud_reconnoiterer/event_component_mapping.json')