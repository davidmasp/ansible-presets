# README

Ansible configuration site.

The aim of this repo is to manage a resetable configuration
playbook for setting up new computers from scratch.

## What it includes?

* Generation of a folder system according to presets
* copy of dotfiles and aliases
* copy of custom scripts
* installation of common packages
* manage project repos

## Usage

Install ansible in the new machine:

```bash
sudo apt update
sudo apt upgrade
sudo apt install ansible
## install required perc
ansible-galaxy collection install community.crypto
```

then, clone the directory 

```bash
cd /tmp
git clone https://github.com/davidmasp/ansible-presets.git
```

and finally run the playbook locally

```bash
ansible-playbook presets.yml --connection=local --ask-become-pass
```

### For Linode machines

Log in as a root and create a user

```bash
## add user, will be asked for password
useradd dmas
## if not,
passwd dmas
```

and put it in the sudoers

```bash
usermod -aG sudo dmas
```

## FAQ

### TMUX 2.9 compatibility

There are 2 tmux conf versions, pre-2.9 and post-2.9.

See [this](https://github.com/tmux/tmux/issues/1689) for more context.

### Error with conda env active

**Error** with conda env.

```
Traceback (most recent call last):
  File "/usr/bin/ansible-playbook", line 34, in <module>
    from ansible import context
ModuleNotFoundError: No module named 'ansible'
```

For some reason if conda is active the ansible
executable is not recognised, for now do
deativate any conda environtment before
runing ansible.

### WIP 

I am trying to download a private repo from github, I
want to do is to generate a key, added into the github
and then download the repo.

```bash
---
- hosts: localhost
  connection: local
  tasks:
  - name: generate key
    community.crypto.openssh_keypair:
    path: ~/.ssh/gh_id
    type: ed25519
  - name: Evaluating the authentication agent & adding the key...
    shell: |
      eval "$(ssh-agent -s)"
      ssh-add ~/.ssh/gh_id
  - name: clone homelab scripts
    ansible.builtin.git:
      repo: 'git@github.com:xx/xx.git'
      dest: /home/dmas/xx/xx
```
