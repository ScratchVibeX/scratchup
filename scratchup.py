class ScratchUp:
    """
    ScratchUp: A safe and advanced Python library for interacting with Scratch's APIs.
    Provides enhanced features with safety and user-friendliness in mind.
    """

    import requests

    def __init__(self, username, password):
        if not isinstance(username, str) or not isinstance(password, str):
            raise ValueError("Username and password must be strings.")
        self.username = username
        self.password = password
        self.session = self.requests.Session()
        self.base_url = "https://api.scratch.mit.edu"
        self.csrf_token = None
        self.session_id = None
        self.logged_in = False

    def _check_login(self):
        if not self.logged_in:
            raise PermissionError("You must be logged in to perform this action.")

    def login(self):
        """Logs in to Scratch and saves the session details securely."""
        login_url = "https://scratch.mit.edu/login/"
        login_data = {
            "username": self.username,
            "password": self.password
        }

        try:
            response = self.session.post(login_url, json=login_data)
            response.raise_for_status()
            if 'token' in response.cookies:
                self.session_id = response.cookies['scratchsessionsid']
                self.csrf_token = response.cookies['scratchcsrftoken']
                self.logged_in = True
                print("Logged in successfully.")
            else:
                raise RuntimeError("Login failed. Please check your credentials.")
        except Exception as e:
            print(f"An error occurred during login: {e}")

    def get_user_info(self, target_username):
        """Gets the information of a specified Scratch user."""
        if not isinstance(target_username, str):
            raise ValueError("Target username must be a string.")

        url = f"{self.base_url}/users/{target_username}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"Failed to fetch user information: {e}"}

    def get_project_info(self, project_id):
        """Gets the information of a specified Scratch project."""
        if not isinstance(project_id, str):
            raise ValueError("Project ID must be a string.")

        url = f"{self.base_url}/projects/{project_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"Failed to fetch project information: {e}"}

    def comment_on_project(self, project_id, comment):
        """Posts a comment on a Scratch project."""
        self._check_login()
        if not isinstance(project_id, str) or not isinstance(comment, str):
            raise ValueError("Project ID and comment must be strings.")

        url = f"{self.base_url}/comments/project/{project_id}/"
        headers = {
            "X-CSRFToken": self.csrf_token,
            "Referer": f"https://scratch.mit.edu/projects/{project_id}/",
        }
        data = {"content": comment}

        try:
            response = self.session.post(url, headers=headers, json=data)
            response.raise_for_status()
            return {"success": "Comment posted successfully."}
        except Exception as e:
            return {"error": f"Failed to post comment: {e}"}

    def follow_user(self, target_username):
        """Follows a specified Scratch user."""
        self._check_login()
        if not isinstance(target_username, str):
            raise ValueError("Target username must be a string.")

        url = f"{self.base_url}/users/{target_username}/followers/"
        headers = {
            "X-CSRFToken": self.csrf_token,
            "Referer": f"https://scratch.mit.edu/users/{target_username}/",
        }

        try:
            response = self.session.post(url, headers=headers)
            response.raise_for_status()
            return {"success": f"You are now following {target_username}."}
        except Exception as e:
            return {"error": f"Failed to follow user: {e}"}

    def get_studio_info(self, studio_id):
        """Gets information about a specified Scratch studio."""
        if not isinstance(studio_id, str):
            raise ValueError("Studio ID must be a string.")

        url = f"{self.base_url}/studios/{studio_id}"
        try:
            response = self.session.get(url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return {"error": f"Failed to fetch studio information: {e}"}

    def add_project_to_studio(self, studio_id, project_id):
        """Adds a project to a Scratch studio."""
        self._check_login()
        if not isinstance(studio_id, str) or not isinstance(project_id, str):
            raise ValueError("Studio ID and Project ID must be strings.")

        url = f"{self.base_url}/studios/{studio_id}/projects/{project_id}/"
        headers = {
            "X-CSRFToken": self.csrf_token,
            "Referer": f"https://scratch.mit.edu/studios/{studio_id}/",
        }

        try:
            response = self.session.post(url, headers=headers)
            response.raise_for_status()
            return {"success": "Project added to studio successfully."}
        except Exception as e:
            return {"error": f"Failed to add project to studio: {e}"}

    def remove_project_from_studio(self, studio_id, project_id):
        """Removes a project from a Scratch studio."""
        self._check_login()
        if not isinstance(studio_id, str) or not isinstance(project_id, str):
            raise ValueError("Studio ID and Project ID must be strings.")

        url = f"{self.base_url}/studios/{studio_id}/projects/{project_id}/"
        headers = {
            "X-CSRFToken": self.csrf_token,
            "Referer": f"https://scratch.mit.edu/studios/{studio_id}/",
        }

        try:
            response = self.session.delete(url, headers=headers)
            response.raise_for_status()
            return {"success": "Project removed from studio successfully."}
        except Exception as e:
            return {"error": f"Failed to remove project from studio: {e}"}

    def love_project(self, project_id):
        """Loves a Scratch project."""
        self._check_login()
        if not isinstance(project_id, str):
            raise ValueError("Project ID must be a string.")

        url = f"{self.base_url}/projects/{project_id}/loves/"
        headers = {
            "X-CSRFToken": self.csrf_token,
            "Referer": f"https://scratch.mit.edu/projects/{project_id}/",
        }

        try:
            response = self.session.post(url, headers=headers)
            response.raise_for_status()
            return {"success": "Project loved successfully."}
        except Exception as e:
            return {"error": f"Failed to love project: {e}"}

    def favorite_project(self, project_id):
        """Favorites a Scratch project."""
        self._check_login()
        if not isinstance(project_id, str):
            raise ValueError("Project ID must be a string.")

        url = f"{self.base_url}/projects/{project_id}/favorites/"
        headers = {
            "X-CSRFToken": self.csrf_token,
            "Referer": f"https://scratch.mit.edu/projects/{project_id}/",
        }

        try:
            response = self.session.post(url, headers=headers)
            response.raise_for_status()
            return {"success": "Project favorited successfully."}
        except Exception as e:
            return {"error": f"Failed to favorite project: {e}"}

# Example usage:
if __name__ == "__main__":
    scratch = ScratchUp("your_username", "your_password")
    try:
        scratch.login()
        print(scratch.get_user_info("griffpatch"))
        print(scratch.get_project_info("123456789"))
        scratch.comment_on_project("123456789", "Amazing project!")
        scratch.follow_user("griffpatch")
        print(scratch.get_studio_info("123456"))
        scratch.add_project_to_studio("123456", "123456789")
        scratch.remove_project_from_studio("123456", "123456789")
        scratch.love_project("123456789")
        scratch.favorite_project("123456789")
    except Exception as e:
        print(f"An error occurred: {e}")
