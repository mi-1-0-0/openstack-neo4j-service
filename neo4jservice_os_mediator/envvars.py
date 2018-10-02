import os

NEO4J_SERVICE_URL = os.getenv('NEO4J_SERVICE_URL', 'http://localhost:15135/neo4j')
OS_AUTH_URL = os.getenv('OS_AUTH_URL', "http://x.x.x.x:5000")
OS_USERNAME = os.getenv('OS_USERNAME', "xxxxxxxxxxxxxxxxxxx")
OS_PASSWORD = os.getenv('OS_PASSWORD', "xxxxxxxxxxxxxxxxxxxxx")
OS_PROJECT_ID = os.getenv('OS_TENANT_ID', "xxxxxxxxxxxxxxxxxxxxxxx")
OS_API_VERSION = os.getenv('OS_API_VERSION', "2.0")
CONFIG_FILE_PATH = os.getenv('CONFIG_FILE_PATH', 'openstack_info.json')
NOTIFICATION_TRANSPORT_URL = os.getenv('NOTIFICATION_TRANSPORT_URL', "rabbit://openstack:xxxxx@x.x.x.x:5672")
NOTIFICATION_EVENT_TYPE = os.getenv('NOTIFICATION_EVENT_TYPE', "^.*?.end$")
NOTIFICATION_TOPIC_NAME = os.getenv('NOTIFICATION_TOPIC_NAME', "notifications")
NOTIFICATION_PUBLISHER_ID = os.getenv('NOTIFICATION_PUBLISHER_ID', "^.*")
PRIVATE_KEY_PATH = os.getenv('PRIVATE_KEY_PATH', "/private_key.key")