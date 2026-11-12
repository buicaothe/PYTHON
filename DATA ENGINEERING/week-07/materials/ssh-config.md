# SSH config for the course virtual machine

The SSH config file stores the address, username, and key for a host, so a short name is enough to log in. The file lives on **your own computer**, next to the key from week 6. It is not a file on the virtual machine.

On Windows that folder is

```text
C:\Users\jmakkonen24\.ssh\config
```

with your own Windows username in place of `jmakkonen24`. Git Bash writes the same file as `~/.ssh/config`. `~` means your home directory, which on Windows is `C:\Users\YourName`.

## 1. Open the file

**Git Bash** (the terminal from week 6):

```bash
mkdir -p ~/.ssh
notepad ~/.ssh/config
```

**PowerShell:**

```powershell
New-Item -ItemType Directory -Force -Path $env:USERPROFILE\.ssh
notepad $env:USERPROFILE\.ssh\config
```

Notepad creates the file if it is missing. If `config` already has other `Host` blocks, add the new block at the end and leave the old ones in place. Save with `Ctrl+S`, then close Notepad.

`nano ~/.ssh/config` is the same step in Git Bash when `nano` is installed. Save with `Ctrl+O`, then Enter, and leave with `Ctrl+X`.

## 2. The host block

`Host` is the short name you will type. `HostName` is the real address. `User` is your username on the virtual machine. `IdentityFile` is the private key created in week 6.

For the student **jmakkonen24** the block is:

```text
Host 2026_deai_intro
  HostName 2026-deai-intro.kuusipalaa.com
  User jmakkonen24
  IdentityFile ~/.ssh/id_ed25519
```

Write your own username on the `User` line. The other three lines stay as they are.

`~/.ssh/id_ed25519` works in Git Bash and in Windows PowerShell. A full Windows path also works, written with forward slashes:

```text
IdentityFile C:/Users/jmakkonen24/.ssh/id_ed25519
```

Use your own name in that path. Backslashes in `IdentityFile` are easy to get wrong, so keep the forward slashes.

## 3. Check the file, then connect

Print the file from Git Bash:

```bash
cat ~/.ssh/config
```

The same print from PowerShell:

```powershell
Get-Content $env:USERPROFILE\.ssh\config
```

The line `IdentityFile` is only a path. Printing the config does not print the private key.

Connect with the short name. This is the same command in Git Bash and in PowerShell:

```bash
ssh 2026_deai_intro
```

The first time, SSH asks whether to trust the server. Type `yes`. A later login goes straight to the shell on the virtual machine.

If Windows refuses the file and the message mentions permissions, restrict the config to your user in PowerShell, then try `ssh` again:

```powershell
icacls $env:USERPROFILE\.ssh\config /inheritance:r /grant:r "${env:USERNAME}:(R,W)"
```
