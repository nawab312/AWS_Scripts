To find the latest Ubuntu AMI ID
```bash
aws ec2 describe-images --owners 099720109477 --filters "Name=name,Values=ubuntu/images/hvm-ssd/ubuntu-*-20.04-amd64-server-*" --query "Images | sort_by(@, &CreationDate) | [-1].ImageId" --output text
```
