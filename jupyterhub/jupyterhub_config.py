import os

# https://github.com/jupyterhub/dockerspawner/blob/master/examples/simple/jupyterhub_config.py
# dummy for testing. Don't use this in production!
c.JupyterHub.authenticator_class = 'jupyterhub.auth.DummyAuthenticator'

# launch with docker
c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'

# we need the hub to listen on all ips when it is in a container
c.JupyterHub.hub_ip = '0.0.0.0'
# the hostname/ip that should be used to connect to the hub
# this is usually the hub container's name
c.JupyterHub.hub_connect_ip = os.environ['JUPYTERHUB_CONTAINER']

# tell the user containers to connect to our docker network
c.DockerSpawner.network_name = os.environ['JUPYTERHUB_NETWORK']

# pick a docker image. This should have the same version of jupyterhub
# in it as our Hub.
c.DockerSpawner.image = os.environ['NOTEBOOK_IMAGE']

# delete containers when the stop
c.DockerSpawner.remove = True

# https://repo2docker.readthedocs.io/en/latest/howto/jupyterhub_images.html
# for images built with repo2docker
c.DockerSpawner.cmd = ['jupyterhub-singleuser']
