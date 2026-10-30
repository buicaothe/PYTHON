# Git setup on Windows

Use **Git Bash** for the commands below. It is installed together with Git for Windows. The course repository is on the school GitLab, and the branch name is `main`.

## 1. Install Git

1. Download Git for Windows from [https://git-scm.com/download/win](https://git-scm.com/download/win).
2. Run the installer. The defaults are fine. When it asks about line endings, keep **Checkout Windows-style, commit Unix-style line endings**.
3. Open **Git Bash** from the Start menu.

Check that Git is available:

```bash
git --version
```

## 2. Tell Git who you are

Git stores this name and email in every commit. Use the email address registered on the school GitLab.

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Check the result:

```bash
git config --global --list
```

## 3. Create an SSH key

The school GitLab address used by Git is `git@git.dc.turkuamk.fi`. An SSH key lets you push without typing a password each time.

Create a key. Press Enter to accept the default file location. You can also press Enter for an empty passphrase.

```bash
ssh-keygen -t ed25519 -C "your.email@example.com"
```

Show the public key and copy the whole line. It starts with `ssh-ed25519`.

```bash
cat ~/.ssh/id_ed25519.pub
```

Add it to GitLab:

1. Open [https://git.dc.turkuamk.fi](https://git.dc.turkuamk.fi).
2. Go to **Preferences** → **SSH Keys**.
3. Paste the public key and save it.

Test the connection. The first time, type `yes` when asked whether to trust the server. A successful test says you have authenticated, then tells you that shell access is not allowed. That message means the key works.

```bash
ssh -T git@git.dc.turkuamk.fi
```

## 4. Clone your repository

On the project page in GitLab, choose **Clone** → **Clone with SSH** and copy the address. In Git Bash, go to the folder where you want the project, then clone it. `origin` is the name Git gives that remote.

```bash
cd /c/Users/YourName/Documents
git clone git@git.dc.turkuamk.fi:your-group/your-project.git
cd your-project
```

## 5. Add a file and commit it

Create a file, or copy one into the project folder. This example uses `notes.txt`.

```bash
echo "First note" > notes.txt
git status
```

`git status` shows `notes.txt` as untracked. Stage it, then commit. A commit is a saved snapshot on your computer. It is not on GitLab yet.

```bash
git add notes.txt
git commit -m "Add notes.txt"
```

To stage every changed file in the current folder:

```bash
git add .
```

## 6. Push and set the upstream

The first push of a branch needs `-u`. That flag sends the commit to `origin` and records `origin/main` as the **upstream** of your local `main` branch. Later, `git push` and `git pull` know which remote branch to use.

```bash
git push -u origin main
```

Check the tracking:

```bash
git status
```

The status line should say that `main` is up to date with `origin/main`.

After this first push, the everyday sequence is:

```bash
git add notes.txt
git commit -m "Update notes.txt"
git push
```

## Pull new course material

If the course project was added as a second remote named `upstream`, download its changes with pull. Push your own work to `origin`, which is your repository.

```bash
git pull origin main
git push
```
