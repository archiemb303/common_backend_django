#API logic
"""
1. Check API authentication
2. Check Session Authentication
3. No validations required specific to this API
4. Fetch all records from supportcentre_postlogintickets table where owner_id = logged in user's profile id

"""

# Sample Input:

"""
    {
        "APIDetails":
            {
            	"token_type":1,
            	"token_vendor_id":1,
            	"token_string":"sdxfcgvbhjnmklasdfghjk",
            	"dev_key":"sjdkljagagerukjdgjncjdsnjkfhkjasdghreuiuie@#$%$dgd#$@d234"
            },
        "SessionDetails":
            {
                "profile_id":186,
                "session_id":566,
                "session_key":"5vWiTkopRkJPcvg45ud3D3JE3E78jDRp"
            }
        "APIParams":
            {
            }
    }
"""

# Sample Output:
"""
{
    "AuthenticationDetails": {
        "Status": "Success",
        "Message": "ApiDetails fine to process"
    },
    "Payload": {
        "Status": "Success",
        "Message": "Congratulations, you areregistered successfully with genericbackend",
        "Payload": {
            [
                {
                    ticket_type_id:1, 
                    ticket_type_text:"How to use", 
                    common_questions: 
                    [
                        {question_id: 1, question_text:"How to I sign in"},
                        {question_id: 2, question_text:"How to I sign out"}
                    ]
                },
                {
                    ticket_type_id:1, 
                    ticket_type_text:"Profile related", 
                    common_questions: 
                    [
                        {question_id: 4, question_text:"How do I update my name"},
                        {question_id: 5, question_text:"How to I update my email"}
                    ]
                }
            ]

        }
    }
}
"""
