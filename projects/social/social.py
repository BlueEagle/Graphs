import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        self.last_id = 0
        self.users = {}
        self.friendships = {}

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

        # Add users
        for i in range(0, num_users):
            self.add_user(f"user{i}")

        # Create friendships
        # print(self.friendships)
        for id in self.users:
            num_friends = random.randrange(0, (avg_friendships*2)+1)
            # print(f"{id} will have {num_friends}") ### The cool printouts
            # print(self.friendships)

            friends_list = [id]
            # friends_list.append(list(self.friendships[id]))
            for item in self.friendships[id]:
                friends_list.append(item)
            friend_id = id
            for friend_count in range(0, num_friends):
                while friend_id in friends_list:
                    friend_id = random.randrange(1, num_users+1)
                friends_list.append(friend_id)
                # print(friends_list)

                self.add_friendship(id, friend_id)

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        # !!!! IMPLEMENT ME
        q = Queue()

        # init the queue, it's ready for looping!
        q.enqueue([user_id])

        while q.size() > 0:
            path = q.dequeue()
            current_user = path[-1]

            if current_user not in visited:
                # print(f"Visiting ID: {current_user}")
                visited[current_user] = path

                for friend in self.friendships[current_user]:
                    # print(friend)
                    q.enqueue(path + [friend])

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    users = 1000
    avg_friends = 100
    sg.populate_graph(users, avg_friends)
    print(f"Printing all social graphs for {users}, whith and average of {avg_friends} friends.")
    print(sg.friendships)

    """
    I expect this to return all the paths for: 1, 3, 5, 7, 9, 10, 4, 8, 2, 6
    """
    user = 1
    print(f"Printing all social paths for user {user}")
    connections = sg.get_all_social_paths(user)
    print(connections)
    count = 0
    avg_separation = 0
    for connection in connections:
        if len(connections[connection]) > 2:
            count += 1
            avg_separation += len(connections[connection])-1

    avg_separation = avg_separation / count
    print(f"That is {count} / {users} users in user {user}'s extended social network. This is at an average of {avg_separation} hops.")
