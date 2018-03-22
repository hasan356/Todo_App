class TodoObject(object):
    todo_id= ""
    created_at = ""


    def __init__(self, title , description , **attrs):
        self.title = title
        self.description = description
