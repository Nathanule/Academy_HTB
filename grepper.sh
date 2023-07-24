#!/bin/bash

search_audit_log() {
    echo "Searching for 'comm=\"su\"' in accessible logs:"
    grep -r --color=auto 'comm="su"' /var/log/*
    echo

    echo "Searching for 'comm=\"sudo\"' in accessible logs:"
    grep -r --color=auto 'comm="sudo"' /var/log/*
    echo
}

search_audit_log
