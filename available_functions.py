functions = [
            {
                "name": "inject_oxytocin",
                "description": "triggered only at the user prompt '/set oxytocin value' where value represesnts the oxytocin level. It can be a number from 0 to 100 or descriptive like low, medium, high",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "value": {
                            "type": "number",
                            "description": "The level of oxytocin as prompted by the user",
                        },
                    },
                },
            },
            {
                "name": "no_formal",
                "description": "When the response is in a formal tone. For eg- 'How can I help you today?'",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The user query",
                        },
                    },
                },
            },
            {
                "name": "fetch_routine",
                "description": "need to know the routine/ plans of the person. For eg- 'What are your plans for today', 'You want to come?'",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "response": {
                            "type": "string",
                            "description": "response",
                        },
                    },
                },
            }
            
        ]