#!/bin/bash

validate_password() {
    password=$1

    if [[ ${#password} -lt 8 ]]; then
        return 1
    fi

    if ! echo "$password" | grep -qE '[A-Z]'; then
        return 1
    fi

    if ! echo "$password" | grep -qE '[a-z]'; then
        return 1
    fi

    if ! echo "$password" | grep -qE '[0-9]'; then
        return 1
    fi

    if echo "$password" | grep -qE '[^a-zA-Z0-9]'; then
        return 1
    fi

    if [[ $(echo "$password" | grep -oE '[0-9]' | wc -l) -gt 5 ]]; then
        return 1
    fi

    echo "Password is valid."
    return 0
}

read -p "Enter the password: " password
validate_password "$password"
