cluster_name = "aks-prod-cluster"
node_count = 3
memory_gb = 31.4
is_healthy = True
last_error = None

print(cluster_name, type(cluster_name))
print(node_count, type(node_count))
print(memory_gb, type(memory_gb))
print(is_healthy, type(is_healthy))
print(last_error, type(last_error))

print(f"Cluster {cluster_name} has {node_count} nodes and is healthy: {is_healthy}")

x = "5"
y = 5
print(type(x), type(y))
print(x * 3)
print(y * 3)