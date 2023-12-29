img:
		@docker build -t pruizca/ft_token_manager .

pull:
		@git pull

login:
		@docker login

logout:
		@docker logout

push:	img
		@docker push pruizca/ft_token_manager:latest
		@docker image rm pruizca/ft_token_manager

multi:
		@docker buildx create --use default
		docker buildx build --push --platform linux/arm64/v8,linux/amd64 --tag pruizca/ft_token_manager:latest .
