# blue prints are imported 
# explicitly instead of using *
from .user import user_views
from .index import index_views
from .auth import auth_views
from .karmascore import karmascore_views
from .students import student_views


views = [user_views, index_views, auth_views, student_views, karmascore_views] 
