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
            }
            
        ]