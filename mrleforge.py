#!/usr/bin/env python
from bash import *
import json
import boto3
import pyperclip
import time

launch_command = """""".replace('\n', ' ')

def main():
    emr = boto3.client('emr')
    cluster_id = launch_new_cluster()
    public_dns = wait_for_and_retrieve_public_dns(emr, cluster_id)
    print(f'public dns is {public_dns}')
    ssh_url = f'hadoop@{public_dns}'
    ssh_command_prefix = f'ssh -i ~/.ssh/id_rsa-emr-prod'
    ssh_command = f'{ssh_command_prefix} {ssh_url}'
    pyperclip.copy(ssh_command)
    print(f'command to ssh is in your keyboard: {ssh_command}')
    print('starting the ssh tunnel')
    ssh_tunnel_process = bash(f'ssh -i ~/.ssh/id_rsa-emr-prod -ND 8157 {ssh_url}', sync=False)
    print_and_wait(ssh_tunnel_process)

def print_buffer(buffer):
    while not buffer.closed:
        line = buffer.readline().decode()
        if len(line) > 0:
            print(line)
            yield line
        else:
            break


def print_and_wait(p):
    lines = []
    while True:
        lines.extend(list(print_buffer(p.p.stdout)))
        lines.extend(list(print_buffer(p.p.stderr)))
        if p.p.poll() is None:
            time.sleep(.05)
        else:
            break
    exit_code = p.p.poll()
    print(f'exit code {exit_code} from subprocess')
    return exit_code, ''.join(lines)

def wait_for_and_retrieve_public_dns(emr, cluster_id):
    time.sleep(15)
    cluster_details = emr.describe_cluster(ClusterId=cluster_id)['Cluster']
    pub_dns_key = 'MasterPublicDnsName'
    while pub_dns_key not in cluster_details:
        time.sleep(.5)
        cluster_details = emr.describe_cluster(ClusterId=cluster_id)['Cluster'] 
    return cluster_details[pub_dns_key]


def launch_new_cluster():
    """
    returns the cluster id
    """
    launch_process = bash(launch_command, sync=False)
    _, out = print_and_wait(launch_process)
    return json.loads(out)['ClusterId']


if __name__ == "__main__":
    main()
