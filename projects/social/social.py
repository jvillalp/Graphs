import random 
import time


class User:
    def __init__(self, name):
        self.name = name
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)
class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    def fisher_yates_shuffle(self,l):
        for i in range(0, len(l)):
            random_index = random.randint(i, len(l) - 1)
            l[random_index], l[i] = l[i], l[random_index]

    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif friend_id in self.friendships[user_id] or user_id in self.friendships[friend_id]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}
        # !!!! IMPLEMENT ME

        total_friendships = num_users * avg_friendships
        

        # Add users
        ##use num_users to use all the users that we need
        for user in range(num_users):
            self.add_user(user)

        # Create friendships
        ## make a list with all possible friendships
        ### Example
        # 5 users
        # num_users[(1,2), (1,3), (1,4), (1,5), (2,3), (2,4), (2,5), (3,4), (3,5), (4,5)]
        friendships = []
        for user in range(1, self.last_id + 1):
            for friend in range(user + 1, num_users+1):
                friendship = (user, friend)
                friendships.append(friendship)
        ##Shuffle the list
        self.fisher_yates_shuffle(friendships)

        ## Take as many as we need
        total_friendships = num_users + avg_friendships

        random_friendships = friendships[:total_friendships//2]

        ## add to self.friendships
        for friendship in random_friendships:
            self.add_friendship(friendship[0], friendship[1])

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """

        q = Queue()

        visited = {}  # Note that this is a dictionary, not a set

        q.enqueue([user_id])
        #while queue isnt empty
        while q.size() > 0:
            #deque the current path
            path = q.dequeue()

            #grap next vertex from the pat
            current_user = path[-1]
            #if it hasnt  been visited, add to our dic
                        ### another way {friend_id: path}
                        ## friends = self.friendships{current_user}
            if current_user not in visited:
                visited[current_user] = path #mark as visited, and remeber path so far
                friends = self.friendships[current_user]
                for friend in friends:
                    # path_copy = list(path)
                    # path_copy.append(neighbor)
                    # q.enqueue(path_copy)
                    #enquee PATHS to each of our neighbors
                    q.enqueue(path + [friend]) # make a new path
        return visited

        #BFS  - shortest path
        #keep track of nodes you've seen before (dic)

        ##want to check if node is in dic (already seen)
        ##want to store path taken to get somewhere
        ##make copy of the list
        # as soon as it sees a node, you store node with path taken to 
        # reach that node and that is guranteed to be the shortest path


        # ** we can do a BFS for each user and add to visited 
        # but that will have a bad time complexity

    def linear_populate_graph(self):
        #reset the graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        #add user
        #use num_users
        for user in range(num_users):
            self.add_user(user)
        #Iterate for number of friendships to generate. 
        target_number_friendships = num_users * avg_friendships
        friendships_created = 0
        # as long as we havent made all the friendships we need
        while friendships_created < target_number_friendships:
            #pick two random number betwwen 1 nd the last id
            friend_one = random.randint(1, self.last_id)
            friend_two = random.randint(1, self.last_id)
        # For each, generate random pair. 
        # Check for existing pair.  
        # A little above linear.

if __name__ == '__main__':
    sg = SocialGraph()

    start_time = time.time()
    sg.populate_graph(1000,5)
    end_time = time.time()

    print(end_time - start_time)

    start_time = time.time()
    sg.linear_populate_graph(1000,5)
    end_time = time.time()

    print(end_time - start_time)

    # print(sg.friendships)
    # connections = sg.get_all_social_paths(1)
    # print(connections)

#percentage in totaluser in our extended social networks
# how many people you know divided by how mnay people there are

print(f'{(len(connections)-1)/1000 * 100 }%')

# what is the avg degree of sep between a user and those in his/her extended network?
# avg length of path to each user
# traverse a user's extended connectipns, 
# gather lengths, sum, 
total_length = 0
for friend in connections:
    total_length += len(connections[friend])
# divide by number of friends in CC
print(f'Avg degree of seperation: {total_length / len(connections)}')