# Setup night (Tue Nov 24)

About 90 minutes. Do the steps in order: each one depends on the one before it.
Mac and Windows differences are marked.

## 1. GitHub account (10 min)

1. Sign up at github.com (or sign in if you already have an account).
2. Turn on two-factor authentication: profile picture → Settings → Password and authentication.
3. Install **GitHub Desktop** from desktop.github.com and sign in with that account.

## 2. Turso and Streamlit, using "Sign in with GitHub" (15 min)

Using your GitHub login for both means one password instead of three.

1. **Turso:** go to app.turso.tech → Continue with GitHub.
   - Create a database named after your project (lowercase, dashes, for example `westgate-payroll`).
   - Open the database → copy the URL (it starts with `libsql://`).
   - Create a token → copy it. Turso shows it only once, so paste it into your `.env` right away (step 4).
2. **Streamlit Community Cloud:** go to share.streamlit.io → Continue with GitHub → allow access to your repositories.

## 3. Your project repo (20 min)

> **Already built most of your project?** If your repo already has `CLAUDE.md` and `pyproject.toml`, skip the `git pull` command below. The template would clash with your own files. Just copy `SETUP.md` and `scripts/check_setup.py` from the template into your repo.

You already have a repo. We clone it, then pull the class template into it.

1. On your repo's GitHub page: **Code** → **Open with GitHub Desktop** → Clone.
   - Mac: it lands in `~/Documents/GitHub/<your-repo>`.
   - Windows: it lands in `Documents\GitHub\<your-repo>`.
2. In GitHub Desktop: **Repository** → **Open in Terminal** (Mac) or **Open in Command Prompt** (Windows).
   - Windows: if it says Git is not installed, install Git for Windows from git-scm.com (all defaults), then try again.
3. Paste this one command and press Enter:

   ```
   git pull --no-rebase https://github.com/Rollins-College-DTAC/da-ai-capstone-template main --allow-unrelated-histories --no-edit
   ```

   - **Empty repo:** done. You now have every template file.
   - **Repo with files:** if it says `CONFLICT` in `README.md`, and your README held only your repo name (GitHub adds one when you tick "Add a README"), keep the template's README with:

     ```
     git checkout --theirs README.md && git add README.md && git commit --no-edit
     ```

   - Any other `CONFLICT`: stop and raise your hand. Don't guess at a conflict.
4. Back in GitHub Desktop: **Push origin**.
5. Make sure the repo is **Public** (Settings → General → Danger Zone → Change visibility), since this is your portfolio piece.
6. Settings → Collaborators → add your instructor.
7. Settings → Code security → turn on **Secret scanning** and **Push protection**. GitHub then blocks a push that contains a key.

## 4. Your .env file (15 min)

The `.env` file holds your keys. Git ignores it, so it never goes to GitHub.

1. Make a copy of `.env.example` named `.env`:
   - Mac (Terminal, in the project folder): `cp .env.example .env`
   - Windows (Command Prompt, in the project folder): `copy .env.example .env`
2. Open `.env` in a text editor and paste in the shared keys from your instructor and your Turso URL and token.
3. Things that go wrong:
   - **Mac:** Finder hides files that start with a dot. Press `Cmd + Shift + .` to show them.
   - **Windows:** Notepad may save it as `.env.txt`. In File Explorer → View → turn on **File name extensions**, then rename it to exactly `.env`.

## 5. Install uv and run the setup check (15 min)

`uv` installs Python and the project's packages for you.

- Mac (Terminal): `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows (PowerShell): `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`

Close and reopen the terminal, go to the project folder, then run:

```
uv sync
uv run python scripts/check_setup.py
```

Fix anything marked `FIX` and run the check again until it says **All set**.

## 6. Move your existing work in, then make the first push (20 min)

1. Copy your existing project files into the repo folder.
2. **Before you commit, look at GitHub Desktop's Changes list:**
   - `.env` must NOT be in the list. If it is, stop and ask your instructor.
   - No real customer, employee or company data. This project uses simulated data only.
   - No keys pasted into code, notebooks or notes.
3. Write a summary (for example "Move in existing work") → **Commit to main** → **Push origin**.

## 7. Deploy the placeholder app (10 min)

1. share.streamlit.io → **Create app** → choose your repo, branch `main`, file `streamlit_app.py`.
2. Advanced settings → Secrets → paste the lines from `.streamlit/secrets.toml.example` with your real values.
3. Deploy. Send your instructor the app URL. That URL is your exit ticket for tonight.
