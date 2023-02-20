#!/bin/bash

function create_namespaces() {
    echo "Creating namespaces"
    cat namespaces.yml
    kubectl apply -f namespaces.yml
}

function deploy_random_number_resources(){
    echo "Deploying blue resources"
    cat random-number-blue-deployment.yml
    kubectl apply -f random-number-blue-deployment.yml
    # Waiting for all replicas be available
    echo "Waiting for blue deployment replicas be all available"
    # kubectl wait deployment.apps/randomnumber-blue --for=jsonpath='{.status.unavailableReplicas}'=0 --timeout=-1s
    kubectl rollout status deployment.apps/randomnumber-blue
    echo "Containers deployed as part of random-blue deployment"
    kubectl get deployments/randomnumber-blue -o jsonpath='{.spec.template.spec.containers[*].name}' | sed 's/\s/\n/g;'
}

function deploy_services(){
    kubectl apply -f services.yml
}

function main() {
    create_namespaces
    deploy_random_number_resources
    deploy_services
}

set -e
main
