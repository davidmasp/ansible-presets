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
sudo apt install ansible
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