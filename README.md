# MLOps CI/CD Using GitHub Actions

Iris classification using Logistic Regression, an 80/20 train/test split and automated pytest checks. The workflow runs on pushes and pull requests to main. Deployment is simulated only after successful tests on a push to main; no cloud resources are created.

## Local execution

```sh
python -m pip install -r requirements.txt
python -m pytest -v
python app.py
```

## Failure demonstration
After the initial workflow passes, temporarily replace `assert accuracy >= 0.80` with `assert accuracy > 1.00` in tests/test_model.py. Commit and push, observe the failed test and skipped deployment. Restore the original test and push again to verify recovery. The intentionally impossible threshold is only for testing CI failure handling.
