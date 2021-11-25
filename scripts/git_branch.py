import subprocess
import re
import uuid


def get_branch_name(strip_punctuation: bool = False, make_unique: bool = False) -> str:
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

    if make_unique:
        new_branch = f"{git_branch}-{str(uuid.uuid4())}"
        return new_branch
    
    return git_branch

if __name__ == "__main__":
    print(get_branch_name())
    print(get_branch_name(make_unique=True))