# albehaviormanager
Behavior Manager for Pepper and Nao Robots

## Installation

SSH to your Pepper or Nao robot:

```
ssh nao@<ip>
```

Of course you have to enter your very secure password!

Clone the Repository:

```
cd ~
wget https://raw.githubusercontent.com/Michdo93/albehaviormanager/main/albehaviormanger.py
```

Make it runnable with `chmod +x albehaviormanger`.

## Run the Behavior Manager:

```
usage: albehaviormanager.py [-h] [--ip IP] [--port PORT]
                            [--behavior_name BEHAVIOR_NAME] --function
                            FUNCTION [--localPath LOCALPATH]
albehaviormanager.py: error: argument --function is required
```

### Local on the Robot via an SSH Session:

As example list first all Behaviors:

List all behaviors:

```
python albehaviormanager.py --function getBehaviorNames
```

Run a specific behavior with `python albehaviormanager.py --function runBehavior --behavior_name <behavior_name>`:

```
python albehaviormanager.py --function runBehavior --behavior_name "System/animations/Stand/BodyTalk/Speaking/BodyTalk_1"
```

Stop the specific behavior  with `python albehaviormanager.py --function stopBehavior --behavior_name <behavior_name>`:

```
python albehaviormanager.py --function stopBehavior --behavior_name "System/animations/Stand/BodyTalk/Speaking/BodyTalk_1"
```

### Remote on the Robot via SSH:

#### Preparation:

Look for bash files:

```
ls -la /etc/skel
total 24
drwxr-xr-x  3 root root 4096 Aug 28  2015 .
drwxr-xr-x 47 root root 4096 Sep 17  2009 ..
-rw-r--r--  1 root root  127 Aug 27  2015 .bash_logout
-rw-r--r--  1 root root  193 Aug 27  2015 .bash_profile
-rw-r--r--  1 root root  551 Aug 27  2015 .bashrc
drwx------  2 root root 4096 Aug 28  2015 .ssh
```

Copy them to `/home/nao`. You will discover that you don't have the right permissions to do that because you are not root. Following workaround will work: `cat` and copy this files.

Create the `.bashrc`:

```
cat /etc/skel/.bashrc

Copy content

nano /home/nao/.bashrc

Paste content
```

Create the `.bash_logout`:

```
cat /etc/skel/.bash_logout

Copy content

nano /home/nao/.bash_logout

Paste content
```

Create the `.bash_profile`:

```
cat /etc/skel/.bash_profile

Copy content

nano /home/nao/.bash_profile

Paste content
```

Now add the `$PYTHONPATH` to `.bashrc` and `.bash_profile`. After that you can run the aldebaran python packages from remote:

```
echo 'export PYTHONPATH=/opt/aldebaran/lib/python2.7/site-packages' >> /home/nao/.bashrc
echo 'export PYTHONPATH=/opt/aldebaran/lib/python2.7/site-packages' >> /home/nao/.bash_profile
```

You can proof that nao has the right to read the bash files:

```
ls -la /home/nao
total 3532
drwxr-xr-x 12 nao  nao     4096 Nov 17 14:53 .
drwxr-xr-x  3 root root    4096 Aug 28  2015 ..
-rw-------  1 nao  nao     2813 Sep 17  2009 .bash_history
-rw-r--r--  1 nao  nao      127 Nov 17 14:53 .bash_logout
-rw-r--r--  1 nao  nao      254 Nov 17 14:54 .bash_profile
-rw-r--r--  1 nao  nao      626 Nov 17 14:54 .bashrc
```

Or simple move the bash files from this repository to `/home/nao`:

```
wget https://raw.githubusercontent.com/Michdo93/albehaviormanager/main/.bash_logout.bak
wget https://raw.githubusercontent.com/Michdo93/albehaviormanager/main/.bash_profile.bak
wget https://raw.githubusercontent.com/Michdo93/albehaviormanager/main/.bashrc.bak
mv .bash_logout.bak .bash_logout
mv .bash_profile.bak .bash_profile
mv .bashrc.bak .bashrc
```

#### Execution:

Run without sshpass...

List all behaviors:

```
/usr/bin/ssh -t -o StrictHostKeyChecking=no nao@<ip> 'source /home/nao/.bash_profile; python albehaviormanager.py --function getBehaviorNames'
```

Run a specific behavior with `python albehaviormanager.py --function runBehavior --behavior_name <behavior_name>`:

```
/usr/bin/ssh -t -o StrictHostKeyChecking=no nao@<ip> 'source /home/nao/.bash_profile; python albehaviormanager.py --function runBehavior --behavior_name "System/animations/Stand/BodyTalk/Speaking/BodyTalk_1"'
```

Stop the specific behavior with `python albehaviormanager.py --function stopBehavior --behavior_name <behavior_name>`:

```
/usr/bin/ssh -t -o StrictHostKeyChecking=no nao@<ip> 'source /home/nao/.bash_profile; python albehaviormanager.py --function stopBehavior --behavior_name "System/animations/Stand/BodyTalk/Speaking/BodyTalk_1"'
```

or with sshpass...

List all behaviors

```
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no nao@<ip> 'source /home/nao/.bash_profile; python albehaviormanager.py --function getBehaviorNames'
```

Run a specific behavior with `python albehaviormanager.py --function runBehavior --behavior_name <behavior_name>`:

```
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no nao@<ip> 'source /home/nao/.bash_profile; python albehaviormanager.py --function runBehavior --behavior_name "System/animations/Stand/BodyTalk/Speaking/BodyTalk_1"'
```

Stop the specific behavior with `python albehaviormanager.py --function stopBehavior --behavior_name <behavior_name>`:

```
/usr/bin/sshpass -p <password> /usr/bin/ssh -t -o StrictHostKeyChecking=no nao@<ip> 'source /home/nao/.bash_profile; python albehaviormanager.py --function stopBehavior --behavior_name "System/animations/Stand/BodyTalk/Speaking/BodyTalk_1"'
```

## Additional Changes

You can also change the `hostname`:

```
hostnamectl set-hostname <hostname>
chown -R nao:nao /etc/hosts
echo '127.0.1.1 <hostname>' >> /etc/hosts
sudo reboot
```

Notice: If you are using a nao robot you can run `sudo shutdown -h now` without knowing the root password but not `sudo reboot`. So if you are using a nao robot you have to poweroff and start again for restarting your nao.
