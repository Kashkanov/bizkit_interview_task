from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!

    filtered = []
    for a in args:
        for user in USERS:
            # check if id matches
            if(a == "id") and (user[a] == args[a]):
                # check if the user is already in the filtered list
                if (user not in filtered):
                    filtered.append(user)
            # check if the name or occupation matches(case insensitive)
            if (a == "name" or a == "occupation") and ((args[a].lower() in user[a].lower())):
                # check if the user is already in the filtered list
                if (user not in filtered):
                    filtered.append(user)
            if (a=="age"):
                # checks if age is equal or one year older or younger
                if(user[a]==int(args[a])) or (user[a]==int(args[a])+1) or (user[a]==int(args[a])-1):
                    # check if the user is already in the filtered list
                    if (user not in filtered):
                        filtered.append(user) 
    return filtered
