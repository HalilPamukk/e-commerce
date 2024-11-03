from django.core.cache import caches
from django.utils.translation import get_language


class BaseCache(object):
    CACHE = "default"
    CACHE_KEY = ""
    CACHE_KEY_BULK = ""
    TIMEOUT = 300

    @classmethod
    def cache_key(cls, obj_id, to_json_func=None):
        if not cls.CACHE_KEY:
            raise Exception("CACHE_KEY not set!")
        lang_code = get_language()
        # cache data formats based on the function name and language for translation
        return (
            f"{cls.CACHE_KEY}-{lang_code}-{obj_id}:{to_json_func.__name__}"
            if to_json_func
            else f"{cls.CACHE_KEY}-{lang_code}-{obj_id}"
        )

    @classmethod
    def _get_cache(cls, cache_key):
        cache = caches[cls.CACHE]
        return cache.get(cache_key)

    @classmethod
    def set_cache(cls, obj_id, data, timeout=300, to_json_func=None):
        cache = caches[cls.CACHE]
        cache.set(
            cls.cache_key(obj_id=obj_id, to_json_func=to_json_func),
            data,
            int(timeout) if timeout else None,
        )

    @classmethod
    def get_cache(cls, obj_id, user=None, to_json_func=None, **kwargs):
        cache = caches[cls.CACHE]
        data = cache.get(cls.cache_key(obj_id, to_json_func=to_json_func))
        if not data:
            return cls.json(
                obj_id=obj_id,
                check_cache=False,
                user=user,
                to_json_func=to_json_func,
                **kwargs,
            )
        return data

    @classmethod
    def _del_cache(cls, key):
        cache = caches[cls.CACHE]
        return cache.delete(key)

    @classmethod
    def del_cache(cls, obj_id):
        return cls._del_cache(cls.cache_key(obj_id))

    @classmethod
    def _set_cache(cls, key, value, timeout=300):
        cache = caches[cls.CACHE]
        cache.set(key, value, int(timeout) if timeout else None)

    @classmethod
    def clear_caches(cls, obj_id):
        cls._del_cache(cls.cache_key(obj_id))
        cls._del_cache(cls.CACHE_KEY_BULK)

    @classmethod
    def bulk_list(cls, timeout=300):
        if timeout is None:
            timeout = cls.TIMEOUT

        cache_data = cls.get_cache(cls.CACHE_KEY_BULK)

        if cache_data:
            return cache_data

        data = cls.objects.filter()
        result = []
        for d in data:
            result.append(d.json(d.id))

        cls._set_cache(cls.CACHE_KEY_BULK, result, timeout)

        return result

    @classmethod
    def json(
        cls,
        obj_id,
        to_json_func=None,
        check_cache=True,
        timeout=300,
        user=None,
        **kwargs,
    ):
        if check_cache:
            cache_data = cls.get_cache(
                obj_id=obj_id, to_json_func=to_json_func, **kwargs
            )
            if cache_data:
                return cache_data

        try:
            obj = cls.objects.get(id=obj_id)
            if to_json_func:
                data = to_json_func(obj, **kwargs)
            else:
                data = obj._json(**kwargs)
        except Exception:
            return None

        cls.set_cache(
            obj_id=obj_id, data=data, timeout=timeout, to_json_func=to_json_func
        )

        return data
