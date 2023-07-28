import requests

def get_repos_list(repos_url: str):
    repos = []
    repository = requests.get(repos_url).json()
    for i in range(len(repository)):
        repos.append(repository[i]['name'])
    
    return repos

def get_github_user(username):
    url = f'https://api.github.com/users/{username}'
    response = requests.get(url)

    if response.status_code == 200:
        user_data = response.json()
        # Traitez les données de l'utilisateur ici
        
        list_repos = get_repos_list(user_data['repos_url'])
        print(list_repos)
        print(user_data)
        return user_data
    else:
        print(f"Erreur de requête. Code de statut : {response.status_code}")
        return 

if __name__ == "__main__":
    # Utilisez la fonction pour obtenir les informations d'un utilisateur
    get_github_user('Tokomichel')
   