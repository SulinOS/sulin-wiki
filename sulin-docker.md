# Pull docker image
|name|type|
|--|--|
|minimal|docker pull sulinos/sulin_development:minimal|
|devel|docker pull sulinos/sulin_development:devel|
|base|docker pull sulinos/sulin_development:base|

# Run docker daemon (as root)
`dockerd`

# Run shell in docker image (as root or docker user)
`docker run -it sulinos/sulin_development:TYPE /bin/bash`
