# Example: ./build.sh appadapterexample1:latest
# Example: ./build.sh appadapterexample2:latest

docker build -t "$1" .
# Building for minikube
minikube image build -t "$1" .