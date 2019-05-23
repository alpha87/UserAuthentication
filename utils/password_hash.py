"""
Desc:
    加密密码
"""

import bcrypt


def hash_password(password):
    """混淆密码"""

    _password = bytes(password, encoding="utf8")
    return bcrypt.hashpw(_password, bcrypt.gensalt())


def check_password(password, hashed):
    """核对密码"""

    _password = bytes(password, encoding="utf8")
    if bcrypt.checkpw(_password, hashed):
        return True
    else:
        return False
