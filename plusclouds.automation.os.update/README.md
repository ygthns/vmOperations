# plusclouds.os.update

This role updates the package manager cache for linux based systems and upgrades packages if specified. Updates the specified categories for windows hosts.

## Role Variables

| Variable       | Required | Default     | Choices                 | Comments                                           |
| -------------- | -------- | ----------- | ----------------------- | -------------------------------------------------- |
| upgrade        | yes      | no          | yes,no                  | Option to upgrade packages                         |
| category_names | yes      | given below | all, or list of strings | List of category names to update, for windows only |

category_names variable is used only on windows hosts. It is a scalar or list of categories to install updates from.  
default = ["CriticalUpdates", "SecurityUpdates", "UpdateRollups"]  
Some possible categories are Application, Connectors, Critical Updates, Definition Updates, Developer Kits, Feature Packs, Guidance, Security Updates, Service Packs, Tools, Update Rollups, Updates, and Upgrades

## Example Playbook

```yaml
- name: main
  hosts: win
  roles:
    - plusclouds.os.update
  vars:
    - upgrade: yes
    - category_names: all
```

## Example Inventory File

```yaml
[linux_servers]
185.44.192.11 ansible_connection=ssh ansible_ssh_user=root ansible_ssh_pass=rndpass ansible_sudo_pass=rndpass
185.44.192.12 ansible_connection=ssh ansible_ssh_user=root ansible_ssh_pass=rndpass ansible_sudo_pass=rndpass


[windows_servers]
185.44.192.13

[win:vars]
ansible_user=Administrator
ansible_password= rndpass
ansible_connection=winrm
ansible_winrm_server_cert_validation=ignore
```
