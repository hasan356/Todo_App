# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import uuid

from cassandra.cqlengine import columns

from cassandra.cqlengine.models import Model

from datetime import datetime


# Create your models here.

class TodoModel(Model):
    todo_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    title_id = columns.Integer(primary_key=True , index= True)
    title = columns.Text(required=True)
    description = columns.Text(required=True)
    created_at = columns.DateTime(default=datetime.now, index=True)



