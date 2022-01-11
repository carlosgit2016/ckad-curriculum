docker build -t "personal-notications:$1" .
# Building for minikube
minikube image build -t "personal-notications:$1" .