This creates a connection to the MySQL server running on the local machine via a UNIX socket (or named pipe), the user name “joebob”, the password “moonpie”, and selects the initial database “thangs”.

We haven’t even begun to touch upon all the parameters connect() can take. For this reason, I prefer to use keyword parameters:

db=_mysql.connect(host="localhost",user="joebob",
                  password="moonpie",database="thangs")


