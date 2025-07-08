#!/bin/bash

keytool -importcert -keystore artifacts/kafka.truststore.jks -alias CARoot -file artifacts/ca.crt -storepass secret -noprompt
keytool -exportcert -keystore artifacts/kafka.truststore.jks -alias CARoot -rfc -file artifacts/ca.pem -storepass secret