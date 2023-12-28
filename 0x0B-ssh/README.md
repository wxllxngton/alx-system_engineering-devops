<details>
<summary>SSH Cheat Sheet</summary>
<br>
## This sheet goes along with this [SSH YouTube tutorial](https://www.youtube.com/watch?v=hQWRp-FdTpc&t=1270s)

### Login via SSH with password (LOCAL SERVER)
```$ ssh brad@192.168.1.29```

### Create folder, file, install Apache (Just messing around)
```$ mkdir test```

```$ cd test```

```$ touch hello.txt```

```$ sudo apt-get install apache2```


### Generate Keys (Local Machine)
```$ ssh-keygen```

### Add Key to server in one command
```> cat ~/.ssh/id_rsa.pub | ssh brad@192.168.1.29 "mkdir -p ~/.ssh && chmod 700 ~/.ssh && cat >>  ~/.ssh/authorized_keys```

### Create & copy a file to the server using SCP
```$ touch test.txt```
```$ scp ~/test.txt brad@192.168.1.29:~```


## DIGITAL OCEAN

> Create account->create droplet

### Create Keys For Droplet (id_rsa_do)
```$ ssh-keygen -t rsa```

> Add Key When Creating Droplet

### Try logging in
```$ ssh root@doserver```

### If it doesn't work
```$ ssh-add ~/.ssh/id_rsa_do```
(or whatever name you used)

### Login should now work
```$ ssh root@doserver```

### Update packages
```$ sudo apt update```

```$ sudo apt upgrade```

### Create new user with sudo
```$ adduser brad```

```$ id brad```

```$ usermod -aG sudo brad```

```$ id brad```

### Login as brad
```> ssh brad@doserver```

### We need to add the key to brads .ssh on the server, log back in as root
```$ ssh root@doserver```

```$ cd /home/brad```

```$ mkdir .ssh```

```$ cd .ssh```

```$ touch authorized_keys```

```> sudo nano authorized_keys```
(paste in the id_rsa_do.pub key, exit and log in as brad)

### Disable root password login
```$ sudo nano /etc/ssh/sshd_config```

### Set the following
```PermitRootLogin no```

```PasswordAuthentication no```

### Reload sshd service
```$ sudo systemctl reload sshd```

### Change owner of /home/brad/* to brad
```$ sudo chown -R brad:brad /home/brad```

### May need to set permission
```$ chmod 700 /home/brad/.ssh```

### Install Apache and visit ip
``` $ sudo apt install apache2 -y```

## Github

### Generate Github Key(On Server)
``` $ ssh-keygen -t rsa```
(id_rsa_github or whatever you want)

## Add new key
```$ ssh-add /home/brad/.ssh/id_rsa_github```

## If you get a message about auth agent, run this and try again
```$ eval `ssh-agent -s````

## Clone repo
```$ git clone git@github.com:bradtraversy/react_otka_auth.git```

## Install Node
```$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -```

```$ sudo apt-get install -y nodejs```

## Install Dependencies
```  $ npm install ```

## Start Dev Server and visit ip:3000
```$ npm start```

## Build Out React App
``` $ npm run build```

## Move static build to web server root
``` $ sudo mv -v /home/brad/react_otka_auth/build/* /var/www/html```
</details>

### 0-use_a_private_key

Write a Bash script that uses `ssh` to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:

- Only use `ssh` single-character flags
- You cannot use `-l`
- You do not need to handle the case of a private key protected by a passphrase

```bash
sylvain@ubuntu$ ./0-use_a_private_key
ubuntu@server01:~$ exit
Connection to 8.8.8.8 closed.
sylvain@ubuntu$
```
### 1-create_ssh_key_pair

Write a Bash script that creates an RSA key pair.

Requirements:

- Name of the created private key must be `school`
- Number of bits in the created key to be created 4096
- The created key must be protected by the passphrase `betty`

Example:

```bash
sylvain@ubuntu$ ls
1-create_ssh_key_pair
sylvain@ubuntu$ ./1-create_ssh_key_pair
Generating public/private rsa key pair.
Your identification has been saved in school.
Your public key has been saved in school.pub.
The key fingerprint is:
5d:a8:c1:f5:98:b6:e5:c0:9b:ee:02:c4:d4:01:f3:ba vagrant@ubuntu
The key's randomart image is:
+--[ RSA 4096]----+
|      oo...      |
|      .+.o =     |
|     o  + B +    |
|      o. = O     |
|     .. S = .    |
|      .. .       |
|      E.  .      |
|        ..       |
|         ..      |
+-----------------+
sylvain@ubuntu$ ls
1-create_ssh_key_pair school  school.pub
sylvain@ubuntu$
```


### 2-ssh_config
Your machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.

Requirements:

- Your SSH client configuration must be configured to use the private key `~/.ssh/school`
- Your SSH client configuration must be configured to refuse to authenticate using a password

Example:

```bash
sylvain@ubuntu$ ssh -v ubuntu@98.98.98.98
OpenSSH_6.6.1, OpenSSL 1.0.1f 6 Jan 2014
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 47: Applying options for *
debug1: Connecting to 98.98.98.98 port 22.
debug1: Connection established.
debug1: identity file /home/sylvain/.ssh/school type -1
debug1: identity file /home/sylvain/.ssh/school-cert type -1
debug1: Enabling compatibility mode for protocol 2.0
debug1: Local version string SSH-2.0-OpenSSH_8.1
debug1:Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4ubuntu0.5
debug1: match: OpenSSH_7.6p1 Ubuntu-4ubuntu2.1 pat OpenSSH* compat 0x04000000
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: server->client aes128-ctr hmac-sha1-etm@openssh.com none
debug1: kex: client->server aes128-ctr hmac-sha1-etm@openssh.com none
debug1: sending SSH2_MSG_KEX_ECDH_INIT
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ECDSA bd:03:f8:6a:12:28:d6:17:85:c1:b6:91:f1:da:0f:37
debug1: Host '98.98.98.98' is known and matches the ECDSA host key.
debug1: Found key in /home/sylvain/.ssh/known_hosts:1
debug1: ssh_ecdsa_verify: signature correct
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: SSH2_MSG_SERVICE_REQUEST sent
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Trying private key: /home/sylvain/.ssh/school
debug1: key_parse_private2: missing begin marker
debug1: read PEM private key done: type RSA
debug1: Authentication succeeded (publickey).
Authenticated to 98.98.98.98 ([98.98.98.98]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: client_input_global_request: rtype hostkeys-00@openssh.com want_reply 0
debug1: Sending environment.
debug1: Sending env LANG = en_US.UTF-8
ubuntu@magic-server:~$
```
In the example above, we can see that ssh tries to authenticate using school and does not try to authenticate using a password. You can replace 98.98.98.98 by the IP of your server for testing purposes.

### 3. Let me in!

Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.

```bash
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDNdtrNGtTXe5Tp1EJQop8mOSAuRGLjJ6DW4PqX4wId/Kawz35ESampIqHSOTJmbQ8UlxdJuk0gAXKk3Ncle4safGYqM/VeDK3LN5iAJxf4kcaxNtS3eVxWBE5iF3FbIjOqwxw5Lf5sRa5yXxA8HfWidhbIG5TqKL922hPgsCGABIrXRlfZYeC0FEuPWdr6smOElSVvIXthRWp9cr685KdCI+COxlj1RdVsvIo+zunmLACF9PYdjB2s96Fn0ocD3c5SGLvDOFCyvDojSAOyE70ebIElnskKsDTGwfT4P6jh9OBzTyQEIS2jOaE5RQq4IB4DsMhvbjDSQrP0MdCLgwkN
```

### 100-puppet_ssh_config.pp
Let’s practice using Puppet to make changes to our configuration file. Just as in the previous configuration file task, we’d like you to set up your client SSH configuration file so that you can connect to a server without typing a password.

Requirements:

- Your SSH client configuration must be configured to use the private key `~/.ssh/school`
- Your SSH client configuration must be configured to refuse to authenticate using a password

Example:

```bash
vagrant@ubuntu:~$ sudo puppet apply 100-puppet_ssh_config.pp
Notice: Compiled catalog for ubuntu-xenial in environment production in 0.11 seconds
Notice: /Stage[main]/Main/File_line[Turn off passwd auth]/ensure: created
Notice: /Stage[main]/Main/File_line[Declare identity file]/ensure: created
Notice: Finished catalog run in 0.03 seconds
vagrant@ubuntu:~$
```

### Ensure that the authorized_keys file inside the .ssh directory has the correct permissions (600):
```bash
chmod 600 /home/ubuntu/.ssh/authorized_keys
```
