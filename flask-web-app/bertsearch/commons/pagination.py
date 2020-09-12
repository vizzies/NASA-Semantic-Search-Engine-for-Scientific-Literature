"""Simple helper to paginate query
"""
from flask import url_for, request
import requests

DEFAULT_PAGE_SIZE = 100
DEFAULT_PAGE_NUMBER = 1


def paginate(query, schema):
    page = request.args.get("page", DEFAULT_PAGE_NUMBER, type=int)
    per_page = request.args.get("page_size", DEFAULT_PAGE_SIZE)
    page_obj = query.paginate(page=page, per_page=per_page)
    next_ = url_for(
        request.endpoint,
        page=page_obj.next_num if page_obj.has_next else None,
        per_page=per_page,
        **request.view_args,
    )
    prev = url_for(
        request.endpoint,
        page=page_obj.prev_num if page_obj.has_prev else None,
        per_page=per_page,
        **request.view_args,
    )

    return {
        "total": page_obj.total,
        "pages": page_obj.pages,
        "next": next_,
        "prev": prev,
        "results": schema.dump(page_obj.items),
    }
