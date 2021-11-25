import subprocess
import re


def get_branch_name(strip_punctuation: bool = False) -> str:
    """
    Runs a subprocess to get the current git branch.
    """
    git_branch = (
        subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], check=True, capture_output=True
        )
        .stdout.decode("utf-8")
        .strip()
    )

    if strip_punctuation:
        return re.sub("[\W_]+", "", git_branch)
    
    return git_branch

if __name__ == "__main__":
    print(get_branch_name())