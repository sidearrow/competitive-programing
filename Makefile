start-python-container:
	docker run -itd \
		--name compro-python \
		--volume ${PWD}/codes:/codes \
		python:3.8.2-slim-buster /bin/sh
