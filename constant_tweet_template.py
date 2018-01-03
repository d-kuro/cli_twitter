# -*- encoding: utf-8 -*-

PRINT_TWEET_DATA = """\
{screen_name} / {name}
[{created_at}] [id={id}]
{text}
"""

PRINT_ACCOUNT_DATA = """\
TwitterID       : {id}
Name            : {screen_name} / {name}
Description     : {description}
FollowersCount  : {followers_count}
FriendsCount    : {friends_count}
FavouritesCount : {favourites_count}
CreatedDate     : {createdDate}
"""

PRINT_POST_TWEET_DATA = """\
posted twees :
{screen_name} / {name}
[{created_at}]
{text}
"""

PRINT_RT_TWEET_DATA = """\
retweeted :
{screen_name} / {name}
[{created_at}]
{text}
"""