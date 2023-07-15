functions = [
            {
                "name": "inject_oxytocin",
                "description": "'/set oxytocin'",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {
                            "type": "number",
                            "description": "The level of oxytocin as prompted by the user",
                        },
                    },
                },
            },
            {
                "name": "inject_endorphin",
                "description": "triggered when encounters '/set endorphin'",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "level": {
                            "type": "number",
                            "description": "The level of endorphin as prompted by the user",
                        },
                    },
                },
            }
            
        ]