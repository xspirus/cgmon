#!/bin/bash

source ${PWD}/functions.sh

# $1 contains the directory of the policy and limit

if [ "$#" -ne 1 ]; then
    echo_error "Usage: ./my_demo.sh [dir]"
    exit 1
fi

WD=${PWD}/$1

# Stop daemon if running
cgmon daemon stop -w ${WD}

echo_warning "Sleep for 1 sec"
sleep 1

# Start daemon
cgmon daemon start -w ${WD} -p ${WD}/mod_policy_cpumin.py -l ${WD}/mod_limit_cpu.py

echo_warning "Sleep for 1 sec"
sleep 1

echo_info "Showing app list"
cgmon app list

echo_warning "Sleep for 1 sec"
sleep 1

echo_info "Creating policies"
cgmon policy create -n anelastic -p 1000
cgmon policy create -n elastic -p 200
cgmon policy list

echo_warning "Sleep for 1 sec"
sleep 1

echo_info "Spawning applications"
cgmon app spawn -p anelastic -e "stress -c 2" -n BANKDB
cgmon app spawn -p elastic -e "stress -c 2" -n CALCULATIONS
cgmon app spawn -p elastic -e "stress -c 2" -n WEBDB
cgmon app spawn -p elastic -e "stress -c 2" -n INSURANCEDB
cgmon app list

echo_warning "Sleep for 2 sec"
sleep 2

cgmon app list

cgmon app spawn -p elastic -e "stress -c 2" -n YOLODB

echo_warning "Sleep for 3 sec"
sleep 3

cgmon app list

echo_warning "Sleep for 5 sec"
sleep 5

cgmon app list

echo_warning "Sleep for 10 sec"
sleep 10

cgmon app list
pkill -f stress
