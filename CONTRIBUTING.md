# Contributing to The Open CodeYard

Thanks for stopping by the junkyard.

The Open CodeYard is a zero-shame digital junkyard for random prototypes, abandoned projects, throwaway scripts, old coding memories, and wild ideas.

## Ground Rules

- **No perfectionism.** Messy code, half-baked ideas, and ugly prototypes are welcome.
- **No judgment.** Share your experiments, abandoned projects, and "what if..." moments.
- **License stays.** Every contribution is released under this project's license. See [LICENSE](LICENSE).
- **Keep it legal.** Only contribute code you have the right to share.
- **Keep it light.** Keep individual projects under 5 MB. No `node_modules`, build artifacts, or binaries unless essential to demo. Big projects belong in their own repo.

## What You Can Contribute

Almost anything belongs here, including:

- Experimental projects
- Half-finished ideas
- Abandoned but useful code
- Reusable snippets
- Small bots
- Game prototypes
- Algorithms
- UI components
- API examples
- Learning exercises

If you built it, forgot about it, and don't want it collecting dust on your hard drive, it's probably a good fit.

---

# How to Contribute

> [!NOTE]
> First time contributing to GitHub? Check out **[first-contributions](https://github.com/firstcontributions/first-contributions)**.

If this repository eventually grows into hundreds of projects, cloning everything just to contribute one small script becomes unnecessary. Pick whichever workflow fits you best.

## Option A: Browser Only (No Git Required)

Perfect if you're contributing a single file or a small project.

1. Fork this repository.
2. Navigate to the appropriate yard folder (for example, `prototypes/memos-and-scraps/`).
3. Click **Add file → Create new file**.
4. Paste your code, commit the changes, and open a Pull Request.

---

## Option B: Sparse Checkout (Git)

Want to use your local editor without downloading the entire junkyard? Use Git's sparse checkout.

```bash
# Clone only the repository structure
git clone --filter=blob:none --sparse https://github.com/speedyk-005/OpenCodeYard.git
cd OpenCodeYard

# Initialize sparse checkout
git sparse-checkout init --cone

# Download only the folder you need
git sparse-checkout set yards/scraps/
```

---

# Folder Layout

Every project should live inside a folder named after your GitHub username. That keeps everyone's scraps separate and avoids accidental conflicts.

```txt  
yards/  
└── [your-chosen-yard]/  # scraps or prototypes  
    └── [your-github-username]/  
        └── [your-project-name]/  
            ├── app.py / index.js / main.go  <-- Your raw code  
            ├── requirements.txt / package.json <-- Your local dependencies  
            └── README.md                    <-- Your scrap label  
```

---

# Project README

Every project should include a small `README.md` so people digging through the yard know what they're looking at.

```md
# Image Compressor

Status: Abandoned
Main Language: Python
Accepting Contributions: Yes

---

## What it does

Compresses PNG images using Pillow.

## How to use it

...

## Notes

...
```

Keep it short. Nobody expects a thesis for scrap metal.

---

# Pull Request Guidelines

Keep things simple.

- Use a clear, descriptive PR title.
- Don't use Conventional Commit prefixes (`feat:`, `fix:`, etc.).
- Put your project in the folder where it belongs.
- Don't overthink it.

---

# Legal Stuff (Apache 2.0)

By submitting code, you agree to license your contribution under the Apache 2.0 License.

In plain English:

- Anyone can use, modify, and redistribute your code.
- Commercial use is allowed.
- Contributors receive patent protection provided by the license.

See the [LICENSE](LICENSE) file for the full legal text.

---

# Code of Conduct

Don't be a jerk.

That's the whole code of conduct.
