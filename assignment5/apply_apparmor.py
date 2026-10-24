import docker

client = docker.from_env()

print("Building image...")
client.images.build(path=".", tag="flask-apparmor")

container = client.containers.run(
    "flask-apparmor",
    ports={'5000/tcp': 5000},
    security_opt=["apparmor=my-apparmor-profile"],
    detach=True
)
print(f"Container started: {container.short_id}")

container_info = client.api.inspect_container(container.id)
print(f"AppArmor profile applied: {container_info['HostConfig']['SecurityOpt']}")

container.stop()
container.remove()
print("Container stopped")
