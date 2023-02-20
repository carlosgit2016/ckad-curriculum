#!/bin/bash
while getopts "gbv:" options; do

    case "${options}" in
        g)
            deployment="green"
            ;;
        b)
            deployment="blue"
            ;;
        v)
            version="${OPTARG}"
            ;;
        :)
            echo "Chose between blue or green deployment"
            exit 1
    esac
done

echo "Printing namespaces"

namespaces=$(kubectl get namespaces | sed '/kube-*/d;1d' | awk '{ print $1 }') # Retrieving all namespaces

for n in $namespaces; do
    echo $n
done

if [ "$deployment" = "green" ]; then
    
    echo "Deploying to green environment, deploying version ${version}"
    kubectl apply -f random-number-blue-deployment.yml 
elif [ "$deployment" = "blue" ]; then

    echo "Deploying to blue environment, deploying version ${version}"
    kubectl apply -f random-number-green-deployment.yml
fi
