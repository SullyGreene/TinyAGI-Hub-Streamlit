
import os
import git
import logging

logger = logging.getLogger(__name__)

def clone_or_update_repo(repo_url, repo_dir):
    if not os.path.exists(repo_dir):
        try:
            logger.info(f"Cloning repository from '{repo_url}' to '{repo_dir}'.")
            git.Repo.clone_from(repo_url, repo_dir)
            logger.info("Repository cloned successfully.")
        except Exception as e:
            logger.error(f"Failed to clone repository: {e}")
    else:
        try:
            repo = git.Repo(repo_dir)
            logger.info(f"Pulling latest changes in '{repo_dir}'.")
            repo.remotes.origin.pull()
            logger.info("Repository updated successfully.")
        except Exception as e:
            logger.error(f"Failed to update repository: {e}")
