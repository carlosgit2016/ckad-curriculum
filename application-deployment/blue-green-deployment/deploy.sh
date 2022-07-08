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

if [ "$deployment" = "green" ]; then
    
    echo "Deploying to green environment, deploying version ${version}"
elif [ "$deployment" = "blue" ]; then
    echo "Deploying to blue environment, deploying version ${version}"
fi