import enum


# Most bigger means more powerfull
class UserStatus(enum.Enum):
    User = 0,  # Simple User (just registered)
    UserFriend = 1  #
    UserStudio = 2  #
    UserSigned = 3  # Signed on label user
    UserModer = 4
    UserAdmin = 5  #
    Moderator = 6  #
    Admin = 10  # Most powerfull, owner or real administrator

# Basic User class
class User:
    id: int = None
    name: str = None
    status: UserStatus = UserStatus.User
    points: int = None  # for scoring user music (100 -> will be signed)

# Users that are signed on label
class SignedUser(User):
    status: UserStatus = UserStatus.UserSigned
