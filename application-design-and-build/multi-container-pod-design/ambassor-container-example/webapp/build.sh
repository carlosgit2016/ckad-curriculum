docker build -t "$1" .
# Building for minikube
minikube image build -t "$1" .