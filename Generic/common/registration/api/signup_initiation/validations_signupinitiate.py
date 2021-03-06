"""Module to validate APIParams for signup initiation."""
import logging
import re
from functools import wraps
from rest_framework.views import Response

# Get an instance of a logger
logger = logging.getLogger("genericbackend_1.0")


def validation_signupinitiate(func):
    """Function to validate apiparams for signup initiation though emailid."""
    @wraps(func)
    def validation_signupinitiate_json(self, request):
        input_json, output_json = request.data['APIParams'], {}
        output_json['AuthenticationDetails'] = request.data['AuthenticationDetails']
        try:
            if input_json['first_name'] == "":
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "First Name can't"
                                                                                                " be an empty String.",
                                                                                     None]))
                return Response(output_json)

            if input_json['first_name'] == {}:
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "First Name can't"
                                                                                                " be an empty json.",
                                                                                     None]))
                return Response(output_json)

            if input_json['first_name'] is None:
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "First Name can't"
                                                                                                " be NULL.", None]))
                return Response(output_json)

            if not isinstance(input_json['first_name'], str):
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "First Name must"
                                                                                                " be string.", None]))
                return Response(output_json)

        except Exception as ex:
            output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', f"Exception encountered: "
                                                                                            f"{ex}", None]))
            return Response(output_json)
        try:
            if input_json['last_name'] == "":
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "Last Name can't"
                                                                                                " be an empty String.",
                                                                                     None]))
                return Response(output_json)

            if input_json['last_name'] == {}:
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "First Name can't"
                                                                                                " be an empty json.",
                                                                                     None]))
                return Response(output_json)

            if input_json['last_name'] is None:
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "Last Name can't"
                                                                                                " be NULL.",
                                                                                     None]))
                return Response(output_json)

            if not isinstance(input_json['last_name'], str):
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure',
                                                                                     "Last Name must be string.",
                                                                                     None]))
                return Response(output_json)

        except Exception as ex:
            output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', f"Exception encountered: "
                                                                                            f"{ex}", None]))
            return Response(output_json)
        try:
            if not isinstance(input_json['email_id'], str):
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "Email Id must be a "
                                                                                                "string.", None]))
                return Response(output_json)
            if input_json['email_id'] is None:
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "Email Id can't be "
                                                                                                "NULL.", None]))

                return Response(output_json)

            if input_json['email_id'] == "":
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "Email Id must be a "
                                                                                                "string.", None]))
                return Response(output_json)
            if input_json['email_id'] == {}:
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "Email Id can't be an "
                                                                                                "empty json.", None]))
                return Response(output_json)

            match = re.search(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", input_json['email_id'])
            try:
                if not match.group():
                    output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', "Not a valid email"
                                                                                                    " id format.",
                                                                                         None]))
                    return Response(output_json)
            except Exception as ex:
                output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', f"Not a valid email"
                                                                                                f" id format.: {ex}",
                                                                                     None]))

        except Exception as ex:
            output_json['Payload'] = dict(zip(['Status', 'Message', 'Payload'], ['Failure', f"Exception encountered: "
                                                                                            f"{ex}", None]))
            return Response(output_json)

        return func(self, request)
    return validation_signupinitiate_json
