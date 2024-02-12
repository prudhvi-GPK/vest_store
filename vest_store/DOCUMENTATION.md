# Documantation for vest_store project.

### Set Up Git Repository and Add Collaborators:

1. **Create a Git Repository:**
   - Initialize a Git repository in project directory:

     ```bash
     git init
     ```

2. **Create a Remote Repository:**
   - Create a remote repository on a platform like GitHub called `vest_store`.

3. **Add Collaborators:**
   - Add teammates as collaborators on the Git repository through the platform's interface.

4. **Link Local Repository to Remote Repository:**
   - Link local repository to the remote repository:

     ```bash
     git remote add origin https://github.com/username/vest_store.git
     ```

5. **Push to Remote Repository:**
   - Push local repository to the remote repository:

     ```bash
     git push -u origin master
     ```

### Initialize a Django Project:

1. **Install Miniconda:**
   - Download and install Miniconda from the [official website](https://docs.conda.io/en/latest/miniconda.html).

2. **Create a Virtual Environment:**
   - Open a terminal or command prompt.
   - Navigate to your project directory.
   - Run the following command to create a new virtual environment:

     ```bash
     conda create --name your_env_name python=3.x
     ```

3. **Activate the Virtual Environment:**
   - Activate the virtual environment using:
     - On Windows: `conda activate your_env_name`
     - On macOS/Linux: `source activate your_env_name`

4. **Install Django:**
   - With the virtual environment activated, install Django using pip:

     ```bash
     pip install django
     ```

5. **Create and Set Up Your Django Project:**
   - Navigate to your project directory.
   - Run the following command to create a new Django project `vest_store`
     ```bash
     django-admin startproject vest_store
     ```

6. **Navigate into Your Project Directory:**
     ```bash
     cd vest_store
     ```

7. **Run Migrations:**
   - Run migrations to create the initial database:

     ```bash
     python manage.py migrate
     ```

8. **Create a Django App:**
   - Run the following command to create a Django app within your project `vest_store_app`

     ```bash
     python manage.py startapp vest_store_app
     ```

### CREATE ABOUT PAGE AND ADD CONTENT

1. In vest_store  `urls.py` create a new url path to redirect everything to homepage
2. add vest_store in INSTALLED_APPS of `settings.py`.
3. Create a tempalte for `about.html`
4. write view for redirecting the url related to `about_page`.
5. create a url path for about in `urls.py` of `vest_store_app`
6. add the content in `about.html` in as per the css and html format.

### CREATE CART PAGE

1. Create a tempalte for `cart.html`
2. write view for redirecting the url related to `cart_page`.
3. create a url path for about in `urls.py` of `vest_store_app`
4. add the css,html,bootstrap content in `cart.html`.