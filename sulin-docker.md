# Run docker daemon (as root)
`nohup dockerd > /var/log/dockerd &`

# Pull docker image
|name|type|
|--|--|
|minimal|docker pull sulinos/sulin_development:minimal|
|devel|docker pull sulinos/sulin_development:devel|
|base|docker pull sulinos/sulin_development:base|


# Run shell in docker image
`docker run -it sulinos/sulin_development:TYPE /bin/bash`
