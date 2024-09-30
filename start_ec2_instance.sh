#!/bin/bash

REGION="us-east-1"

INSTANCE_NAMES=$(aws ec2 describe-instances --region $REGION --query 'Reservations[].Instances[].Tags[?Key == `Name`].Value' --output text)

echo "Select an instance to start:"

select INSTANCE_NAME in $INSTANCE_NAMES; do
  if [ -n "$INSTANCE_NAME" ]; then
    break
  else
    echo "Invalid Selectio"
  fi
done

echo $INSTANCE_NAME
INSTANCE_ID=$(aws ec2 describe-instances --region $REGION --filters Name=tag:Name,Values="$INSTANCE_NAME" --query 'Reservations[].Instances[].InstanceId' --output text)

aws ec2 start-instances --region $REGION --instance-ids $INSTANCE_ID

echo "Starting Instance: $INSTANCE_NAME"
