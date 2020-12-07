# -*- coding: utf-8 -*-
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import check_payload
from rest_framework_jwt.utils import check_user
from rest_framework_jwt.utils import unix_epoch


# reference: rest_framework_jwt.serializers.RefreshAuthTokenSerializer.validate()
def refresh_token(token):
    payload = check_payload(token=token)
    user = check_user(payload=payload)

    # Get and check 'orig_iat'
    orig_iat = payload.get('orig_iat')
    if orig_iat is None:
        msg = _('orig_iat field not found in token.')
        raise RuntimeError(msg)

        # Verify expiration
    refresh_limit = \
        api_settings.JWT_REFRESH_EXPIRATION_DELTA.total_seconds()

    expiration_timestamp = orig_iat + refresh_limit
    now_timestamp = unix_epoch()

    if now_timestamp > expiration_timestamp:
        msg = _('Refresh has expired.')
        raise RuntimeError(msg)

    new_payload = JSONWebTokenAuthentication.jwt_create_payload(user)
    new_payload['orig_iat'] = orig_iat

    # Track the token ID of the original token, if it exists
    orig_jti = payload.get('orig_jti') or payload.get('jti')
    if orig_jti:
        new_payload['orig_jti'] = orig_jti
    elif api_settings.JWT_TOKEN_ID == 'require':
        msg = _('orig_jti or jti field not found in token.')
        raise RuntimeError(msg)

    return {
        'token':
            JSONWebTokenAuthentication.jwt_encode_payload(new_payload),
        'user':
            user,
        'issued_at':
            new_payload.get('iat', unix_epoch())
    }
