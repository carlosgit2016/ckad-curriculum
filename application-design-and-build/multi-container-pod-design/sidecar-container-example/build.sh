docker build -t "sidecar-example:$1" .
# Building for minikube
minikube image build -t "sidecar-example:$1" .