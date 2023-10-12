import requests
import json

def repos(user):
    path = ('https://api.github.com/users/{0}/repos').format(user)
    data = requests.get(path).json()
    #data = json.loads(data)
    userRepos = []
    for dict in data:
        userRepos.append(dict.get('name'))
    return userRepos

def commits(user, repos):
    repoCommits = {}
    for repo in repos:
        path = ('https://api.github.com/repos/{0}/{1}/commits').format(user, repo)
        print('Repo: ' + repo + ' Number of Commits: ' + str(len(requests.get(path).json())))
        #repoCommits[repo] = len(requests.get(path).json())
    #return repoCommits

userRepos = repos('richkempinski')
commits('richkempinski', userRepos)