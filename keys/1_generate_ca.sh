#!/bin/bash

mkdir artifacts
openssl req -new -x509 -keyout artifacts/ca.key -out artifacts/ca.crt -days 365 -subj "/CN=My ENV CA" -passout pass:secret -nodes