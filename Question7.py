class RouteTrieNode:
    def __init__(self, handler = None):
        self.handler = handler
        self.children = {}
    
    def insert(self, path_endpoint, handler):
         self.children[path_endpoint] = RouteTrieNode(handler)
         
    def __repr__(self):
        return str(self.children)

 
class RouteTrie:
    def __init__(self,root_handler = None):
        self.root = RouteTrieNode(root_handler)

     
    def insert(self, path_endpoints, handler):
    
        current_node = self.root
        #Set length of path
        for path_endpoint in path_endpoints:
            if path_endpoint not in current_node.children:
                current_node.children[path_endpoint] = RouteTrieNode(None)
            #Advance current node
            current_node = current_node.children[path_endpoint]
        #Insert handler tp current node
        current_node.handler = handler
        

    def find(self, path_endpoints):
        if len(path_endpoints) == 0:
            return self.root.handler
        #Set current node to root
        current_node = self.root
        for path_endpoint in path_endpoints:
            if path_endpoint not in current_node.children:
                return None 
            #Advance current node
            current_node =  current_node = current_node.children[path_endpoint]

        return current_node.handler


# The Router class wraps the RouteTrie class 
      
class Router:
    def __init__(self, handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(handler)
        self.route_trie.root.handler = handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_endpoints = self.split_path(path)
        self.route_trie.insert(path_endpoints , handler)
        

    def lookup(self,path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_endpoints = self.split_path(path)
        return  self.route_trie.find(path_endpoints)

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here

        if path == "/":
            return []
        path_endpoints = path.split('/')
        #remove the initial empty string from path_endpoints 
        path_endpoints.remove('')
        return path_endpoints

# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


print("-------------------------------------------------------------------------------------------------------------------------")
routing = Router("root handler")
routing.add_handler("/udapeople/users/id", "user information")

print(routing.lookup("/")) # should print 'root handler'
print(routing.lookup("/udapeople/users")) # should print 'not found handler' or None if you did not implement one
print(routing.lookup("/udapeople/users/id")) # should print 'user information'




#  empty route input : returns root handler
print(router.lookup("")) # should print 'root handler'