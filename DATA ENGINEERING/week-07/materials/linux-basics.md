# Linux basics on the course virtual machine

Week 6 used Git Bash on your own computer. This week the commands run on the course virtual machine. Set up the short name `2026_deai_intro` in `week-07/materials/ssh-config.md`, then log in from your own computer:

```bash
ssh 2026_deai_intro
```

The line that waits for a command is the shell. You type a command, press Enter, and the shell prints the result under it. Practice in a folder of your own so the course repository stays untouched until you copy the homework across.

```bash
mkdir ~/week-07
cd ~/week-07
```

`~` is your home directory.

## 1. Where you are

`pwd` prints the current directory. `ls` prints the names in it. `ls -l` adds the size and the date.

```bash
pwd
ls
ls -l
```

`cd` changes directory. `cd ~/week-07` returns to the practice folder. Names are case-sensitive: `Notes.txt` and `notes.txt` are different files. When a name contains a space, wrap it in quotes.

## 2. Create a file with nano

`nano` is a small editor that runs in the terminal. This opens `notes.txt`, or creates it if it is not there yet.

```bash
nano notes.txt
```

Type a line of text. The bar at the bottom lists actions. `^` means the Ctrl key.

- `Ctrl+O`, then Enter, writes the file to disk.
- `Ctrl+X` leaves nano. If nano asks whether to save a modified buffer, press `Y`, then Enter.

## 3. Print a file with cat

`cat` prints the whole file to the terminal.

```bash
cat notes.txt
```

`head` prints only the start of a file. The count after `-n` is the number of lines. Use it on a long download so the terminal stays readable.

```bash
head -n 15 notes.txt
```

## 4. Rename a file with mv

`mv` changes the name. After this command the file is `greeting.txt`, and `notes.txt` is gone.

```bash
mv notes.txt greeting.txt
ls
```

When the second name is an existing directory, `mv` moves the file into that directory and keeps the file name.

## 5. Copy a file with cp

`cp` makes a second file and leaves the original in place.

```bash
cp greeting.txt greeting-copy.txt
ls -l
```

The first name is the source. The second name is the copy. Copying onto an existing name replaces that file.

## 6. Download a page with wget

`wget` fetches a URL and saves the response as a file in the current directory. This saves the Google front page. The plain command takes the file name from the URL, which for this address is `index.html`.

```bash
wget https://www.google.com/
ls -l index.html
head -n 15 index.html
```

`-O` chooses the file name yourself. The capital letter matters.

```bash
wget -O google-index.html https://www.google.com/
```

`curl` does the same download. `-L` follows a redirect, and `-o` sets the file name.

```bash
curl -L -o google-index.html https://www.google.com/
```

The saved file is HTML. The first lines usually contain `<!doctype html>` or `<html>`.

## Homework

The exercises are in `week-07/assignments/`. Copy the files you create, and paste the terminal output, into `week-07/student_work/homework_answers/`.
