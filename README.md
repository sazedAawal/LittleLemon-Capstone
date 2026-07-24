# LittleLemon-Capstone
---
    - Apps: LittleLemonAPI(For testing)
    - restaurant(main app)

**Criteria Overview**
-   Web application to use Django to serve static HTML content
-   Connect the backend to a MySQL database
-   Implement menu and table booking APIs
-   Application to be set up with user registration and authentication
-   Application to contain unit tests
-   API is to be tested with the Insomnia REST client

**SuperUser**
- username: capstoneUser
- email: cUser@llemon.com
- password: cUser123!
- token: 9725bc058659030e96333e970a69dd671a690ecb

**Dependencies**
- pip install django
- pip install djangorestframework
- pip install djangorestframework-xml
- pip install djoser
- pip install mysqlclient

**Database**
- CREATE DATABASE l_lemon_capstone;

**For Testing**
- GRANT ALL PRIVILEGES ON *.* TO 'main-user'@'127.0.0.1' WITH GRANT OPTION;


**URLs**
- http://127.0.0.1:8000/
- http://127.0.0.1:8000/about/
- http://127.0.0.1:8000/menu/
- http://127.0.0.1:8000/menu_item/<id>/
- http://127.0.0.1:8000/book/
- http://127.0.0.1:8000/admin/

- http://127.0.0.1:8000/router/users/
- http://127.0.0.1:8000/router/test-users/
- http://127.0.0.1:8000/auth/users/

- http://127.0.0.1:8000/auth/users/me/
- http://127.0.0.1:8000/auth/token/login/
- http://127.0.0.1:8000/auth/token/logout/

- http://127.0.0.1:8000/api-auth/login/
- http://127.0.0.1:8000/api-auth/logout/

- http://127.0.0.1:8000/api/api-menu/
- http://127.0.0.1:8000/api/bookings/
- http://127.0.0.1:8000/api/bookings/<id>/
- http://127.0.0.1:8000/api/api-token-auth/

- http://127.0.0.1:8000/api/menu-items/
- http://127.0.0.1:8000/api/menu-items/<id>
- http://127.0.0.1:8000/api/message/
- http://127.0.0.1:8000/api/registration/
- http://127.0.0.1:8000/api/test/menu-items-test/
