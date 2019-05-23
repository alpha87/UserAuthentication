"""
Desc:
    加密密码
"""

import bcrypt


def hash_password(password):
    """混淆密码"""

    _password = bytes(password, encoding="utf8")
    hashed = str(bcrypt.hashpw(_password, bcrypt.gensalt()), encoding = "utf-8")
    return hashed


def check_password(password, hashed):
    """核对密码"""

    _password = bytes(password, encoding="utf8")
    _hashed = bytes(hashed, encoding="utf8")
    if bcrypt.checkpw(_password, _hashed):
        return True
    else:
        return False
