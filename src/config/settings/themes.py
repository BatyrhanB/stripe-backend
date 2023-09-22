JAZZMIN_SETTINGS = {
    "site_title": "Stripe",
    "site_header": "Stripe",
    "site_brand": "Stripe Admin",
    "site_logo_classes": "img-circle",
    "site_icon": "/assets/icons/admin_logo.svg",
    "welcome_sign": "Добро пожаловать в панель администратора сайта Stripe!",
    "copyright": "Batyrhan",
    # "search_model": "user.User",
    # "user_avatar": "None",
    "topmenu_links": [
        {"name": "Главная", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],
    # "usermenu_links": [
    #     {
    #         "model": "user.User",
    #     },
    # ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "icons": {
        "user.User": "fas fa-user",
    },
    "order_with_respect_to": [
        # "user",
        "common",
    ],
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-thumbtack",
    "related_modal_active": False,
    "custom_js": None,
    "show_ui_builder": True,
    "changeform_format": "vertical_tabs",
}

JAZZMIN_UI_TWEAKS = {
    "navbar_small_text": False,
    "footer_small_text": False,
    "body_small_text": True,
    "brand_small_text": False,
    "brand_colour": "navbar-dark",
    "accent": "accent-primary",
    "navbar": "navbar-white navbar-light",
    "no_navbar_border": False,
    "navbar_fixed": False,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_fixed": True,
    "sidebar": "sidebar-dark-primary",
    "sidebar_nav_small_text": False,
    "sidebar_disable_expand": False,
    "sidebar_nav_child_indent": False,
    "sidebar_nav_compact_style": True,
    "sidebar_nav_legacy_style": False,
    "sidebar_nav_flat_style": True,
    "theme": "default",
    "dark_mode_theme": None,
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
    "actions_sticky_top": False,
}
