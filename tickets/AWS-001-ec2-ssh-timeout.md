# AWS-001: EC2 SSH Timeout

## Summary
Unable to SSH into EC2 instance.

## Symptoms
- SSH connection timed out
- Instance running state confirmed

## Troubleshooting Steps
1. Verified EC2 instance state (running)
2. Confirmed correct public IP
3. Checked local firewall
4. Reviewed Security Group inbound rules
5. Identified missing TCP port 22 rule

## Root Cause
Inbound SSH rule removed from Security Group.

## Resolution
Re-added TCP port 22 from trusted IP address.

## Preventative Action
- Restrict SSH to specific IP range
- Document change management before modifying security groups
