from api_client import ApiClient


client = ApiClient(host='https://company.cloud.databricks.com?o=123')
print(client.get_url("/"))

client = ApiClient(host='https://mydatabricksproxyservice.com/databricks/proxy')
print(client.get_url("/"))