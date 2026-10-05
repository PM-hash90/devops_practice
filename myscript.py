# 1. Data Structure: A list of dictionaries representing our infrastructure
cloud_infrastructure = [
    {"name": "web-prod-01", "status": "OFFLINE"},
    {"name": "database-prod-01", "status": "OFFLINE"},
    {"name": "cache-prod-01", "status": "ONLINE"}
]

broken_servers = []
print("--- Starting Global Infrastructure Scan ---")

for machine in cloud_infrastructure:
	if machine ["status"] == "OFFLINE":
		print (f"🚨 ALERT: {machine ['name']} is down!")
		broken_servers.append (machine["name"])

print("--- Scan Complete ---")

if len (broken_servers) > 0:
	print (f"⚠️ Action Required: Please fix these servers: {broken_servers}")
else:
	print ("✅ All remaining servers are perfectly fine!")