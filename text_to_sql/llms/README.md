# 📦 Git Submodule Guide for LLMs

This repository uses Git submodules to include other repositories as part of its structure. This guide covers both:

- ✅ How to add a new submodule (for maintainers).
- 🔄 How to initialize/update submodules (for contributors and CI).

## ➕ Adding a New Submodule (For Maintainers)

Run this command from the root of the repository:

```bash
git submodule add https://github.com/<owner>/<repo>.git <destination-path>
```

Example:

```bash
git submodule add https://github.com/mahant-solutions/llms.git ./text_to_sql/llms
```

Then, run:

```bash
git submodule update --init --recursive
```

And commit the changes:

```bash
git commit -am "Added llms as a submodule"
```

This will:

- Create/update a .gitmodules file.
- Stage the submodule reference in the main repo.
- Ensure the submodule is checked out properly.

## 📥 Cloning the Repository with Submodules (For Everyone)

If you’re cloning the repo for the first time, use:

```bash
git clone --recurse-submodules https://github.com/<your-org>/<your-repo>.git
```

Or, if you’ve already cloned it:

```bash
git submodule update --init --recursive
```

## 🔄 Updating Submodules

To pull the latest changes from the main repo and update all submodules:

```bash
git pull --recurse-submodules
git submodule update --recursive --remote
```

## 🧪 Optional: Setup Script

You can create a helper script like init-submodules.sh:

```bash
#!/bin/bash
echo "Initializing submodules..."
git submodule update --init --recursive
```

Make it executable:

```bash
chmod +x init-submodules.sh
```

Run it any time with:

```bash
./init-submodules.sh
```

## 📄 Notes

- Submodules are pinned to specific commits—they don’t auto-update unless you explicitly pull inside them.
- Make sure you have permission to access private submodules (e.g., through GitHub login, credentials helper, or token-based access).

## 🧵 Detailed Breakdown

1. `git pull --recurse-submodules`
   - Purpose: Sync your local repo with the remote main repository, including submodules.
   - It pulls changes in the parent repository and then checks out each submodule to the specific commit referenced by the updated parent repo.
   - It does NOT fetch the latest changes from the submodule’s remote—it just checks out the pinned commit.

   Think of it like:

   “Follow whatever commit the main repo is pointing to for each submodule.”

2. `git submodule update --recursive --remote`
   - Purpose: Actively updates submodules to the latest commit on their tracking branch (usually main or master).
   - It ignores what commit the main repo is pointing to and instead fetches the latest from the submodule’s remote.
   - Useful when you want to upgrade the submodule to the latest available version.
