import json
import logging
import  os



class User:

    def __init__(self, _id =None , active= None, alias=None, created_at= None, external_id= None, last_login_at= None, locale= None, name=None, organization_id =None,
                 phone= None, role=None, shared= None, signature= None, suspended= None, tags=None, timezone= None, url=None, verified=None,email=None):
        self._id = _id
        self.external_id = external_id
        self.active = active
        self.alias = alias
        self.created_at = created_at
        self.email = email
        self.last_login_at = last_login_at
        self.locale = locale
        self.name = name
        self.organization_id = organization_id
        self.phone = phone
        self.role = role
        self.shared = shared
        self.signature = signature
        self.suspended = suspended
        self.tags = tags
        self.timezone = timezone
        self.url = url
        self.verified = verified

        def from_json(cls, json_string):
            json_dict = json.load(json_string)
            return cls(**json_dict)

        def __repr__(self):
            return f'<User {self.name}>'



    @staticmethod
    def read_file_user():
            use_list = []
            with open('JsonStore\\users.json') as json_file:
                user_data = json.loads(json_file.read())
                for user in user_data:
                    use_list.append(User(**user))
            return use_list

class Tickets:
    def __init__(self, _id=None, assignee_id=None, created_at=None, description=None, due_at=None, external_id=None, has_incidents=None, organization_id=None,
                 priority=None, status=None, subject=None, submitter_id=None, tags=None, type=None, url=None, via=None):
        self._id = _id
        self.assignee_id = assignee_id
        self.created_at = created_at
        self.description = description
        self.due_at = due_at
        self.external_id = external_id
        self.has_incidents = has_incidents
        self.organization_id = organization_id
        self.priority = priority
        self.status = status
        self.subject = subject
        self.submitter_id = submitter_id
        self.tags = tags
        self.type = type
        self.url = url
        self.via = via


        def from_json(cls, json_string):
            json_dict = json.load(json_string)
            return cls(**json_dict)

        def __repr__(self):
            return f'<Tickets {self._id}>'


    @staticmethod
    def read_file_tickets():
        ticket_list = []
        with open('JsonStore\\tickets.json') as json_file:
            ticket_data = json.loads(json_file.read())
            for ticket in ticket_data:
                ticket_list.append(Tickets(**ticket))
        return ticket_list


class Organizations:
    def __init__(self, _id=None, created_at=None, details=None, domain_names=None, external_id=None, name=None, shared_tickets=None, tags=None, url=None):
        self._id = _id
        self.created_at = created_at
        self.details = details
        self.domain_names = domain_names
        self.external_id = external_id
        self.name = name
        self.shared_tickets = shared_tickets
        self.tags = tags
        self.url =url


        def from_json(cls, json_string):
            json_dict = json.load(json_string)
            return cls(**json_dict)

        def __repr__(self):
            return f'<Organizations {self._id}>'



    @staticmethod
    def read_file_Orgz():
        orgz_list = []
        with open('JsonStore\\organizations.json') as json_file:
            organizations_data = json.loads(json_file.read())

            for organization in organizations_data:
                orgz_list.append(Organizations(**organization))

        return orgz_list

