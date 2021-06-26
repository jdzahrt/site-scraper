import requests
from bs4 import BeautifulSoup as bs


def get_user_info():
    github_user = input('Input GitHub User: ')

    return github_user


def get_user_url(github_user):
    user_url = f'https://github.com/{github_user}'

    return user_url


def get_image(user_url):
    req = requests.get(user_url)

    soup = bs(req.content, 'html.parser')

    profile_image = soup.find('img', {'alt': 'Avatar'})['src']

    print(profile_image)


def get_readme(user, repo):
    req = requests.get(f'https://raw.githubusercontent.com/{user}/{repo}/master/README.md')

    with open('test.md', 'wb') as f:
        f.write(req.content)


def main():
    user = get_user_info()
    user_url = get_user_url(user)

    get_image(user_url)

    get_readme(user, 'github-notifications')

    # # get_repos(user_url)


if __name__ == '__main__':
    main()
