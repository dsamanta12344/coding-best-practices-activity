# Coding Best Practices Activity

A pair of command-line fortune tellers used to demonstrate three programming principles:

1. **DRY** (Don't Repeat Yourself)
2. **Single Responsibility**
3. **Document your code** (including common commenting errors)

## Files

| File | Role |
|------|------|
| `fortune_teller_issues.py` | Same program, written to **violate** the three principles |
| `fortune_teller_fixed.py` | Same program, written to **follow** the three principles |
| `Coding_Best_Practices_Writeup.pdf` | Description of the code and the principles |

## Run

```bash
python fortune_teller_issues.py
python fortune_teller_fixed.py
```

Both programs ask for a name, birth month, and lucky number, then print love, career, and luck readings.

## GitHub workflow (bonus)

Work was split onto feature branches and merged with pull requests:

- [`feature/violations`](https://github.com/dsamanta12344/coding-best-practices-activity/tree/feature/violations) → [PR #1](https://github.com/dsamanta12344/coding-best-practices-activity/pull/1)
- [`feature/fixes`](https://github.com/dsamanta12344/coding-best-practices-activity/tree/feature/fixes) → [PR #2](https://github.com/dsamanta12344/coding-best-practices-activity/pull/2)

Screenshots of the repo, branches, commits, and pull requests are in `screenshots/`.

## Author

Deb Samanta ([dsamanta12344](https://github.com/dsamanta12344))

Completed independently (no partner was available). Both program versions and the write-up are in this repository.
