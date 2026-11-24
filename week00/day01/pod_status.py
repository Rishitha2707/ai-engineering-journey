pod_name = "api-7d9f"
namespace = "dna"
restart_count = 2
cpu_usage_percent = 45.5
is_ready = True
last_error = None

print(pod_name, type(pod_name))
print(namespace, type(namespace))
print(restart_count, type(restart_count))
print(cpu_usage_percent, type(cpu_usage_percent))
print(is_ready, type(is_ready))
print(last_error, type(last_error))

print("=" * 40)

print(f"pod {pod_name} in namespace {namespace}: ready={is_ready}, restarts={restart_count}, CPU={cpu_usage_percent}%")


replicas = 3
print(type(replicas))
replicas = "three"
print(type(replicas))