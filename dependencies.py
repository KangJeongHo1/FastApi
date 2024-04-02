# 인증관련추가 -> 토큰기반으로 유저 네임값을 가져올 수 있도록 한다.

users = {
    1: {'username': '123'},
    2: {'username': '1234'}
}

def get_username(token: str):
    # 토큰을 유저 ID로 간주
    user_id = int(token)

    user = users.get(user_id)

    return user['username']