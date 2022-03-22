from github import Github

g = Github("hellboy8171", "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")
user = g.get_user()
repo = user.create_repo('gam')
