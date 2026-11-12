# Exercise 3 — Download a page with wget

In `~/week-07` on the course virtual machine, save the Google front page:

```bash
wget -O google-index.html https://www.google.com/
ls -l google-index.html
head -n 15 google-index.html
```

Copy `google-index.html` to `student_work/homework_answers/google-index.html`.

Paste the output of `ls -l` and `head` into `student_work/homework_answers/exercise_03.md`. If `wget` prints an error instead of saving a file, paste that error into the same file.
