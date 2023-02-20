# !/bin/bash
echo "=== Building image to minikube ==="
minikube image build -t "randomnumberapp:$1" -f Dockerfile .
echo "=== image to minikube DONE ===\n\n\n\n"
echo "=== Building image to local daemon ==="
docker build -t "randomnumberapp:$1" .
echo "=== image to local daemon DONE ==="
